# Security Risk Assessment Report  
## Network Hardening Analysis – Social Media Organization

---

## Context

This security risk assessment analyzes a simulated incident involving a social media organization that experienced a data breach exposing customers’ personal information, including names and addresses. The purpose of this assessment is to identify critical security weaknesses within the organization’s network and recommend network hardening controls that reduce the likelihood of future breaches.

---

## Identified Security Issues

After reviewing the organization’s network and security practices, the following issues were identified:

1. **Employees share passwords**, increasing the risk of unauthorized access and eliminating accountability.
2. **The database administrator password is set to the default**, creating a well-known and easily exploitable attack vector.
3. **Firewalls do not have rules configured to filter inbound and outbound traffic**, allowing unrestricted network communication.
4. **Multifactor authentication (MFA) is not implemented**, enabling attackers to gain access using stolen credentials alone.

If left unaddressed, these issues significantly increase the organization’s exposure to data breaches, unauthorized access, and data exfiltration.

---

## Part 1: Selected Network Hardening Tools and Methods

The following three network hardening controls were selected to address the identified issues:

1. **Multifactor Authentication (MFA)**
2. **Password Policies**
3. **Firewall Maintenance and Port Filtering**

---

## Part 2: Explanation of Recommendations

### 1. Multifactor Authentication (MFA)

Multifactor authentication requires users to verify their identity using two or more authentication factors, such as a password combined with a one-time passcode or biometric verification. The absence of MFA allows attackers to gain access if credentials are compromised through phishing, brute force attacks, or password reuse.

Implementing MFA adds an additional layer of security that prevents unauthorized access even when passwords are stolen. This control is especially important for administrative and database access.

**Risk Mitigated:**  
- Credential theft  
- Account takeover  
- Unauthorized access to sensitive systems  

---

### 2. Password Policies

Employees sharing passwords and the use of default administrative credentials present a critical security risk. Password policies aligned with current NIST recommendations enforce unique credentials, proper password hashing and salting, and the removal of default passwords.

Strong password policies reduce the effectiveness of brute force and credential-stuffing attacks while improving accountability by ensuring each user has a unique identity.

**Risk Mitigated:**  
- Password sharing  
- Default credential exploitation  
- Brute force attacks  

---

### 3. Firewall Maintenance and Port Filtering

The organization’s firewalls currently allow unrestricted inbound and outbound traffic, increasing exposure to malicious activity. Firewall maintenance involves
