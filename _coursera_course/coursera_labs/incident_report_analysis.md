# Incident Report Analysis
## Denial-of-Service (DoS) Attack – ICMP Flood

---

## Security Event Summary

The organization experienced a Denial-of-Service (DoS) attack that disrupted internal network operations for approximately two hours. During the incident, the network became unresponsive due to a large volume of incoming ICMP echo request (ping) packets. Normal internal network traffic was unable to access network resources.

The attack was caused by a malicious actor exploiting an unconfigured firewall that allowed unrestricted ICMP traffic. This vulnerability enabled the attacker to overwhelm network resources.

### Impact
- Network services unavailable for two hours
- Internal users unable to access network resources
- Business operations disrupted

### Response
- Incoming ICMP traffic was blocked at the firewall
- Non-critical services were taken offline
- Critical network services were restored
- A security investigation was conducted

### Targeted Systems and Attack Source
- Targeted systems: Network firewall, internal network infrastructure, network services
- Attack source: External malicious actor using unverified or spoofed IP addresses

---

##  Identify the Type of Attack and Systems Affected (Identify)

### Type of Attack
- Denial-of-Service (DoS) attack
- ICMP flood attack

### Systems Affected
- Network firewall
- Internal network infrastructure
- Network-dependent services

### Identified Vulnerabilities
- Unconfigured firewall
- Lack of ICMP rate limiting
- No source IP address verification

---

## Protect Organizational Assets (Protect)

To improve protection against future attacks, the following actions should be taken:

- Implement ICMP rate limiting on the firewall
- Enable source IP address verification
- Establish baseline firewall configurations
- Apply network hardening policies
- Train IT staff on secure network configurations
- Restrict unnecessary external access to internal services

These measures reduce the organization’s exposure to DoS attacks and improve network resilience.

---

## Detect Similar Incidents in the Future (Detect)

To detect similar incidents early, the organization should:

- Deploy network monitoring software to analyze traffic patterns
- Implement IDS/IPS systems to identify malicious ICMP traffic
- Configure alerts for abnormal ICMP packet rates
- Monitor traffic from non-trusted IP addresses
- Enable centralized logging for network devices and security tools

These detection mechanisms improve visibility and response time.

---

## Respond to Future Cybersecurity Incidents (Respond)

### Containment
- Isolate affected network segments or devices
- Block malicious IP addresses and traffic types
- Disable non-essential services when necessary

### Neutralization
- Update firewall and IDS/IPS rules
- Remove malicious traffic patterns
- Verify system integrity after mitigation

### Analysis
- Review firewall logs, IDS/IPS alerts, and traffic data
- Identify attack indicators such as source IPs and packet types
- Document findings for future reference

### Process Improvements
- Develop a formal incident response playbook
- Define escalation and communication procedures
- Conduct post-incident reviews

---

## Recover from the Incident (Recover)

### Recovery Actions
- Restore all network services to normal operation
- Validate firewall and monitoring configurations
- Verify critical systems functionality
- Review and update backup and recovery procedures

### Information Required for Recovery
- Network configurations and firewall rules
- Incident logs and alerts
- Backup system images and configurations

### Recovery Outcome
The organization resumes normal operations with improved defenses and incident preparedness.
