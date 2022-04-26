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
FILE DESCRIPTION: calc_hash_value() function definition
"""

# Import Python Modules
import hashlib


def calc_hash_value(input_val, space):
    # function to calculate the hash value of an input value
    output_val = hashlib.sha1()
    output_val.update(str(input_val).encode())
    output_val = int(output_val.hexdigest(), 16)
    output_val = output_val % space
    return output_val
