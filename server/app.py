#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bs = []
    for b in Bakery.query.all():
        data = b.to_dict()
        bs.append(data)
    response = make_response(
    jsonify(bs),
    200,
    {"Content-Type": "application/json"}
    )
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    b = Bakery.query.filter(Bakery.id == id).first()
    b_dict = b.to_dict()

    response = make_response(
        jsonify(b_dict),
        200
    )

    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    bs = []
    for b in BakedGood.query.order_by(BakedGood.price.desc()):
        data = b.to_dict()
        bs.append(data)
    response = make_response(
    jsonify(bs),
    200,
    {"Content-Type": "application/json"}
    )
    return response     

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    b = BakedGood.query.order_by(BakedGood.price.desc()).first()
    data = b.to_dict()

    response = make_response(
        jsonify(data),
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
