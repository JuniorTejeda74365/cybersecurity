==================================================
FILE PERMISSIONS IN LINUX
==================================================


PROJECT DESCRIPTION
-------------------
In this project, I acted as a security professional responsible for managing file and directory permissions for a research team in a Linux environment. I reviewed existing permissions to identify unauthorized access and used Linux commands to enforce proper authorization. By applying the principle of least privilege, I ensured that only authorized users could access sensitive research files and directories.


==================================================
STEP 1: SCENARIO OVERVIEW
==================================================
As a security professional working with a research team, my responsibility was to ensure that file system permissions aligned with organizational security policies. This involved examining current permissions, identifying unauthorized access, and modifying permissions to protect sensitive research data.


==================================================
STEP 2: CHECK FILE AND DIRECTORY DETAILS
==================================================

COMMAND USED:
ls -la

EXPLANATION:
The ls -la command lists all files and directories, including hidden files, and displays detailed information such as permissions, ownership, and group. The -l option shows permissions in long format, and the -a option ensures hidden files are included.


==================================================
STEP 3: CURRENT FILE PERMISSIONS
==================================================

project_k.txt
-rw-rw-rw-

project_m.txt
-rw-r-----

project_r.txt
-rw-rw-r--

project_t.txt
-rw-rw-r--

.project_x.txt
-rw--w----

drafts
drwx--x---


==================================================
STEP 4: DESCRIBE THE PERMISSIONS STRING
==================================================

EXAMPLE PERMISSIONS STRING:
-rw-rw-r--

EXPLANATION:
The first character (-) indicates the file type, which means this is a regular file.
The next three characters (rw-) represent the user permissions, allowing read and write access.
The next three characters (rw-) represent the group permissions, allowing read and write access.
The final three characters (r--) represent the permissions for others, allowing read-only access.

This 10-character string is used to determine who can access or modify a file.


==================================================
STEP 5: CHANGE FILE PERMISSIONS
==================================================

SECURITY REQUIREMENT:
The organization does not allow others to have write access to any files.

IDENTIFIED FILE:
project_k.txt

COMMAND USED:
chmod o-w project_k.txt

VERIFICATION:
ls -l project_k.txt

This command removes write access from others while preserving permissions for the user and group.


==================================================
STEP 6: CHANGE FILE PERMISSIONS ON A HIDDEN FILE
==================================================

FILE:
.project_x.txt

REQUIRED PERMISSIONS:
User: read
Group: read
Other: none

COMMAND USED:
chmod 440 .project_x.txt

VERIFICATION:
ls -l .project_x.txt

This ensures the file is read-only for the user and group and inaccessible to others.


==================================================
STEP 7: CHANGE DIRECTORY PERMISSIONS
==================================================

DIRECTORY:
drafts

REQUIRED PERMISSIONS:
User: read, write, execute
Group: none
Other: none

COMMAND USED:
chmod 700 drafts

VERIFICATION:
ls -ld drafts

This restricts access so that only the owner can access the directory and its contents.


==================================================
STEP 8: SUMMARY
==================================================

In this activity, I reviewed file and directory permissions using the ls -la command to identify unauthorized access. I interpreted Linux permission strings and used the chmod command to update file, hidden file, and directory permissions according to organizational security policies. These actions enforced the principle of least privilege and demonstrated effective access control management in a Linux environment.
