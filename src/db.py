from py2neo import Graph

from src.config import settings
from src.app.utils.logger import logger


class Neo4jConnection:
    """
    Класс для управления подключением к базе данных Neo4j.

    Этот класс обеспечивает создание единственного экземпляра подключения к Neo4j
    с использованием библиотеки py2neo. При первом вызове создается подключение,
    которое используется повторно при последующих вызовах.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            logger.info("Initializing Neo4j connection")
            bolt_url = settings.NEO4J_BOLT_URL
            user = settings.NEO4J_USER
            password = settings.NEO4J_PASSWORD
            cls._instance = Graph(bolt_url, auth=(user, password))
            logger.info("Neo4j connection initialized successfully")
        return cls._instance