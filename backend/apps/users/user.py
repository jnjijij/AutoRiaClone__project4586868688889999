from urllib import request

from flask import redirect, url_for

from backend.core import db
from backend.apps.users.models import UserMixin, ROLE_ADMIN
from flask import current_user

from frontend.system.cars_search import app


class User(UserMixin, db.Model):
    # ...
    query = None
    role = db.Column()
    # ...


def role():
    return None

@app.route("/change_role", methods=["POST"])
def change_role():
    if not current_user.is_authenticated or current_user.role != ROLE_ADMIN:
        return "Forbidden", 403

    user_id = request.form["user_id"]
    new_role = request.form["new_role"]

    user = User.query.get(user_id)
    if user is None:
        return "User not found", 404

    user.role = new_role
    db.session.commit()

    return redirect(url_for("admin"))