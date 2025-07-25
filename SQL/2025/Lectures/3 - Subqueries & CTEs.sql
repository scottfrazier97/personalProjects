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
----Ex: Return each country's happiness score for the year alongside the country's average happiness score

SELECT
	hs.year
	,hs.country
	,hs.happiness_score
	,sq.AVGHAPPY

FROM happiness_scores hs
	
	LEFT JOIN 

		(SELECT 
			country
			,AVG(happiness_score) AS AVGHAPPY

		FROM happiness_scores
		GROUP BY 
			country) sq

		ON hs.country = sq.country;

--6) Multiple Subqueries
--Queries can contain multiple subqueries as long as each one has a different alias
--Ex: Return years where happiness score is a whole point greater than the country's avg happiness score

--Actual solution
SELECT mq.* FROM

	(SELECT
		hs.year
		,hs.country
		,hs.happiness_score
		,sq.AVGHAPPY
		,(hs.happiness_score - sq.AVGHAPPY) AS HappyDiff

		FROM   (SELECT year, country, happiness_score FROM happiness_scores
				UNION ALL
				SELECT 2024, country, ladder_score FROM happiness_scores_current) AS hs

				LEFT JOIN 

				(SELECT country, AVG(happiness_score) AS AVGHAPPY
				FROM happiness_scores
				GROUP BY country) AS sq

					ON hs.country = sq.country) mq

WHERE HappyDiff > 1
ORDER BY HappyDiff DESC

--My (simpler) solution
SELECT
	hs.year
	,hs.country
	,hs.happiness_score
	,sq.AVGHAPPY
	,(hs.happiness_score - AVGHAPPY) AS Diff

FROM happiness_scores hs
	
	LEFT JOIN 

		(SELECT country, AVG(happiness_score) AS AVGHAPPY
		 FROM happiness_scores
		 GROUP BY country) sq

		ON hs.country = sq.country

WHERE (hs.happiness_score - AVGHAPPY) > 1
ORDER BY Diff DESC

----ASSIGNMENT (Subquery in FROM)
----Review products produced by each factory. Give a list of factories along with the names of the products
----they produce and the number of products they produce

SELECT 
	sq1.factory
	,sq1.product_name
	,sq2.product_count

FROM

	(SELECT factory, product_name
		FROM products
		GROUP BY factory, product_name) sq1

	LEFT JOIN 

	(SELECT factory, COUNT(product_name) AS product_count
		FROM products
		GROUP BY factory) sq2

		ON sq1.factory = sq2.factory

GROUP BY
	sq1.factory
	,sq1.product_name
	,sq2.product_count

ORDER BY 
	sq1.factory
	,sq1.product_name;

--7) Subqueries in the WHERE & HAVING clauses
--Ex: Return regions with above average happiness score

--Using subquery in WHERE
SELECT *
FROM happiness_scores
WHERE happiness_score > (SELECT AVG(happiness_score) FROM happiness_scores)

--Using subquery in HAVING
SELECT 
	region
	,AVG(happiness_score) AS AVG_HAPPY
FROM happiness_scores
GROUP BY 
	region
							  --Subequery below filters the grouped regional data
HAVING AVG(happiness_score) > (SELECT AVG(happiness_score) FROM happiness_scores)
ORDER BY AVG_HAPPY DESC

--8) ANY vs ALL