-- PART I: SCHOOL ANALYSIS
-- 1. View the schools and school details tables
SELECT TOP 1000 * FROM schools;
SELECT TOP 1000 * FROM school_details;

-- 2. In each decade, how many schools were there that produced players?
SELECT
	ROUND(yearID, -1) AS year_decade
	,COUNT(DISTINCT schoolID)

FROM schools
GROUP BY ROUND(yearID, -1)
ORDER BY year_decade;

-- 3. What are the names of the top 5 schools that produced the most players?
SELECT TOP 5
	sd.name_full
	,COUNT(DISTINCT s.playerID) AS school_player_count

FROM schools s
		
	LEFT JOIN school_details sd
	ON s.schoolID = sd.schoolID

GROUP BY 
	s.schoolID, 
	sd.name_full
ORDER BY school_player_count DESC;

-- 4. For each decade, what were the names of the top 3 schools that produced the most players?
WITH decades AS (
	SELECT
		s.schoolID
		,sd.name_full
		,ROUND(s.yearID, -1) AS year_decade
		,COUNT(DISTINCT s.playerID) AS schoolID_count
		,ROW_NUMBER() OVER (PARTITION BY ROUND(s.yearID, -1) ORDER BY COUNT(DISTINCT s.playerID) DESC) AS dnse_rnk

	FROM schools s

		LEFT JOIN school_details sd
		ON s.schoolID = sd.schoolID

	GROUP BY 
		s.schoolID
		,sd.name_full
		,ROUND(s.yearID, -1)
)

SELECT
	name_full
	,year_decade
	,schoolID_count

FROM decades 
WHERE dnse_rnk < 4
ORDER BY 
	year_decade, 
	schoolID_count DESC;

-- PART II: SALARY ANALYSIS
-- 1. View the salaries table
SELECT TOP 1000 * FROM salaries;

-- 2. Return the top 20% of teams in terms of average annual spending
WITH team_averages AS (
	SELECT
		teamID
		,yearID
		,SUM(salary) AS totals

	FROM salaries
	GROUP BY 
		teamID
		,yearID
),

percentages AS (
	SELECT 
		teamID
		,AVG(CAST(totals AS BIGINT)) AS avg_salary
		,NTILE(5) OVER (ORDER BY AVG(CAST(totals AS BIGINT)) DESC) AS avgsalary_percentile

	FROM team_averages
	GROUP BY teamID
)

SELECT *
FROM percentages
WHERE avgsalary_percentile = 1
ORDER BY avg_salary DESC;

-- 3. For each team, show the cumulative sum of spending over the years
WITH yearly_sums AS (
	SELECT
		teamID
		,yearID
		,SUM(salary) AS salary_sum

	FROM salaries
	GROUP BY teamID, yearID
)

SELECT 
	teamID
	,yearID
	,SUM(CAST(salary_sum AS BIGINT)) OVER (PARTITION BY teamID ORDER BY yearID) AS cumulative_sum 

FROM yearly_sums
ORDER BY teamID, yearID;

-- 4. Return the first year that each team's cumulative spending surpassed 1 billion
WITH yearly_sums AS (
	SELECT
		teamID
		,yearID
		,SUM(salary) AS salary_sum

	FROM salaries
	GROUP BY teamID, yearID
),

csum AS (
	SELECT 
		teamID
		,yearID
		,SUM(CAST(salary_sum AS BIGINT)) OVER (PARTITION BY teamID ORDER BY yearID) AS cumulative_sum 
	
	FROM yearly_sums
),

ranking AS (
	SELECT
		*
		,ROW_NUMBER() OVER (PARTITION BY teamID ORDER BY cumulative_sum) AS [Flag: Billions]

	FROM csum
	WHERE cumulative_sum > 1000000000
)

SELECT 
	teamID
	,yearID
	,FORMAT(cumulative_sum / 1000000000.0, 'N2') + 'B' AS [CumulativeSum]
FROM ranking
WHERE [Flag: Billions] = 1;

-- PART III: PLAYER CAREER ANALYSIS
-- 1. View the players table and find the number of players in the table
SELECT TOP 1000 * FROM players;

