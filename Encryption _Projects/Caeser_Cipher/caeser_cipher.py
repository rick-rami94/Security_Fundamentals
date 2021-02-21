# Importing the string library to be able to use alphabets to use alphabets.
import string
# Users neet to provide the string that they are looking to "encrypt" and how many rotations do they want to cipher.
plain_text = input("Pass the string to encrypt: ")
rot = input("Pass the number of rotations:")
rot = int(rot)
# Creating a class that is able to take a string and encrypt it using ROT cipher. 
class Encrypted_String:
    def __init__(self):
        super().__init__()
    # The arguments are the string to pass, the number of rotations, and the default alphabets being used. 
    def rot_cipher(self,string, rotations, alphabets = [string.ascii_lowercase, string.ascii_uppercase,string.punctuation]):
        # This subfunction will take the provide alphabets and return the rotated values. 
            def shift_alphabet(alphabet):
                return alphabet[rotations:] + alphabet[:rotations]

            shifted_alphabets = tuple(map(shift_alphabet, alphabets))
            final_alphabet = ''.join(alphabets)
            final_shifted_alphabet = ''.join(shifted_alphabets)
            table = str.maketrans(final_alphabet, final_shifted_alphabet)
            return string.translate(table)
# Creating the class object.
rot_string = Encrypted_String()
# Printing the output to the screen.
print(rot_string.rot_cipher(plain_text,rot))
