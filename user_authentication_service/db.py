#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import User, Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed: str) -> User:
        """Add a user to the database
        """
        if email and hashed:
            user = User(email=email, hashed_password=hashed)
            session = self._session
            session.add(user)
            session.commit()
            return user
        return None

    def find_user_by(self, **kwargs) -> User:
        """
        This method takes in arbitrary keyword arguments and returns the
        first row found in the users table as filtered by the method’s input
        arguments
        """
        session = self._session
        try:
            user = session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        method that takes as argument a required user_id integer and arbitrary keyword arguments, and returns None
        """
        session = self._session
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError
            session.commit()
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError
