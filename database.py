import mysql.connector
import helper
conn = mysql.connector.connect(**helper.db_config)

print("DATABASE CONNECTION SUCCESSFUL")
# Define cursor
c = conn.cursor()

# Create database
c.execute("CREATE DATABASE IF NOT EXISTS hms")
print("DATABASE CREATED")

# Use database
c.execute("USE hms")

# Temporarily disable foreign key checks
c.execute("SET FOREIGN_KEY_CHECKS = 0")

# Drop tables if they exist
c.execute("DROP TABLE IF EXISTS PATIENT")
c.execute("DROP TABLE IF EXISTS CONTACT_NO")
c.execute("DROP TABLE IF EXISTS doctors")
c.execute("DROP TABLE IF EXISTS TREATMENT")
c.execute("DROP TABLE IF EXISTS MEDICINE")
c.execute("DROP TABLE IF EXISTS ROOM")
c.execute("DROP TABLE IF EXISTS APPOINTMENT")

# Re-enable foreign key checks
c.execute("SET FOREIGN_KEY_CHECKS = 1")

# Create PATIENT table
c.execute("""CREATE TABLE PATIENT (
    PATIENT_ID INT(10) PRIMARY KEY,
    NAME VARCHAR(20) NOT NULL,
    GENDER VARCHAR(10) NOT NULL,
    BLOOD_GROUP VARCHAR(5) NOT NULL,
    DOB DATE NOT NULL,
    ADDRESS VARCHAR(100) NOT NULL,
    CONSULT_TEAM VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(20) NOT NULL,
    PHONE VARCHAR(12) NOT NULL,
    ALT_PHONE VARCHAR(12)
)""")

print("PATIENT TABLE CREATED SUCCESSFULLY")

# Create CONTACT_NO table
c.execute("""CREATE TABLE CONTACT_NO (
    PATIENT_ID INT(10) PRIMARY KEY,
    CONTACTNO VARCHAR(15) NOT NULL,
    ALT_CONTACT VARCHAR(15),
    FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
)""")

print("CONTACT_NO TABLE CREATED SUCCESSFULLY")

# Create DOCTOR table
c.execute("""CREATE TABLE DOCTORS (
    DOC_ID VARCHAR(10) PRIMARY KEY,
    DOC_NAME VARCHAR(20) NOT NULL,
    GENDER VARCHAR(10) NOT NULL,
    AGE INT(5) NOT NULL,
    DESIG VARCHAR(20) NOT NULL,
    SAL INT(10) NOT NULL,
    EXP VARCHAR(100) NOT NULL,
    EMAIL VARCHAR(20) NOT NULL,
    PHONE VARCHAR(12)
)""")

print("DOCTOR TABLE CREATED SUCCESSFULLY")

# Create TREATMENT table
c.execute("""CREATE TABLE TREATMENT (
    PATIENT_ID INT(10) PRIMARY KEY,
    TREATMENT VARCHAR(100) NOT NULL,
    TREATMENT_CODE VARCHAR(30) NOT NULL,
    T_COST INT(20) NOT NULL,
    FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
)""")

print("TREATMENT TABLE CREATED SUCCESSFULLY")

# Create MEDICINE table
c.execute("""CREATE TABLE MEDICINE (
    PATIENT_ID INT(10) PRIMARY KEY,
    MEDICINE_NAME VARCHAR(100) NOT NULL,
    M_COST INT(20) NOT NULL,
    M_QTY INT(10) NOT NULL,
    FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
)""")

print("MEDICINE TABLE CREATED SUCCESSFULLY")

# Create ROOM table
c.execute("""CREATE TABLE ROOM (
    PATIENT_ID INT(10) NOT NULL,
    ROOM_NO VARCHAR(20) PRIMARY KEY,
    ROOM_TYPE VARCHAR(10) NOT NULL,
    RATE INT(10) NOT NULL,
    DATE_ADMITTED DATE,
    DATE_DISCHARGED DATE NULL,
    FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
)""")

print("ROOM TABLE CREATED SUCCESSFULLY")

# Create APPOINTMENT table
c.execute("""CREATE TABLE APPOINTMENT (
    PATIENT_ID INT(20) NOT NULL,
    DOC_ID VARCHAR(10) NOT NULL,
    AP_NO VARCHAR(10) PRIMARY KEY,
    AP_TIME TIME,
    AP_DATE DATE,
    DESCRIPTION VARCHAR(100),
    FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID),
    FOREIGN KEY(doc_ID) REFERENCES doctors(doc_ID)
)""")

print("APPOINTMENT TABLE CREATED SUCCESSFULLY")

# Commit changes and close connection
conn.commit()
conn.close()