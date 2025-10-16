class User:
	"""User domain model."""

	def __init__(self, id: int, first_name: str, last_name: str, age: int) -> None:
		"""Initialize the User domain model."""
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
