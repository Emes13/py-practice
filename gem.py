from math import floor

gematriot = []
alphabet_h = "אבגדהוזחטיכלמנסעפצקרשת"
## 1) added method to convert end letters to non-end forms
## 2) added reversed (correct) display of Hebrew using [::-1] string slicer
alphabet_eng = "abcdefghijklmnopqrstuvwxyz"

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
            print("One or more final forms were automatically replaced with non-final forms.")
        return normalized_Hstring  

def main():
    english_switch = input("For English mode, type 'e' and Enter. Otherwise press Enter now: ").lower()
    if english_switch == "e":
        encoded_alpha = encode_alphabet(alphabet_eng) #dict
        user_input = input("Enter the text to find the gematria: ").lower()
    else:
        encoded_alpha = encode_alphabet(alphabet_h)
        user_input = normalize(input("Enter the text to find the gematria: "), strip_space=False, verbose=True)[::-1] #reverse for LTR display

    for char in user_input:
        if char != " ": # tbd: implement better error checking
            gematriot.append(gem(encoded_alpha[char]))
    
    print(f"Input: {user_input}")
    print(f"The gematria of the entire text totals: {sum(gematriot)}")
    print("Here are the individual values of each character:\n", gematriot)
    
# Begin program
main()
