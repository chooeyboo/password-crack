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

# Prompt user for the attack method
method = input("Select attack method (1 for brute force, 2 for dictionary): ")

# Perform the selected attack method
if method == "1":
    # Brute-force attack
    for i in range(1, 99):
        bruteForce(i)
elif method == "2":
    # Dictionary attack
    dictionaryAttack("dictionary.txt")
else:
    print("Invalid choice. Please enter 1 for brute force or 2 for dictionary.")
