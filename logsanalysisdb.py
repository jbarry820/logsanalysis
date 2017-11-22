# "Database code" for the Logs Analysis Project
import psycopg2

DBNAME = "news"

def top_three_articles():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("SELECT path, COUNT(*) FROM log GROUP BY path ORDER BY COUNT DESC LIMIT 3")
  rows=c.fetchall()
  db.close()
  return rows

def most_pop_authors():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select authors.name, article_views.article_views from authors join article_views on authors.id = article_views.author")
  rows=c.fetchall()
  db.close()
  return rows

def days_most_errors():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select date, count(date) from status_date group by date order by count(date) desc")
  rows=c.fetchall()
  db.close()
  return rows

print(top_three_articles())
print(most_pop_authors())
print(days_most_errors())














