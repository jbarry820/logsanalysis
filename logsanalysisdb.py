#! /usr/bin/env python3

import psycopg2
DB_NAME = "news"


# 1. This creates a dictionary for the results of top_three_articles
top_three_articles_result = dict()
top_three_articles_result['title'] = """'\n1. The 3 most popular
 articles of all time are:\n'"""


# 1. What are the most popular three articles of all time?
def top_three_articles():
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select title, article_views from article_views limit 3")
    results = c.fetchall()
    db.close()
    return results


# 1. This will be called to print the top 3 articles
def print_top_three_articles():
    print (top_three_articles_result['title'])
    for result in top_three_articles_result['results']:
        print('\t' + str(result[0]) + ' ---> '
            + str(result[1]) + ' views')


# 1. This stores the results of top_three_articles
top_three_articles_result['results'] = top_three_articles()


# 1. This prints the formatted output of top_three_articles
print_top_three_articles()

# ------------------------------------------

# 2. This creates a dictionary for the results of top_three_authors
top_three_authors_result = dict()
top_three_authors_result['title'] = """'\n2. The 3 most popular authors
of all time are:\n'"""


# 2. What are the most popular three authors of all time?
def top_three_authors():
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("SELECT * FROM authors_view")
    results = c.fetchall()
    db.close()
    return results


# 2. This will be called to print the top 3 authors
def print_top_three_authors():
    print (top_three_authors_result['title'])
    for result in top_three_authors_result['results']:
        print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' views')


# 2. This stores the results of top_three_authors
top_three_authors_result['results'] = top_three_authors()


# 2. This prints the formatted output of top_three_authors
print_top_three_authors()

# ------------------------------------------

# 3. This creates a dictionary for the results of days_most_errors
days_most_errors_result = dict()
days_most_errors_result['title'] = "\n3. The days with errors over 1% :\n"


# 3. What are the days with errors over 1%?
def days_most_errors():
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute('select * from error_view where "Error_Percent" > 1')
    rows = c.fetchall()
    db.close()
    return rows


# 3. This will be called to print the days with most errors
def print_days_most_errors():
    print (days_most_errors_result['title'])
    for result in days_most_errors_result['results']:
        print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' %')

# 3. This stores the results of top_three_articles
days_most_errors_result['results'] = days_most_errors()

# 3. This prints the formatted output of top_three_articles
print_days_most_errors()
