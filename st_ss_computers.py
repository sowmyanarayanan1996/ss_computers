

import streamlit as st
from datetime import datetime
import sqlite3
import pandas as pd

# Function to create the database table if it doesn't exist
def create_table():
    conn = sqlite3.connect("typewriting_institute.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS enquiries (
                    id INTEGER PRIMARY KEY,
                    candidate_name TEXT,
                    course TEXT,
                    email TEXT,
                    contact TEXT,
                    enquiry_datetime TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS admissions (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    course TEXT,
                    level TEXT,
                    fees_structure TEXT,
                    fees TEXT,
                    address TEXT,
                    admission_datetime TEXT
                )''')
    conn.commit()
    conn.close()

# Function to add a new enquiry
def add_enquiry(candidate_name, course, email, contact):
    enquiry_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("typewriting_institute.db")
    c = conn.cursor()
    c.execute('''INSERT INTO enquiries (candidate_name, course, email, contact, enquiry_datetime)
                VALUES (?, ?, ?, ?, ?)''', (candidate_name, course, email, contact, enquiry_datetime))
    conn.commit()
    conn.close()

# Function to add a new admission
def add_admission(name, course, level, fees_structure, fees, address):
    admission_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("typewriting_institute.db")
    c = conn.cursor()
    c.execute('''INSERT INTO admissions (name, course, level, fees_structure, fees, address, admission_datetime)
                VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, course, level, fees_structure, fees, address, admission_datetime))
    conn.commit()
    conn.close()

# Function to fetch all enquiries from the database
def get_enquiries():
    conn = sqlite3.connect("typewriting_institute.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM enquiries''')
    enquiries = c.fetchall()
    conn.close()
    return enquiries

# Function to fetch all admissions from the database
def get_admissions():
    conn = sqlite3.connect("typewriting_institute.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM admissions''')
    admissions = c.fetchall()
    conn.close()
    return admissions

# Function to delete selected enquiries
def delete_selected_enquiries(selected_enquiries):
    conn = sqlite3.connect("typewriting_institute.db")
    c = conn.cursor()
    for enquiry_id in selected_enquiries:
        c.execute('''DELETE FROM enquiries WHERE id = ?''', (enquiry_id,))
    conn.commit()
    conn.close()

# Function to delete selected admissions
def delete_selected_admissions(selected_admissions):
    conn = sqlite3.connect("typewriting_institute.db")
    c = conn.cursor()
    for admission_id in selected_admissions:
        c.execute('''DELETE FROM admissions WHERE id = ?''', (admission_id,))
    conn.commit()
    conn.close()

# Main Streamlit app
def main():
    create_table()

    st.title("Typewriting Institute Management System")

    # Sidebar navigation
    option = st.sidebar.selectbox("Navigation", ["Dashboard", "Enquiries", "Admission", "Finance"])

    # Dashboard section
    if option == "Dashboard":
        st.header("Dashboard")
        
        # Enquiries
        st.subheader("Enquiries")
        enquiries = get_enquiries()
        if enquiries:
            enquiries_df = pd.DataFrame(enquiries, columns=["ID", "Candidate Name", "Course", "Email", "Contact", "Enquiry Datetime"])
            selected_enquiries = st.multiselect("Select Enquiries to Delete", enquiries_df["ID"].tolist())
            if st.button("Delete Selected Enquiries"):
                delete_selected_enquiries(selected_enquiries)
                st.success("Enquiries deleted successfully!")
            st.write(enquiries_df)
        else:
            st.info("No enquiries found.")
        
        # Admissions
        st.subheader("Admissions")
        admissions = get_admissions()
        if admissions:
            admissions_df = pd.DataFrame(admissions, columns=["ID", "Name", "Course", "Level", "Fees Structure", "Fees", "Address", "Admission Datetime"])
            selected_admissions = st.multiselect("Select Admissions to Delete", admissions_df["ID"].tolist())
            if st.button("Delete Selected Admissions"):
                delete_selected_admissions(selected_admissions)
                st.success("Admissions deleted successfully!")
            st.write(admissions_df)
        else:
            st.info("No admissions found.")

    # Enquiries section
    elif option == "Enquiries":
        st.header("Enquiries")
        st.subheader("Add New Enquiry")

        candidate_name = st.text_input("Candidate Name")
        course = st.text_input("Course")
        email = st.text_input("Email")
        contact = st.text_input("Contact")

        if st.button("Submit Enquiry"):
            add_enquiry(candidate_name, course, email, contact)
            st.success("Enquiry added successfully!")

    # Admission section
    elif option == "Admission":
        st.header("Admission")
        st.subheader("Add New Admission")

        name = st.text_input("Name")
        course = st.selectbox("Course", ["Tamil", "English"])
        level = st.selectbox("Level", ["Junior", "Senior"])
        fees_structure = st.selectbox("Fees Structure", ["Monthly", "Quarterly", "Yearly"])
        fees = st.selectbox("Fees", ["650", "750", "550"])  # Corrected selectbox for fees
        address = st.text_area("Address")

        if st.button("Submit Admission"):
            add_admission(name, course, level, fees_structure, fees, address)  # Corrected argument for fees
            st.success("Admission added successfully!")

    # Finance section
    elif option == "Finance":
        st.header("Finance")

        # Fetch total number of enquiries
        total_enquiries = len(get_enquiries())
        st.subheader(f"Total Enquiries: {total_enquiries}")

        # Fetch total number of admissions
        total_admissions = len(get_admissions())
        st.subheader(f"Total Admissions: {total_admissions}")

        # Calculate total fees collected
        total_fees_collected = sum(int(admission[5]) for admission in get_admissions())
        st.subheader(f"Total Fees Collected: {total_fees_collected} INR")

if __name__ == "__main__":
    main()
