from src.data.interfaces.user_repository import UsersRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


class UserFinder(UserFinderInterface):
	"""Use case for finding users."""

	def __init__(self, user_repository: UsersRepositoryInterface) -> None:
		"""Initialize the UserFinder with a user repository."""
		self.__user_repository = user_repository

	def find(self, first_name: str) -> dict:
		"""Find a user by their first name."""
		if not first_name.isalpha():
			raise Exception('O nome deve conter apenas letras.')
		if len(first_name) > 18:
			raise Exception('O nome deve ter no máximo 18 caracteres.')

		users = self.__user_repository.get_user(first_name)
		if users == []:
			raise Exception('Usuário não encontrado.')

		return {
			'type': 'Users',
			'count': len(users),
			'attributes': users,
		}
