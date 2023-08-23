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
FILE DESCRIPTION: WiCHORD+ Simulator in Python
"""

# import Python modules
import matplotlib as mpl
import matplotlib.pyplot as plt
import secrets
import random
import pandas as pd

# Import other modules from this project
from globals import hash_space_bits
from network_build import network_build
from SensorNode import SensorNode
from Query import Query

# Global Variables
# Set the appearance parameters for the plots
mpl.rcParams['figure.figsize'] = [25, 15]
mpl.rcParams['xtick.labelsize'] = 30
mpl.rcParams['ytick.labelsize'] = 30
mpl.rcParams['axes.titlesize'] = 40
mpl.rcParams['axes.labelsize'] = 25

# Function Definitions
def create_random_wsn(num_of_nodes):
    """
    Function to create random WSNs with nodes of random generated mac addresses
    :param num_of_nodes: the desired total num of nodes on the WSN
    :return: the created and built WSN instance with the initial nodes joined
    """
    # Create random sensor node mac addresses to add to the network
    nodes_list = []
    for n in range(0, num_of_nodes):
        mac_addr = secrets.token_hex(6)  # Generate random MAC addresses
        nodes_list.append(SensorNode(mac_addr, None))  # add random node to list
    # Sort the list of nodes by NODE ID
    nodes_list.sort(key=lambda node: node.node_id)

    # Add the above random sensor nodes to a new empty network
    sensornet = network_build(nodes_list)

    return sensornet

"""
Main Application
"""
if __name__ == "__main__":
    print("+-----------------------------------+")
    print("|                                   |")
    print("|        Wi-CHORD+ Simulator        |")
    print("|                                   |")
    print("+-----------------------------------+")
    print("Chord Protocol Application on Wireless Sensor Networks")
    print("Implementation by Christos-Panagiotis Mpalatsouras")
    print("ORCID: orcid.org/0000-0001-8914-7559")

    # ---- 1. Simulation #1: Key Load Balancing
    print("\nExperiment: Measuring the Average NodeID Storage per total number of Nodes\n")
    # Experiment details
    minimum_nodes = int(input("Please Specify the minimum num of nodes on the network: "))
    print("Minimum nodes on a sensor network: ", minimum_nodes)
    maximum_nodes = int(input("Please Specify the maximum num of nodes on the network: "))
    print("Maximum nodes on a sensor network: ", maximum_nodes)
    step = int(input("Please specify the total nodes increment step: "))
    print("Increment step: ", step)

    # Main Simulation for Storage Efficiency
    results = []  # list to store the results
    for total_nodes in range(minimum_nodes, maximum_nodes, step):
        print("\nRunning Experiment with total nodes: ", total_nodes)

        # Create a random WSN with random sensor node MAC Addresses
        wsn = create_random_wsn(total_nodes)

        # Export the network's list of nodes
        list_of_nodes = wsn.List_of_Nodes

        # ---- Find the average number of node IDs stored in the memory of each node ----
        sum_of_contacts = 0  # the total sum of node contacts
        for node in list_of_nodes:
            node.update_total_num_of_contacts()
            sum_of_contacts = sum_of_contacts + node.contacts_num  # update the total sum of node contacts

        local_average = sum_of_contacts / total_nodes
        local_result = {
            "Nodes": total_nodes,
            "Avg_Num_of_Contacts": local_average
        }
        results.append(local_result)

    # Simulation results
    results_df = pd.DataFrame(results)
    print("Simulation results: ", results_df)

    # Plot the simulation experiment results
    # Show the plot/plots
    plt.plot(
        results_df["Nodes"],
        results_df["Avg_Num_of_Contacts"],
        label="Average number of stored Node IDs"
    )
    plt.ylabel("Average number of contacts (Node IDs) stored in node's memory", fontsize=22)
    plt.xlabel("Total Number of Nodes on the Network", fontsize=22)
    plt.title("Average number of contacts (Node IDs) stored in the memory of each node per total number of nodes (hash space bits: "+str(hash_space_bits)+")", fontsize=24)
    plt.legend(prop={'size': 26})
    plt.show()

    # ---- 2. Simulation #2: Energy Efficiency and total energy consumption (Node Join Operation)
    print("\nExperiment: Measuring the number of nodes involved for a node join query\n")
    # Experiment details
    total_runs_per_experiment = int(input("Please Specify the total runs per experiment: "))
    print("Total runs per experiment: ", total_runs_per_experiment)
    minimum_nodes = int(input("Please Specify the minimum num of nodes on the network: "))
    print("Minimum nodes on a sensor network: ", minimum_nodes)
    maximum_nodes = int(input("Please Specify the maximum num of nodes on the network: "))
    print("Maximum nodes on a sensor network: ", maximum_nodes)
    step = int(input("Please specify the total nodes increment step: "))
    print("Increment step: ", step)

    # Main Simulation for Join Operation Energy Efficiency
    results = []  # list to store the results
    for total_nodes in range(minimum_nodes, maximum_nodes, step):
        print("\nRunning Experiment with total nodes: ", total_nodes)

        # Perform the simulation experiment
        sum_of_involved_nodes = 0  # the sum of nodes involved for a query to be resolved
        for i in range(0, total_runs_per_experiment):
            wsn = create_random_wsn(total_nodes)  # Create a random WSN with random sensor node MAC Addresses
            list_of_nodes = wsn.List_of_Nodes  # Export the network's list of nodes
            # Create a new random node to add to the network
            mac_addr = secrets.token_hex(6)  # Generate random MAC addresses
            new_node = SensorNode(mac_addr, None)  # random node instance
            q = Query("join")  # query instance
            new_node.node_join(wsn, query_id=q)  # perform the query
            sum_of_involved_nodes = sum_of_involved_nodes + q.nodes_involved  # update the sum of involved nodes for the query to be resolved

        # Calculate the local average result
        local_average = sum_of_involved_nodes / total_runs_per_experiment
        local_result = {
            "Nodes": total_nodes,
            "Avg_Num_of_Involved_Nodes": local_average
        }
        results.append(local_result)

    # Simulation results
    results_df = pd.DataFrame(results)
    print("Simulation results: ", results_df)

    # Plot the simulation experiment results
    # Show the plot/plots
    plt.plot(
        results_df["Nodes"],
        results_df["Avg_Num_of_Involved_Nodes"],
        label="Average number of involved Nodes on a Join Query"
    )
    plt.ylabel("Average number of involved nodes", fontsize=22)
    plt.xlabel("Total Number of Nodes on the Network", fontsize=22)
    plt.title("Average number of involved Nodes on a Join Query per total number of nodes", fontsize=24)
    plt.legend(prop={'size': 26})
    plt.show()

    # --- 3. Simulation #3: Energy Efficiency and total energy consumption (Node Leave Operation)
    print("\nExperiment: Measuring the number of nodes involved for a node leave query\n")
    # Experiment details
    total_runs_per_experiment = int(input("Please Specify the total runs per experiment: "))
    print("Total runs per experiment: ", total_runs_per_experiment)
    minimum_nodes = int(input("Please Specify the minimum num of nodes on the network: "))
    print("Minimum nodes on a sensor network: ", minimum_nodes)
    maximum_nodes = int(input("Please Specify the maximum num of nodes on the network: "))
    print("Maximum nodes on a sensor network: ", maximum_nodes)
    step = int(input("Please specify the total nodes increment step: "))
    print("Increment step: ", step)

    # Main Simulation for Leave Operation Energy Efficiency
    results = []  # list to store the results
    for total_nodes in range(minimum_nodes, maximum_nodes, step):
        print("\nRunning Experiment with total nodes: ", total_nodes)

        # Perform the simulation experiment
        sum_of_involved_nodes = 0  # the sum of nodes involved for a query to be resolved
        for i in range(0, total_runs_per_experiment):
            wsn = create_random_wsn(total_nodes)  # Create a random WSN with random sensor node MAC Addresses
            list_of_nodes = wsn.List_of_Nodes  # Export the network's list of nodes
            active_node = random.choice(
                list_of_nodes)  # Pick a random node to sign-in and then perform the simulation experiment
            q = Query("leave")  # query instance
            active_node.node_leave(query_id=q)  # perform the query
            wsn.network_reload()
            sum_of_involved_nodes = sum_of_involved_nodes + q.nodes_involved  # update the sum of involved nodes for the query to be resolved

        # Calculate the local average result
        local_average = sum_of_involved_nodes / total_runs_per_experiment
        local_result = {
            "Nodes": total_nodes,
            "Avg_Num_of_Involved_Nodes": local_average
        }
        results.append(local_result)

    # Simulation results
    results_df = pd.DataFrame(results)
    print("Simulation results: ", results_df)

    # Plot the simulation experiment results
    # Show the plot/plots
    plt.plot(
        results_df["Nodes"],
        results_df["Avg_Num_of_Involved_Nodes"],
        label="Average number of involved Nodes on a Leave Query"
    )
    plt.ylabel("Average number of involved nodes", fontsize=22)
    plt.xlabel("Total Number of Nodes on the Network", fontsize=22)
    plt.title("Average number of involved Nodes on a Leave Query per total number of nodes", fontsize=24)
    plt.legend(prop={'size': 26})
    plt.show()

    # ---- 4. Simulation #4: Energy Efficiency and total energy consumption (Node Lookup Operation)
    print("\nExperiment: Measuring the number of nodes involved for a node lookup query\n")
    # Experiment details
    total_runs_per_experiment = int(input("Please Specify the total runs per experiment: "))
    print("Total runs per experiment: ", total_runs_per_experiment)
    minimum_nodes = int(input("Please Specify the minimum num of nodes on the network: "))
    print("Minimum nodes on a sensor network: ", minimum_nodes)
    maximum_nodes = int(input("Please Specify the maximum num of nodes on the network: "))
    print("Maximum nodes on a sensor network: ", maximum_nodes)
    step = int(input("Please specify the total nodes increment step: "))
    print("Increment step: ", step)

    # Main Simulation for Lookup Operation Energy Efficiency
    results = []  # list to store the results
    for total_nodes in range(minimum_nodes, maximum_nodes, step):
        print("\nRunning Experiment with total nodes: ", total_nodes)

        # Create a random WSN with random sensor node MAC Addresses
        wsn = create_random_wsn(total_nodes)

        # Export the network's list of nodes
        list_of_nodes = wsn.List_of_Nodes

        # Pick a random node to sign-in and then perform the simulation experiment
        active_node = random.choice(list_of_nodes)
        """
        print(
            "\nYou are connected to the Node with MAC: ",
            current_node.node_name, " and ID: ",
            current_node.node_id, "\n"
        )
        """

        # Perform the simulation experiment
        sum_of_involved_nodes = 1  # the sum of nodes involved for a query to be resolved (start with one to count the initial node)
        for i in range(0, total_runs_per_experiment):
            selected_node = random.choice(list_of_nodes)  # select a random node of the network to look up
            while selected_node == active_node:  # select a node other than the current
                selected_node = random.choice(list_of_nodes)
            lookup_value = selected_node.node_name
            q = Query("lookup")  # query instance
            lookup_node = active_node.lookup_query(lookup_value, q)  # perform lookup query
            sum_of_involved_nodes = sum_of_involved_nodes + q.query_hops

        # Calculate the local average result
        local_average = sum_of_involved_nodes / total_runs_per_experiment
        local_result = {
            "Nodes": total_nodes,
            "Avg_Num_of_Involved_Nodes": local_average
        }
        results.append(local_result)

    # Simulation results
    results_df = pd.DataFrame(results)
    print("Simulation results: ", results_df)

    # Plot the simulation experiment results
    # Show the plot/plots
    plt.plot(
        results_df["Nodes"],
        results_df["Avg_Num_of_Involved_Nodes"],
        label="Average number of involved Nodes on a Lookup Query"
    )
    plt.ylabel("Average number of involved nodes", fontsize=22)
    plt.xlabel("Total Number of Nodes on the Network", fontsize=22)
    plt.title("Average number of involved Nodes on a Lookup Query per total number of nodes", fontsize=24)
    plt.legend(prop={'size': 26})
    plt.show()
