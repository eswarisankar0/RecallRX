import os
from dotenv import load_dotenv
from falkordb import FalkorDB

load_dotenv()

client = FalkorDB(
    host=os.getenv("FALKORDB_HOST", "localhost"),
    port=int(os.getenv("FALKORDB_PORT", "6379")),
    password=os.getenv("FALKORDB_PASSWORD") or None,
)
graph = client.select_graph("recallrx")


def query(cypher, params=None):
    return graph.query(cypher, params or {}).result_set