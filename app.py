from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def home():
    # return render_template('index.html')
    return index()


@app.route('/movie')
def movie():
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select * from movie250'
    data = cur.execute(sql)
    # for item in data:
    #     movie.append(item)
    movies = list(data)
    cur.close()
    conn.close()
    return render_template('movie.html',movies=movies)


@app.route('/score')
def score():
    scores = []     # 评分
    numbers = []    # 每个评分统计出的电影数
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select score, count(score) from movie250 group by score order by score'
    data = cur.execute(sql)
    for item in data:
        scores.append(str(item[0]))
        numbers.append(item[1])
    cur.close()
    conn.close()

    return render_template('score.html', scores=scores, numbers=numbers)


@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/team')
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run()
