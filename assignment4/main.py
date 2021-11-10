from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template
from flask.json import jsonify
from Paragraphs import CoinInfo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:5432@localhost/assignment4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

db = SQLAlchemy(app)

class Paragraphs(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    coin_name =  db.Column(db.String)

    body = db.Column(db.String)

    title = db.Column(db.String)

    link =  db.Column(db.String)

    def __init__(self, coin_name, title, body, link):

        self.coin_name = coin_name

        self.title = title

        self.body = body

        self.link = link


    def __repr__(self):

        return '<title %r>' % self.title

db.create_all()

@app.route("/coin", methods = ['POST', 'GET'])
def coininfo():
    if request.method == 'POST':

        coin_name = request.form['coin'].lower()

        db_articles = Paragraphs.query.filter_by(coin_name = coin_name).all()

        if (db_articles):
            return render_template('web.html', articles = db_articles)

        coininfo = CoinInfo()
        articles = coininfo.get_paragraphs(coin_name)

        for article in articles:
            db.session.add(Paragraphs(coin_name, article['title'], article['body'], article['link']))

        
        db.session.commit()

        return render_template('web.html', articles = articles)


       
    elif request.method == 'GET':
        return render_template('web.html')





if __name__ == '__main__':
    app.run(debug=True)