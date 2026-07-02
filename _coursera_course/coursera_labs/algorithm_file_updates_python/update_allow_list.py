"""
Project: Update Allow List

Description:
This Python script automates the process of updating an allow list of IP
addresses. It reads a text file containing authorized IP addresses, removes
any IP addresses listed in the remove list, and saves the updated allow list
back to the original file.

Skills Demonstrated:
- File handling (read/write)
- Lists
- Loops
- Conditional statements
- String manipulation
- Automation
"""

from pathlib import Path

# File in the same folder as this Python script
import_file = Path(__file__).with_name("allow_list.txt")

# IP addresses to remove
remove_list = [
    "192.168.97.225",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

# Read the allow list
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert string into a list
ip_addresses = ip_addresses.split()

print("Original allow list:")
print(ip_addresses)

# Remove IPs that are in remove_list
for ip in remove_list:
    if ip in ip_addresses:
        ip_addresses.remove(ip)

print("\nUpdated allow list:")
print(ip_addresses)

# Convert list back into text
ip_addresses = "\n".join(ip_addresses)

# Write updated list back to the file
with open(import_file, "w") as file:
    file.write(ip_addresses)

print("\nallow_list.txt updated successfully.")