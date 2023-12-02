# Password Cracking Tool

This simple Python script is a password cracking tool that allows users to guess passwords using brute-force and dictionary attacks. The tool can also crack MD5, SHA-256, and Bcrypt hashed passwords.

Group: Minasha Gunarathna and Chris Wang

## How to Run

Dependencies: You may need to run `pip install hashlib` or `pip install bcrypt` if these libraries are not already present on your system.

Download the repository, open a terminal in the directory of the downloaded repo, and run `python3 passwordCrack.py [password or hash] [argument]`.

Replace `[password or hash]` above with the plaintext password or MD5/SHA-256/Bcrypt hash you would like to crack.
Then replace `[argument]` with the type of password cracking you would like the program to use. The arguments are `-p` for plaintext brute-force, `-d` for dictionary, `-m` for MD5, `-s` for SHA-256, and `-b` for Bcrypt.

## Warning

Since all methods except dictionary are based on brute-force, any password that is longer than 4 characters can take a long time. Bcrypt will especially take a long time, with any character length, since Bcrypt uses salting.

## Rubric

- [x] (3) Regular usage of Git
> In the top right, under the green "Code" button, click on the number of commits to the project to see regular usage of Git.

- [x] (4) Able to load dataset of top 10K most common passwords
> The files `dictionary1.txt`, `dictionary2.txt` and `dictionary3.txt` collectively contain over one million common passwords.

- [x] (10) Implement brute force password cracking

> This is done through the `bruteForce` function.
- [x] (10) Implement dictionary attack password cracking

> This is done through the dictionaryAttack function.
- [x] (4) Able to run program via command line with various arguments

> See above in the "How to Run" section for the command line arguments.
- [x] (4) Able to add arguments when running program via command line

> See above in the "How to Run" section for the command line arguments.
- [x] (5) Implement MD5 password cracking

> This is done through the `bruteForceMD5Hash` function.
- [x] (5) Implement Bcrypt password cracking

> This is done through the `bruteForceBcrypt` function.
- [x] (5) Implement SHA-256 password cracking

> This is done through the `bruteForceSHA256Hash` function.
- [x] (1) README.md with dependencies and commands/arguments to run

> What you're reading right now!

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
Note that Bcrypt uses salts, so bcrypt.gensalt() generates a new salt for each attempt. This is generally very slow because of the use of salting in Bcrypt hashes.
