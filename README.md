# Password Cracking Tool

This simple Python script is a password cracking tool that allows users to guess passwords using brute-force and dictionary attacks. The tool can also crack MD5, SHA-256, and Bcrypt hashed passwords.

Group: Minasha Gunarathna and Chris Wang

## How it Works

### Brute Force Attack
The function takes two parameters: size (the length of the password to attempt) and attempt (the current attempt at the password).
In the base case (size == 0), it checks if the current attempt matches the provided plaintext password (password).
If a match is found, it prints the cracked password, the number of tries, and exits the program.
If no match is found, it recursively generates new attempts by appending characters (from ASCII 32 to 126) and continues the search.

### Dictionary Attack
The function takes a list of dictionary_files as input, which are assumed to be text files containing a list of possible passwords (one per line).
It iterates through each dictionary file, reading its content and splitting it into a list of words.
It then iterates through each word in the dictionary and compares it with the provided password.
If a match is found, it prints the cracked password, the number of tries, and exits the program.
This is generally the fastest way to crack a password, since the script can iterate through the dictionary relatively quickly.

### SHA-256 Hash Cracking
The function takes two parameters: size (the length of the password to attempt) and attempt (the current attempt at the password).
In the base case (size == 0), it calculates the SHA-256 hash of the current attempt and checks if it matches the provided SHA-256 hash (password).
If a match is found, it prints the cracked password, the number of tries, and exits the program.
If no match is found, it recursively generates new attempts by appending characters (from ASCII 32 to 126) and continues the search.

### MD5 Hash Cracking
The logic is the same as for SHA-256, but it calculates the MD5 hash instead.

### Bcrypt Hash Cracking
In this case, the Bcrypt library is used to hash the current attempt, and it checks if the hashed attempt matches the provided Bcrypt hash (password).
Note that Bcrypt uses salts, so bcrypt.gensalt() generates a new salt for each attempt.

## How to Run

Download the repository, open a terminal in the directory of the downloaded repo, and run `python3 passwordCrack.py`.

## Warning

Since all methods except dictionary are based on brute-force, any password that is longer than 4 characters can take a long time. Bcrypt will especially take a long time, with any character length, since Bcrypt uses salting.
