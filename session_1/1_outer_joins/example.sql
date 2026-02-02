-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 university.db
-- 2. Load this script: .read example.sql
-- 3. Exit SQLite: .exit

-- Shows all students with their departments using an INNER JOIN
SELECT Students.name, Department.name
FROM
Students JOIN Department
ON Students.department_id = Department.id
ORDER BY Students.name;

-- Show all students and their courses using an INNER JOIN
SELECT Students.name, Courses.name
FROM
Students JOIN Courses
ON Students.department_id = Courses.department_id
ORDER By Students.name;

-- Courses with less then 20 students (INNER JOIN)
SELECT Courses.Name As CourseName, COUNT(StudentCourses.Student_ID) As TotalStudents
FROM
Courses JOIN StudentCourses
ON Courses.ID = StudentCourses.Course_ID
GROUP BY Courses.Name HAVING TotalStudents < 20;

-- Courses with less then 20 students (LEFT JOIN so shows null entries)
SELECT Courses.Name As CourseName, COUNT(StudentCourses.Student_ID) As TotalStudents
FROM
Courses LEFT JOIN StudentCourses
ON Courses.ID = StudentCourses.Course_ID
GROUP BY Courses.Name HAVING TotalStudents < 20;
