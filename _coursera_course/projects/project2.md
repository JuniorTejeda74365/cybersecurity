In this activity, you will analyze DNS and ICMP traffic in transit using data from a network protocol analyzer tool. You will identify which network protocol was utilized in assessment of the cybersecurity incident. 

In the internet layer of the TCP/IP model, the IP formats data packets into IP datagrams. The information provided in the datagram of an IP packet can provide security analysts with insight into suspicious data packets in transit.

Knowing how to identify potentially malicious traffic on a network can help cybersecurity analysts assess security risks on a network and reinforce network security.

You are a cybersecurity analyst working at a company that specializes in providing IT services for clients. Several customers of clients reported that they were not able to access the client company website www.yummyrecipesforme.com, and saw the error “destination port unreachable” after waiting for the page to load. 

You are tasked with analyzing the situation and determining which network protocol was affected during this incident. To start, you attempt to visit the website and you also receive the error “destination port unreachable.” To troubleshoot the issue, you load your network analyzer tool, tcpdump, and attempt to load the webpage again. To load the webpage, your browser sends a query to a DNS server via the UDP protocol to retrieve the IP address for the website's domain name; this is part of the DNS protocol. Your browser then uses this IP address as the destination IP for sending an HTTPS request to the web server to display the webpage  The analyzer shows that when you send UDP packets to the DNS server, you receive ICMP packets containing the error message: “udp port 53 unreachable.” 

13:24:32.192571 IP 192.51.100.15.52444 > 203.0.113.2. domain: 35084+ A?
yummyrecipesforme.com. (24)
13:24:36.098564 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2
udp port 53 unreachable length 254
13:26:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A?
yummyrecipesforme.com. 24)
13:27:15.934126 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2
udp port 53 unreachable length 320
13:28:32.192571 IP 192.51.100.15.52444 > 203.0.113.2. domain: 35084+ A?
yummyrecipesforme.com. (24)
13:28:50.022967 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2
udp port 53 unreachable length 150

The DNS and ICMP traffic logs show that the client sent DNS queries over UDP port 53 to resolve the domain yummyrecipesforme.com. Instead of receiving a DNS response, the client received ICMP error messages indicating “UDP port 53 unreachable.” This shows that the DNS service was unavailable or inaccessible, preventing the domain name from being resolved and stopping the website from loading.

The problem was first reported when users were unable to access the yummyrecipesforme.com website and received a “destination port unreachable” error. At the time of the incident, the client attempted to load the website, triggering DNS resolution requests to determine the server’s IP address.

The tcpdump log shows that DNS queries were sent using UDP to port 53, but the DNS server responded with ICMP error messages indicating that UDP port 53 was unreachable. This confirms that the DNS service was unavailable or inaccessible. As a result, the client could not resolve the domain name, and the HTTPS request to the web server never occurred.

Currently, the issue remains unresolved, as repeated DNS requests continue to fail and generate ICMP error responses. Investigation of the traffic revealed that the issue is isolated to DNS communication and not the web server itself.

The next steps in troubleshooting include verifying that the DNS service is running on the server, checking firewall rules or access control lists that may be blocking UDP port 53, and confirming proper network configuration between the client and DNS server.

The suspected root cause of the incident is a misconfigured or unavailable DNS service, or a firewall blocking UDP traffic on port 53.
