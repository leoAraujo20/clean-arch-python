"""Define the user entity model for the database."""

from sqlalchemy import Column, Integer, String

from src.infra.db.settings.base import Base


class Users(Base):
	"""User entity model for the database."""

	__tablename__ = 'Users'

	id = Column(Integer, primary_key=True, autoincrement=True)
	first_name = Column(String(255), nullable=False)
	last_name = Column(String(255), nullable=False)
	age = Column(Integer, nullable=False)

	def __repr__(self) -> str:
		"""Return the string representation of the Users model."""
		return f'Users(id={self.id}, first_name="{self.first_name}", last_name="{self.last_name}", age={self.age})'
