from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
db = SQLAlchemy(app)
migrate = Migrate(app, db)




class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    species = db.Column(db.String(255))
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'))
    
    zookeeper = db.relationship('Zookeeper', back_populates='animals')
    enclosure = db.relationship('Enclosure', back_populates='animals')

class Zookeeper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    birthday = db.Column(db.String(255))
    
    animals = db.relationship('Animal', back_populates='zookeeper')

class Enclosure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(255))
    open_to_visitors = db.Column(db.Boolean)
    
    animals = db.relationship('Animal', back_populates='enclosure')

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    return render_template('animal.html', animal=animal)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    return render_template('zookeeper.html', zookeeper=zookeeper)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    return render_template('enclosure.html', enclosure=enclosure)

if __name__ == "__main__":
    app.run(debug=True)
