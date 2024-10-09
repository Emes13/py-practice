#Little coding practice

activesession = True
user_defined_data = []

def is_command(raw_text):
    if raw_text[:3] == "]\ ":
        return True
    return False
    
def process_command(command):
    global activesession
    global user_defined_data
  
    if command[3:] == "quit":
        activesession = False
        return
    
    if command[3:9] == "search":
        search_term = command.split(" ")[2]
        term_exists = False # Does not exist until proven otherwise.
        for i in user_defined_data:
            if search_term in i:
                term_exists = True
                print(i)
            
        if not term_exists: print("Your search term was not found.")
        return
            
    if command[3:7] == "list":
        for i in user_defined_data:
            print(i,)
        return

def store_data():
    global user_defined_data
    user_input = input("=> ")
    
    if is_command(user_input):
        process_command(user_input)
    else:    
        user_defined_data.append(user_input.split(" "))
        
    return
    
while activesession == True:
    store_data()