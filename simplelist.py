#Little coding practice

# To do:
# 1. make search not case sensitive
# 2. figure out how to avoid globals by returning list from function instead

activesession = True
user_defined_data = []

'''
I want to wrap the user input in a function that will return a list of the terms, 
rather than splitting the string on the fly every time
'''
def get_text():
	return input("=> ").split(" ")

def is_command(user_input_list):
    if user_input_list[0] == "]": #use of \ was causing escape problems
        return True
    return False
    
def process_command(command):
    global activesession
    global user_defined_data
  
    if command[1] == "quit":
        activesession = False
        return
    
    elif command[1] == "search": #elif for readability even tho prev if returns
        search_term = command[2]
        term_exists = False # Does not exist until proven otherwise.
        for i in user_defined_data:
            if search_term in i:
                term_exists = True
                print(i)
            
        if not term_exists: print("Your search term was not found.")
        return
            
    elif command[1] == "list":
        for i in user_defined_data:
            print(i,)
        return
		
    else:
	    print("Invalid command.")
	    return

def store_data():
    global user_defined_data
    user_input_list = get_text()
    
    if is_command(user_input_list):
        process_command(user_input_list)
    else:    
		#each separate word is listed separately
        user_defined_data.extend(user_input_list) 
        
    return
    
while activesession:
    store_data()