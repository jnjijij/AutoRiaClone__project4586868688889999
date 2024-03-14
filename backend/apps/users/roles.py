from functools import wraps
from flask import abort, request, current_app, redirect, url_for
from flask import current_user

from backend.apps.core import db
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