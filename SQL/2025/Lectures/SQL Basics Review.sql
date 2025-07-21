--=== The Big 6 ===--
SELECT						--Column(s) to display
	grade_level				
	,AVG(gpa) as avg_gpa	
FROM students				--Table(s) to pull data from
WHERE school_lunch = 'Yes'	--Criteria to filter the rows by
GROUP BY grade_level		--Column to group rows by
HAVING AVG(gpa) > 3.3		--Criteria to filter the grouped rows by
ORDER BY grade_level;		--Columns to sort values by

--The Big 6 must always be written in this order
-- The only required clause within a SQL query is a SELECT

--=== Common SQL Keywords===--
--AND is being used to filter/combine an output where grade level is less than 12 AND they receive a school lunch
SELECT *
FROM students
WHERE grade_level < 12 AND school_lunch = 'Yes';

--IN is being used to compare grade_level and search for those containing 10,11,12
SELECT *
FROM students
WHERE grade_level IN (10,11,12);

--LIKE is being used to filter records that contain ".com" domains
SELECT *
FROM students
WHERE email LIKE '%.com';

--DESC orders the results in DESCENDING order, ASCENDING (ASC) is the default
SELECT student_name, gpa
FROM students
ORDER BY gpa DESC;

--Return only the TOP 5 results, based on GPA in DESC order
SELECT TOP 5 *
FROM students
ORDER BY gpa DESC;

--CASE statements use the following syntax to do IF-ELSE logic within SQL:
SELECT 
	student_name
	,grade_level
	,CASE WHEN grade_level = 9 THEN 'Freshman'
		  WHEN grade_level = 10 THEN 'Sophomore'
		  WHEN grade_level = 11 THEN 'Junior'
		  ELSE 'Senior' END AS student_class
FROM students;