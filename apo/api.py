from flask import (
    flash,
    make_response,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)
from flask_login import current_user, login_required

from apo import app, db, login_manager
from apo.forms import LostReportForm
from apo.models import (
    User,
    BacktestClasses,
    Backtest,
    Chargers,
)  # , LostReport, LostItem

from apo.helpers import chargers

"""
API
"""


@app.route("/api/v1/chargers", methods=["GET"])
def list_chargers_api():
    app.logger.info(f"/api/v1/chargers called")
    return make_response(chargers.list_chargers(), 200)


# @login_required
@app.route("/api/v1/chargers/admin", methods=["GET"])
def list_chargers_admin_api():
    app.logger.info(f"/api/v1/chargers/admin called")
    return make_response(chargers.list_chargers(True), 200)


# @login_required
@app.route("/api/v1/chargers/admin/edit/desc", methods=["PUT"])
def update_charger_desc_api():
    app.logger.info(f"/api/v1/chargers/admin/checkout called")
    app.logger.debug(f"response data: {request.get_json()}")
    return chargers.edit_desc(request.get_json())


# @login_required
@app.route("/api/v1/chargers/admin/checkout", methods=["PUT"])
def checkout_charger_api():
    app.logger.debug(f"/api/v1/chargers/admin/checkout")
    app.logger.debug(f"response data: {request.get_json()}")
    return chargers.checkout(request.get_json())


# @login_required
@app.route("/api/v1/chargers/admin/checkin", methods=["PUT"])
def checkin_charger_api():
    app.logger.debug(f"/api/v1/chargers/admin/checkin")
    app.logger.debug(f"response data: {request.get_json()}")
    return chargers.checkin(request.get_json())


# @login_required
@app.route("/api/v1/chargers/admin/create", methods=["POST"])
def create_charger_api():
    app.logger.debug(f"/api/v1/chargers/admin/create")
    app.logger.debug(f"response data: {request.get_json()}")
    return chargers.create(request.get_json())


# @login_required
@app.route("/api/v1/chargers/admin/delete", methods=["DELETE"])
def delete_charger_api():
    app.logger.debug(f"/api/v1/chargers/admin/delete")
    app.logger.debug(f"response data: {request.get_json()}")
    return chargers.delete(request.get_json())