SELECT 
	COUNT(DISTINCT playerID) AS distinct_player_count
	,COUNT(*) AS full_record_count

FROM players;

-- 2. For each player, calculate (all in years), Sort from longest career to shortest career.:
--a) Age at their first game
--b) Age at their last game
--c) Their career length

WITH full_birthdays AS (
	SELECT
		playerID
		,nameFirst
		,nameLast
		,birthYear
		,debut
		,finalGame
		,CAST(CONCAT(COALESCE(birthYear, 1900), '-', COALESCE(birthMonth, 1), '-', COALESCE(birthDay, 1)) AS DATE) AS full_birthday

	FROM players
)

SELECT 
	playerID
	,nameFirst
	,nameLast
	,DATEDIFF(year, full_birthday, debut) AS age_first_game
	,DATEDIFF(year, full_birthday, finalGame) AS age_last_game
	,DATEDIFF(year, debut, finalGame) AS career_length

FROM full_birthdays
ORDER BY career_length DESC;


-- 3. What team did each player play on for their starting and ending years?
SELECT TOP 1000 * FROM players;
SELECT TOP 1000 * FROM salaries;

--My initial solution:
WITH player_teams AS (
	SELECT
		p.playerID
		,p.nameFirst
		,p.nameLast
		,s.yearID
		,s.teamID
		,ROW_NUMBER() OVER (PARTITION BY p.playerID ORDER BY s.yearID ASC) AS first_team
		,ROW_NUMBER() OVER (PARTITION BY p.playerID ORDER BY s.yearID DESC) AS last_team

	FROM players p
		
		INNER JOIN salaries s
		ON p.playerID = s.playerID

	--ORDER BY playerID, yearID
),

first_team_CTE AS (
	SELECT 
		playerID
		,nameFirst
		,nameLast
		,teamID AS first_team_name

	FROM player_teams
	WHERE 
		first_team = 1

	GROUP BY 
		playerID
		,nameFirst
		,nameLast
		,teamID
),

last_team_CTE AS (
	SELECT 
		playerID
		,nameFirst
		,nameLast
		,teamID AS last_team_name

	FROM player_teams
	WHERE 
		last_team = 1

	GROUP BY 
		playerID
		,nameFirst
		,nameLast
		,teamID
)

SELECT 
	pt.playerID
	,pt.nameFirst
	,pt.nameLast
	,ft.first_team_name
	,lt.last_team_name

FROM player_teams pt
	
	LEFT JOIN first_team_CTE ft
	ON pt.playerID = ft.playerID

	LEFT JOIN last_team_CTE lt
	ON pt.playerID = lt.playerID

GROUP BY 
	pt.playerID
	,pt.nameFirst
	,pt.nameLast
	,ft.first_team_name
	,lt.last_team_name

ORDER BY playerID;


--Program's (leaner) solution
SELECT 
	p.nameGiven
	,s.yearId AS start_year
	,s.teamID AS start_team
	,e.yearID AS end_year
	,e.teamID AS end_team

FROM players p
	
	INNER JOIN salaries s
	ON p.playerID = s.playerID
	AND YEAR(p.debut) = s.yearID

	INNER JOIN salaries e
	ON p.playerID = e.playerID
	AND YEAR(p.finalGame) = e.yearID

-- 4. How many players started and ended on the same team and also played for over a decade?
SELECT 
	p.nameGiven
	,s.yearId AS start_year
	,s.teamID AS start_team
	,e.yearID AS end_year
	,e.teamID AS end_team

FROM players p
	
	INNER JOIN salaries s
	ON p.playerID = s.playerID
	AND YEAR(p.debut) = s.yearID

	INNER JOIN salaries e
	ON p.playerID = e.playerID
	AND YEAR(p.finalGame) = e.yearID

WHERE 
	s.teamID = e.teamID
	AND (e.yearID - s.yearID) > 10

-- PART IV: PLAYER COMPARISON ANALYSIS
-- 1. View the players table
-- 2. Which players have the same birthday?
-- 3. Create a summary table that shows for each team, what percent of players bat right, left and both
-- 4. How have average height and weight at debut game changed over the years, and what's the decade-over-decade difference?
