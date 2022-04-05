CREATE TABLE patient (
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Mobile BIGINT,
    Email VARCHAR(100),
    Address VARCHAR(300),
    Password VARCHAR(15)
);

CREATE TABLE doctor (
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Mobile BIGINT,
    Email VARCHAR(100),
    Address VARCHAR(300),
    Password VARCHAR(15),
    /*College VARCHAR(75),*/
    Education VARCHAR(10),
    Specialization VARCHAR(50)
);

ALTER TABLE patient 
    ADD CONSTRAINT Pk_Patient PRIMARY KEY (Email);

ALTER TABLE doctor
    ADD CONSTRAINT Pk_Doctor PRIMARY KEY (Email);

ALTER TABLE doctor
    DROP COLUMN College;

CREATE TABLE appointment(
    MeetId VARCHAR(500),
    StartTime VARCHAR(30),
    Duration VARCHAR(20),
    MeetName VARCHAR(100),
    DoctorId VARCHAR(100),
    PatientId VARCHAR(100),
    Problem VARCHAR(500)
);

ALTER TABLE appointment
    ADD CONSTRAINT Pk_MeetId PRIMARY KEY (MeetId);

ALTER TABLE appointment
    ADD CONSTRAINT Fk_Meet_Doctor FOREIGN KEY (DoctorId) REFERENCES doctor(Email);

ALTER TABLE appointment
    ADD CONSTRAINT Fk_Meet_Patient FOREIGN KEY (PatientId) REFERENCES patient(Email);