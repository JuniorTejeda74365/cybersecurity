# Security Risk Assessment Report

---

## Part 1: Select up to three hardening tools and methods to implement

The following network hardening tools and methods are recommended to address the vulnerabilities identified within the organization:

1. **Multifactor Authentication (MFA)**
2. **Password Policies**
3. **Firewall Maintenance and Port Filtering**

---

## Part 2: Explain your recommendations

### 1. Multifactor Authentication (MFA)

Multifactor authentication requires users to verify their identity using two or more authentication factors, such as a password combined with a one-time passcode or biometric verification. Currently, the organization does not use MFA, which allows attackers to gain access to systems if passwords are compromised.

Implementing MFA significantly reduces the risk of unauthorized access, even if employee credentials are stolen through phishing, brute force attacks, or password sharing. This method helps protect both employee accounts and administrative access, preventing attackers from easily accessing sensitive systems and customer data.

---

### 2. Password Policies

The organization’s employees currently share passwords, and the database administrator password is set to the default. Password policies based on current NIST recommendations ensure that passwords are properly salted and hashed and that default credentials are removed.

Enforcing strong password policies prevents credential reuse and password sharing, improves accountability, and reduces the risk of brute force attacks. Changing default administrative passwords removes a well-known attack vector commonly exploited by malicious actors.

---

### 3. Firewall Maintenance and Port Filtering

The organization’s firewalls currently do not have rules in place to filter incoming and outgoing traffic. Firewall maintenance involves regularly reviewing and updating firewall rules, while port filtering blocks or allows specific port numbers to control network communication.

Implementing firewall rules and port filtering reduces the attack surface by allowing only necessary traffic into and out of the network. Blocking unused or high-risk ports helps prevent unauthorized access, malware communication, and data exfiltration attempts, thereby reducing the likelihood of future breaches.

---

## Conclusion

The data breach occurred due to weak authentication practices, default credentials, and insufficient network traffic filtering. Implementing multifactor authentication, enforcing strong password policies, and maintaining firewalls with proper port filtering will significantly improve the organization’s security posture. These network hardening practices reduce unauthorized access, improve monitoring, and help prevent similar breaches in the future.
