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
--Creating summary tables in SQL
--Allows us to transform rows into columns to summarize data
--Can be achieved using CASE statements
--PIVOT is available in SQL Server though, less code and no need for CASE statements

--Ex: Creating a summary table by pivoting the crust type column in the pizza table
SELECT * FROM pizza_table;

--OPTION 1: Creates a summary table using PIVOT
SELECT * FROM (                 -- Select everything from the subquery (the pivot will be applied here)
    SELECT
        category,               -- Pizza category (e.g., Chicken, Classic)
        crust_type,             -- Type of crust (e.g., Gluten-Free, Thin, Standard)
        pizza_name              -- Name of the pizza

    FROM pizza_table            -- Source table containing pizza data
) PizzaResults                  -- Alias for the subquery used in the pivot
PIVOT (
    COUNT(crust_type)           -- Aggregate: count how many pizzas have each crust type
    FOR crust_type              -- The column whose distinct values will become pivoted columns
    IN (
        [Gluten-Free Crust],    -- Column for Gluten-Free Crust count
        [Thin Crust],           -- Column for Thin Crust count
        [Standard Crust]        -- Column for Standard Crust count
		)
) AS PivotTable;                -- Alias for the resulting pivoted table

--OPTION 2: Creating summary table using CASE statements
SELECT
	category
	,SUM(CASE WHEN crust_type = 'Gluten-Free Crust'	THEN 1 ELSE 0 END) AS [Gluten-Free Crust]
	,SUM(CASE WHEN crust_type = 'Standard Crust'	THEN 1 ELSE 0 END) AS [Standard Crust]
	,SUM(CASE WHEN crust_type = 'Thin Crust'		THEN 1 ELSE 0 END) AS [Thin Crust]

FROM pizza_table
GROUP BY category;

--ASSIGNMENT: Pivoting
--Create a summary table which shows average grade for each department and grade level
SELECT * FROM students;
SELECT * FROM student_grades;

--PIVOT
SELECT * FROM (                 
    SELECT
        sg.department,               
        s.grade_level,             
        sg.final_grade              

    FROM students s
	
		INNER JOIN student_grades sg
		ON s.id = sg.student_id

) GradeResults                   
PIVOT (
    AVG(final_grade)           
    FOR grade_level              
    IN (
        [9],    
        [10],           
        [11],
		[12]
		)
) AS PivotTable;   

--CASE statment
SELECT
	sg.department
	,AVG(CASE WHEN s.grade_level = 9	THEN sg.final_grade END) AS [Freshman]
	,AVG(CASE WHEN s.grade_level = 10	THEN sg.final_grade END) AS [Sophomore]
	,AVG(CASE WHEN s.grade_level = 11	THEN sg.final_grade END) AS [Junior]
	,AVG(CASE WHEN s.grade_level = 12	THEN sg.final_grade END) AS [Senior]

FROM students s
	
	INNER JOIN student_grades sg
	ON s.id = sg.student_id

GROUP BY department;