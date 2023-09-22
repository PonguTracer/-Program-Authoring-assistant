user_prompt = input("Enter a sample text:\n")
print()
print(f"You entered: {user_prompt}")

def print_menu():
    print("MENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q - Quit")


def execute_menu():
    global user_prompt
    print()
    print_menu()
    print()
    user_input = input("Choose an option:\n")
    while user_input != "q":
        if user_input == "c":
            print(f"Number of non-whitespace characters: {get_num_of_non_WS_characters(user_prompt)}")
        elif user_input == "w":
            print(f"Number of words: {get_num_of_words(user_prompt)}")
        elif user_input == "f":
            user_prompt = fix_capitalization(user_prompt)  # Update user_prompt with corrected text
            print(f"Fixed capitalization: {user_prompt}")
        elif user_input == "r":
            print(f"Number of punctuation characters replaced: {replace_punctuation(user_prompt)}")
        elif user_input == "s":
            user_prompt = shorten_space(user_prompt)  # Update user_prompt with shortened text
            print(f"Spaces shortened: {user_prompt}")
        else:
            print("Invalid input")
        print()
        print_menu()
        print()
        user_input = input("Choose an option:\n")
    print("Goodbye")

# Define the fix_capitalization function to correct the capitalization of words
def fix_capitalization(text):
    words = text.split()
    corrected_words = [word.capitalize() for word in words]
    return ' '.join(corrected_words)

def get_num_of_non_WS_characters(text):
    count = 0
    for i in text:
        if i != " ":
            count += 1
    return count

def get_num_of_words(text):
    count = len(text.split())
    return count

def replace_punctuation(text):
    count = 0
    for i in text:
        if i in ",;:.!?":
            count += 1
    return count

def shorten_space(text):
    while "  " in text:
        text = text.replace("  ", " ")
    return text



execute_menu()
