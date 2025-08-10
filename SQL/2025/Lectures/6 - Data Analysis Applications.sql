--=== Data Analysis Applications ===--

----1) Duplicate Values

--Viewing duplicates
SELECT * FROM employee_details;
	
--Duplicate employees
SELECT
	employee_name
	,COUNT(*)

FROM employee_details
GROUP BY
	employee_name
HAVING COUNT(*) > 1;

--Duplicate combinations of region + employee name
SELECT
	region
	,employee_name
	,COUNT(*)

FROM employee_details
GROUP BY
	region
	,employee_name
HAVING COUNT(*) > 1;

--Entire duplicate rows
SELECT
	region
	,employee_name
	,salary
	,COUNT(*)

FROM employee_details
GROUP BY
	region
	,employee_name
	,salary

HAVING COUNT(*) > 1;

--Excluding fully duplicate rows
SELECT DISTINCT
	region
	,employee_name
	,salary

FROM employee_details;

--Excluding partially duplicate rows with WINDOW FUNCTIONS (unique employee name for each row)
WITH salary_ranking AS (
	SELECT 
		region
		,employee_name
		,salary
		,ROW_NUMBER() OVER (PARTITION BY employee_name ORDER BY salary DESC) AS top_salary

	FROM employee_details
)

SELECT *
FROM salary_ranking
WHERE top_salary = 1;

--Excluding partially duplicate rows (unique combination region + employee_name)
WITH salary_ranking AS (
	SELECT 
		region
		,employee_name
		,salary
		,ROW_NUMBER() OVER (PARTITION BY region, employee_name ORDER BY salary DESC) AS top_salary

	FROM employee_details
)

SELECT *
FROM salary_ranking
WHERE top_salary = 1;

--ASSIGNMENT: Duplicate values
--Generate a report of the students and their emails and exclude duplicate student records
SELECT * FROM students;

WITH duplicate_students AS (
	SELECT 
		id
		,student_name
		,email
		,ROW_NUMBER() OVER (PARTITION BY student_name ORDER BY id DESC) AS student_rank

	FROM students
)

SELECT 
	id
	,student_name
	,email
FROM duplicate_students
WHERE student_rank = 1;


----2) MIN / MAX Value Filtering
--Allows you to filter data based on the lowest or highest values within each group

--Ex: Return most recent sales amount for each sales rep
SELECT * FROM sales;

--Getting initial most recent date, but can't include sales too without a JOIN or WINDOW function
SELECT 
	sales_rep
	,MAX(date) AS most_recent_date

FROM sales
GROUP BY sales_rep;

--JOIN
WITH max_date AS (
	SELECT 
		sales_rep
		,MAX(date) AS most_recent_date

	FROM sales
	GROUP BY sales_rep
)

SELECT 
	s.sales_rep
	,md.most_recent_date
	,s.sales
FROM sales s

	INNER JOIN max_date md
		ON s.sales_rep = md.sales_rep
		AND s.date = md.most_recent_date;

--WINDOW FUNCTION
WITH date_ranks AS (
	SELECT 
		sales_rep
		,date
		,sales
		,ROW_NUMBER() OVER (PARTITION BY sales_rep ORDER BY date DESC) AS row_num

	FROM sales
)

SELECT 
	sales_rep
	,date
	,sales
FROM date_ranks 
WHERE row_num = 1

--ASSIGNMENT: MIN / MAX value filtering
--Create a report of each student with their highest grade for the semester, as well as which class it was in
SELECT * FROM students;
SELECT * FROM student_grades;

WITH max_grades AS (
	SELECT
		student_id
		,class_name
		,final_grade

		--Using DENSE_RANK because a student might have the same grade across multiple courses
		,DENSE_RANK() OVER (PARTITION BY student_id ORDER BY final_grade DESC) AS row_num

	FROM student_grades
)

SELECT 
	s.id
	,s.student_name
	,mg.final_grade
	,mg.class_name

FROM students s

	LEFT JOIN max_grades mg
		ON s.id = mg.student_id

WHERE row_num = 1;

----3) Pivoting


