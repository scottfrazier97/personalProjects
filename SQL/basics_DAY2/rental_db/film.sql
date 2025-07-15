select * from film

--***COUTNING total number of films based on the count of film_id values***
select 
count (film_id) as total_films
from film

--***AGGREGATING to find unique count of each movie by rating***
select 
	rating,
	count(*)
from 
	film 
group by 
	rating
	
----	
select 
	rating,
	avg(rental_duration)
from
	film
group by 
	rating
	
----
select 
	rental_duration,
	avg(rental_rate) as avg_rental_rate
from 
film
group by 
rental_duration

----
select 
* from film
where rental_duration = 3
and rental_rate = 4.99
----
----
select 
	rental_duration,
	avg(rental_rate) as avg_rental_rate
from 
film
group by 
rental_duration
--***IF filtering on aggregation, must use "having" keyword, not WHERE "...."
having 
	avg(rental_rate) > 3