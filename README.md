# Project-Naan Mudhalvan
<h2>Name: Kamaleshwaran.S<br>
Course:B.E-Computer Science & Engineering<br>
College:Aalim Muhammed Salegh College of Engineering</h2>
<img src="https://github.com/Kamaleshwaran11/Project-NM/blob/main/cyber.webp">

# Problem Statement:
<p>Phishing Attack Incident in Real Time or online financials scams: <br>
Examine a real-world case where a phishing attack compromised sensitive information in an organization. Discuss preventative measures and employee training programs to ensure the risks of social engineering attacks. </p>

# Keylogger

This is a simple keylogger implemented in Python using the `pynput` library. It captures keyboard events and logs them to a text file (`key_log.txt`) and a JSON file (`key_log.json`).

## Features:
- Records pressed, held, and released keys.
- Saves key logs in both text and JSON formats.
- Provides a graphical user interface (GUI) built with Tkinter for starting and stopping the keylogger.

## Requirements:
- Python 3.x
- pynput library (`pip install pynput`)

## Usage:
1. Run the script (`keylogger.py`).
2. Click the "Start" button to begin keylogging.
3. Press keys on your keyboard.
4. Click the "Stop" button to stop keylogging.

## Files:
- `keylogger.py`: The main Python script containing the keylogger implementation.
- `key_log.txt`: Text file containing logged key events.
- `key_log.json`: JSON file containing logged key events in JSON format.

## How It Works:
- The `on_press` function is called whenever a key is pressed.
- The `on_release` function is called whenever a key is released.
- Key events are stored in a list `keys_used` and periodically saved to text and JSON files.
- The keylogger can be started and stopped using the GUI buttons.

## Note:
- This keylogger is for educational purposes only. Do not use it for malicious purposes.
- Be cautious when running the keylogger, as it can log sensitive information.

- # Whaling

## What is Whaling?

"Whaling" is a specific type of cyber attack that targets high-profile individuals within organizations, typically executives or senior management, with the aim of stealing sensitive information or financial assets. It is considered a form of phishing, but with a focus on individuals of significant authority or importance within a company.

## Problem Statement:
<p><b>Phishing Attack Incident in Real Time or online financials scams: </b><br>
Examine a real-world case where a phishing attack compromised sensitive information in an organization. Discuss preventative measures and employee training programs to ensure the risks of social engineering attacks. </p>

<b>Real Time Case Example:</b>Whaling Attack Leads To Firing Of FACC Boss
In 2016, Austrian Aerospace company FACC had been subject to one of the most prominent Whaling attacks ever, dubbed the Fake President Incident, where the attacker made away with $56 million.

In a classic whaling attack, the perpetrator impersonated the CEO and sending an email to an employee of the finance department requested an immediate funds transfer.

The attack didn't only cost the firm financial losses, but it also cost the CEO at the time, Walter Stephan, his position. Although the details were not revealed, the sack was on the grounds of violation of duties

## Features:
<b>Email Authentication:</b> Placeholder function to implement DKIM and SPF verification.

<b>User Awareness Training:</b> Placeholder function for user training modules.

<b>Email Filtering:</b>Checks for keywords like "urgent transfer" and "CEO request" in email content.

<b>Multi-Factor Authentication (MFA):</b> Placeholder function for MFA logic implementation.

<b>Transaction Monitoring:</b> Placeholder function for monitoring transactions.

<b>Behavioral Analytics:</b>Placeholder function for analyzing user behavior.

<b>Access Control:</b> Placeholder function for enforcing access control.

<b>Incident Response Plan:</b> Placeholder function for handling security incidents.

<b>Security Auditing:</b> Placeholder function for security auditing.

<b>Encryption:</b> Placeholder function for applying encryption.

<b>Send Email:</b> Function to send an email using SMTP with basic authentication.

The main() function orchestrates these functions to showcase a holistic cybersecurity approach. Additional information can be added by expanding the placeholder functions with specific logic tailored to the organization's cybersecurity requirements. Each function can be further developed to enhance security measures and strengthen the overall cybersecurity posture.

## Requirements:
- Python 3.x
- Standard libraries: re, random, smtplib, email.mime.text, email.mime.multipart

## Usage:
- Ensure you have Python installed on your system.
- Run the whaling.py script.

## Files Included:

- whaling.py: Main Python script containing the project code.
- No additional files are mentioned in the provided code.

## How It Works:
- The whaling.py script defines several functions to simulate various security-related operations.
- Each function represents a different aspect of cybersecurity, such as email authentication, user training, etc.
- Upon execution, the script calls each function to demonstrate its functionality.
- For example, the script simulates DKIM and SPF verifications for email authentication, checks for suspicious keywords in email content, analyzes user login attempts from access logs, etc.
- The output of the script displays messages indicating the success or failure of each simulated operation.

## Output:
<img src="https://github.com/Kamaleshwaran11/Project-NM/blob/main/Whaling/output.png">

## Note:
- This Whaling is for educational purposes only. Do not use it for malicious purposes.
- Be cautious when running the Whaling, as it can log sensitive information.
