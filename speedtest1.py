from datetime import datetime
import sys

#needed variables
speed_text = "How fast can you type this sentence?"
text_length = len(speed_text)
num_of_words = len(speed_text.split(" "))
avg_num_words = text_length / 5
user_prompt = "\nWhen you hit Enter, begin typing the above text. Then hit Enter again to end the speed test.\n"

print(speed_text,)
input(user_prompt)
start_time = datetime.now()
user_entered_text = input("> ")
end_time = datetime.now()

if user_entered_text != speed_text:
    print("You made an error. Speed not calculated")
    sys.exit()

typing_time = (end_time - start_time).total_seconds() / 60

print("*** Your typing speed ***")
print(f"cpm: {text_length / typing_time}")
print(f"wpm: {avg_num_words / typing_time}")
print(f"real wpm: {num_of_words / typing_time}")
