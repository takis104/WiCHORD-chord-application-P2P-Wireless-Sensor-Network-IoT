# Advanced Chord Implementation in Python
# Created by Christos-Panagiotis Balatsouras
# ORCID: https://orcid.org/0000-0001-8914-7559

"""
Use Case: Application of Chord Protocol Based Routing in Wireless Sensor Networks
Application Functionality:
1. Node Join / Leave
2. Network Build
3. Data Lookup Query
"""

# Import Python Modules
import secrets

# Import modules from this project
from network_build import network_build
from SensorNode import SensorNode

# Global Variables
num_of_nodes = 9


class Query:
    """
    Class Query: Stores useful information about a query such as the type and the num of node hops to resolve the query
    """
    def __init__(self, query_type):
        self.query_type = query_type
        self.query_hops = 0  # variable to calculate the num of hops for a query to be resolved

    def hops_increment(self):
        self.query_hops += 1  # increment the hops between nodes for the query execution


"""
# main application process
"""
if __name__ == "__main__":  # Execute these lines, only if this module is executed by itself.
    print("+-----------------------------------+")
    print("|                                   |")
    print("|             Wi-CHORD              |")
    print("|                                   |")
    print("+-----------------------------------+")
    print("Chord Protocol Application on Wireless Sensor Networks")
    print("Implementation by Christos-Panagiotis Mpalatsouras")
    print("ORCID: orcid.org/0000-0001-8914-7559")

    print("\nScanning for nodes to add to the network...")
    node_list = []
    for n in range(0, num_of_nodes + 1):
        mac_address = secrets.token_hex(6)  # Generate random MAC addresses
        node_list.append(SensorNode(mac_address, None))
        print("Found node with MAC Address: ", mac_address)
    # Sort the list of nodes by NODE ID, TO-DO: Find out a way to build the network without sorting (dynamic)
    node_list.sort(key=lambda node: node.node_id)

    print("\nAdding nodes to the network...")
    net1 = network_build(node_list)

    opt1 = int(
        input(
            "\nOptions: \n"
            "1. Log-in to one of the available nodes \n"
            "2. Register a new node \n"
            "Select one of the above (1-2): "
        )
    )
    current_node = None
    if opt1 == 1:
        selected_id = int(input("Select one Node ID from the above: "))
        for node in net1.List_of_Nodes:
            if node.node_id == selected_id:
                current_node = node
    elif opt1 == 2:
        new_node_name = input("Enter the MAC address of the new node: ")
        new_node = SensorNode(new_node_name, None)
        new_node.node_join(net1)
        for node in net1.List_of_Nodes:  # update the finger tables for all the nodes
            node.update_finger_table()
        current_node = new_node
    print("\nYou are connected to the Node with MAC: ", current_node.node_name, " and ID: ", current_node.node_id, "\n")

    opt2 = int(
        input(
            "\nOptions: \n"
            "1. Print current sensor values \n"
            "2. Refresh sensor values \n"
            "3. Lookup values from other node \n"
            "Select one of the above (1-3): "
        )
    )
    if opt2 == 1:
        current_node.sensor_data_print()
    elif opt2 == 2:
        current_node.sensor_data_reload()
        current_node.sensor_data_print()
    elif opt2 == 3:
        lookup_value = input("Enter node MAC Address to lookup: ")
        q1 = Query("lookup")
        lookup_node = current_node.lookup_query(lookup_value, q1)
        print("\nFound node with ID: ", lookup_node.node_id)
        lookup_node.sensor_data_print()
        print("\nQuery type: ", q1.query_type,
              "\nTotal node hops to resolve this query: ", q1.query_hops)
