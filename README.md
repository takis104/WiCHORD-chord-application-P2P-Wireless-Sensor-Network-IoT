# WiCHORD: A Chord Protocol Application on P2P LoRa Wireless Sensor Networks - IoT
P2P Wireless Sensor Network (WSN) System Based on the Chord Protocol from DHTs and LoRa Wireless Technology

The case study of this project is to customize the Chord Protocol on a Wireless Sensor Network environment.

## Publication
This solution was proposed on a conference paper on the IEEE IISA 2022 Conference, held at Ionial University on July 18 2022, in Corfu Greece.

The publication is available on IEEE Xplore: https://ieeexplore.ieee.org/document/9904339

Publisher: IEEE

### Publication's Authors
Christos-Panagiotis Balatsouras, Aristeidis Karras, Christos Karras, Dimitrios Tsolis, Spyros Sioutas

### Publication's Abstract
On the modern era of Internet of Things (IoT) and Industry 4.0 there is a growing need for reliable wireless long range communications. LoRa is an emerging technology for effective long range communications which can be directly applied to IoT applications. Wireless sensor networks (WSNs) are by far an efficient infrastructure where sensors act as nodes and exchange information among themselves. Distributed applications such as Peer-to-Peer (P2P) networks are inextricably linked with Distributed Hash Tables (DHTs) whereabouts DHTs offer effective and speedy data indexing. A Distributed Hash Table structure known as the Chord algorithm enables the lookup operation of nodes which is a major algorithmic function of P2P networks. In the context of this paper, the inner workings of Chord protocol are highlighted along with an introduced modified version of it for WSNs. Additionally, we adapt the proposed method on LoRa networks where sensors function as nodes. The outcomes of the proposed method are encouraging as per complexity and usability and future directions of this work include the deployment of the proposed method in a large scale environment, security enhancements and distributed join, leave and lookup operations.

### Publication's Presentation
https://www.youtube.com/watch?v=yVesxUl2fR4

## Cite this work
If you find this work useful, please cite the above mentioned publication as follows:

### Plain Text Citation
C. -P. Balatsouras, A. Karras, C. Karras, D. Tsolis and S. Sioutas, "WiCHORD: A Chord Protocol Application on P2P LoRa Wireless Sensor Networks," 2022 13th International Conference on Information, Intelligence, Systems & Applications (IISA), 2022, pp. 1-8, doi: 10.1109/IISA56318.2022.9904339.

### BiBTeX
@INPROCEEDINGS{9904339,  
author={Balatsouras, Christos-Panagiotis and Karras, Aristeidis and Karras, Christos and Tsolis, Dimitrios and Sioutas, Spyros},  
booktitle={2022 13th International Conference on Information, Intelligence, Systems & Applications (IISA)},   
title={WiCHORD: A Chord Protocol Application on P2P LoRa Wireless Sensor Networks},   
year={2022},  
volume={},  
number={},  
pages={1-8},  
doi={10.1109/IISA56318.2022.9904339}}

## Repository Contents (Code)
- Simulator Application of the Chord Protocol overlay on sensor networks in Python, with the following contents:
  * Chord Network Build Operation
  * Node Join/Leave Operation
  * Node Lookup Query Operation
  * Calculation of Lookup Query Path Length
- Chord protocol overlay for LoRa Wireless Sensor Networks in Arduino C++
  * Supported LoRa MCU Board: LILYGO TTGO T-Beam v1.1 ESP32
