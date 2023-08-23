from flask import Flask, render_template, request, redirect
from repositories import user_repository
from repositories import task_repository
from models.user import User

from flask import Blueprint
users_blueprint = Blueprint("users", __name__)


# INDEX
# GET '/users'

@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", all_users = users)

# NEW
# GET '/users/new'

@users_blueprint.route("/users/new")
def new_user():
    
    return render_template("users/new.html")

# CREATE
# POST '/users'

@users_blueprint.route("/users", methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    user = User(first_name, last_name)
    user_repository.save(user)
    return redirect('/users')

# SHOW
# GET '/user/<id>'
@users_blueprint.route("/users/<id>")
def show_user(id):
    user = user_repository.select(id)
    return render_template("users/show.html", user=user)

# EDIT
# GET '/users/<id>/edit'
@users_blueprint.route("/users/<id>/edit")
def edit_user(id):
    user = user_repository.select(id)
    return render_template("users/edit.html", user=user)

# UPDATE
# PUT '/users/<id>'
@users_blueprint.route("/users/<id>", methods=['POST'])
def update_user(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    user = User(first_name, last_name, id)
    user_repository.update(user)
    return redirect('/users')

# DELETE
# DELETE '/users/<id>
@users_blueprint.route("/users/<id>/delete", methods=['POST'])
def delete_user(id):
    user_repository.delete(id)
    return redirect('/users')
    


