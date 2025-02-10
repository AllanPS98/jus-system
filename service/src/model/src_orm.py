from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class SrcOrm:

    def __init__(self, connection_string):
        engine = create_engine(connection_string, pool_size=2, max_overflow=6, pool_timeout=30, pool_pre_ping=True)
        self.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    def add_object(self, obj):
        self.session.add(obj)
        self.commit()

    def commit(self):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def remove_session(self):
        self.session.remove()

    def close(self):
        self.session.close()