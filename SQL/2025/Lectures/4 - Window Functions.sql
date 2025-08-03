--=== Window Functions ===--

--1) Window Function Basics
----Used to apply a function to a "window" of data
----Windows are essentially groups of data (each individual country could be a window)
----Different from a GROUP BY because we collapse rows in each group and apply a calculation in that case
----In a window function, we leave the rows as they are and apply calculations by window

--2) Breaking down window functions
----Window functions have four main components
--a) The function being applied to each window (REQUIRED), ex: ROW_NUMBER()
--b) The OVER keyword (it states that this is a window function, REQUIRED) 
--c) How you're splitting the rows into windows (OPTIONAL), ex: One columns, multiple columns, entire table if left blank
--d) ORDER BY, how each window should be sorted BEFORE the function is applied. REQUIRED in MSSQL.

--ROW_NUMBER OVER() is the most basic form of a window function, essentially a counter for entire table
SELECT 
	
	country
	,year
	,happiness_score
	,ROW_NUMBER() OVER (PARTITION BY country ORDER BY happiness_score) AS row_num

FROM happiness_scores;

--ASSIGNMENT: Window Functions Basics
SELECT * FROM orders ORDER BY customer_id, transaction_id;

SELECT 
	customer_id
	,order_id
	,transaction_id
	,ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY transaction_id) AS row_num

FROM orders;

--3) Window Functions 
--Row Numbering:
---ROW_NUMBER
---RANK
---DENSE_RANK

--Value within a window:
---FIRST_VALUE
---LAST_VALUE
---NTH_VALUE

--Value relative to a window
---LEAD
---LAG

--Aggregate Functions
---SUM
---AVG
---COUNT
---MIN
---MAX

--Statistical Functions
---NTILE
---CUME_DIST
---PERCENT_RANK

--4) Row Numbering
SELECT * FROM baby_girl_names

SELECT 
	name
	,babies
	,ROW_NUMBER() OVER (ORDER BY babies DESC) AS [row_num]		--Gives every row a unique number
	,RANK() OVER (ORDER BY babies DESC) AS [rank]				--Accounts for ties (skips numbers)
	,DENSE_RANK() OVER (ORDER BY babies DESC) AS [dense_rank]	--Accounts for ties and leaves no missing numbers between

FROM baby_girl_names;

--ASSIGNMENT: Row Numbering
--Create a product rank field that returns a 1 for the most popular in an order, 2 for second most, so on...
SELECT * FROM products;
SELECT * FROM orders;

SELECT 
	o.order_id
	,p.product_name
	,o.units
	,DENSE_RANK() OVER (PARTITION BY o.order_id ORDER BY o.units DESC) AS [product_rank]

FROM orders o
	
	LEFT JOIN products p
	ON o.product_id = p.product_id;

--5) Value within a window (First, Last, NTH Value)
SELECT * FROM baby_girl_names;

--FIRST_VALUE
--Ex: Below example creates a window on gender, and then sorts on num of baby names, and grabs first value
	--in that window (name with the highest count value in babies)
SELECT 
	gender
	,name
	,babies

	--Extracts first value within a window, in sequential row order
	,FIRST_VALUE(name) OVER (PARTITION BY gender ORDER BY babies DESC) AS top_name

FROM baby_names;

--LAST_VALUE (actually FIRST_VALUE but reversing window sort)
--Below example is grabbing last value, but LAST_VALUE does not work as expected so we use FIRST_VALUE along with
--ASC order to sort from least to greatest, and grab the first value of that instead (bottom value essentially)
SELECT 
	gender
	,name
	,babies

	--Extracts last value within a window
	,FIRST_VALUE(name) OVER (PARTITION BY gender ORDER BY babies ASC) AS bottom_name

FROM baby_names;
	
--NTH_VALUE (Not available in SQL Server, use a form of ROW_NUMBER(), RANK(), or DENSE_RANK())
----SELECT 
----	gender
----	,name
----	,babies

----	--Extracts first value within a window, in sequential row order
----	,NTH_VALUE(name, 2) OVER (PARTITION BY gender ORDER BY babies ASC) AS bottom_name

----FROM baby_names;

WITH MAIN AS ( 
	SELECT 
		gender
		,name
		,babies
		,ROW_NUMBER() OVER (PARTITION BY gender ORDER BY babies) AS row_num

	FROM baby_names
)

