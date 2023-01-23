import pyperclip as pc

# alphabet list ---------------------------------------
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
# welcome logo ---------------------------------------
welcome = """
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱┃┃
┃┃╱╰╋━━┳━━┳━━┳━━┳━╮┃┃╱╰╋┳━━┫╰━┳━━┳━╮
┃┃╱╭┫┃━┫╭╮┃━━┫┃━┫╭╯┃┃╱╭╋┫╭╮┃╭╮┃┃━┫╭╯
┃╰━╯┃┃━┫╭╮┣━━┃┃━┫┃╱┃╰━╯┃┃╰╯┃┃┃┃┃━┫┃
╰━━━┻━━┻╯╰┻━━┻━━┻╯╱╰━━━┻┫╭━┻╯╰┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯"""


# enryptor -=--=--=--=--=--=--=--=--=--=--=--=-
def enrypt(text, shift):
    temp = ""
    for i in range(0, len(text)):
        index = alphabet.index(text[i])
        if (index + shift) >= len(alphabet):
            temp += alphabet[index + shift - len(alphabet)]
        else:
            temp += alphabet[index + shift]
    pc.copy(temp)
    return temp


# decryptor -=--=--=--=--=--=--=--=--=--=--=--=--=-
def decrypt(text, shift):
    temp = ""
    for i in range(0, len(text)):
        index = alphabet.index(text[i])
        if (index - shift) < 0:
            temp += alphabet[index - shift + len(alphabet)]
        else:
            temp += alphabet[index - shift]
    pc.copy(temp)
    return temp


# ask user for inputs -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
print(welcome)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))
# check & fix shift ratio -=--=--=--=--=--=--=--=--=--=--=--=-
if shift > len(alphabet):
    shift -= len(alphabet)
elif shift < 0:
    shift *= -1
# check user inputs-=--=--=--=--=--=--=--=--=--=--=--=--=--=-
if direction == "encode":
    print(enrypt(text, shift))
else:
    print(decrypt(text, shift))
print("The result is saved in the clipboard")
