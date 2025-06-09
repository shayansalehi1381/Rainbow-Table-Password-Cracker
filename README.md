# Rainbow Table Password Cracker

This Python project implements a brute-force rainbow table technique to recover 4-digit passwords from SHA-256 hashes.

## Features
- Reads a CSV file with usernames and SHA-256 password hashes
- Checks all 4-digit numeric combinations (1000–9999)
- Matches hash to real password using OrderedDict for deterministic output
- Writes recovered passwords to output CSV file

## Technologies Used
- Python
- hashlib
- csv
- OrderedDict (collections)

## Sample Input (input.csv)
