from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import *
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route('/random',methods=["GET","POST"])
def random():
    cafe = Cafe()
    random_cafe = choice(cafe.query.all())
    api_dict = {
        'cafe':{
            'id':random_cafe.id,
            'img_url':random_cafe.img_url,
            'location':random_cafe.location,
            'map_url':random_cafe.map_url,
            'name':random_cafe.name,
            'seats':random_cafe.seats,
        },
        "amenities":{
            'can_take_calls': random_cafe.can_take_calls,
            'coffee_price': random_cafe.coffee_price,
            'has_sockets': random_cafe.has_sockets,
            'has_wifi': random_cafe.has_wifi,
            'has_toilet': random_cafe.has_toilet,
        }
    }
    return jsonify(api_dict)
    #print(cafe.query.all())
@app.route('/all')
def all_cafes():
    cafe = Cafe()
    all_cofes=cafe.query.all()
    api_list = []
    for cofee in all_cofes:
        api_dict={
            'id': cofee.id,
            'img_url': cofee.img_url,
            'location': cofee.location,
            'map_url': cofee.map_url,
            'name': cofee.name,
            'seats': cofee.seats,
            'can_take_calls': cofee.can_take_calls,
            'coffee_price': cofee.coffee_price,
            'has_sockets': cofee.has_sockets,
            'has_wifi': cofee.has_wifi,
            'has_toilet': cofee.has_toilet,
        }
        api_list.append(api_dict)
    return jsonify(cafes=api_list)
@app.route('/search')
def search():
    cafe = Cafe()
    location = request.args.get('loc')
    print(location)
    location_cafes=cafe.query.filter_by(location=location).all()
    print(location_cafes)
    if location_cafes:
        api_list = []
        for cofee in location_cafes:
            api_dict={
                'id': cofee.id,
                'img_url': cofee.img_url,
                'location': cofee.location,
                'map_url': cofee.map_url,
                'name': cofee.name,
                'seats': cofee.seats,
                'can_take_calls': cofee.can_take_calls,
                'coffee_price': cofee.coffee_price,
                'has_sockets': cofee.has_sockets,
                'has_wifi': cofee.has_wifi,
                'has_toilet': cofee.has_toilet,
            }
            api_list.append(api_dict)
        return jsonify(cafes=api_list)
    else:
        return jsonify(error={
            'Not Found': 'Sorry We dont have a caffe in that location',
        })

## HTTP POST - Create Record
@app.route('/add', methods=['GET','POST'])
def add():
    api_key = request.args.get('api_key')
    if api_key == "TopSecretAPIKey":
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    else:
        return jsonify(response={"error": "Incorrect API KEY"})
## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>',methods=['GET','POST','PUT','PATCH'])
def update_price(cafe_id):
    cafe = Cafe()
    coffe = cafe.query.get(cafe_id)
    new_price = request.args.get('new_price')
    if not new_price:
        return jsonify(error={"Not Found": "The new_price was not given"}),404
    if coffe:
        coffe.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Successfully added the new cafe."}),200
    else:
        return jsonify(error={"Not Found": "Sorry the cafe with that id was not found in the database"}) ,404
## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>',methods=['GET',"DELETE"])
def delete_cafe(cafe_id):
    cafe = Cafe()
    api_key = request.args.get('api_key')
    coffe = cafe.query.get(cafe_id)
    if api_key == "TopSecretAPIKEY":
        if coffe:
            db.session.delete(coffe)
            db.session.commit()
            return jsonify({"success": "Successfully deleted cafe."}),200
        else:
            return jsonify(error={"Not Found": "Sorry the cafe with that id was not found in the database"}), 404

    else:
        return jsonify({"error":"Sorry, that's not allowed. Make sure you have the correct api_key"}), 404

if __name__ == '__main__':
    app.run(debug=True)
