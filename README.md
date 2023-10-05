# Password Strength Checker

A tool that evaluates the strength of a given password based on common security guidelines and estimates the time it might take to crack it.

## Usage:

1. Run the checker: `python password_checker.py`
2. Enter the password you wish to test.
3. Receive feedback on the strength score (out of 5) and an estimated crack time.

## Scoring:

- Passwords are scored on a scale of 0 to 5 based on:
  - Length (>= 8 characters)
  - Presence of lowercase letters
  - Presence of uppercase letters
  - Presence of numbers
  - Presence of special characters (@#$%^&+=)

## Crack Time Estimate:

- The estimated crack time is a rough approximation based on the strength score. 
- Note: Actual crack times may vary based on numerous factors such as attacker's resources, techniques used, etc.

Always use strong, unique passwords for different services to ensure optimal security.
