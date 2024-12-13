from src.db import Neo4jConnection
from src.app.utils.logger import logger

# Получаем подключение
graph = Neo4jConnection()


class Neo4jQueries:
    @staticmethod
    def get_all_nodes():
        logger.info("Fetching all nodes with id and label...")
        query = "MATCH (n) RETURN id(n) AS id, labels(n)[0] AS label"
        return graph.run(query).data()

    @staticmethod
    def get_node_and_relationships(node_id: int):
        logger.info(f"Fetching node {node_id} and its relationships...")
        query = """
        MATCH (n)-[r]-(m)
        WHERE id(n) = $node_id
        RETURN n, r, m
        """
        return graph.run(query, {"node_id": node_id}).data()

    @staticmethod
    def insert_node_and_relationships(node, relationships):
        """
        Добавляет узел и его связи в базу данных.
        :param node: Данные узла
        :param relationships: Список связей
        """
        node_query = f"""
        CREATE (n:{node.label} {{
            id: $id, name: $name, screen_name: $screen_name,
            sex: $sex, home_town: $home_town
        }})
        """
        graph.run(node_query, {
            "id": node.id,
            "name": node.name,
            "screen_name": node.screen_name,
            "sex": node.sex,
            "home_town": node.home_town
        })

        if relationships:
            rel_query = """
            UNWIND $relationships AS rel
            MATCH (n {id: $node_id}), (m {id: rel.end_node_id})
            CREATE (n)-[r:REL_TYPE {id: rel.id}]->(m)
            """
            rel_data = [
                {"id": rel.id, "type": rel.type.value, "end_node_id": rel.end_node_id}
                for rel in relationships
            ]
            graph.run(rel_query, {
                "node_id": node.id,
                "relationships": rel_data
            })

            logger.info(f"Relationships for node {node.id} added.")

    @staticmethod
    def delete_node_and_relationships(node_id: int):
        logger.info(f"Deleting node {node_id} and its relationships...")
        query = """
        MATCH (n)-[r]-(m)
        WHERE id(n) = $node_id
        DELETE r, n
        """
        graph.run(query, {"node_id": node_id})
        logger.info(f"Node {node_id} and its relationships deleted.")