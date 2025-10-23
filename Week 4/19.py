def caesar_cipher_encrypt(text, shift=3):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Leave non-alphabetic characters unchanged
            result += char

    return result

input_text = "Hello, World!"
encrypted_text = caesar_cipher_encrypt(input_text)

print("Original Text :", input_text)
print("Encrypted Text:", encrypted_text)