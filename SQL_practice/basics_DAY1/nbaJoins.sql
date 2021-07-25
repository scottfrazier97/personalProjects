-- Create tables and import data
-- Drop table if exists
DROP TABLE IF EXISTS players;

-- Create new table
CREATE TABLE players (
  player_id serial primary key,
  player VARCHAR,
  height INT,
  weight INT,
  college VARCHAR,
  born INT,
  birth_city VARCHAR,
  birth_state VARCHAR,
  last_updated timestamp default localtimestamp
);

-- Verify successful data import
SELECT * FROM players;

-- Drop if exists
DROP TABLE IF EXISTS seasons_stats;

-- Create new table
CREATE TABLE seasons_stats (
  id serial primary key,
  player_id INT,
  year DEC,
  position VARCHAR,
  age DEC,
  Tm VARCHAR,
  G VARCHAR,
  TS_Percentage DEC,
  FTr DEC,
  OWS DEC,
  DWS DEC,
  WS DEC,
  FG DEC,
  FGA DEC,
  FG_Percentage DEC,
  Two_Points DEC,
  Two_PA DEC,
  Two_Point_Percentage DEC,
  eFG_Percentage DEC,
  FT DEC,
  FTA DEC,
  FT_Percentage DEC,
  AST DEC,
  PF DEC,
  PTS DEC,
  last_updated timestamp default localtimestamp
);

-- Verify successful data import
SELECT * FROM seasons_stats;

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------

select * from seasons_stats

--***FIXING INDEXING***
update seasons_stats
set player_id = player_id + 1;


--***BASIC JOINING OF TWO CSVs***
select 
* 
from 
players p
join seasons_stats s on p.player_id = s.player_id
where
s.year = 2015

--***MORE JOIN PRACTICE***
select 
	p.player_id,
	p.player,
	s.year,
	s.position,
	s.fg,
	s.fga,
	s.ft,
	s.ft_percentage,
	s.pts
from
	players p
	left join seasons_stats s on p.player_id = s.player_id
where
	s.year = 2015
order by s.pts desc


select 
	year,
	sum(pts)
from 
seasons_stats
group by year
order by year


