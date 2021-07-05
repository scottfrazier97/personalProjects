--***SEVERAL tables being joined through the proper pipeline of the ERD.***
select *
from actor a 
join film_actor fa on a.actor_id = fa.actor_id
join film f on fa.film_id = f.film_id

--***PULLING specific columns from the joined tables***
select 
a.actor_id,
a.first_name,
a.last_name,
f.film_id,
f.title,
f.rating
from actor a 
join film_actor fa on a.actor_id = fa.actor_id
join film f on fa.film_id = f.film_id

--***WRITING a four layer-deep join, via the ERD***
select 
*
from
customer c
join rental r on c.customer_id = r.rental_id
join inventory i on r.inventory_id = r.inventory_id
join film f on i.film_id = f.film_id
where title = 'BLANKET BEVERLY'

--***SUBQUERY, good use when dealing with aggregation as a filter***
select
* 
from film
where rental_rate = (
	select 
	max(rental_rate)
	from film
)