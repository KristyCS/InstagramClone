from flask import Blueprint, request
from flask.wrappers import Request
from flask_login import login_required
from app.models import db, User

user_routes = Blueprint('users', __name__)


@user_routes.route('')
@login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_user(id):
    data = request.json
    user = User.query.get(id)
    user.update(*data)
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

    
@user_routes.route('/dashboard/<string:username>')
# @login_required
def selected_user(username):
    user = User.query.filter(User.username == username).first()
    return user.to_dict()


@user_routes.route('/<string:username>/followers')
# @login_required
def user_followers(username):
    user = User.query.filter(User.username == username).first()
    followers = user.followers_dict()["followers"]
    followers_list = []
    for follower in followers:
        if follower["confirmed"] == True:
            user = User.query.get(follower["follower_id"])
            follower = user.to_simple_dict()
            followers_list.append(follower)

    return {"followers": followers_list}


@user_routes.route('/<string:username>/following')
# @login_required
def user_following(username):
    user = User.query.filter(User.username == username).first()
    following = user.following_dict()["following"]
    following_list = []
    for follow in following:
        if follow["confirmed"] == True:
            user = User.query.get(follow["user_id"])
            following = user.to_simple_dict()
            following_list.append(following)

    return {"following": following_list}
