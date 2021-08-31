from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Add the connection string to the application sqlite (testing)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///example.db"

#db (database) Links the db variable the the SQLAlchemy that is in the application. 
db = SQLAlchemy(app)

db.drop_all() 

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    rating = db.Column(db.String(30))
    developer = db.Column(db.String(30))
    price = db.Column(db.Integer)

db.create_all()

crazy_taxi = Games(name="Crazy Taxi", rating="5", developer="Sega", price="0")
crash_bandicoot = Games(name="Crash Bandicoot", rating="6", developer="Naughty Dog", price="40")

#This will add the game to the database
db.session.add(crazy_taxi)
db.session.add(crash_bandicoot)


db.session.commit()

@app.route('/', methods=['GET'])
def home(): 
    all_games = Games.query.all()
    print(all_games)
    games_string = ""
    for game in all_games:
        games_string = f"{game.name}, {game.rating}, {game.developer}, {game.price}"
    return games_string

if __name__=='__main__':
    app.run(debug=True)