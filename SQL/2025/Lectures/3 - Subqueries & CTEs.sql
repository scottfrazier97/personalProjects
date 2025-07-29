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
----These provide more specific filtering logic
----Ex: Return happiness scores that are greater than ANY / ALL of the current happiness scores
----ANY is short form for using the OR condition a bunch of times: (Also essentially the same as MIN)
----a) price > value 1 
----b) OR price > value 2 
----c) OR price> value 3, etc. 
SELECT * 
FROM happiness_scores
WHERE happiness_score > 
	
	ANY(SELECT ladder_score
		FROM happiness_scores_current)

----ALL is short form for using the AND condition a bunch of times: (Also essentially the same as MAX)
----a) price > value 1 
----b) AND price > value 2 
----c) AND price> value 3, etc. 
SELECT * 
FROM happiness_scores
WHERE happiness_score > 
	
	ALL(SELECT ladder_score
		FROM happiness_scores_current)

--9) EXISTS
----Can use EXISTS to accomplish a similar result to ANY and ALL
--Ex: Only return happiness scores for countries that EXIST in the inflation rates table
--Correlated subquery: A subquery that references tables outside of the subquery.
----As a result, can't stand alone and run on it's own. This type of subquery is known to be slow usually.
----If it is slow, we can rewrite our correlated subquery as an INNER JOIN to run faster

--Correlated Subquery
SELECT * 
FROM happiness_scores h
WHERE EXISTS 
		(SELECT i.country_name
		 FROM inflation_rates i
		 WHERE i.country_name = h.country);
			
--INNER JOIN (Faster, but less readable for some people)			
SELECT * 
FROM happiness_scores h

	INNER JOIN inflation_rates i
		ON h.country = i.country_name
		AND h.year = i.year;

--ASSIGNMENT (Subquery in the WHERE clause)
--Identify products with a unit price less than the unit price of all products

SELECT * 
FROM products;

SELECT * 
FROM products
WHERE unit_price < 
	
	ALL(SELECT unit_price
		FROM products
		WHERE factory = 'Wicked Choccy''s')

--10) Common Table Expressions (CTEs)
--A temporary output that can be referenced within another query
--a) Ex (Same as section 7): Return each country's happiness score for the year alongside the country's avg
----happiness score
--b) CTEs are a bit more readable and user friendly than subqueries.
----Can be referenced anywhere in query as if it is a normal table, see JOIN below
----CTEs start with "WITH" keyword, followed by alias, and query wrapped in parenthesis
----CTEs can handle recursiveness which can call itself again and again

SELECT * FROM happiness_scores; 

WITH AVG_HAPPY_CTE AS (

	SELECT 
		country
		,AVG(happiness_score) AS avg_happy --Aliasing aggregation seemed to remove error
	FROM happiness_scores
	GROUP BY country

)

SELECT 
	
	h.year
	,h.country
	,h.happiness_score
	,a.avg_happy

FROM happiness_scores h

	LEFT JOIN AVG_HAPPY_CTE a
		ON h.country = a.country; --Entire section is one code block, CTE and final query.

--11) Referencing a CTE multiple times
----Can be done with CTEs and not subqueries
----Ex: For each country return countries from the same region with a lower happiness score in 2023

WITH hs AS (

	SELECT
		year
		,region
		,country
		,happiness_score

	FROM happiness_scores
	WHERE year = 2023

)

SELECT 
	hs1.year
	,hs1.country
	,hs1.region
	,hs1.happiness_score
	,hs2.country
	,hs2.happiness_score


FROM hs hs1

	INNER JOIN hs hs2
		ON hs1.region = hs2.region

WHERE hs1.happiness_score > hs2.happiness_score

--ASSIGNMENT: CTEs
----Send a list of all orders over $200, and the number of orders over $200
--Can't use ORDER BY within CTE since ordering comes from main query after CTE

WITH summary AS (
	SELECT 
		o.order_id
		,SUM(o.units * p.unit_price) AS total_amount_spent

	FROM orders o

		LEFT JOIN products p
			ON o.product_id = p.product_id

	GROUP BY 
		o.order_id

	HAVING SUM(o.units * p.unit_price) > 200
)

--Count of records with total amount spent > 200, answer: 7
SELECT COUNT(*) FROM summary;