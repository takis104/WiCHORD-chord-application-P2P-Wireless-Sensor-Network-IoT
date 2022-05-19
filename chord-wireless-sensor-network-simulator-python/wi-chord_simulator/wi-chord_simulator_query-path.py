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
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import secrets
import random

# Import modules from this project
from network_build import network_build
from SensorNode import SensorNode

# Global Variables
# num_of_nodes = 9
total_runs_per_experiment = 10


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
    print("|        Wi-CHORD Simulator         |")
    print("|                                   |")
    print("+-----------------------------------+")
    print("Chord Protocol Application on Wireless Sensor Networks")
    print("Implementation by Christos-Panagiotis Mpalatsouras")
    print("ORCID: orcid.org/0000-0001-8914-7559")

    print("\nExperiment: Measuring the Average Query Path Length per total number of Nodes\n")

    total_runs_per_experiment = int(input("Please Specify the total runs per experiment: "))
    minimum_nodes = int(input("Please Specify the minimum num of nodes on the network: "))
    maximum_nodes = int(input("Please Specify the maximum num of nodes on the network: "))
    step = int(input("Please specify the total nodes increment step: "))

    results = []  # list to store the results

    for total_nodes in range(minimum_nodes, maximum_nodes, step):
        num_of_nodes = total_nodes
        print("\nRunning Experiment with total nodes: ", num_of_nodes)

        print("\nScanning for nodes to add to the network...")
        node_list = []
        for n in range(0, num_of_nodes + 1):
            mac_address = secrets.token_hex(6)  # Generate random MAC addresses
            node_list.append(SensorNode(mac_address, None))
            # print("Found node with MAC Address: ", mac_address)
        # Sort the list of nodes by NODE ID, TO-DO: Find out a way to build the network without sorting (dynamic)
        node_list.sort(key=lambda node: node.node_id)

        print("\nAdding nodes to the network...")
        net1 = network_build(node_list)

        # current_node = None

        # Να βάλω να παίρνει ένα κόμβο τυχαία από τη λίστα
        list_of_nodes = net1.List_of_Nodes
        current_node = random.choice(list_of_nodes)

        print(
            "\nYou are connected to the Node with MAC: ",
            current_node.node_name, " and ID: ",
            current_node.node_id, "\n"
        )

        sum_of_lengths = 0  # the sum of query path lengths

        for i in range(0, total_runs_per_experiment):
            # select a random node of the network to be looked up
            dest_node = random.choice(list_of_nodes)
            while dest_node == current_node:  # select a node other than the current
                dest_node = random.choice(list_of_nodes)
            lookup_value = dest_node.node_name
            q1 = Query("lookup")
            lookup_node = current_node.lookup_query(lookup_value, q1)
            print("\nFound node with ID: ", lookup_node.node_id)
            # lookup_node.sensor_data_print()
            # print("\nQuery type: ", q1.query_type, "\nTotal node hops to resolve this query: ", q1.query_hops)
            sum_of_lengths = sum_of_lengths + q1.query_hops

        local_average_path = sum_of_lengths / total_runs_per_experiment
        local_result = {"Nodes": num_of_nodes, "Avg_Path": local_average_path}
        results.append(local_result)

    # Export results to CSV
    print("\nExporting results to CSV...\n")
    with open('wichord-sim_experiment1.csv', mode='w', newline='') as results_file:
        results_writer = csv.writer(results_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        results_writer.writerow(["Total_nodes", "Average_Path_Length"])
        for item in results:
            results_writer.writerow([item["Nodes"], item["Avg_Path"]])

    # Export results to TXT for MatplotLib
    print("\nExporting results to TXT...\n")
    with open('wichord-sim_experiment1.txt', mode='w', newline='') as results_file:
        nodes_num = []
        avg_path = []
        for item in results:
            nodes_num.append(item["Nodes"])
            avg_path.append(item["Avg_Path"])
        results_file.write("%s\n" % nodes_num)
        results_file.write("%s\n" % avg_path)

    # Plot the simulation results
    mpl.rcParams['axes.linewidth'] = 2
    mpl.rcParams['lines.linewidth'] = 3
    mpl.rcParams['xtick.labelsize'] = 20
    mpl.rcParams['ytick.labelsize'] = 20

    plt.plot(nodes_num, avg_path, label='Average Query Path Length')

    plt.ylabel("Average Lookup Query Path Length", fontsize=22)
    plt.xlabel("Total Number of Nodes on the Network", fontsize=22)
    plt.title("Average Lookup Query Path Length per Total Number of Nodes", fontsize=24)
    plt.legend(prop={'size': 26})

    plt.show()
