# Overview:

# Botium Toys Internal Security Audit Report
1. Executive Summary

Botium Toys is a growing U.S.-based toy company with a physical storefront, warehouse, and expanding online presence. Due to increased customer data processing and international sales, the IT manager requested an internal security audit to assess risks, controls, and compliance with major regulations.

The current audit identifies critical issues including lack of encryption, no backups, missing least-privilege access controls, weak password requirements, and several compliance gaps. Overall risk score: 8/10 (High).

2. Scope of the Audit

The scope includes the entire security program at Botium Toys:
Employee devices
Internal network
Systems and software
Data handling and storage
Physical security
Legacy systems
Online payment processing
Compliance with U.S. and E.U. regulations

3. Audit Goals

Identify and classify existing assets
Evaluate current administrative, technical, and physical controls
Assess PCI DSS, GDPR, and SOC 1/2 compliance
Identify risks, gaps, and recommend improvements

4. Asset Inventory

4.1 Hardware Assets

Office desktops/laptops
Smartphones
Remote workstations
Keyboards, mice, docking stations
Headsets
Surveillance cameras
Warehouse/storefront equipment
Legacy systems (end-of-life equipment requiring monitoring)

4.2 Software & Systems

Accounting systems
Telecommunication systems
Inventory management
Ecommerce platform
Security software
Databases

4.3 Network Assets

Internal network
Internet access
Firewalls

4.4 Data Assets

Customer PII/SPII
Credit card data
Employee data
Internal business data
Inventory data
Ecommerce transactions

5. Risk Assessment

5.1 Risk Description

Botium Toys lacks adequate asset management and several required controls. Compliance with regulatory standards is incomplete, creating legal, financial, and operational risks.

5.2 Risk Score

8 out of 10 — High risk.

5.3 Impact Level:

Medium impact on operations, high risk for fines and data exposure.

5.4 Key Risk Findings:

All employees can access PII and cardholder data

No encryption for credit card data

No least privilege or separation of duties

No IDS (Intrusion Detection System)

No backups

No disaster recovery plan

Legacy systems unscheduled maintenance

Weak password policy

No password management system

6. Controls Assessment Checklist

Control	In Place?

Least Privilege	No

Separation of Duties  No

Password Policies  Yes (weak)

Password Management System  No

Firewall  Yes

IDS (Intrusion Detection System)  No

Antivirus Softwar  Yes

Backups	No

Disaster Recovery Plans	No

Manual Legacy System Maintenance  Yes (not scheduled)

Encryption	No

Locks	Yes

CCTV	Yes

Fire Detection/Prevention	Yes

7. Compliance Checklist

7.1 PCI DSS

Best Practice	In Place?

Only authorized users access credit card info	No

Credit card data stored/processed securely	No

Encryption implemented for card data	No

Secure password management	No

7.2 GDPR

Best Practice	In Place?

E.U. customer data kept private/secure	No

72-hour breach notification plan	Yes

Data classified and inventoried	No

Privacy policies enforced	Yes


7.3 SOC 1 / SOC 2

Best Practice	In Place?

User access policies established    No

PII/SPII kept confidential	No

Data integrity controls	Yes

Data availability controls	Yes


8. Gap Analysis

Category	Gap Identified	Impact	Priority

Access Control	No least privilege	High risk of unauthorized access	High

Access Control	No separation of duties	Fraud/abuse possible	High

Encryption	Card data unencrypted  PCI violation	Critical

Monitoring	No IDS	Attacks may go undetected	High

Business Continuity	No backups	Data loss risk	Critical

Business Continuity	No disaster recovery plan	Extended downtime	Critical

Identity Management	Weak passwords Account compromise	High

Identity Management	No password manager	Reuse/weak passwords	Medium

Asset Management	No classification/inventory	Unknown risks	Medium

Legacy Systems	No schedule for monitoring	Unexpected failures	Medium


9. Recommendations

Critical Priority

Implement encryption on all card data

Build daily automated backups

Establish a full disaster recovery plan

Deploy an IDS across the network

High Priority

Implement least privilege

Create separation of duties

Strengthen password policies

Introduce centralized password management

Properly classify & inventory all assets

Implement role-based access control (RBAC)

Medium Priority

Schedule regular legacy system maintenance

Improve secure data handling processes

Low Priority
Continue maintaining physical controls (locks, CCTV, fire detection)

10. Conclusion

Botium Toys has significant security risks due to missing technical and administrative controls and incomplete compliance with major standards. Fixing the identified gaps—especially encryption, backups, access controls, and monitoring—will greatly improve their security posture and reduce the risk of costly breaches or fines.

This internal audit provides a roadmap for prioritizing improvements and aligning Botium Toys with industry standards and regulatory requirements.


