"""Model module."""
from sqlalchemy_mixins import AllFeaturesMixin

from app.extensions import db


class BaseModel(db.Model, AllFeaturesMixin):
    """BaseModel class for models."""

    _session = db.session
    __abstract__ = True
    __repr__ = AllFeaturesMixin.__repr__

    def _asdict(self):
        """Add support to simplejson encoder."""
        return self.to_dict()


class Product(BaseModel):
    """Product model."""

    __tablename__ = 'products'
    __repr_attrs__ = ['name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
