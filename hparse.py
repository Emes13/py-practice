''' 
class HebrewParse:
    def __init__(self, Hstring):
        self.original = Hstring
'''
    
    def normalize(original, strip_space=False):
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
        return normalized_Hstring            
                
                
"האם זה עובד?"