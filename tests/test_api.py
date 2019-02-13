"""Teste for API module."""
import unittest

from app import create_app, db, models


class TestAPI(unittest.TestCase):
    """Test for API routes."""

    def setUp(self):
        """Set up for tests."""
        self.app = create_app(config='test')
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def test_post_product(self):
        """Test wether product is created."""
        res = self.client.post('/api/produtos/', data={'name': 'Towel'})
        self.assertEqual(201, res.status_code, 'Product wasn\'t created')

    def test_return_products(self):
        """Test wether endpoint return products."""
        res = self.client.get('/api/produtos/')
        expected = []
        self.assertEqual(expected, res.json,
                         'Product must be a towel')
