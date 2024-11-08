from math import floor

gematriot = []
# alphabet = "אבגדהוזחטיכלמנסעפצקרשת"
## Issues to fix with Hebrew: 1) method to convert end letters to non-end forms
## 2) typing into the terminal in Hebrew renders the characters in reverse order,
## which is annoying at best
alphabet = "abcdefghijklmnopqrstuvwxyz"

def gem(x):
    if x > 0:
        gematria = (10**(floor((x-1)/9))) * (x - (9*floor((x-1)/9)))
    else:
        gematria = 0
    return gematria

def encode_alphabet(alphabet):
    encoded_alpha = {}
    for index, char in enumerate(alphabet):
        encoded_alpha[char] = index + 1
    return encoded_alpha

def main():
    encoded_alpha = encode_alphabet(alphabet) #dict
    user_input = input("Enter the text to find the gematria: ").lower()

    for char in user_input:
        if char != " ": # tbd: implement better error checking
            gematriot.append(gem(encoded_alpha[char]))
    
    print(f"The gematria of the entire text totals: {sum(gematriot)}")
    print("Here are the individual values of each character:\n", gematriot)
    
# Begin program
main()
