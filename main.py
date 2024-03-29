# The Encryption Function
def cipher_encrypt(plain_text: str, key: int):

    encrypted = ""

    for c in plain_text:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower(): #check if it's a lowecase character

            # subtract the unicode of 'a' to get index in [0-25] range
            c_index = ord(c) - ord('a')

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if it's neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted

# The Decryption Function
def cipher_decrypt(ciphertext: str, key: int):

    decrypted = ""

    for c in ciphertext:

        if c.isupper():

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if it's neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted

print(f"****************************************************Autocaeser**************************************************")
print(f"Choose one of the options:")
print(f"1. Encrypt")
print(f"2. Decrypt")
opt = int(input())
if opt not in  [1, 2]:
    print(f"Wrong option!")
else:
    if opt == 1:
        opt_text = f"encryption"
    else:
        opt_text = f"decryption"
    print(f"Enter text for {opt_text}: ")
    text = str(input())
    print(f"Enter key for {opt_text}: ")
    key = int(input())
    print(f"{opt_text.capitalize()} result: {cipher_encrypt(text, key) if opt == 1 else cipher_decrypt(text, key)}")