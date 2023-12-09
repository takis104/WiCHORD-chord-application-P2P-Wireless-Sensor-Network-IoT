# WiCHORD: A Chord Protocol Adaptation on P2P Wireless Sensor Networks powered by LoRa Wireless Communication Technology
P2P Wireless Sensor Network (WSN) Overlay, based on the Chord Protocol from DHTs and LoRa Wireless Technology

The case study of this project is to customize the Chord Protocol on a Wireless Sensor Network environment, first in terms of simulation and then in terms of implementation.

**This work is published in the following publications:**
1. **Conference Paper on IEEE IISA 2022**, entitled: "WiCHORD: A Chord Protocol Application on P2P LoRa Wireless Sensor Networks" (C. -P. Balatsouras, A. Karras, C. Karras, D. Tsolis and S. Sioutas, "WiCHORD: A Chord Protocol Application on P2P LoRa Wireless Sensor Networks," 2022 13th International Conference on Information, Intelligence, Systems & Applications (IISA), Corfu, Greece, 2022, pp. 1-8, doi: 10.1109/IISA56318.2022.9904339.)
2. **Journal Paper on MDPI Sensors**, entitled: "WiCHORD+: A Scalable and Sustainable Chord-based Ecosystem for Smart Agriculture Applications" (Balatsouras, C.-P.; Karras, A.; Karras, C.; Karydis, I.; Sioutas, S. WiCHORD+: A Scalable, Sustainable, and P2P Chord-Based Ecosystem for Smart Agriculture Applications. Sensors 2023, 23, 9486. https://doi.org/10.3390/s23239486)

## Repository Contents (Code)
- Simulator Application of the Chord Protocol overlay on sensor networks in Python, with the following contents:
  * (WiCHORD): Sensor Network & Sensor Node Instance Classes Definition
  * (WiCHORD): Chord Network Build Operation
  * (WiCHORD): Node Join/Leave Operation
  * (WiCHORD): Node Lookup Query Operation
  * (WiCHORD): Calculation of Lookup Query Path Length
  * (WiCHORD+): Calculation of total number of Node IDs (contacts) stored for each sensor node on the network
  * (WiCHORD+): Calculation of the average number of sensor nodes involved on a Join/Leave/Lookup Query resolution
<!-- - Chord protocol overlay for LoRa Wireless Sensor Networks in Arduino Embedded C++
  * Supported LoRa MCU Board: LILYGO TTGO T-Beam v1.1 ESP32 -->

### Required Python Packages
pandas, matplotlib, hashlib, random, secrets, csv

### Simulator Python Scripts Functionality
- WiCHORD-Simulator-Python-Implementation/wi-chord_simulator.py: Main simulator that tests the WiCHORD network build functionality and supports lookup queries.
- WiCHORD-Simulator-Python-Implementation/wi-chord_simulator_query-path.py: Runs the experiment of measuring the query path length per total nodes on a WiCHORD Network.
- WiCHORD-Plus-Simulator-Python/wichord-plus-simulator.py: Runs the experiments of key load balancing evaluation on the nodes of a WiCHORD Network alongside with the number of involved nodes to perform the join/leave/lookup operations per total network nodes in order to evaluate the energy efficiency of the WiCHORD Protocol overlay for Wireless Sensor Networks.

## 1. Conference Paper on IEEE IISA 2022: "WiCHORD: A Chord Protocol Application on P2P LoRa Wireless Sensor Networks"
This solution was proposed on a conference paper entitled "WiCHORD: A Chord Protocol Application on P2P LoRa Wireless Sensor Networks" on the IEEE IISA 2022 Conference, held at Ionial University on July 18 2022, in Corfu Greece.

The publication is available on IEEE Xplore: https://ieeexplore.ieee.org/document/9904339

Publisher: IEEE

<a href="https://www.researchgate.net/profile/Christos-Panagiotis-Balatsouras/publication/361745127_WiCHORD_A_Chord_Protocol_Application_on_P2P_LoRa_Wireless_Sensor_Networks/links/63387d83ff870c55cef0a565/WiCHORD-A-Chord-Protocol-Application-on-P2P-LoRa-Wireless-Sensor-Networks.pdf"> Read the publication on ResearchGate </a>

### Publication's Authors
Christos-Panagiotis Balatsouras, Aristeidis Karras, Christos Karras, Dimitrios Tsolis, Spyros Sioutas

### Publication's Abstract
On the modern era of Internet of Things (IoT) and Industry 4.0 there is a growing need for reliable wireless long range communications. LoRa is an emerging technology for effective long range communications which can be directly applied to IoT applications. Wireless sensor networks (WSNs) are by far an efficient infrastructure where sensors act as nodes and exchange information among themselves. Distributed applications such as Peer-to-Peer (P2P) networks are inextricably linked with Distributed Hash Tables (DHTs) whereabouts DHTs offer effective and speedy data indexing. A Distributed Hash Table structure known as the Chord algorithm enables the lookup operation of nodes which is a major algorithmic function of P2P networks. In the context of this paper, the inner workings of Chord protocol are highlighted along with an introduced modified version of it for WSNs. Additionally, we adapt the proposed method on LoRa networks where sensors function as nodes. The outcomes of the proposed method are encouraging as per complexity and usability and future directions of this work include the deployment of the proposed method in a large scale environment, security enhancements and distributed join, leave and lookup operations.

### Publication's Presentation
https://www.youtube.com/watch?v=yVesxUl2fR4

## 2. Journal Paper on MDPI Sensors: "WiCHORD+: A Scalable, Sustainable and P2P Chord-based Ecosystem for Smart Agriculture Applications"
The extended version of this solution was proposed on a journal paper entitled: "WiCHORD+: A Scalable, Sustainable, and P2P Chord-Based Ecosystem for Smart Agriculture Applications", which was published on the MDPI Sensors Open Access Journal.

This publication is available to read online on MDPI: https://www.mdpi.com/1424-8220/23/23/9486

Publisher: MDPI

### Publication's Authors
Christos-Panagiotis Balatsouras, Aristeidis Karras, Christos Karras, Ioannis Karydis, Spyros Sioutas

### Publication's Abstract
In the evolving landscape of Industry 4.0, the convergence of peer-to-peer (P2P) systems, LoRa-enabled wireless sensor networks (WSNs), and distributed hash tables (DHTs) represents a major advancement that enhances sustainability in the modern agriculture framework and its applications. In this study, we propose a P2P Chord-based ecosystem for sustainable and smart agriculture applications, inspired by the inner workings of the Chord protocol. The node-centric approach of WiCHORD+ is a standout feature, streamlining operations in WSNs and leading to more energy-efficient and straightforward system interactions. Instead of traditional key-centric methods, WiCHORD+ is a node-centric protocol that is compatible with the inherent characteristics of WSNs. This unique design integrates seamlessly with distributed hash tables (DHTs), providing an efficient mechanism to locate nodes and ensure robust data retrieval while reducing energy consumption. Additionally, by utilizing the MAC address of each node in data routing, WiCHORD+ offers a more direct and efficient data lookup mechanism, essential for the timely and energy-efficient operation of WSNs. While the increasing dependence of smart agriculture on cloud computing environments for data storage and machine learning techniques for real-time prediction and analytics continues, frameworks like the proposed WiCHORD+ appear promising for future IoT applications due to their compatibility with modern devices and peripherals. Ultimately, the proposed approach aims to effectively incorporate LoRa, WSNs, DHTs, cloud computing, and machine learning, by providing practical solutions to the ongoing challenges in the current smart agriculture landscape and IoT applications.

## Cite this work
If you find this work useful, please cite the above mentioned publications as follows:

### Plain Text Citations
- C. -P. Balatsouras, A. Karras, C. Karras, D. Tsolis and S. Sioutas, "WiCHORD: A Chord Protocol Application on P2P LoRa Wireless Sensor Networks," 2022 13th International Conference on Information, Intelligence, Systems & Applications (IISA), 2022, pp. 1-8, doi: 10.1109/IISA56318.2022.9904339.
- Balatsouras, C.-P.; Karras, A.; Karras, C.; Karydis, I.; Sioutas, S. WiCHORD+: A Scalable, Sustainable, and P2P Chord-Based Ecosystem for Smart Agriculture Applications. Sensors 2023, 23, 9486. https://doi.org/10.3390/s23239486 

### BiBTeX Citations
 - @INPROCEEDINGS{9904339, author={Balatsouras, Christos-Panagiotis and Karras, Aristeidis and Karras, Christos and Tsolis, Dimitrios and Sioutas, Spyros}, booktitle={2022 13th International Conference on Information, Intelligence, Systems & Applications (IISA)}, title={WiCHORD: A Chord Protocol Application on P2P LoRa Wireless Sensor Networks}, year={2022}, volume={}, number={}, pages={1-8}, doi={10.1109/IISA56318.2022.9904339}}
 - @Article{s23239486, AUTHOR = {Balatsouras, Christos-Panagiotis and Karras, Aristeidis and Karras, Christos and Karydis, Ioannis and Sioutas, Spyros}, TITLE = {WiCHORD+: A Scalable, Sustainable, and P2P Chord-Based Ecosystem for Smart Agriculture Applications}, JOURNAL = {Sensors}, VOLUME = {23}, YEAR = {2023}, NUMBER = {23}, ARTICLE-NUMBER = {9486}, URL = {https://www.mdpi.com/1424-8220/23/23/9486}, ISSN = {1424-8220}, DOI = {10.3390/s23239486}}
