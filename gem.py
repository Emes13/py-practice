from math import floor
from os import system
system('cls')

def menu(): # returns chosen alphabet for gematria encoding, and an identifier int
    alphabets = {"English": "abcdefghijklmnopqrstuvwxyz", "Hebrew": "אבגדהוזחטיכלמנסעפצקרשת"}
    while True: #invalid input just loops back to the question
        menu_choice = input("Type 1 for English, 2 for Hebrew, or 3 to define your own alphabet: ")
        if menu_choice == "1":
            return alphabets["English"], 1
        elif menu_choice == "2":
            return alphabets["Hebrew"], 2
        elif menu_choice == "3":
            return input("Type your alphabet (do not use spaces): "), 3
        else:
            continue
              
def gem(x):
    if x > 0:
        # An equation I came up with. It uses a starting index of 1 (sorry). As with classic gematria,
        # every 10th number raises the sequence to the next power of 10.
        # e.g. 1, 2, 3, ..., 9, 10, 20, 30, ..., 90, 100, 200, 300, ..., 900, 1000, ...
        gematria = (10**(floor((x-1)/9))) * (x - (9*floor((x-1)/9)))
    else:
        gematria = 0
    return gematria

def encode_alphabet(alphabet):
    encoded_alpha = {}
    for index, char in enumerate(alphabet):
        encoded_alpha[char] = index + 1
    return encoded_alpha
    
def normalize(original, strip_space=False, verbose=False):
        normalized_Hstring = ""
        for char in original:
            match char:
                case "ם":
                    normalized_Hstring += "מ"
                case "ן":
                    normalized_Hstring += "נ"
                case "ץ":
                    normalized_Hstring += "צ"
                case "ף":
                    normalized_Hstring += "פ"
                case "ך":
                    normalized_Hstring += "כ"
                case " ":
                    if strip_space:
                        continue
                    else:
                        normalized_Hstring += " "
                case _:
                    normalized_Hstring += char
        if original != normalized_Hstring and verbose == True:
            # warning in green text (tested only in PowerShell terminal)
            print("\033[92mOne or more final forms were automatically replaced with non-final forms.\033[0m")
        return normalized_Hstring

def main():
    gematriot = []
    chosen_alphabet, identifier = menu()
    encoded_alpha = encode_alphabet(chosen_alphabet) # dict
    
    # If alphabet is Hebrew, .lower() method has no effect; if it's English, normalize() has no effect (unlesss strip_space=True).
    # Edge case: someone tries to define a custom alphabet including Hebrew final forms. It won't work.
    user_input = normalize(input("Enter the text to find the gematria: ").lower(), strip_space=False, verbose=True)
    
    for char in user_input:
        if char != " ": # tbd: implement better error checking
            gematriot.append(gem(encoded_alpha[char]))
    
    print(f"Input: {user_input}")
    if identifier == 2: print(f"Standardized input: {user_input[::-1]}")
    print(f"The gematria of the entire text totals: {sum(gematriot)}")
    print("Here are the individual values of each character:\n", gematriot,"\n")
    
# Begin program (looped)
while True:
    main()