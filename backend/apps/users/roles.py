from functools import wraps
from os import abort

from celery import current_app
from django.shortcuts import redirect

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from rest_framework import request
from sqlalchemy.sql.functions import current_user

from backend.apps.users.routes import url_for
from backend.configs import models
from backend.core import db
from backend.apps.users import user
from backend.apps.users.models import ROLE_ADMIN, User
from frontend.system.cars_search import app


def get_current_user():
    pass


def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if request.method in ["GET", "HEAD"] and current_app.config["ALLOW_ANONYMOUS_GET"]:
                return f(*args, **kwargs)

            user = get_current_user()
            if user is None or user.role != role:
                abort(403)

            return f(*args, **kwargs)

        return wrapper

    return decorator


def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if request.method in ["GET", "HEAD"] and current_app.config["ALLOW_ANONYMOUS_GET"]:
                return f(*args, **kwargs)

            get_current_user()
            if user is None or user.role != role:
                abort(403)

            @app.route("/admin")
            @role_required(ROLE_ADMIN)
            def admin():
                return f(*args, **kwargs)

        return wrapper

    return decorator


def admin_required(args):
    pass


@app.route("/change_role", methods=["POST"])
@admin_required
def change_role():
    user_id = request.form["user_id"]
    new_role = request.form["new_role"]

    user = User.query.get(user_id)
    if user is None:
        return "User not found", 404

    if current_user.id == user.id:
        return "Cannot change your own role", 403

    user.role = new_role
    db.session.commit()

    return redirect(url_for("admin"))


class User(AbstractUser):
    ROLES = [
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
        ('sales', 'Sales'),
        ('mechanic', 'Mechanic'),
        ('partner', 'Partner'),
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='customer')


Group.objects.create(name='sellers')
