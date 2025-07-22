--=== Mutli Table Analysis ===--

--Two main ways to combine multiple tables into a single table for analysis (JOINs & UNIONs)
--JOIN adds related columns from one table to another based on common columns
--UNION stacks the rows from multiple tables with the same column structure

--=== Basic Joins ===--
--The two tables must have one column with matching values
--Specify JOIN type: INNER, LEFT, RIGHT, OUTER

--Specifying the join condition (ON hs.country = cs.country) prevents duplicates
--Using a simple join without the additional condition results in every row pairing with every other row (duplicates)
SELECT *
FROM happiness_scores hs
	INNER JOIN country_stats cs
	ON hs.country = cs.country;

SELECT

	hs.year
	,hs.[country]
	,hs.[region]
    ,hs.[happiness_score]
    ,cs.[continent]
	
FROM happiness_scores hs
	INNER JOIN country_stats cs
	ON hs.country = cs.country;

--=== Basic Join Types ===--
--INNER: Return records that exist in both tables
--LEFT: Return all records that exist in LEFT table, and any matching records from the RIGHT table
--RIGHT: Return all records that exist in RIGHT table, and any matching records from the LEFT table
--OUTER: Return all records from BOTH tables, including non-matching records

--INNER and LEFT joins are the most commonly used
--SQLite does not support RIGHT JOINs, and MySQL and SQLite do not support FULL OUTER JOINs
--Anything that meets criteria for one of the tables but not the other will be replaced with NULL

--INNER JOIN 
--(No NULL values with INNER JOINs)
SELECT

	hs.year
	,hs.[country]
    ,hs.[happiness_score]
	,cs.country
    ,cs.[continent]
	
FROM happiness_scores hs
	INNER JOIN country_stats cs
	ON hs.country = cs.country;

--LEFT JOIN 
--We see NULLs where our right table (country_stats) does not have a match country to happiness_scores
SELECT

	hs.year
	,hs.[country]
    ,hs.[happiness_score]
	,cs.country
    ,cs.[continent]
	
FROM happiness_scores hs
	LEFT JOIN country_stats cs
	ON hs.country = cs.country;

--RIGHT JOIN 
SELECT

	hs.year
	,hs.[country]
    ,hs.[happiness_score]
	,cs.country
    ,cs.[continent]
	
FROM happiness_scores hs
	RIGHT JOIN country_stats cs
	ON hs.country = cs.country;

--FULL OUTER JOIN 
SELECT

	hs.year
	,hs.[country]
    ,hs.[happiness_score]
	,cs.country
    ,cs.[continent]
	
FROM happiness_scores hs
	FULL OUTER JOIN country_stats cs
	ON hs.country = cs.country;

--Finding countries that exist in the LEFT table but not the RIGHT
SELECT DISTINCT
	hs.[country]
	
FROM happiness_scores hs
	LEFT JOIN country_stats cs
	ON hs.country = cs.country
WHERE cs.country IS NULL;


--=== DEMO ===--
--Find all products that exist in one table but not the other
SELECT 
	p.product_id
	,p.product_name
	,o.product_id AS product_id_in_orders

FROM products p
	LEFT JOIN orders o 
	ON p.product_id = o.product_id

WHERE o.product_id IS NULL;


--=== Joining on Multiple Columns ===--
--You can join on multiple columns using "AND" in the join condition
--If we have a case such as year and country, we can't join on just country. 
--Need another identifier to join the data properly (combination of year and country MAKES it a unique identifier)

SELECT

	hs.year
	,hs.country
	,hs.happiness_score
	,ir.inflation_rate

FROM happiness_scores hs

	INNER JOIN inflation_rates ir
		ON hs.year = ir.year
		AND hs.country = ir.country_name;


--=== Joining Multiple Tables ===--
--You can join more than two tables as long as you specify the columns that link the tables together

SELECT

	hs.year
	,hs.country
	,hs.happiness_score
	,cs.continent
	,ir.inflation_rate

FROM happiness_scores hs

	LEFT JOIN country_stats cs
		ON hs.country = cs.country

	LEFT JOIN inflation_rates ir
		ON hs.year = ir.year 
		AND hs.country = ir.country_name


--=== SELF JOIN ===--
--Joining a table with itself, and involves two steps:
--1) Combine a table with itself based on a matching column
--2) Filter on the resulting rows based on some criteria
--Ex 1: Identifying matching salary rows within a table (comparing rows side by side):
----If two people from the employees table had the same salary but different names, 
----then it would return those records

SELECT 
	e1.employee_name
	,e1.salary
	,e2.employee_name
	,e2.salary

FROM employees e1 
	
	INNER JOIN employees e2
		ON e1.salary = e2.salary

WHERE e1.employee_name <> e2.employee_name

ORDER BY e1.employee_name

--Ex 2: Comparing values within rows in a table
--Finding employees that have higher salaries than other employees

SELECT 
	e1.employee_name
	,e1.salary
	,e2.employee_name
	,e2.salary

FROM employees e1 
	
	INNER JOIN employees e2
		ON e1.salary > e2.salary

ORDER BY e1.employee_name

--Ex 3: Display relationships within a table
SELECT
	m1.employee_id
	,m1.employee_name
	,m1.manager_id
	,m2.employee_name AS ManagerName

FROM employees m1

	LEFT JOIN employees m2
		ON m1.manager_id = m2.employee_id
