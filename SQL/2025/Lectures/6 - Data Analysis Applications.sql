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

----4) Rolling Calculations
--Include subtotals, cumulative sums, and moving averages allow you to perform calculations across rows of data
SELECT * FROM pizza_orders;

--Subtotals accomplished with WITH ROLLUP
SELECT
	customer_name
	,order_date
	,SUM(price)

FROM pizza_orders
GROUP BY 
	customer_name
	,order_date

WITH ROLLUP --Add after GROUP BY, creates subtotal rows

ORDER BY 
	customer_name,
	order_date


--Cumulative sums accomplished with SUM() along with a window function
WITH total_sales AS (
	SELECT
		order_date
		,SUM(price) AS daily_sum

	FROM pizza_orders
	GROUP BY order_date
)

SELECT 
	order_date
	,SUM(daily_sum) OVER (ORDER BY order_date) AS cumulative_sum --Excluding partition applies function on whole table

FROM total_sales;

--Moving averages accomplished with AVG() along with a window function
--Ex: calculate 3 year moving average of happiness scores for each country
--Interpretation: Each row's moving AVG happiness score, is an AVG of current and prior 2 rows
WITH happ_scores AS (
	SELECT
		country
		,year
		,happiness_score
		,ROW_NUMBER() OVER (PARTITION BY country ORDER BY year) AS row_num

	FROM happiness_scores
)

SELECT
	country
	,year
	,happiness_score

	--Line 326 states to look at 3 previous rows (years) and calculate average happiness score
	,AVG(happiness_score) OVER (PARTITION BY country ORDER BY year 
								ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_happy

FROM happiness_scores;

--ASSIGNMENT: Rolling Calculations
--Generate a report that shows the total sales for each month, as well as cumulative sum of sales and the six-month
--moving average of sales
SELECT * FROM orders;
SELECT * FROM products;

WITH total_sales AS (
	SELECT
		YEAR(o.order_date) AS order_year
		,MONTH(o.order_date) AS order_month
		,SUM((o.units * p.unit_price)) AS total_sales

	FROM orders o

		LEFT JOIN products p
		ON o.product_id = p.product_id

	GROUP BY 
		YEAR(o.order_date)
		,MONTH(o.order_date)
)

SELECT 
	order_year
	,order_month
	,total_sales
	,SUM(total_sales) OVER (ORDER BY order_year, order_month) AS cumulative_sum
	,AVG(total_sales) OVER (ORDER BY order_year, order_month
							ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS six_mo_movingAVG

FROM total_sales

ORDER BY order_year, order_month