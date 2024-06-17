def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        ascii_offset = ord('a') if char.islower() else ord('A')
        shifted_value = (ord(char) - ascii_offset + key[i]) % 26
        new_char = chr(shifted_value + ascii_offset)
        result += new_char
    return result

def main():
    key = [30, 26, 100, 8, 50]
    key = [k % 26 for k in key]  # Convert keys to 0-25 range
    text = "abcde"
    encrypted_text = encrypt(text, key)
    print(encrypted_text)

if __name__ == "__main__":
    main()