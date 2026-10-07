DROP DATABASE IF EXISTS institute_course_finder;
CREATE DATABASE institute_course_finder;

USE institute_course_finder;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    experience_status VARCHAR(30),
    interested_course VARCHAR(100),
    preferred_location VARCHAR(100)
);

CREATE TABLE admins (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE institutes (
    institute_id INT AUTO_INCREMENT PRIMARY KEY,
    institute_name VARCHAR(150) NOT NULL,
    location VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(30),
    website VARCHAR(200),
    description TEXT
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    institute_id INT NOT NULL,
    course_name VARCHAR(150) NOT NULL,
    duration VARCHAR(50) NOT NULL,
    fees DECIMAL(10,2) NOT NULL,
    mode VARCHAR(50),
    description TEXT,
    FOREIGN KEY (institute_id)
        REFERENCES institutes(institute_id)
        ON DELETE CASCADE
);

INSERT INTO admins (username, password)
VALUES ('admin', 'admin123');

INSERT INTO institutes
(institute_name, location, address, phone, website, description)
VALUES
('FITA Academy', 'Chennai', 'T Nagar, Chennai', '9876543210',
 'www.fita.in', 'Training institute offering software and analytics courses.'),

('SLA Institute', 'Chennai', 'KK Nagar, Chennai', '9876543211',
 'www.softlogicsys.in', 'Technology training institute offering IT and analytics programs.'),

('Besant Technologies', 'Chennai', 'OMR, Chennai', '9876543212',
 'www.besanttechnologies.com', 'IT training institute offering programming and analytics courses.'),

('Greens Technology', 'Chennai', 'OMR, Chennai', '9876543213',
 'www.greenstechnologys.com', 'Training institute offering software development and analytics courses.'),

('DIT Academy', 'Chennai', 'Velachery, Chennai', '9876543214',
 'www.ditacademy.in', 'Training institute providing software and professional courses.'),

('Login360', 'Chennai', 'Velachery, Chennai', '9876543215',
 'www.login360.in', 'IT training institute offering development and testing courses.'),

('QSpiders', 'Chennai', 'Tambaram, Chennai', '9876543216',
 'www.qspiders.com', 'Training institute specializing in software testing and development.'),

('JSpiders', 'Chennai', 'Guindy, Chennai', '9876543217',
 'www.jspiders.com', 'Training institute offering Java and full-stack development programs.'),

('ACTE', 'Chennai', 'Porur, Chennai', '9876543218',
 'www.acte.in', 'Professional training institute offering technology courses.'),

('FIT Academy', 'Chennai', 'Anna Nagar, Chennai', '9876543219',
 'www.fitacademy.in', 'Career-oriented technology training institute.');

INSERT INTO courses
(institute_id, course_name, duration, fees, mode, description)
VALUES

(1, 'Data Analytics', '4 Months', 35000, 'Offline',
 'SQL, Excel, Power BI and Python analytics training.'),

(1, 'Python Full Stack', '6 Months', 45000, 'Offline',
 'Python, Django, SQL, HTML, CSS and JavaScript.'),

(1, 'Data Science', '6 Months', 55000, 'Offline',
 'Python, statistics, machine learning and data science.'),

(2, 'Data Analytics', '5 Months', 40000, 'Offline',
 'Excel, SQL, Power BI and Python.'),

(2, 'Python', '4 Months', 30000, 'Offline',
 'Python programming and application development.'),

(2, 'SQL', '2 Months', 18000, 'Offline',
 'MySQL, SQL queries, joins and database concepts.'),

(3, 'Data Analytics', '4 Months', 32000, 'Offline',
 'Excel, SQL, Power BI and analytics concepts.'),

(3, 'Python Full Stack', '6 Months', 42000, 'Offline',
 'Python full-stack web development.'),

(3, 'Java Full Stack', '6 Months', 45000, 'Offline',
 'Java, Spring, SQL and web development.'),

(4, 'Data Science', '6 Months', 50000, 'Offline',
 'Python, statistics, machine learning and visualization.'),

(4, 'Data Analytics', '5 Months', 38000, 'Offline',
 'Data analysis, visualization and business intelligence.'),

(5, 'Python', '4 Months', 28000, 'Offline',
 'Core Python and practical programming.'),

(5, 'Software Testing', '4 Months', 30000, 'Offline',
 'Manual testing, SQL and automation basics.'),

(6, 'Python Full Stack', '6 Months', 40000, 'Offline',
 'Python, Django, frontend and databases.'),

(6, 'Software Testing', '4 Months', 32000, 'Offline',
 'Manual and automation testing.'),

(7, 'Software Testing', '4 Months', 30000, 'Offline',
 'Manual testing, Selenium and SQL.'),

(7, 'Java Full Stack', '6 Months', 42000, 'Offline',
 'Java programming and full-stack development.'),

(8, 'Java Full Stack', '6 Months', 40000, 'Offline',
 'Java, Spring Boot, SQL and web development.'),

(8, 'Python', '4 Months', 30000, 'Offline',
 'Python programming and database concepts.'),

(9, 'Data Analytics', '3 Months', 25000, 'Online',
 'Excel, SQL and Power BI.'),

(9, 'Python', '4 Months', 28000, 'Online',
 'Python programming and practical projects.'),

(10, 'Data Analytics', '4 Months', 30000, 'Offline',
 'Excel, SQL, Power BI and reporting.'),

(10, 'SQL', '2 Months', 15000, 'Offline',
 'SQL and database fundamentals.');

SELECT
    c.course_id,
    i.institute_name,
    c.course_name,
    c.duration,
    c.fees,
    c.mode,
    i.location
FROM courses c
JOIN institutes i
ON c.institute_id = i.institute_id
ORDER BY i.institute_name;
