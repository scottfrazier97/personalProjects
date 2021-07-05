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

