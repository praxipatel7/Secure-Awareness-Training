import os

print(" Simple Secure Code Review Tool")

# Step 1: Ask user for a file
file_to_scan = input("Enter the Python file name to review: ")

# Step 2: Check if file exists
if not os.path.isfile(file_to_scan):
    print(" File not found!")
    exit()

# Step 3: Run Bandit (security analyzer)
print("\n[+] Running Bandit Security Scan...\n")
os.system(f"bandit {file_to_scan}")

# Step 4: Done
print("\n Review Finished! Check above for issues & recommendations.")