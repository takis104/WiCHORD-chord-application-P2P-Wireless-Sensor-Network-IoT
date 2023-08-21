# Advanced Chord Implementation in Python
# WiCHORD+ Wireless Sensor Network Overlay for LoRa WSNs on IoT Applications
# Created by Christos-Panagiotis Balatsouras
# ORCID: https://orcid.org/0000-0001-8914-7559

"""
Use Case: Application of Chord Protocol Based Routing in Wireless Sensor Networks
Application Functionality:
1. Node Join / Leave
2. Network Build
3. Data Lookup Query
4. WiCHORD Evaluation on LoRa WSNs

****
FILE DESCRIPTION: Query class definition
"""


class Query:
    """
    Class Query: Stores useful info about a query such as the type and the num of nodes involved to resolve the query
    """
    def __init__(self, query_type):
        self.query_type = query_type
        self.query_hops = 0  # counter for the num of hops for a query to be resolved
        self.nodes_involved = 0  # counter for the num of nodes involved for a join/leave operation to be completed

    def hops_increment(self):
        """
        Function to increment the query hops each time a lookup query is forwarded to a different node
        """
        self.query_hops += 1  # increment the hops between nodes for the query execution

    def nodes_increment(self):
        """
        Function to increment the num of nodes involved for a join/leave operation to be completed
        """
        self.nodes_involved += 1  # increment the num of nodes involved
