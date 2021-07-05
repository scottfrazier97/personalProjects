--1. What is the average cost to rent a film in the stores?
select avg(rental_rate)
from film

    Answer: 2.98000000000000000

--2. What is the average rental cost of films by rating? On average, what is the cheapest rating of films to rent? What is the most expensive?
select 
	rating,
	avg(rental_rate) as avg_rental_rate
from 
film
group by 
rating
order by avg_rental_rate

    Answer:
    G: 2.88 - Least expensive
    R: 2.93
    NC-17: 2.97
    PG-13: 3.03
    PG: 3.05 - Most expensive

--3. How much would it cost to replace all films in the database?
select sum(replacement_cost)
from film

    Answer: $19,984.00

--4. How much would it cost to replace all films in each ratings category?
select 
    rating,
    sum(replacement_cost) as sum_of_replacement_cost
from film
group by rating
order by sum_of_replacement_cost

    Answer: 
    G: $3,582.22 - Least expensive
    PG: $3,678.06
    R: $3,945.05
    NC-17: $4,228.90
    PG-13: $4.549.77 - Most expensive

--5. How long is the longest movie in the database? How long is the shortest movie?
select 
	min(length),
	max(length)
from film

    Answer: 
    Shortest: 46 minutes
    Longest: 185 minutes

-----------------------------------------

--1. List the names and ID numbers of cities that are in the following list: Qalyub, Qinhuangdao, Qomsheh, Quilmes.
SELECT 
	city_id,
	city
FROM
	city
WHERE
	city IN ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
ORDER BY
	city_id ASC;

--2. Display the districts in the above list of cities.
select  
	c.city_id,
	c.city,
	a.district
from 
	city c 
	join address a on c.city_id = a.city_id
where c.city in ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')

--3. Using joins, find the first and last names of customers who reside in cities that begin with the letter Q.
select 
	cu.first_name,
	cu.last_name,
	c.city
from customer cu 
join address a on cu.address_id = a.address_id
join city c on a.city_id = c.city_id
where 
c.city like 'Q%'

--4. Create a query to check the movies, and the count of each movie that has been rented out by employee Jon Stephens.
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





