
#%%
from diagrams import Cluster, Edge, Diagram
from diagrams.onprem.container import Docker
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.database import Postgresql
from diagrams.onprem.queue import Kafka
from diagrams.onprem.queue import Zookeeper
from diagrams.onprem.queue import ControlCenter, SchemaRegistry
from diagrams.onprem.database import Cassandra
from diagrams.onprem.compute import Server


with Diagram("arch_image", show=False, outpath="architecture_diagram"):
    # Define Nodes
    api = Docker("API")
    postgres = Postgresql("PostgreSQL")
    airflow = Airflow("Airflow")
    kafka = Kafka("Kafka")
    cassandra = Cassandra("Cassandra")
    
    with Cluster("PySpark"):
        master = Server("Master")
        with Cluster("Workers"):
            worker1 = Server("Worker 1")
            worker2 = Server("Worker 2")

    # Define Edges
    kafka >> Edge(label="Data Stream", color="blue") >> master
    master >> Edge(label="Processing", color="green") >> cassandra
    master >> Edge(color="purple") << worker1
    master >> Edge(color="purple") << worker2

