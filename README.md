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
