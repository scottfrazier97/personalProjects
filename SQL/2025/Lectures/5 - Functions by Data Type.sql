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

--ASSIGNMENT: