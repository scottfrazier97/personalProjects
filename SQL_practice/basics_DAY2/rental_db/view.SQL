--A view is a virtual table that can be created from a single table, multiple tables, or another view. 
--It is NOT part of the schema, but it has rows and columns.
--They are created using the CREATE VIEW statement.
--Can be re-run at a later date and the data will be updated, e.g.: If Jon Stephens makes another sale.
--CAN'T be updated, READ-ONLY.

EXAMPLE: 

CREATE VIEW myBoysSales AS

select 
	f.title,
	count(*)
from 
	staff s
	join rental r on s.staff_id = r.staff_id
	join inventory i on r.inventory_id = i.inventory_id
	join film f on i.film_id = f.film_id
where
	s.first_name = 'Jon' AND 
	s.last_name = 'Stephens'
group by 
	f.title
order by 
	count(*) desc

........ AND THEN: 

check "Views" under schema to see that it saved, and you can now call the view by doing the following:

select 
* 
from 
myBoysSales