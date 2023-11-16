import hashlib

password = input("Give password: ")
crack = ""
count = 0

# Function for brute-force attack
def bruteForce(size, attempt=""):
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
            bruteForce(size - 1, newTry)

# Function for dictionary attack
def dictionaryAttack(dictionary_file):
    global count
    with open(dictionary_file, 'r') as file:
        words = file.read().splitlines()

    for word in words:
        count += 1
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        if hashed_word == password:
            crack = word
            print("Cracked password: " + crack)
            print(count, " tries")
            exit()

# Function to crack MD5 hash
def crackMD5Hash(md5_hash):
    global count
    for i in range(1, 99):
        bruteForce(i)
        count = 0  # Reset count for the dictionary attack
        dictionaryAttack("dictionary.txt")
        count = 0  # Reset count for the next iteration

# Prompt user for the attack method
method = input("Select attack method (1 for brute force, 2 for dictionary, 3 for MD5 hash): ")

# Perform the selected attack method
if method == "1":
    # Brute-force attack
    for i in range(1, 99):
        bruteForce(i)
elif method == "2":
    # Dictionary attack
    dictionaryAttack("dictionary.txt")
elif method == "3":
    # MD5 hash cracking
    md5_hash = ""
    crackMD5Hash(md5_hash)
else:
    print("Invalid choice. Please enter 1 for brute force, 2 for dictionary, or 3 for MD5 hash.")
