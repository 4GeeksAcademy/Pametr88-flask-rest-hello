"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planets, Films, Species, Favorites
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()                                        #trae todo
    if len(users) < 1:                                              #verifica que no haya usuarios
        return jsonify({"msg": "not found"}), 404
    serialized_users = list(map(lambda x: x.serialize(), users))    #un mapeo de toda la informacion de user que encuentres
    return serialized_users, 200

@app.route('/user/<int:user_id>', methods=['GET'])                          # destina la ruta int es el entero
def get_one_user(user_id):                                                  # funcion donde pasamos un parametro
    user = User.query.get(user_id)                                          # revisa la tabla query.get trae el especifico lo que le pedimos en parametro
    if user is None:                                                        # None es null si no existe retorna un objeto ""
        return jsonify({"msg": f"user with id {user_id} not found"}), 404
    serialized_user = user.serialize()
    return serialized_user, 200

@app.route('/user', methods=['POST'])
def create_one_user():
    body = json.loads(request.data)
    new_user = User(
        name = body["name"],
        email = body["email"],
        password = body["password"],
        is_active = True
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "user created succesfull", "user_added": new_user}), 200

@app.route('/user/<int:user_id>', methods=['PUT'])
def edit_one_user(user_id):
    body = json.loads(request.data)
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": f"user with id {user_id} not found"}), 404
    for key, value in body.items(): 
        setattr(user, key, value )
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "user edited succesfull", "user_edited": user.serialize()}), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_one_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": f"user with id {user_id} not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "user deleted"}), 200

@app.route('/Character', methods=['GET'])
def handle_Charact():
    characters = Character.query.all()                                       
    if len(characters) < 1:                                              
        return jsonify({"msg": "not found"}), 404
    serialized_characters = list(map(lambda x: x.serialize(), characters))    
    return serialized_characters, 200

@app.route('/Character/<int:Character_id>', methods=['GET'])
def get_one_character(Character_id):
    character = Character.query.get(Character_id)
    if character is None:
        return jsonify({"msg": f"Character with id {Character_id} not found"}), 404
    serialized_character = character.serialize()
    return serialized_character, 200

@app.route('/Character', methods=['POST'])
def create_one_character():
    body = json.loads(request.data)
    new_character = Character(
        name = body["name"],
        height = body["name"],
        mass = body["mass"],
        hair_color = body["hair_color"],
        skin_color = body["skin_color"],
        eye_color = body["eye_color"],
    )
    db.session.add(new_character)
    db.session.commit()
    return jsonify({"msg": "Character created succesfull", "character_added": new_character}), 200

@app.route('/Character/<int:Character_id>', methods=['PUT'])
def edit_one_character(Character_id):
    body = json.loads(request.data)
    character = Character.query.get(Character_id)
    if character is None:
        return jsonify({"msg": f"Character with id {Character_id} not found"}), 404
    for key, value in body.items(): 
        setattr(character, key, value )
    db.session.add(character)
    db.session.commit()
    return jsonify({"msg": "character edited succesfull", "character_edited": character.serialize()}), 200

@app.route('/Character/<int:Character_id>', methods=['DELETE'])
def delete_one_character(Character_id):
    character = Character.query.get(Character_id)
    if character is None:
        return jsonify({"msg": f"Character with id {Character_id} not found"}), 404
    db.session.delete(character)
    db.session.commit()
    return jsonify({"msg": "Character deleted"}), 200

@app.route('/Planets', methods=['GET'])
def handle_Planet():
    planets = Planets.query.all()                                       
    if len(planets) < 1:                                              
        return jsonify({"msg": "not found"}), 404
    serialized_planets = list(map(lambda x: x.serialize(), planets))    
    return serialized_planets, 200

@app.route('/Planets/<int:Planets_id>', methods=['GET'])
def get_one_planet(Planet_id):
    planet = Planets.query.get(Planet_id)
    if planet is None:
        return jsonify({"msg": f"Planet with id {Planet_id} not found"}), 404
    serialized_planet = planet.serialize()
    return serialized_planet, 200

@app.route('/Planets', methods=['POST'])
def create_one_planet():
    body = json.loads(request.data)
    new_planet = Planets(
        name = body["name"],
        diameter = body["diameter"],
        rotation_period = body["rotation_period"],
        orbital_period = body["orbital_period"],
        gravity = body["gravity"],
        population = body["population"],
        climate = body["climate"],
    )
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({"msg": "Planet created succesfull", "planet_added": new_planet}), 200

@app.route('/Planets/<int:Planets_id>', methods=['PUT'])
def edit_one_planet(Planet_id):
    body = json.loads(request.data)
    planet = Planets.query.get(Planet_id)
    if planet is None:
        return jsonify({"msg": f"Planet with id {Planet_id} not found"}), 404
    for key, value in body.items(): 
        setattr(planet, key, value )
    db.session.add(planet)
    db.session.commit()
    return jsonify({"msg": "Planet edited succesfull", "planet_edited": planet.serialize()}), 200

@app.route('/Plantes/<int:Planets_id>', methods=['DELETE'])
def delete_one_planet(Planet_id):
    planet = Planets.query.get(Planet_id)
    if planet is None:
        return jsonify({"msg": f"Planet with id {Planet_id} not found"}), 404
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"msg": "Planet deleted"}), 200

