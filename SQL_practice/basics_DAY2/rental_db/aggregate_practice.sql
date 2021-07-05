select * from film

select 
rating,
sum(replacement_cost) as sum_of_replacement_cost
from film
group by rating
order by sum_of_replacement_cost

select sum(replacement_cost)
from film

select 
	min(length),
	max(length)
from film

select 
	first_name,
	count(*)
from 
actor
group by first_name
