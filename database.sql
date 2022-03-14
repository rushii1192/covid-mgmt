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