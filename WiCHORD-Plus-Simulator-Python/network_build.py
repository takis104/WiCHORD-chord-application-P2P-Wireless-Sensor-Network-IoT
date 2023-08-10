# Advanced Chord Implementation in Python
# Created by Christos-Panagiotis Balatsouras
# ORCID: https://orcid.org/0000-0001-8914-7559

"""
Use Case: Application of Chord Protocol Based Routing in Wireless Sensor Networks
Application Functionality:
1. Node Join / Leave
2. Network Build
3. Data Lookup Query

****
FILE DESCRIPTION: network_build() function definition
"""

# Import modules from this project
from SensorNetwork import SensorNetwork


def network_build(node_list):
    # function to build the chord sensor network. Returns the network as an entity
    network = SensorNetwork()  # create the network instance
    for node in node_list:  # join the nodes from the list
        node.node_join(network)
    for node in network.List_of_Nodes:  # update the finger tables for all the nodes
        node.update_finger_table()
    return network
