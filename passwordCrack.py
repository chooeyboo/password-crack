import hashlib

password = input("Give password: ")
crack = ""
count = 0

# Function for brute-force attack
def bruteForce(size, attempt=""):
    global count
    if size == 0:
        if attempt == password:
            crack = attempt
            print("Cracked password: " + crack)
            print(count, " tries")
            exit()
    else:
        for x in range(32, 127):
            count += 1
            newTry = attempt + chr(x)
            bruteForce(size - 1, newTry)

# Function for dictionary attack
def dictionaryAttack(dictionary_file):
    global count
    with open(dictionary_file, 'r') as file:
        words = file.read().splitlines()

    for word in words:
        count += 1
        if word == password:
            crack = word
            print("Cracked password: " + crack)
            print(count, " tries")
            exit()

# Function for MD5 hash brute-force attack
def bruteForceMD5Hash(size, attempt=""):
    global count
    if size == 0:
        hashed_attempt = hashlib.md5(attempt.encode()).hexdigest()
        if hashed_attempt == password:
            crack = attempt
            print("Cracked password: " + crack)
            print(count, " tries")
            exit()
    else:
        for x in range(32, 127):
            count += 1
            newTry = attempt + chr(x)
            bruteForceMD5Hash(size - 1, newTry)

# Function for MD5 hash cracking
def crackMD5Hash(md5_hash):
    global count
    if hashlib.md5(md5_hash.encode()).hexdigest() == password:
        print("MD5 hash cracked: " + md5_hash)
        print(count, " tries")
        exit()

def bruteForceSHA256Hash(size, attempt=""):
    global count
    if size == 0:
        hashed_attempt = hashlib.sha256(attempt.encode()).hexdigest()
        if hashed_attempt == password:
            crack = attempt
            print("Cracked password: " + crack)
            print(count, " tries")
            exit()
    else:
        for x in range(32, 127):
            count += 1
            newTry = attempt + chr(x)
            bruteForceSHA256Hash(size - 1, newTry)

# Prompt user for the attack method
method = input("Select attack method (1 for brute force, 2 for dictionary, 3 for MD5 hash, 4 for SHA-256 hash): ")

# Perform the selected attack method
if method == "1":
    # Brute-force attack
    for i in range(1, 99):
        bruteForce(i)
elif method == "2":
    # Dictionary attack
    dictionaryAttack("dictionary.txt")
    print("Password not found in the dictionary. Switching to brute force attack.")
    for i in range(1, 99):
        bruteForce(i)
elif method == "3":
    # MD5 hash brute-force attack
    for i in range(1, 99):
        bruteForceMD5Hash(i)
elif method == "4":
    # SHA-256 hash brute-force attack
    for i in range(1, 99):
        bruteForceSHA256Hash(i)
else:
    print("Invalid choice. Please enter 1 for brute force, 2 for dictionary, or 3 for MD5 hash.")
