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
        pass

    def network_reload(self):
        pass


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
    def __init__(self):
        pass
    
    def node_join(self):
        pass
    
    def node_leave(self):
        pass
    
    def lookup_query(self):
        pass
    
    def data_reload(self):
        pass


"""
# main process
"""
if __name__ == "__main__":  # Execute these lines, only if this module is executed by itself.
    print("Chord Protocol Application on Wireless Sensor Networks")
    print("Implementation by Christos-Panagiotis Mpalatsouras")
