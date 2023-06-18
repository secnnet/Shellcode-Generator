#!/usr/bin/env python
import sys

def generate_c_shellcode(filename):
    # Generate C shellcode
    shellcode = "\""
    ctr = 1
    maxlen = 15

    try:
        with open(filename, "rb") as file:
            for b in file.read():
                shellcode += "\\x" + b.encode("hex")  # Convert each byte to hexadecimal
                if ctr == maxlen:
                    shellcode += "\" \n\""  # Split the shellcode into multiple lines if maxlen is reached
                    ctr = 0
                ctr += 1
        shellcode += "\""
        return shellcode
    except IOError:
        print("Error: Failed to read the input file.")
        sys.exit(1)

def generate_cs_shellcode(filename):
    # Generate C# shellcode
    shellcode = ""
    ctr = 1
    maxlen = 15

    try:
        with open(filename, "rb") as file:
            for b in file.read():
                shellcode += "0x" + b.encode("hex") + ","  # Convert each byte to hexadecimal
                if ctr == maxlen:
                    shellcode += "\n"  # Split the shellcode into multiple lines if maxlen is reached
                    ctr = 0
                ctr += 1
        return shellcode
    except IOError:
        print("Error: Failed to read the input file.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: %s file.bin c|cs\n" % (sys.argv[0],))
        sys.exit(0)

    if sys.argv[2] == "c":
        # Generate C shellcode
        shellcode = generate_c_shellcode(sys.argv[1])
        print(shellcode)
    else:
        # Generate C# shellcode
        shellcode = generate_cs_shellcode(sys.argv[1])
        print(shellcode)
