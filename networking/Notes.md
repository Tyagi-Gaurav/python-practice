# Introduction

*. Ethernet Switch to connect computers & printers via ethernet cables.
*. Ethernet switch could also be a Wifi router
*. Ethernet Frame has
    *. Payload
    *. Destination Mac
    *. Source Mac

* Hubs
    *. Unicast (one-to-one communication)
        * One device trying to connect to another device
        * When hub gets the message it transmits it to all the devices attached to the hub.
    * Can't handle multiple messages transmitted at the same time as a collision occurs.
    * No Mac address tables
*. Bridge
    * The problem of hub was solved by the bridge.
    * The bridge solved the problem by maintaining a list of mac addresses
    *. Breaks the collision domain into half
*. Switch (Layer 2)
    * The bridge was a precursor to switch
        * The switch has a mac table - so its a hub and bridge into one.
        * Every single port on the switch is its own collision domain i.e. it knows its mac address.
        * The message is not transmitted to all the ports.
    * Has Mac address tables
    * A switch is a broadcast domain
    * More devices = More Broadcast
    * Router breaks down the broadcast domain 
* Routers
    * Reduces number of broadcasts when there are too many switches in the network
    * Create boundaries between different segments of network (called subnets)
    * Each subnet has its own unique network address
    * Instead connect switch to a router

* OSI Model
    * Networking
        * Layer 1 - Physical
            * Switch (Layer 2)
            * Send to router
            * Ethernet Cable
        * Layer 2 - DataLink
            * Local Network
            * Mac address of NIC
            * Source address (Mac Address)
            * Sends to the switch
        * Layer 3 - Network
            * IP Address of the destination system
            * IP Address of the Source system
        * Layer 4 - Transport
            * HTTP
            * TCP/UDP Port
    * Browser
        * Layer 5 - Session
        * Layer 6 - Presentation
        * Layer 7 - Application

 * Broadcast messages
    * ARP (IP -> MAC)
        * L2 Broadcast
    * Unknown Unicast (Multiple switches)
        * Create large layer 2 network
    
* Default Gateway
    * A default gateway is a networking device or router that serves as an access point between a local network and external networks, such as the internet. It is responsible for forwarding network traffic from devices within the local network to destinations outside of it. When a device on the local network wants to communicate with a device in another network, it sends its data to the default gateway, which then routes it to the appropriate destination.
    * Maintains the ARP table
    * Forward traffic based on Ips.
    * It also is capable of holding VLAN mapping

* Switches vs Hubs vs Routers
    * Switches use MAC tables to make forwarding decisions by learning and associating MAC addresses with specific switch ports, allowing them to efficiently send data to the appropriate destination. Hubs and routers, on the other hand, do not use MAC tables; hubs broadcast data to all connected devices, while routers make forwarding decisions based on IP addresses and do not operate at the MAC address level.
    * Switches forward traffic based on Mac.
    * Switch maintains a separate MAC table for each VLAN

* VLAN 
 * Logical Segmentation of switch
 * Each VLAN has a subnet
 * Each VLAN has Mac address table
 * All machines within the same VLAN share the same subnet

* WAN
 * Dedicated physical circuit
 * Ex: 10G dedicated connection 

* IP Sec
  * Networks on both sides of an IPsec VPN connection typically have different address ranges to ensure proper routing and prevent IP conflicts. 
  * Different address ranges allow the VPN to distinguish between local and remote networks, ensuring that traffic is appropriately routed through the secure tunnel and avoiding IP address conflicts that could disrupt communication.

* Layer 2 VPN
  * They are used when maintaining the same IP address scheme is critical.
  * Layer 2 VPNs are invaluable in scenarios where maintaining consistent addressing across locations is essential.
  * Extends a segment
  * Disaster Recovery
  * Configuration
    * Configuring a Layer 2 VPN involves establishing a secure VPN tunnel, similar to IPSEC VPNs. Routers at both ends communicate, sharing secret passwords and using their public IP addresses to set up the tunnel.
  * Layer 2 VPNs allow for the extension of Layer 2 networks over geographic distances. This extension provides disaster recovery capabilities, enabling the restoration of workloads at different locations without IP address changes. It also facilitates mobility, as virtual machines can be moved between locations without altering their IP or MAC addresses.
  * A Layer 2 VPN typically extends the Ethernet broadcast domain across the VPN, allowing broadcast traffic, such as ARP (Address Resolution Protocol) requests, to traverse the VPN and reach devices in the same subnet on the other side.

* DHCP
 * DHCP request is a Layer 2 broadcast 
 * When a machine issues a DHCP (Dynamic Host Configuration Protocol) request, it typically sends an Ethernet broadcast message on the local network. 
 * This broadcast is used to discover and contact a DHCP server within the network, requesting an IP address assignment and other network configuration information.

 * Wifi 
    * Frequencies
        * 2.4Gz
            * Range: 150 feet/45 meters (Indoor)
            * Range: 300 feet/90 meters (Outdoor)
            * Approx 150Mbps
        * 5 Ghz
            * 50 feet / 15 meters (Indoors)
            * Approx 1300Mbps
    * WiFi access points (APs), these APs are typically connected to a wired network infrastructure, often through Ethernet cables. This wired network can include routers, switches, and possibly a central network controller if it's a managed wireless network.

* WLAN
    * Wireless Lan controllers help to manage the Wireless Adaptors

* Netflow/IPFix
    * Netflow is Cisco
        * NetFlow is useful for various network monitoring and troubleshooting tasks, including: Bandwidth Utilization: NetFlow helps identify which applications or devices are consuming the most bandwidth on the network, allowing administrators to optimize resource allocation and plan for capacity upgrades. 
        * Security: It aids in detecting and mitigating security threats by analyzing traffic patterns, identifying anomalies, and tracking potential malicious activity such as DDoS attacks, unusual port scans, or unauthorized access attempts.
    * IpFix is industry specific

* Why is NTP (Network Time Protocol) important?
    * Log Interpretation
    * Alarms and event correlations
    * Digital Certificates
    * Traffic flows over the UDP port 123

* IP Addressing
    * CIDR (Classless Inter Domain Routing)
        * Quicker way to write subnet mask
    * Subnet mask is used to figure out the network & host portion of the IP address
    * Number of hosts in a network
        * 1 address reserved for network itself
        * 1 for broadcast address 