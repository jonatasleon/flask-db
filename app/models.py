"""Model module."""
from sqlalchemy_mixins import ActiveRecordMixin, ReprMixin

from app.extensions import db


class BaseModel(db.Model, ActiveRecordMixin, ReprMixin):
    """BaseModel class for models."""

    _session = db.session
    __abstract__ = True
    __repr__ = ReprMixin.__repr__


class Product(BaseModel):
    """Product model."""

    __tablename__ = 'products'
    __repr_attrs__ = ['name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
