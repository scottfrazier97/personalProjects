--=== Subqueries & CTEs ===--
--KEY TAKEAWAYS--
--1) A subquery is a query nested within a main query
----In the SELECT clause, they can be used to make calculations
----In the FROM clause, they can be used to join query results and require an alias using AS
----In the WHERE or HAVING clause, they can be used to filter results (can use keywords like ANY, ALL, EXISTS)
----Avoid correlated subqueries by using INNER JOINs if possible

--2) A common table expression (CTE) creates a named temporary output
----CTEs are more readable, can be referenced multiple times, and you can create multiple CTEs within a query
----Recursive CTEs are useful for generating values and working with hierarchical data, but are less common

--3) Temp table and Views are other options for using the results of a query
----Subqueries and CTEs exists only for the duration of a query, and require minimal permissions to create
----Temp tables exist for the duration of a session, and views exist indefinitely but they often require 
--additional permissions to create and maintain


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

--12) Multiple CTEs
--Can use multiple CTEs in a query, even combine them with subqueries
--Only need a single WITH keyword, separate CTEs with a comma
--Ex: Compare 2023 vs 2024 happiness scores side by side

WITH CTE2023 AS (
	SELECT 
		year
		,country
		,happiness_score

	FROM happiness_scores
	WHERE year = 2023),

	CTE2024 AS (
		SELECT 
		2024 AS "year"
		,country
		,ladder_score

	FROM happiness_scores_current) --Limited to just 2024 already

SELECT 

	 hs23.year
	,hs23.country
	,hs23.happiness_score
	,hs24.year
	,hs24.country
	,hs24.ladder_score

FROM CTE2023 hs23
	
	INNER JOIN CTE2024 hs24
		ON hs23.country = hs24.country
		
--Lecture uses a subquery here, but WHERE is easier to accomplish same result
WHERE hs23.happiness_score < hs24.ladder_score;

--ASSIGNMENT: Rewrite subquery using multiple CTEs
SELECT * FROM products;

WITH facs AS (
	SELECT factory, product_name
	FROM products
	GROUP BY factory, product_name),

	COUNTS AS (
	SELECT factory, COUNT(product_name) AS product_count
	FROM products
	GROUP BY factory)

SELECT 
	f.factory
	,f.product_name
	,c.product_count

FROM facs f

		INNER JOIN COUNTS c
		ON f.factory = c.factory

GROUP BY
	f.factory
	,f.product_name
	,c.product_count

ORDER BY 
	f.factory
	,f.product_name;

--13) Recursive CTEs
----A query that references itself which is useful for generating sequences and working with hierarchical data
--a) First SELECT statement is known as the anchor member, no recursion just yet
--b) UNION or UNION ALL is known as the connectors. These connect our anchor values with all other values
--that are going to be generated using recursion
--c) Second SELECT statement is known as the recursive member that references the CTE.

--Ex: Returning daily stock prices including dates with missing prices
SELECT * FROM stock_prices;

----We can generate the missing dates with a recursive CTE
--Step 1: Generate a column of dates
WITH my_dates AS (
	
	--Anchor, saying "Start at the date below"
    SELECT CAST('2024-11-01' AS DATE) AS dt

	--UNION ALL for connector
    UNION ALL

	--Recursive member, adds 1 day after the initial anchor date. Keeps doing this until it meets our 
	--final WHERE criteria (maximum date limitation)
    SELECT DATEADD(DAY, 1, dt)
    FROM my_dates
    WHERE dt < '2024-11-06'
)

--STEP 2: Join with the stock prices table
SELECT 
	md.dt
	,sp.price

FROM my_dates md
	LEFT JOIN stock_prices sp
		ON md.dt = sp.date

OPTION (MAXRECURSION 0);  -- Allows unlimited recursion (or up to 32,767 if needed)

--14) Temp tables & Views
--Both are options for querying the results of a query
--Both subqueries and CTEs only exist for the duration of the query
--Temp tables exist for a session and views continue to exist until modified or dropped

--Temp Tables
IF OBJECT_ID('tempdb..#wickedchoc') IS NOT NULL
DROP TABLE #wickedchoc;

SELECT * 
INTO #wickedchoc --Auto creates/populates the temp table if it doesn't already exist
FROM products
WHERE unit_price < 
	
	ALL(SELECT unit_price
		FROM products
		WHERE factory = 'Wicked Choccy''s')
		
SELECT * FROM #wickedchoc;

---VIEW
-- Create a view
CREATE VIEW Master.dbo.MyView AS
SELECT 
    ID,
    Name,
    CreatedDate
FROM SomeOtherTable
WHERE IsActive = 1;


