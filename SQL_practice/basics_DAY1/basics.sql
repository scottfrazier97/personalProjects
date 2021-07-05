--***MOST of the time, you will not need to manually create table***
CREATE TABLE cities (
	--Using id, serial, and primary key creates a unique id column, and also makes it so that each row can not be replecated based on certain criteria
	id serial primary key,
	city VARCHAR(30) NOT NULL,
	state VARCHAR(5) NOT NULL,
	population INT NOT NULL,
	is_part_of_unitedStates BOOLEAN default false,
	last_updated timestamp default localtimestamp
);
-- INSERT INTO cities (city, state, population, is_part_of_unitedStates)
-- VALUES ('Alameda', 'CA', 79177, true),
-- 	('Mesa', 'AZ', 496401, true),
-- 	 ('Boerne', 'TX', 16056, true),
-- 	 ('Anaheim', 'CA', 352497, true),
-- 	 ('Tucson', 'AZ', 535677, true),
-- 	 ('Garland', 'TX', 238002, true);

select * from cities

--DEC = decimal

--select city from cities

--select city from cities where state = 'AZ'

-- select city from cities where population < 100000

-- -- select city from cities where state = 'CA'
-- -- AND population < 100000

--select * from cities limit 3

--select * from cities where state = 'TX' or state = 'CA'

--***UPDATING CERTAIN VALUES***
-- -- Update cities 
-- -- set is_part_of_unitedStates = false
-- -- where id = 6

--order by population DESC -- DESC = descending order, ASC = ascending. ASC is the default
--order by id

-- alter table cities
-- add column have_visited BOOLEAN default false;

-- -- Update cities
-- -- set have_visited = false
-- -- where id = 2;

--***DROPPING COLUMN***
-- alter table cities
-- drop column useless_column;

--***DELETING ROWS***
-- DELETE FROM cities WHERE id = 6;




