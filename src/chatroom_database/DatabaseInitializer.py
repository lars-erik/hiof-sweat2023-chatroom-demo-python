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
            cls.engine = create_engine(connection_string)
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
        path = cls.connection_string.replace('sqlite:///', '')
        if os.path.exists(path):
            os.remove(path)

    @classmethod
    def recreate_database(cls):
        """
        Removes the database completely and recreates it
        :return: None
        """
        cls.remove_database()
        cls.create_database()