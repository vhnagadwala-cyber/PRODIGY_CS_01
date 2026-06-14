# Task 02 - Image Encryption using Pixel Manipulation
# Prodigy InfoTech Cyber Security Internship
# Author: Veer Nagadwala
#
# How it works:
# Every image is made up of pixels, and each pixel has 3 color values: Red, Green, Blue (RGB).
# We use XOR (^) to flip those values using a secret key number.
# The cool thing about XOR is - doing it twice with the same key brings back the original!
# So the same function works for both encrypting AND decrypting.

from PIL import Image
import os


def process_image(image_path, save_path, key):
    # Open the image and make sure it's in RGB format
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    print(f"\nProcessing image... ({width}x{height} pixels)")

    # Go through every single pixel and XOR its R, G, B values with the key
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(save_path)
    print(f"Done! Saved to --> {save_path}")


def main():
    print("\n======================================")
    print("   Image Encryption Tool")
    print("   Prodigy InfoTech | Task 02")
    print("======================================")
    print("\nThis tool encrypts or decrypts an image using a secret key.")
    print("Use the SAME key to decrypt that you used to encrypt!\n")

    print("What do you want to do?")
    print("  1. Encrypt an image")
    print("  2. Decrypt an image")
    choice = input("\nEnter 1 or 2: ").strip()

    if choice not in ("1", "2"):
        print("Invalid choice. Please run the program again.")
        return

    image_path = input("\nEnter the path of your image (e.g. photo.png): ").strip()

    if not os.path.exists(image_path):
        print("Oops! That file doesn't exist. Check the path and try again.")
        return

    save_path = input("Enter a name for the output image (e.g. encrypted.png): ").strip()

    try:
        key = int(input("Enter your secret key (any number from 0 to 255): ").strip())
        if not (0 <= key <= 255):
            print("Key must be between 0 and 255. Try again.")
            return
    except ValueError:
        print("That doesn't look like a number. Please enter a value between 0 and 255.")
        return

    action = "Encrypting" if choice == "1" else "Decrypting"
    print(f"\n{action} your image with key = {key}...")

    process_image(image_path, save_path, key)

    print("\nRemember: Use the same key to reverse the process!")


if __name__ == "__main__":
    main()
