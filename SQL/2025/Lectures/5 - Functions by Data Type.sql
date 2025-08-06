--=== Functions by Data Type===--

----1) Function Basics
--a) Definition: Within SQL, a function takes in zero or more inputs, applies a calculation or a transformation
--and ouputs a value
--b) Can recognize functions by a keyword followed by ()
--c) Best practice to capitalize functions so they stand out
--d) Function categories:
	--Aggregate functions:
		--Applies a calculation to many rows of data and returns a single value
		--Often used alongside GROUP BY
	--Window Functions:
		--Perform calculations across a window of rows
	--General Functions:
		--Performs calculations on all individual values within a column

----2) Numeric Functions
--a) Can be applied to numeric columns (integer, decimal, etc.)

--LEAST & GREATEST
--a) Apply a calculation across a row instead of a column

SELECT 
	GREATEST(q1, q2, q3, q4) AS most_miles

FROM miles_run;

--Sneak peak for dealing with NULLs
--If a NULL is present in the Q4 column, replace that with a zero
SELECT 
	GREATEST(q1, q2, q3, COALESCE(q4, 0)) AS most_miles

FROM miles_run;


--Math and Rounding
SELECT
	country
	,population
	,LOG(population) AS log_pop
	,ROUND(LOG(population), 2) AS log_pop_round

FROM country_stats;

--FLOOR for binning rows
--FLOOR creates separate bins for each of the largest integer values less than or equal to specified expression
--Explained: Take population, divide by 1M, and then create bins for each country based on their FLOORed pop
WITH pm AS (
	SELECT
		country
		,population
		,FLOOR(population / 1000000) AS pop_millions

	FROM country_stats
)

SELECT 
	pop_millions
	,COUNT(country)
FROM pm
GROUP BY pop_millions
ORDER BY pop_millions;

--3) Cast & Convert
--Turning our str_value column into a new column with proper FLOAT data type
--Could also do salary / 1.0 to convert an integer into a FLOAT, but CAST is more formal
--***FLOATs give APPROXIMATE values, DECIMALs give EXACT
SELECT 
	id
	,str_value

	--Could not previously conduct the multiplication because it was formerly a string value before being CAST
	,CAST(str_value AS FLOAT) * 2 AS float_value

FROM sample_table;

--ASSIGNMENT: Numeric Functions
--Interested in seeing how many customers have spent $0-$10 on our products, $10-$20 and so on for every $10 range
WITH num_assignment AS (
	SELECT 
	
		customer_id
		,SUM(o.units * p.unit_price) AS total_spend
		,FLOOR(SUM(o.units * p.unit_price) / 10) * 10 AS spend_bin

	FROM orders o
	
		LEFT JOIN products p
		ON o.product_id = p.product_id

	GROUP BY customer_id
)

SELECT
	spend_bin
	,COUNT(customer_id)

FROM num_assignment
GROUP BY spend_bin
ORDER BY spend_bin;

--4) Datetime functions
--Can be applied to datetime columns (date, time, etc)

SELECT 
	event_name
	,event_date
	,YEAR(event_date) AS event_year	--2025
	,MONTH(event_date) AS event_month	--Integer
	,DATENAME(m, event_date) AS month_name	--Month name: July, August
	,DATENAME(dw, event_date) AS dow_name	--Day name: Monday, Tuesday
	,DATEPART(dw, event_date) AS dow_num	--Day of week number: 2, 3
	,GETDATE() AS today_datetime	--2025-08-05 19:37:34.343
	,CAST(GETDATE() AS DATE) AS today_date	--2025-08-05
	,CAST(GETDATE() AS TIME) AS today_time	--19:37:34.3433333
	,DATEDIFF(d, event_date, GETDATE()) AS days_since_event
	,DATEADD(d, 1, CAST(GETDATE() AS DATE)) AS tomorrow_date	--2025-08-06

FROM my_events;

--ASSIGNMENT: Datetime Functions
--Provide a Q2 2024 data pull, also want a ship_date column (two days after order_date)

SELECT 
	order_id
	,order_date
	,DATEADD(d, 2, order_date) AS ship_date

FROM orders
WHERE 
	MONTH(order_date) BETWEEN 4 AND 6
	AND YEAR(order_date) = 2024

ORDER BY 
	order_date
	,order_id;