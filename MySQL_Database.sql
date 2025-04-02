DROP DATABASE IF EXISTS personsdb;
CREATE DATABASE personsdb;
USE personsdb;

CREATE TABLE pets (
    petid VARCHAR(50) PRIMARY KEY,
    petname VARCHAR(50)
);

CREATE TABLE hobbies (
    hobbyid VARCHAR(50) PRIMARY KEY,
    hobby VARCHAR(50)
);

CREATE TABLE persons (
    personid INT PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(50),
    surname VARCHAR(50),
    email VARCHAR(50),
    petid VARCHAR(50),
    hobbyid VARCHAR(50),
    FOREIGN KEY (petid) REFERENCES pets(petid),
    FOREIGN KEY (hobbyid) REFERENCES hobbies(hobbyid)
);


INSERT INTO pets VALUES
('p1', 'Dog'), 
('p2', 'Cat'), 
('p3', 'Bird'), 
('p4', 'Hamster');

INSERT INTO hobbies VALUES
('h1', 'Swimming'), 
('h2', 'Football'), 
('h3', 'Dancing'), 
('h4', 'Singing'), 
('h5', 'Cooking'), 
('h6', 'Reading');
