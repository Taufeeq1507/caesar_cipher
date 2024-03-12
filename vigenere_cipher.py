def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

while 1 :
    option=input("For the encryption of a message type-----> '1'\nFor the decryption of a message type-----> '2'\n")


    if option=='1':
        text=input("Please enter the message to be encrypted:")
        custom_key=input("Please enter the unique key or password to be used for encryption:-\n(warning:It should consist of alphabetical characters only otherwise there will be generation of wrong message or message will not generate at all)\n")
        encryption=encrypt(text, custom_key)
        print(f'Message to be encrypted: {text}\n')
        print(f'Key or Password used for the encryption: {custom_key}\n')
        print(f'Encrypted text: {encryption}\n\n\n')
        
        
    elif option=='2':
        text=input("Please enter the message to be decrypted:")
        custom_key=input("Please enter the unique key or password to be used for deryption:-\n(warning:It should consist of alphabetical characters only otherwise there will be generation of wrong message or message will not generate at all)\n")
        decryption=decrypt(text, custom_key)
        print(f'Message to be derypted: {text}\n')
        print(f'Key or Password used for the deryption: {custom_key}\n')
        print(f'Decrypted text: {decryption}\n\n\n')
            
            
    else:
        print("Please chose the given options between encryption and decryption!!!!!")
