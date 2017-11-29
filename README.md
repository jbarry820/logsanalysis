# Logs Analysis Project

This is the repo for [Udacity's Logs Analysis Project]() in the Full
Stack Web Developer Nanodegree Program. This file explains how to use
the files that are included.

## Table of Contents

* [Instructions](#instructions)
* [Creator](#creators)

## How Views Were Created

* article_view view
	"CREATE OR REPLACE VIEW article_views
        AS
        SELECT
        articles.title, authors.name as author,
        count(*) AS article_views
        FROM log, articles, authors
        WHERE articles.slug = "substring"(log.path, 10) and authors.id = articles.author
        GROUP BY articles.title, articles.author, authors.name
        ORDER BY (COUNT(*)) DESC limit 3;"
* status_date view
"CREATE OR REPLACE VIEW status_date
	AS
	SELECT id, status, date(time) FROM log;"
* authors_view view
	CREATE OR REPLACE VIEW authors_view
	AS
	select authors.name as Author,
	count(*) as Views
	from log, articles, authors
	where articles.slug = "substring"(log.path, 10) and authors.id = articles.author
	group by authors.name
	order by (count(*)) desc;
* error_view view -
"create or replace view error_view
	as select
	date,round(100.0*sum(case status_date.status when '200 OK' then 0 else 1 end)
	/count(status_date.status),3) as "Error_Percent" from status_date group by
	date order by "Error_Percent" desc;"

## Instructions

* clone the project from [https://github.com/jbarry820/logsanalysis]
(https://github.com/jbarry820/logsanalysis).
* This needs to be cloned into the subdirectory that is shared with your
vagrant virtual machine.
* Open a vagrant environment with "Vagrant up" and "Vagrant ssh"
* From the logsanalysis subdirectory run "python3 logsanalysisdb.py"
* Three print statments in the py file will execute top_three_articles(),
most_pop_authors() and days_most_errors()

## Creator

* Jim Barry
    - [https://github.com/jbarry820](https://github.com/jbarry820)

With the help of:

* Udacity videos
* Udacity Forums - johan.soetens helped by guiding me toward using "Case"
* The Python Mega Course from Udemy
* Online research
* Github repo "https://github.com/sagarchoudhary96/Log-Analysis" - This helped me
understand how to use Case for the question on errors.
