# 1. Import required modules
import pikepdf
from tqdm import tqdm  # tqdm for progress bar

# 2. Define the password text file and the protected PDF file paths
password_text_file = "all_dates.txt"  # The text file containing passwords
pdf_file = "Crack.pdf"       # The PDF file to unlock

# 3. Initialize an empty list to store the passwords
passwords = []

# 4. Iterate through each line in the password text file and store in the passwords list
with open(password_text_file, 'r') as file:
    for line in file:
        passwords.append(line.strip())

# 5. Try each password from the list to unlock the PDF
for password in tqdm(passwords, desc="Cracking PDF File"):
    try:
        # Try opening the PDF file with the current password
        with pikepdf.open(pdf_file, password=password) as pdf:
            # If password is correct, print and break the loop
            print("[+] Password found:", password)
            break
    except pikepdf.PasswordError:
        # If the password is incorrect, continue the loop
        continue
else:
    print("[-] Password not found. Try another wordlist.")
