# Shellcode Generator

This is a Python script that generates shellcode in C and C# programming languages from a binary file. Shellcode is commonly used in software exploitation and security testing for tasks such as code injection and payload execution.

## Features

- Generates C shellcode: The script reads a binary file and converts each byte into its hexadecimal representation, producing C shellcode as output.

- Generates C# shellcode: Similar to the C shellcode, the script generates C# shellcode by prefixing each byte with "0x" and separating them with commas.

- Customizable output format: The C shellcode can be split into multiple lines if a maximum length is reached. The script provides flexibility in adjusting the maximum length.

## Usage

1. Make sure you have Python installed on your system.

2. Clone the repository:

`git clone https://github.com/your-username/shellcode-generator.git`

3. Navigate to the project directory:

`cd shellcode-generator`

4. Run the script with the following command:

`python shellcode_generator.py <filename> <output_language>`

- `<filename>`: The name of the binary file you want to generate shellcode from.
- `<output_language>`: Specify the output language as either "c" for C shellcode or "cs" for C# shellcode.

5. The generated shellcode will be displayed in the console.

## Examples

To generate C shellcode from a binary file named "payload.bin", run the following command:

`python shellcode_generator.py payload.bin c`

To generate C# shellcode from the same file, use:

`python shellcode_generator.py payload.bin cs`

## License

This project is licensed under the [MIT License](LICENSE).
