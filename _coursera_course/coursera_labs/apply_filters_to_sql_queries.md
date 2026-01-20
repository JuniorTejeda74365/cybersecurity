APPLY FILTERS TO SQL QUERIES
===========================

PROJECT DESCRIPTION
-------------------
In this project, I acted as a security professional at a large organization responsible for investigating potential security issues related to login attempts and employee machines. I examined organizational data using SQL to analyze authentication activity and employee information to identify suspicious behavior and determine which systems required security updates. By applying SQL filters such as AND, OR, NOT, and LIKE, I supported incident investigation and access control decision-making.


STEP 1: SCENARIO OVERVIEW
------------------------
You are a security professional at a large organization. Part of your role is to investigate security issues to help keep systems secure. You recently discovered potential security issues involving login attempts and employee machines. To investigate these issues, you must examine data stored in the employees and log_in_attempts tables using SQL filters.


STEP 2: EXAMINE THE TABLES
-------------------------
To complete this investigation, the following tables were examined:

log_in_attempts  
This table contains information about login activity, including login date, login time, success status, and country.

employees  
This table contains employee details such as department and office location.

These tables provide the data required to analyze suspicious login activity and determine which employee machines require security updates.


STEP 3: RETRIEVE AFTER-HOURS FAILED LOGIN ATTEMPTS
--------------------------------------------------
A potential security incident occurred after business hours. To investigate this, the log_in_attempts table was queried to identify all failed login attempts that occurred after 18:00.

Command used:

SELECT *
FROM log_in_attempts
WHERE success = 0
AND login_time > '18:00:00';

Explanation:
This query filters for failed login attempts using success = 0 and limits results to login attempts occurring after 18:00. The AND operator ensures both conditions must be met, highlighting potentially suspicious after-hours activity.


STEP 4: RETRIEVE LOGIN ATTEMPTS ON SPECIFIC DATES
------------------------------------------------
A suspicious event occurred on 2022-05-09. To investigate this event, login attempts from that date and the day before were reviewed.

Command used:

SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
OR login_date = '2022-05-08';

Explanation:
This query uses the OR operator to retrieve login attempts from either specified date, allowing analysis of activity surrounding the suspected security incident.


STEP 5: RETRIEVE LOGIN ATTEMPTS OUTSIDE OF MEXICO
------------------------------------------------
Suspicious login activity was determined not to originate from Mexico. Login attempts occurring outside of Mexico were investigated.

Command used:

SELECT *
FROM log_in_attempts
WHERE country NOT LIKE 'MEX%';

Explanation:
This query uses the LIKE keyword with the % wildcard to match both MEX and MEXICO. The NOT operator excludes those records, allowing the investigation to focus on login attempts originating outside of Mexico.


STEP 6: RETRIEVE EMPLOYEES IN MARKETING
--------------------------------------
The security team needed to perform updates on employee machines in the Marketing department located in the East building.

Command used:

SELECT *
FROM employees
WHERE department LIKE '%Marketing%'
AND office LIKE 'East%';

Explanation:
This query filters employees by department and office location. The LIKE keyword allows pattern matching, and the AND operator ensures both conditions are met.


STEP 7: RETRIEVE EMPLOYEES IN FINANCE OR SALES
---------------------------------------------
A different security update was required for employees in the Finance and Sales departments.

Command used:

SELECT *
FROM employees
WHERE department LIKE '%Finance%'
OR department LIKE '%Sales%';

Explanation:
This query uses the OR operator to retrieve employees from either department so updates can be applied to both groups.


STEP 8: RETRIEVE ALL EMPLOYEES NOT IN IT
---------------------------------------
Employees in the Information Technology department had already received the update. All other employees still required it.

Command used:

SELECT *
FROM employees
WHERE department NOT LIKE '%Information Technology%';

Explanation:
This query uses the NOT operator to exclude IT employees, ensuring updates are applied only to employees who still need them.


STEP 9: FINAL SUMMARY
--------------------
In this activity, I used SQL filters to investigate potential security issues involving login attempts and employee machines. By filtering data based on time, date, location, and department using AND, OR, NOT, and LIKE, I identified suspicious login activity and determined which employee systems required security updates. This activity demonstrates how SQL can be used to support real-world security investigations and access control decisions.
