import os
import uuid

from sqlalchemy import create_engine, MetaData, Table, Column, String, Uuid, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, registry

from chatroom.model import ChatMessage


class DatabaseInitializer:

    metadata = None
    engine = None
    session_maker = None

    @classmethod
    def initialize(cls, connection_string):
        if cls.metadata is None:
            cls.connection_string = connection_string
            cls.engine = create_engine(connection_string, echo=True)
            cls.session_maker = sessionmaker(bind=cls.engine)
            cls.metadata = MetaData()

            chatmessage_table = Table(
                'chatmessages',
                cls.metadata,
                Column('id', Uuid, primary_key=True),
                Column('user', String(50)),
                Column('message', String(512)),
                Column('time', DateTime)
            )
            PrimaryKeyConstraint('chatmessages', name='PK_chatmessages')

            registry().map_imperatively(ChatMessage, chatmessage_table, primary_key=chatmessage_table.c.id)


    @classmethod
    def create_session(cls):
        """
        Creates a new connection and transction to the database
        :return: A SQLAlchemy Session
        """
        return cls.session_maker()

    @classmethod
    def ensure_database(cls):
        if (not cls.database_exists()):
            cls.create_database()

    @classmethod
    def create_database(cls):
        """
        Creates the required tables in the database
        :return: None
        """
        cls.metadata.create_all(cls.engine)

    @classmethod
    def remove_database(cls):
        """
        Removes all tables from the database and finally the database file
        :return: None
        """
        cls.metadata.drop_all(cls.engine)
        cls.engine.dispose()
        exists = cls.database_exists()
        if exists:
            os.remove(cls.get_path())

    @classmethod
    def database_exists(cls):
        exists = os.path.exists(cls.get_path())
        return exists

    @classmethod
    def get_path(cls):
        path = cls.connection_string.replace('sqlite:///', '')
        return path

    @classmethod
    def recreate_database(cls):
        """
        Removes the database completely and recreates it
        :return: None
        """
        cls.remove_database()
        cls.create_database()