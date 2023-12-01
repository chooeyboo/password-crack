# Password Cracking Tool

This simple Python script is a password cracking tool that allows users to guess passwords using brute-force and dictionary attacks. The tool can also crack MD5 hashed passwords.

Group: Minasha Gunarathna and Chris Wang

## Usage

### Brute Force Attack

The brute force attack generates all possible combinations of characters to guess the password. It starts with a minimum length and gradually increases.

### Dictionary Attack

The dictionary attack uses a list of words from a specified file (`dictionary1.txt, dictionary2.txt, dictionary3.txt`) to guess the password.

### MD5 Hash Cracking

The MD5 hash cracking option allows users to input an MD5 hash, and the program attempts to find the original plaintext using brute-force. A brute-force algorithm generates a passphrase, the passphrase is hashed with MD5, then the hash is compared to the user-entered hash.

### SHA-256 Hash Cracking

The SHA-256 hash cracking option allows users to input an SHA-256 hash, and the program attempts to find the original plaintext using brute-force. A brute-force algorithm generates a passphrase, the passphrase is hashed with SHA-256, then the hash is compared to the user-entered hash.

## How to Run

Download the repository, open a terminal in the directory of the downloaded repo, and run `python3 passwordCrack.py`.

## Warning

Since all methods except dictionary are based on brute-force, any password that is longer than 4 characters can take a long time.
