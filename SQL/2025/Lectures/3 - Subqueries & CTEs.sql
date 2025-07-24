--=== Subqueries & CTEs ===--

--Subquery Basics
--1) A subquery is a query nested within a main query and is typically used for solving a problem in
--multiple steps
----Ex: Returning all countries that have an above average happiness score

----Step 1: Calculate the average happiness score
SELECT AVG(happiness_score)
FROM happiness_scores

----Step 2: Return all rows with a happiness score greater than the first query result
SELECT *
FROM happiness_scores
WHERE happiness_score > (SELECT AVG(happiness_score) FROM happiness_scores)

--2) Code in subquery is run first before the main query
----Good practice to write subquery first

--3) Where can subqueries be written?
---- a) Calculations in the SELECT statement
---- b) Part of the JOIN in the FROM clause
---- c) Filtering in the WHERE and HAVING clauses

--4) Subqueries in the SELECT statement
----Ex: Return the difference between each country's happiness score and the average

SELECT
	country,
	happiness_score - (SELECT AVG(happiness_score) FROM happiness_scores) as happy_diff_from_avg

FROM happiness_scores;

----ASSIGNMENT (Subquery in SELECT)
SELECT 
	*
	,(SELECT AVG(unit_price) FROM products) AS AVG_PRICE
	,unit_price - (SELECT AVG(unit_price) FROM products)
	
FROM Products
ORDER BY [unit_price] DESC

--5) Subqueries in the FROM clause