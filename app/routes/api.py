"""API."""
from flask import Blueprint, jsonify, request

from app import models

api = Blueprint('api', __name__)


@api.route('/api/produtos/', methods=['GET'])
def get_products():
    """Return products."""
    products = models.Product.all()
    return jsonify(products)


@api.route('/api/produtos/', methods=['POST'])
def save_products():
    """Save products."""
    product = models.Product.create(**request.form.to_dict())
    return jsonify(product), 201


@api.route('/api/produtos/<int:id>', methods=['GET'])
def get_product(id):
    product = models.Product.find_or_fail(id)
    return jsonify(product), 200
