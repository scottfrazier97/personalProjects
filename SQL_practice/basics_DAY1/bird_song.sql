CREATE TABLE bird_song(
	id serial PRIMARY KEY,
	english_name VARCHAR,
	country VARCHAR,
	latitude DEC,
	longitude DEC,
	last_updated timestamp default localtimestamp
);

--***To load CSV, right click on table within SCHEMAS,
-- click import/ export, an then make sure import slider is on,
-- make sure header is ON if the CSV file has a header row,
-- choose file using filepath after clicking three dots,
-- choose/ delete certain columns based on what you need,
-- and also what you already have.

-- View table columns and datatypes
SELECT * FROM bird_song;

--***DROP ENTIRE TABLE***
-- DROP TABLE bird_song;

--***PULL DISTINCT DATA BASED ON COLUMN***
-- -- SELECT DISTINCT 
-- -- country
-- -- from 
-- -- bird_song
-- -- -- ***ORDER ALPHABETICALLY***
-- -- -- order by country asc

--***COUNT OF SPECIFIC DATA***
select country,
count(*)
from
bird_song
group by country;

