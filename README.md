# Password Cracking Tool

This simple Python script is a password cracking tool that allows users to guess passwords using brute-force and dictionary attacks. The tool can also crack MD5 hashed passwords.

Group: Minasha Gunarathna and Chris Wang

## Table of Contents

- [Usage](#usage)
  - [Brute Force Attack](#brute-force-attack)
  - [Dictionary Attack](#dictionary-attack)
  - [MD5 Hash Cracking](#md5-hash-cracking)
- [How to Run](#how-to-run)

## Usage

### Brute Force Attack

The brute force attack generates all possible combinations of characters to guess the password. It starts with a minimum length and gradually increases.

### Dictionary Attack

The dictionary attack uses a list of words from a specified file (`dictionary.txt`) to guess the password.

### MD5 Hash Cracking

The MD5 hash cracking option allows users to input an MD5 hash, and the program attempts to find the original plaintext using both brute-force and dictionary methods.

## How to Run

Download the repository, open a terminal in the directory of the downloaded repo, and run `python3 passwordCrack.py`.
