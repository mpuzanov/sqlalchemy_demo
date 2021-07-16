import os
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
print('dotenv_path', dotenv_path)
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
db_url = os.environ.get("DATABASE_URL")

engine = create_engine(db_url, fast_executemany=True, echo=False)


class DbManager:

    def __init__(self, url: str = db_url):
        self._engine = create_engine(url, fast_executemany=True, echo=False)

    def get_execute_sql(self, query: str, params: dict) -> list[dict]:
        """ Получение списка словарей результата выполнения запроса """

        # 1 вариант запуска запроса
        db_session = sessionmaker(bind=self._engine)
        session = db_session()
        try:
            result = list(session.execute(text(query), params))
        finally:
            session.close()

        # 2 вариант запуска запроса
        # try:
        #     conn = self._engine.connect()
        #     results = conn.execute(text(query), params)
        # finally:
        #     conn.close()

        # закидываем в список словарей
        return [{key: value for (key, value) in dict(row).items()} for row in result]
