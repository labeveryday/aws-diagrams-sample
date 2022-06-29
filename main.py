# Amazon VPC Diagram
# https://diagrams.mingrammer.com/
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.client import Client
from diagrams.onprem.network import Internet
from diagrams.aws.network import InternetGateway
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS


# Represents the diagram that all clusters, nodes, and edges are nested
with Diagram("Building an Amazon VPC", show=False, outformat = "png",
             filename = "images/Building-an-Amazon-VPC",
             graph_attr={
                            "fontsize": "40"
                        }
            ):
    # VPC cluster that contains subnets
    with Cluster("VPC", graph_attr={"bgcolor": "white"}):
        internet = InternetGateway("IGW")
        # Subnet cluster that contains an EC2 instance
        with Cluster(label="Public Subnet", graph_attr={"fontcolor": "darkgreen",
                                                        "bgcolor": "#e2f4ea"}):
            ec2 = EC2("ec2")
        # Subnet cluster that contains an RDS instance
        with Cluster("Private Subnet", graph_attr={"fontcolor": "darkblue",
                                                   "bgcolor": "#c4e4f9"}):
            rds = RDS("db")
    # Client connection to the internet that connects to the IGW >> ec2 >> rds
    Client() - Internet("internet") >> Edge(color="darkgreen", style="dotted") << internet >> ec2 >> rds
