"""Teste for API module."""
import unittest

from flask import url_for

from app import create_app, db, models


class TestAPI(unittest.TestCase):
    """Test for API routes."""

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(config='test')
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.test_request_context()

    def setUp(self):
        """Set up for tests."""
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.app_context.pop()

    def test_post_product(self):
        """Test whether product is created."""
        res = self.client.post(url_for('api.save_products'),
                               data={'name': 'Towel'})
        self.assertEqual(201, res.status_code, 'Product wasn\'t created')

    def test_return_products(self):
        """Test whether endpoint returns list of products."""
        expected = [
            {
                'id': 1,
                'name': 'Towel',
            }
        ]
        models.Product.create(name='Towel')
        res = self.client.get(url_for('api.get_products'))
        self.assertEqual(expected, res.json,
                         'In products should have a towel')

    def test_return_only_specified_product(self):
        """Test whether endpoint returns product by id."""
        expected = {
            'id': 1,
            'name': 'Towel',
        }
        models.Product.create(id=1, name='Towel')
        res = self.client.get(url_for('api.get_product', id=1))
        self.assertEqual(expected, res.json, 'Towel wasn\'t returned')
