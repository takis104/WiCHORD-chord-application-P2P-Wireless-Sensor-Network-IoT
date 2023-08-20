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
FILE DESCRIPTION: Message class definition
"""

# import Python modules
# ...

# Import other modules from this project
# ...


# The class for each message passed from one sensor node to another on the network
class Message:
    """
    Class Message:
    Data: Message Attributes
    Operations:
    To be added later...
    """

    def __int__(self, message_type, network_id, routing_flag, message_origin, message_forwarded_node, message_destination):
        self.query_type = message_type
        self.net_id = network_id
        self.wichord_routing_flag = routing_flag
        self.origin_node = message_origin
        self.intermediate_node = message_forwarded_node
        self.destination_node = message_destination

