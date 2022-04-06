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
import hashlib

# Global Variables
hash_space_bits = 4
hash_space = 2 ** hash_space_bits


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
        pass  # to be updated


# The class for each sensor node on the sensor network
class SensorNode:
    """
    Class SensorNode:
    Data: Basic Info about each Sensor Node
    Operations:
    1. Join / Leave
    2. Find successor / closest predecessor node
    3. Node Data Lookup Query
    4. Node Data Reload
    """
    def __init__(self, nodeid, network):
        self.node_id = nodeid  # node's ID on the network.
        # By design, this ID derives from the line-of-sight distance of the node from the base station
        # self.base_station_distance = 0 (input argument that will give the node id through a custom hash function)
        self.network = network  # the identification of the chord ring network that the node has joined.
        self.successor_id = 0  # initially is zero, will be updated later
        self.predecessor_id = 0  # initially is zero, will be updated later
        self.finger_table = []  # the i-th closest neighbor nodes from the finger table.
        """TO-DO: Να προσθέσω και ένα δεύτερο finger table για την επιστροφή του query"""
        self.node_data = "data"  # the sensor data stored on the node's memory

    def update_finger_table(self):
        # function to update the node's finger table
        pass  # to be updated

    def update_successor_predecessor(self):
        # function to update the successor and predecessor of the node
        if self.node_id == self.network.last_node:  # if the current node is the last node on the ring network
            self.successor_id = self.network.List_of_Nodes[0]
            self.predecessor_id = self.network.List_of_Nodes[self.network.Num_of_Nodes - 2]
        elif self.node_id == self.network.first_node:  # if the current node is the first node on the ring network
            self.successor_id = self.network.List_of_Nodes[1]
            self.predecessor_id = self.network.List_of_Nodes[self.network.Num_of_Nodes - 1]
        else:  # if the current node is any other node within the ring network
            pos = 0  # the position of this node on the chord ring (zero value initially)
            for i in range(0, self.network.Num_of_Nodes):  # find the position of the current node by incrementing pos
                if self.network.List_of_Nodes[i] < self.node_id:
                    pos += 1  # increment position
            self.successor_id = self.network.List_of_Nodes[pos+1]  # successor is the next node
            self.predecessor_id = self.network.List_of_Nodes[pos-1]  # predecessor is the previous

    def find_successor(self, key):
        # function to find the successor node to a lookup key
        pass  # to be updated

    def find_closest_predecessor(self, key):
        # function to find the closest predecessor node of a lookup key
        pass  # to be updated

    def node_join(self, ring_id):
        # function to join the node on the chord ring network
        pass  # to be updated

    def node_leave(self):
        # function to remove the node on the chord ring network
        pass  # to be updated

    def lookup_query(self, value):
        # function to look up a key
        pass  # to be updated

    def sensor_data_reload(self):
        # function to refresh the data from the node's sensors
        pass  # to be updated


"""
# main process
"""
if __name__ == "__main__":
    # Execute these lines, only if this module is executed by itself.
    print("Chord Protocol Application on Wireless Sensor Networks")
    print("Implementation by Christos-Panagiotis Mpalatsouras")
    print("ORCID: orcid.org/0000-0001-8914-7559")
