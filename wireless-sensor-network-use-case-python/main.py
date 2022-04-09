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
hash_space_bits = 6
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

    def __init__(self, node_name, network):
        self.node_name = node_name
        self.node_id = calc_hash_value(node_name, hash_space)  # node's ID on the network.
        # By design, this ID derives from the line-of-sight distance of the node from the base station
        # self.base_station_distance = 0 (input argument that will give the node id through a custom hash function)
        self.network = network  # the identification of the chord ring network that the node has joined.
        self.successor_id = None  # initially is zero, will be updated later
        self.predecessor_id = None  # initially is zero, will be updated later
        self.finger_table = []  # the i-th closest neighbor nodes from the finger table.
        """TO-DO: Να προσθέσω και ένα δεύτερο finger table για την επιστροφή του query"""
        # the sensor data stored on the node's memory
        self.node_data = {"GPS": {"Latitude": None, "Longitude": None}, "Temp": None, "Humidity": None}

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
            if forward_node == self:
                return self
            else:
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
        # self.successor_id.update_successor_predecessor()
        # self.predecessor_id.update_successor_predecessor()

        # Find the finger table for the new node
        self.finger_table = []  # initialize finger table with empty list

        # then ask from any pre-existing (by design the first node is chosen) node to lookup fingers of this node
        finger_keys = []
        for i in range(0, hash_space_bits):
            finger_key = self.node_id + 2 ** i
            first_node = self.network.List_of_Nodes[0]
            finger_keys.append(first_node.find_successor(finger_key))
        # calculate the final finger table after the join operation
        for item in range(0, hash_space_bits):
            self.finger_table.append(finger_keys[item])

        # update the details of existing nodes that point to the new node
        self.existing_nodes_update()

        print("Sensor node with name: ", self.node_name, " ID: ", self.node_id,
              "joined the chord wireless sensor network")

    def existing_nodes_update(self):
        # update existing node details to point to the new node
        # update nodes in the ranges: [predecessor_id-2^i+1, self_id-2^i], for i from 0 to hash_space_bits
        for i in range(0, hash_space_bits):
            ptr1 = self.predecessor_id.node_id - (2 ** i) + 1  # left edge of the range
            ptr2 = self.node_id - (2 ** i)  # right edge of the range
            if ptr1 < 0:  # if this edge of the selected range is < 0, the edge takes the value of predecessor_id + 1
                ptr1 = (2 ** i) + ptr1
            if ptr2 < 0:  # if this edge of the selected range is < 0, the edge takes the value of self_id + 1
                ptr2 = (2 ** i) + ptr2
            for node in self.network.List_of_Nodes:  # update the finger table for all the nodes on the range
                if ptr1 <= node.node_id <= ptr2:
                    node.update_successor_predecessor()  # update successor/predecessor of the node
                    node.update_finger_table()  # update the finger table of the node

    def node_leave(self):
        # function to remove the node on the chord ring network
        self.network.List_of_Nodes.remove(self)  # remove this node from the list of nodes of the network
        self.network.network_reload()  # reload the network variables
        self.successor_id.update_successor_predecessor()  # update successor's details
        self.predecessor_id.update_successor_predecessor()  # update predecessor's details
        self.existing_nodes_update()  # update the details of existing nodes that point to this node
        self.network = None  # clear the network id from the node attributes
        self.successor_id = None  # clear the successor id from node attributes
        self.predecessor_id = None  # clear the predecessor id from node attributes

        print("Sensor node with name: ", self.node_name, " ID: ", self.node_id,
              "disconnected from the chord wireless sensor network")

    def lookup_query(self, value):
        # function to look up a key (node)
        lookup_key = calc_hash_value(value, hash_space)
        if self != self.network.last_node or self.node_id < lookup_key:
            resp_node = self.find_successor(lookup_key)
        else:
            first_node = self.network.first_node
            resp_node = first_node.find_successor(lookup_key)
        return resp_node

    def sensor_data_reload(self):
        # function to refresh the data from the node's sensors
        pass  # to be updated (with random values for the example)

    def sensor_data_print(self):
        # function to print the data from the node's sensors
        print("Sensor Node with Name: ", self.node_name, "and with ID: ", self.node_id)
        print("Current Sensor Values: ")
        print("GPS:  Latitude: ", self.node_data["GPS"]["Latitude"],
              " Longitude: ", self.node_data["GPS"]["Longitude"],
              " Temp: ", self.node_data["Temp"], " Humidity: ", self.node_data["Humidity"])


def network_build(node_list):
    # function to build the chord sensor network. Returns the network as an entity
    network = SensorNetwork()  # create the network instance
    for node in node_list:  # join the nodes from the list
        node.node_join(network)
    for node in network.List_of_Nodes:  # update the finger tables for all the nodes
        node.update_finger_table()
    return network


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

    node_list = []
    node1 = SensorNode("A0E1", None)
    node_list.append(node1)
    node2 = SensorNode("A2B8", None)
    node_list.append(node2)
    node3 = SensorNode("B3F8", None)
    node_list.append(node3)
    node4 = SensorNode("D0F0", None)
    node_list.append(node4)
    net1 = network_build(node_list)

    print(net1.List_of_Nodes)
