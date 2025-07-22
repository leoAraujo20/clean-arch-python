"""Define the declarative base class for SQLAlchemy ORM models."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
	"""Base class to be inherited by all SQLAlchemy ORM models in the project."""
