from flask import Blueprint, jsonify
import rest_service

api = Blueprint("api", __name__)

@api.route("/scripts", methods=["GET"])
def get_all_scripts():
    return jsonify(rest_service.get_all_scripts())

@api.route("/scripts/<script_name>", methods=["POST"])
def execute_script(script_name):
    rest_service.execute_script(script_name)
    return "", 200
