from src.data.use_cases.user_finder import UserFinder
from src.infra.db.tests.users_repository import UsersRepositorySpy


def test_user_finder() -> None:
	"""Test case for the UserFinder use case."""
	first_name = 'Test'
	user_repository = UsersRepositorySpy()
	user_finder = UserFinder(user_repository)
	response = user_finder.find(first_name)

	assert response['type'] == 'Users'
	assert response['count'] == len(response['attributes'])
	assert response['attributes'] != []
	assert user_repository.get_user_attributes['first_name'] == first_name
