
Section One: Network Intrusion Attack Analysis

Network attacks are attempts to disrupt, degrade, or gain unauthorized access to network services by exploiting weaknesses in protocols, configurations, or system resources. Common network-based attacks include denial-of-service (DoS) attacks, distributed denial-of-service (DDoS) attacks, man-in-the-middle attacks, spoofing, and flooding attacks that overwhelm a target with excessive traffic.

The symptoms described in the incident—slow website loading, repeated connection attempts, TCP reset packets, and connection timeout errors—are most consistent with a denial-of-service–type attack, specifically a TCP SYN flood attack. This type of attack exploits the TCP three-way handshake by sending a large number of SYN packets without completing the connection process, causing the server to maintain numerous half-open connections and exhaust available resources.

A DoS attack originates from a single source and focuses on overwhelming the target system’s resources, while a DDoS attack uses multiple distributed systems to generate attack traffic simultaneously. Although both attacks have the same goal of disrupting service availability, DDoS attacks are more difficult to mitigate due to the volume and geographic distribution of the traffic. Based on the Wireshark data, the traffic appears to originate from a limited number of sources, which aligns more closely with a DoS attack rather than a DDoS attack.

The website is taking a long time to load and reporting connection timeout errors because the web server is unable to process legitimate client requests while managing an excessive number of incomplete TCP connection attempts. This results in delayed responses, dropped connections, and web application timeout errors such as 504 Gateway Time-out.

Review of the Wireshark capture reveals repeated TCP SYN packets, incomplete three-way handshakes, frequent RST/ACK packets, and multiple failed connection attempts to web services operating over TCP port 443. These patterns indicate that the server’s resources are being consumed by half-open connections, confirming that a TCP SYN flood–based denial-of-service attack caused the service interruption.

Section Two: Impact Analysis and Network Activity Review

The Wireshark capture indicates that the organization experienced a denial-of-service (DoS) attack, specifically a TCP SYN flood attack, targeting the web server over TCP port 443. This attack is characterized by a high volume of TCP SYN packets sent to the server without completing the TCP three-way handshake. The capture shows repeated SYN packets, incomplete connection attempts, frequent TCP reset (RST/ACK) packets, and web application timeout errors, which are common indicators of this type of attack.

The attack involved external client systems repeatedly initiating TCP connections to the organization’s web server. Network devices such as firewalls, routers, and the web server itself were required to process and track these connection attempts. As the number of half-open connections increased, the server’s available resources became constrained, resulting in delayed responses and failed connection attempts for legitimate users.

This attack affected the organization’s network by degrading the availability and performance of the website. Legitimate web requests over TCP port 443 were either delayed or dropped, causing slow page loads, repeated connection retries, and application-layer errors such as 504 Gateway Time-out. Although the web server was still reachable, it could not reliably maintain connections due to resource exhaustion, which disrupted normal website functionality.

The potential consequences of this attack include prolonged website downtime, loss of customer trust, and possible financial impact due to interrupted services. Continued exposure to this type of attack could also strain network infrastructure, increase operational costs, and create opportunities for additional attacks while defenses are overwhelmed.

To prevent similar attacks in the future, the organization could implement network security measures such as TCP SYN cookies, rate limiting, firewall rules to filter abnormal traffic patterns, and intrusion detection or prevention systems (IDS/IPS). These controls would help detect and mitigate excessive connection attempts before they impact server availability.

## Evidence

The following Wireshark capture was used to identify and analyze the network intrusion:

- `analyze_network_attacks_evidence/wireshark_tcp443_syn_flood.log`
