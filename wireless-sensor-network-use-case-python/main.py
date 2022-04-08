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
        self.Num_of_Nodes = len(self.List_of_Nodes)  # update num of nodes
        self.List_of_Nodes.sort(key=lambda n: n.node_id)  # sort list of nodes by node id in ascending order
        self.first_node = self.List_of_Nodes[0]  # update first node
        self.last_node = self.List_of_Nodes[self.Num_of_Nodes - 1]  # update last node


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

    Design Choices:
    1. When referring to a node, refer to the node as object and not by id
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

        # initially populate the finger table with only the id of current node,
        # because current node knows only itself before joining the network
        for i in range(0, hash_space_bits):
            self.finger_table.append(self)

    def update_finger_table(self):
        # function to update the node's finger table
        for i in range(0, hash_space_bits):
            finger = self.node_id + 2 ** i
            finger_node = self.find_successor(finger)
            self.finger_table[i] = finger_node

    def update_successor_predecessor(self):
        # function to update the successor and predecessor of the node
        pos = 0  # the position of this node on the chord ring (zero value initially)
        if self.node_id == self.network.last_node.node_id:  # if the current node is the last node on the network
            self.successor_id = self.network.List_of_Nodes[0]
            self.predecessor_id = self.network.List_of_Nodes[self.network.Num_of_Nodes - 2]
        elif self.node_id == self.network.first_node.node_id:  # if the current node is the first node on the network
            self.successor_id = self.network.List_of_Nodes[1]
            self.predecessor_id = self.network.List_of_Nodes[self.network.Num_of_Nodes - 1]
        else:  # if the current node is any other node within the ring network
            for i in range(0, self.network.Num_of_Nodes):  # find the position of the current node by incrementing pos
                if self.network.List_of_Nodes[i].node_id < self.node_id:
                    pos += 1  # increment position
            self.successor_id = self.network.List_of_Nodes[pos + 1]  # successor is the next node
            self.predecessor_id = self.network.List_of_Nodes[pos - 1]  # predecessor is the previous

    def find_successor(self, key):
        # function to find the successor node to a lookup key
        if self.node_id < key <= self.successor_id.node_id:  # key is between current node and it's successor
            return self.successor_id
        elif self.node_id == key:  # if key is the same as current node id
            return self
        elif self.node_id == self.network.last_node.node_id:  # the last node returns the first as successor
            return self.network.first_node
        else:  # if key is greater than the current node
            forward_node = self.find_closest_predecessor(key)
            return forward_node.find_successor(key)

    def find_closest_predecessor(self, key):
        # function to find the closest predecessor node of a lookup key
        for i in range(hash_space_bits-1, -1, -1):
            if self.node_id < self.finger_table[i].node_id < key:
                return self.finger_table[i]
        return self

    def node_join(self, ring_id):
        # function to join the node on the chord ring network
        self.network = ring_id
        self.network.List_of_Nodes.append(self)
        self.network.network_reload()
        self.update_successor_predecessor()

        # Find the finger table for the new node
        # calculate the initial finger table knowing only self and successor
        # then calculate again the finger table

    def node_reload(self):
        # update node details
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


def network_build(node_list):
    # function to build the chord sensor network. Returns the network as an entity
    pass  # to be updated


def calc_hash_value(input_val, space):
    # function to calculate the hash value of an input value
    output_val = hashlib.sha1()
    output_val.update(str(input_val).encode())
    output_val = int(output_val.hexdigest(), 16)
    output_val = output_val % space
    return output_val


"""
# main application process
"""
if __name__ == "__main__":  # Execute these lines, only if this module is executed by itself.
    print("Chord Protocol Application on Wireless Sensor Networks")
    print("Implementation by Christos-Panagiotis Mpalatsouras")
    print("ORCID: orcid.org/0000-0001-8914-7559")
