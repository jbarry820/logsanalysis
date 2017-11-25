# Version Control with Git

This is the repo for [Udacity's Logs Analysis Project]() in the Full
Stack Web Developer Nanodegree Program. This file explains how to use
the files that are included.

## Table of Contents

* [Instructions](#instructions)
* [Creator](#creators)

## How Views Were Created

* article_view was created by  - "CREATE OR REPLACE VIEW article_views AS
SELECT articles.author, count(*) AS
article_views FROM log, articles WHERE articles.slug = substring(log.path,10)
GROUP BY articles.author limit 5;"
* status_date view was created by - "CREATE OR REPLACE VIEW status_date AS
SELECT id, status, date(time) FROM log;"

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
* Udacity Forums
* The Python Mega Course from Udemy
* Online research
