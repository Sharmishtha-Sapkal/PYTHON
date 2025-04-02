import re

def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

# Example usage
input_text = "Hello! This is a test @string with #special *characters*..."
clean_text = remove_special_characters(input_text)
print("Original:", input_text)
print("Cleaned:", clean_text)