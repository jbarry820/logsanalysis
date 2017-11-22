#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from logsanalysisdb import top_three_articles, most_pop_authors, days_most_errors

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Log Analysis</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>Log Analysis</h1>
    <form method=post>
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="go" type="submit">Top 3 Articles</button></div>
    </form>
    <!-- Top 3 articles will go here -->
%s
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''


@app.route('/', methods=['GET'])
def main():
  '''Main page of the Log Analysis.'''
  posts = "".join(POST % (date, text) for text, date in get_posts())
  html = HTML_WRAP % posts
  return html


@app.route('/', methods=['POST'])
def post():
  '''New post submission.'''
  message = request.form['content']
  add_post(message)
  return redirect(url_for('main'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

