import sys

import segno
from PIL import Image
from pyzbar.pyzbar import decode


def generate_qr_code(menu_text, filename):
    text = segno.make(menu_text)
    text.save(filename)
    print("QR code generated successfully.")

def scan_qr_code(filename):
    img = Image.open(filename)
    decode_text = decode(img)
    for obj in decode_text:
        data = obj.data.decode("utf-8")
        return data

if __name__ == "__main__":
    menu_text = "It's the 28th of April, 2025. I am tireddd!!"

    generate_qr_code(menu_text, filename="note.png")
    scan_qr_code("note.png")