SELECT *
FROM MAIN
WHERE row_num = 2

--ASSIGNMENT: Value within a window
----Provide a list of the 2nd most popular product within each order
SELECT * FROM orders;

WITH pop_orders AS ( 
	SELECT 
		order_id
		,product_id
		,units
		,ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY units DESC) AS row_num

	FROM orders
)

SELECT 
	order_id
	,product_id
	,units
FROM pop_orders
WHERE row_num = 2


--6) Value relative to a row (LEAD and LAG)
--For both LAG and LEAD, you can specify an offset which tells SQL how many rows to skip

--LAG (allows you to retrieve a value from the previous row, within each window)
SELECT 
	country
	,year
	,happiness_score
	,LAG(happiness_score) OVER (PARTITION BY country ORDER BY year) AS prior_happiness_score

FROM happiness_scores;

--LEAD (allows you to retrieve a value from the next row, within each window)
SELECT 
	country
	,year
	,happiness_score
	,LEAD(happiness_score) OVER (PARTITION BY country ORDER BY year) AS next_happiness_score

FROM happiness_scores;

--ASSIGNMENT: Value relative to a row
--Produce a table that contains info about each customer and their orders. Provide the number of units in 
--each order and the change in units from order to order?
SELECT * FROM orders;

WITH prior_cte AS (
	SELECT
		customer_id
		,order_id
		,SUM(units) AS total_units
	FROM orders
	GROUP BY 
		customer_id
		,order_id
)

SELECT 
	customer_id
	,order_id
	,total_units
	,LAG(total_units) OVER (PARTITION BY customer_id ORDER BY order_id) AS prior_units
	,(total_units - LAG(total_units) OVER (PARTITION BY customer_id ORDER BY order_id)) AS diff_units

FROM prior_cte
ORDER BY customer_id;

--7) Statistical Functions

--NTILE() divides the rows in a window into a specified number of percentiles
--Ex: View the top 25% of happiness scores for each region

WITH perc_CTE AS (
	SELECT
		region
		,country
		,happiness_score

		--NTILE(4) means the range of 100% of the rows in each window is divided into 4 groups of 25%,
		--with 1 representing the top percentile group, and 4 being the bottom
		,NTILE(4) OVER (PARTITION BY region ORDER BY happiness_score DESC) AS hs_percentile

	FROM happiness_scores
	WHERE year = 2023
)

SELECT 
	region
	,country
	,happiness_score	
	,hs_percentile

FROM perc_CTE
WHERE hs_percentile = 1

--ASSIGNMENT: Statistical Functions
--Create a rewards program for our top 1% of customers. Pull a list of top 1% of customers in terms of how
--they have spent with us.

WITH totalspend_CTE AS (
	SELECT
		o.customer_id
		,SUM(o.units * p.unit_price) AS total_spend

	FROM orders o
		
		LEFT JOIN products p
			ON o.product_id = p.product_id

	GROUP BY 		
	o.customer_id

),

PERC_FINAL AS (
	SELECT 
		customer_id
		,total_spend

		--IMPORTANT, we are not partioning by anything because we want to do this across the WHOLE table
		--, and not doing this affects the number of rows we see in our end result. 32 is proper result COUNT.
		,NTILE(100) OVER (ORDER BY total_spend DESC) AS hs_percentile

	FROM totalspend_CTE
)

SELECT *
FROM PERC_FINAL
WHERE hs_percentile = 1
ORDER BY total_spend DESC;

--===KEY TAKEAWAYS===--
--Window Functions
--a) Used to apply a function across windows of data
--b) Windows refer to groups of rows in a table (region)
--c) Aggregate functions collapse the rows in each group, but window functions leave rows untouched

--General Syntax
--a) FUNCTION OVER (PARTITION BY column1 ORDER BY column2)
--b) OVER indicates that we're writing a window function
--c) PARTITION BY states how we'd like to split up the rows into groups
--d) ORDER BY states how the rows within each window should be ordered BEFORE applying the function

--The FUNCTION portion of a window function is applied to each window
--a) Number rows with ROW_NUMBER(), RANK(), DENSE_RANK()
--b) Identify values within a window with FIRST_RANK(), LAST_RANK(), NTH_VALUE()
--c) Return values from relative rows with LEAD() and LAG()
--d) Use statistical functions like NTILE() for making percentile calculations
--e) Use aggregate functions like AVG() for making moving average calculations