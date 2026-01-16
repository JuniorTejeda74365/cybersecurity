# Cybersecurity Incident Report: Network Traffic Analysis

---

## Part One: Summary of the Problem Identified in the tcpdump Log

After analyzing the tcpdump log, the network traffic shows repeated DNS queries sent from the client to a DNS server using the UDP protocol. These DNS requests were made in an attempt to resolve the domain name `www.yummyrecipesforme.com`, but none of the requests were successfully completed.

The tcpdump log indicates that instead of receiving valid DNS responses, the client received ICMP error messages stating **“udp port 53 unreachable.”** Port 53 is commonly used by DNS services to resolve domain names into IP addresses. The repeated appearance of this port number in the log indicates an issue with DNS communication.

The log shows that DNS requests over UDP were sent multiple times and that each request resulted in the same ICMP error message. This pattern suggests that the DNS server was not accepting or processing requests on UDP port 53. As a result, DNS resolution failed, preventing the browser from obtaining the IP address needed to load the website.

---

## Part Two: Analysis of the Data and Incident Explanation

### Time Incident Occurred
The incident first occurred at approximately **13:24**, based on the timestamps recorded in the tcpdump traffic log.

### How the IT Team Became Aware of the Incident
The IT team became aware of the incident after multiple customers reported that they were unable to access the website and encountered a “destination port unreachable” error after attempting to load the page.

### Actions Taken to Investigate the Incident
The IT department attempted to access the affected website and then used the network analyzer tool **tcpdump** to capture and analyze network traffic. The investigation focused on DNS requests sent over UDP and the ICMP responses returned by the DNS server.

### Information Discovered During the Investigation
The investigation revealed that DNS queries sent to the DNS server over **UDP port 53** resulted in ICMP error messages indicating that the port was unreachable. This confirmed that DNS resolution was failing and that the browser could not retrieve the website’s IP address. The repeated ICMP responses showed that the issue persisted across multiple attempts.

### Current Status of the Issue
At the time of analysis, the issue remained unresolved and was being escalated to security engineers for further investigation and remediation.

### Next Steps in Troubleshooting and Resolution
Next steps include verifying the DNS server configuration, checking firewall rules related to UDP port 53, confirming that the DNS service is running correctly, and restoring DNS availability so domain name resolution can occur successfully.

### Suspected Root Cause of the Incident
The suspected root cause of the incident is a DNS service failure, firewall misconfiguration, or network issue that blocked or disabled UDP traffic on port 53, causing DNS requests to fail.

---

## Evidence (tcpdump Excerpt)

The following tcpdump output shows repeated DNS queries over UDP followed by ICMP error messages indicating that UDP port 53 was unreachable:

```text
13:24:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)
13:24:36.098564 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 udp port 53 unreachable length 254
13:26:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)
13:27:15.934126 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 udp port 53 unreachable length 320
13:28:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)
13:28:50.022967 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 udp port 53 unreachable length 150