@app.route('/Films', methods=['GET'])
def handle_Film():
    films = Films.query.all()                                       
    if len(films) < 1:                                              
        return jsonify({"msg": "not found"}), 404
    serialized_films = list(map(lambda x: x.serialize(), films))    
    return serialized_films, 200

@app.route('/Films/<int:Films_id>', methods=['GET'])
def get_one_film(Film_id):
    film = Films.query.get(Film_id)
    if film is None:
        return jsonify({"msg": f"Film with id {Film_id} not found"}), 404
    serialized_film = film.serialize()
    return serialized_film, 200

@app.route('/Films', methods=['POST'])
def create_one_film():
    body = json.loads(request.data)
    new_film = Films(
        name = body["name"],
        created = body["created"],
        edited = body["edited"],
        producer = body["producer"],
        title = body["title"],
        director = body["director"],
        release_date = body["release_date"],
    )
    db.session.add(new_film)
    db.session.commit()
    return jsonify({"msg": "Film created succesfull", "film_added": new_film}), 200

@app.route('/Films/<int:Films_id>', methods=['PUT'])
def edit_one_film(Films_id):
    body = json.loads(request.data)
    film = Films.query.get(Films_id)
    if film is None:
        return jsonify({"msg": f"Film with id {Films_id} not found"}), 404
    for key, value in body.items(): 
        setattr(film, key, value )
    db.session.add(film)
    db.session.commit()
    return jsonify({"msg": "Film edited succesfull", "film_edited": film.serialize()}), 200

@app.route('/Films/<int:Films_id>', methods=['DELETE'])
def delete_one_film(Films_id):
    film = Films.query.get(Films_id)
    if film is None:
        return jsonify({"msg": f"Film with id {Films_id} not found"}), 404
    db.session.delete(film)
    db.session.commit()
    return jsonify({"msg": "Film deleted"}), 200

@app.route('/Species', methods=['GET'])
def handle_Specie():
    species = Species.query.all()                                       
    if len(species) < 1:                                              
        return jsonify({"msg": "not found"}), 404
    serialized_species = list(map(lambda x: x.serialize(), species))    
    return serialized_species, 200

@app.route('/Species/<int:Species_id>', methods=['GET'])
def get_one_specie(Specie_id):
    specie = Species.query.get(Specie_id)
    if specie is None:
        return jsonify({"msg": f"Film with id {Specie_id} not found"}), 404
    serialized_specie = specie.serialize()
    return serialized_specie, 200

@app.route('/Species', methods=['POST'])
def create_one_specie():
    body = json.loads(request.data)
    new_specie = Species(
        name = body["name"],
        classification = body["classification"],
        designation = body["designation"],
        average_height = body["average_height"],
        average_lifespan = body["average_lifespan"],
        hair_colors = body["hair_colors"],
        skin_colors = body["skin_colors"],
    )
    db.session.add(new_specie)
    db.session.commit()
    return jsonify({"msg": "Specie created succesfull", "specie_added": new_specie}), 200

@app.route('/Species/<int:Species_id>', methods=['PUT'])
def edit_one_specie(Specie_id):
    body = json.loads(request.data)
    specie = Species.query.get(Specie_id)
    if specie is None:
        return jsonify({"msg": f"Specie with id {Specie_id} not found"}), 404
    for key, value in body.items(): 
        setattr(specie, key, value )
    db.session.add(specie)
    db.session.commit()
    return jsonify({"msg": "Specie edited succesfull", "specie_edited": specie.serialize()}), 200

@app.route('/Species/<int:Species_id>', methods=['DELETE'])
def delete_one_specie(Specie_id):
    specie = Species.query.get(Specie_id)
    if specie is None:
        return jsonify({"msg": f"Specie with id {Specie_id} not found"}), 404
    db.session.delete(specie)
    db.session.commit()
    return jsonify({"msg": "specie deleted"}), 200

@app.route('/user/<int:user_id>/favorites', methods=['GET'])
def get_all_favorites(user_id):
    favorites = Favorites.query.filter_by(user_id = user_id).all()
    if len(favorites) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_favorites = list(map(lambda x: x.serialize(), favorites))
    return serialized_favorites, 200

@app.route('/favorites', methods=['POST'])
def add_favorites():
    body = request.json 
    new_favorite = Favorites(
        user_id = body["user_id"],
        character_id = body["character_id"],
        planets_id = body["planets_id"],
        films_id = body["films_id"],
        species_id = body["species_id"] 
    )
    if new_favorite.character_id is None and new_favorite.planets_id is None and new_favorite.films_id is None and new_favorite.species_id is None:
      return jsonify({"msg": "No hay favoritos"}), 400
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({"msg": "Existe favoritos", "added_favorite": new_favorite})


@app.route('/favorites/<int:favorite_id>', methods=['DELETE'])
def delete_one_favorite(favorite_id):
    favorite = Favorites.query.get(favorite_id)
    if favorite is None:
        return jsonify({"msg": f"favorite with id {favorite_id} not found"}), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg": "favorite deleted"}), 200  


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
