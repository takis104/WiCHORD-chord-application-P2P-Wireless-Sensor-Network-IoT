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
FILE DESCRIPTION: SensorNetwork class definition
"""

# Import modules from this project
from globals import hash_space


# The class for the Sensor Network as a total entity
class SensorNetwork:
    """
    Class SensorNetwork:
    Data: Basic Info about the Sensor Network
    Operations:
    1. Reload Network Details
    """
    def __init__(self):
        self.List_of_Nodes = []  # the list of node entities on the network
        self.Num_of_Nodes = len(self.List_of_Nodes)  # the number of total nodes in the network
        # self.Node_Key_List = []  # a list with the keys of all the nodes (optional)
        self.max_network_key = hash_space - 1  # the maximum key value on the network is 2^m - 1
        self.min_network_key = 0  # the minimum key value on the network is 0
        self.first_node = 0  # zero value initially, to be updated later
        self.last_node = 0  # zero value initially, to be updated later

    def network_reload(self):
        # reload all the sensor network specifications
        self.Num_of_Nodes = len(self.List_of_Nodes)  # update num of nodes
        self.List_of_Nodes.sort(key=lambda n: n.node_id)  # sort list of nodes by node id in ascending order
        self.first_node = self.List_of_Nodes[0]  # update first node
        self.last_node = self.List_of_Nodes[self.Num_of_Nodes - 1]  # update last node
