#! /usr/bin/env python3

import psycopg2
DBNAME = "news"

article_query = "select title, article_views from article_views limit 3"
author_query = "SELECT * FROM authors_view"
error_query = 'select * from error_view where "Error_Percent" > 1'

article_result = dict()
article_result['title'] = """'\n1. The 3 most popular
 articles of all time are:\n'"""

author_result = dict()
author_result['title'] = """'\n1. The 3 most popular
 authors of all time are:\n'"""

error_result = dict()
error_result['title'] = """'\n1. The days with more than 1% errors are:\n'"""


def get_results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' views')


def print_error_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' %')


article_result['results'] = get_results(article_query)
author_result['results'] = get_results(author_query)
error_result['results'] = get_results(error_query)


print_results(article_result)
print_results(author_result)
print_error_results(error_result)
