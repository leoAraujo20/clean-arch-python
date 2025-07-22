"""Database connection handler for the application."""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class DBConnectionHandler:
	"""Handles the database connection for the application."""

	def __init__(self) -> None:
		"""Initialize the database connection handler."""
		self.__connection_string = 'sqlite:///clean_database.db'
		self.__engine = self.__create_database_engine()
		self.session = None

	def __create_database_engine(self) -> Engine:
		return create_engine(self.__connection_string)

	def get_engine(self) -> Engine:
		"""Get the database engine."""
		return self.__engine

	def __enter__(self) -> 'DBConnectionHandler':
		"""Enter the runtime context related to this object."""
		self.session = Session(self.__engine)
		return self

	def __exit__(self, exc_type, exc_value, traceback) -> None:
		"""Exit the runtime context related to this object."""
		if self.session:
			self.session.close()
