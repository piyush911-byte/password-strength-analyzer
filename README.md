# Secure Password Strength Analyzer

A Python-based command-line tool to analyze the strength of a password based on multiple security metrics.

## Features
- **Length Analysis:** Scores passwords based on length.
- **Character Variety Analysis:** Checks for the presence of uppercase, lowercase, numbers, and symbols.
- **Commonality Check:** Cross-references the password against a list of the 10,000 most commonly breached passwords to prevent the use of weak, known credentials.
- **Scoring System:** Provides a final strength score (0-100) and actionable feedback.

## How to Use
1. Ensure you have Python 3 installed.
2. Download the repository files.
3. Place the `10k-most-common.txt` file in the same directory as `main.py`.
4. Run the script from your terminal: `python main.py`
5. Enter a password when prompted to receive your analysis.