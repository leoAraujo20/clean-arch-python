from abc import ABC, abstractmethod

from src.domain.model.users import User


class UsersRepositoryInterface(ABC):
	"""Repository for managing user entities in the database."""

	@abstractmethod
	def insert_user(self, first_name: str, last_name: str, age: int) -> None:
		"""Insert a new user into the database."""
		pass

	@abstractmethod
	def get_user(self, first_name: str, last_name: str, age: int) -> User:
		"""Retrieve a user from the database."""
		pass
