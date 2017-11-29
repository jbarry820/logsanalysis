#!/usr/bin/env python3

# "Database code" for the Logs Analysis Project
import psycopg2

DBNAME = "news"


def top_three_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT * FROM article_views""")
    rows = c.fetchall()
    db.close()
    return rows


def most_pop_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT * FROM authors_view""")
    rows = c.fetchall()
    db.close()
    return rows


def days_most_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('select * from error_view where "Error_Percent" > 1')
    rows = c.fetchall()
    db.close()
    return rows

print(top_three_articles())
print(most_pop_authors())
print(days_most_errors())
