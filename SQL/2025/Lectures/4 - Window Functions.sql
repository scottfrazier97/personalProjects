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