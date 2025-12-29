# Botium Toys Internal Security Audit Report

---

## Executive Summary

Botium Toys is a growing U.S.-based toy company with a physical storefront, warehouse, and expanding online presence. Due to increased customer data processing and international sales, the IT manager requested an internal security audit to assess organizational risks, security controls, and regulatory compliance.

This audit identified several critical security weaknesses, including a lack of encryption, absence of data backups, missing least-privilege access controls, weak password requirements, and multiple compliance gaps. Based on these findings, the overall risk score for Botium Toys is **8/10 (High)**.

---

## Scope of the Audit

The scope of this audit includes the organization’s entire security program, covering:

* Employee devices
* Internal network infrastructure
* Systems and software
* Data handling and storage practices
* Physical security controls
* Legacy systems
* Online payment processing
* Compliance with U.S. and E.U. regulations

---

## Audit Goals

The objectives of this audit were to:

* Identify and classify existing assets
* Evaluate current administrative, technical, and physical controls
* Assess compliance with PCI DSS, GDPR, and SOC 1/2 standards
* Identify security risks and gaps
* Recommend improvements to strengthen the security posture

---

## Asset Inventory

### Hardware Assets

* Office desktops and laptops
* Smartphones
* Remote workstations
* Keyboards, mice, and docking stations
* Headsets
* Surveillance cameras
* Warehouse and storefront equipment
* Legacy systems (end-of-life equipment requiring monitoring)

### Software & Systems

* Accounting systems
* Telecommunication systems
* Inventory management systems
* Ecommerce platform
* Security software
* Databases

### Network Assets

* Internal network
* Internet access infrastructure
* Firewalls

### Data Assets

* Customer PII/SPII
* Credit card data
* Employee data
* Internal business data
* Inventory data
* Ecommerce transaction data

---

## Risk Assessment

### Risk Description

Botium Toys lacks adequate asset management and several required security controls. Compliance with regulatory standards is incomplete, creating increased legal, financial, and operational risks.

### Risk Score

**8 out of 10 — High Risk**

### Impact Level

* Medium impact on day-to-day operations
* High risk of regulatory fines and sensitive data exposure

### Key Risk Findings

* All employees can access PII and cardholder data
* No encryption implemented for credit card data
* No least-privilege access or separation of duties
* No intrusion detection system (IDS)
* No data backups
* No disaster recovery plan
* Legacy systems lack scheduled maintenance
* Weak password policy
* No password management system

---

## Controls Assessment Checklist

| Control                          | In Place            |
| -------------------------------- | ------------------- |
| Least Privilege                  | No                  |
| Separation of Duties             | No                  |
| Password Policies                | Yes (weak)          |
| Password Management System       | No                  |
| Firewall                         | Yes                 |
| Intrusion Detection System (IDS) | No                  |
| Antivirus Software               | Yes                 |
| Backups                          | No                  |
| Disaster Recovery Plan           | No                  |
| Manual Legacy System Maintenance | Yes (not scheduled) |
| Encryption                       | No                  |
| Physical Locks                   | Yes                 |
| CCTV                             | Yes                 |
| Fire Detection / Prevention      | Yes                 |

---

## Compliance Assessment

### PCI DSS

| Best Practice                              | In Place |
| ------------------------------------------ | -------- |
| Authorized access to cardholder data only  | No       |
| Secure storage and processing of card data | No       |
| Encryption of card data                    | No       |
| Secure password management                 | No       |

### GDPR

| Best Practice                              | In Place |
| ------------------------------------------ | -------- |
| E.U. customer data kept private and secure | No       |
| 72-hour breach notification plan           | Yes      |
| Data classified and inventoried            | No       |
| Privacy policies enforced                  | Yes      |

### SOC 1 / SOC 2

| Best Practice                    | In Place |
| -------------------------------- | -------- |
| User access policies established | No       |
| PII/SPII kept confidential       | No       |
| Data integrity controls          | Yes      |
| Data availability controls       | Yes      |

---

## Gap Analysis

| Category            | Gap Identified            | Impact              | Priority |
| ------------------- | ------------------------- | ------------------- | -------- |
| Access Control      | No least privilege        | Unauthorized access | High     |
| Access Control      | No separation of duties   | Fraud risk          | High     |
| Encryption          | Card data unencrypted     | PCI violation       | Critical |
| Monitoring          | No IDS                    | Undetected attacks  | High     |
| Business Continuity | No backups                | Data loss           | Critical |
| Business Continuity | No disaster recovery plan | Extended downtime   | Critical |
| Identity Management | Weak passwords            | Account compromise  | High     |
| Identity Management | No password manager       | Password reuse      | Medium   |
| Asset Management    | No asset classification   | Unknown risks       | Medium   |
| Legacy Systems      | No maintenance schedule   | System failures     | Medium   |

---

## Recommendations

### Critical Priority

* Implement encryption for all cardholder data
* Build daily automated backups
* Establish a full disaster recovery plan
* Deploy an intrusion detection system (IDS)

### High Priority

* Implement least-privilege access controls
* Establish separation of duties
* Strengthen password policies
* Introduce centralized password management
* Classify and inventory all assets
* Implement role-based access control (RBAC)

### Medium Priority

* Schedule regular maintenance for legacy systems
* Improve secure data handling processes

### Low Priority

* Continue maintaining physical security controls (locks, CCTV, fire detection)

---

## Conclusion

Botium Toys faces significant security risks due to missing technical and administrative controls and incomplete regulatory compliance. Addressing the identified gaps—particularly encryption, backups, access controls, and monitoring—will substantially improve the organization’s security posture and reduce the likelihood of data breaches or regulatory penalties.

This internal audit provides a clear roadmap for prioritizing remediation efforts and aligning Botium Toys with industry best practices and regulatory requirements.


