from abc import ABC, abstractmethod


class UserFinder(ABC):
	"""Abstract base class for finding users."""

	@abstractmethod
	def find(self, first_name: str) -> dict:
		"""Find a user by their first name."""
		pass
