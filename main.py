alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
welcome = """
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱┃┃
┃┃╱╰╋━━┳━━┳━━┳━━┳━╮┃┃╱╰╋┳━━┫╰━┳━━┳━╮
┃┃╱╭┫┃━┫╭╮┃━━┫┃━┫╭╯┃┃╱╭╋┫╭╮┃╭╮┃┃━┫╭╯
┃╰━╯┃┃━┫╭╮┣━━┃┃━┫┃╱┃╰━╯┃┃╰╯┃┃┃┃┃━┫┃
╰━━━┻━━┻╯╰┻━━┻━━┻╯╱╰━━━┻┫╭━┻╯╰┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯"""

def enrypt(text, shift):
    temp = ""
    for i in range(0, len(text)):
        index = alphabet.index(text[i])
        if (index + shift) >= len(alphabet):
            temp += alphabet[index + shift - len(alphabet)]
        else:
            temp += alphabet[index + shift]
    return temp


def decrypt(text, shift):
    temp = ""
    for i in range(0, len(text)):
        index = alphabet.index(text[i])
        if (index - shift) < 0:
            temp += alphabet[index - shift + len(alphabet)]
        else:
            temp += alphabet[index - shift]
    return temp
print(welcome)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))
if direction == "encode":
    print(enrypt(text, shift))
else:
    print(decrypt(text, shift))