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