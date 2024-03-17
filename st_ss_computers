import streamlit as st
from datetime import datetime
import sqlite3

# Function to create the database table if it doesn't exist
def create_table():
    conn = sqlite3.connect("typewriting_institute.db")
    c = conn.cursor()
    # c.execute('''DROP TABLE IF EXISTS enquiries''')
    # c.execute('''DROP TABLE IF EXISTS admissions''')

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

# Main Streamlit app
def main():
    create_table()

    st.title("Typewriting Institute Management System")

    # Sidebar navigation
    option = st.sidebar.selectbox("Navigation", ["Dashboard", "Enquiries", "Admission", "Finance"])

    # Dashboard section
    if option == "Dashboard":
        st.header("Dashboard")
        st.subheader("Enquiries")
        enquiries = get_enquiries()
        if enquiries:
            st.table(enquiries)
        else:
            st.info("No enquiries found.")
        
        st.subheader("Admissions")
        admissions = get_admissions()
        if admissions:
            st.table(admissions)
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
