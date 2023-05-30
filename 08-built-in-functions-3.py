# String Functions

# Checking if a string starts with a specific substring

url = "https://www.example.com"
starts_with_https = url.startswith("https")
print(starts_with_https)  # Output: True

# Splitting a string into a list

text = "python,javascript,java"
programming_languages = text.split(",")
print(programming_languages)  # Output: ['python', 'javascript', 'java']

# Finding the index of a substring within a string

sentence = "This is a test case."
index = sentence.find("test")
print(index)  # Output: 10

# Replacing a substring with another substring in a string

sentence = "This is a python code."
new_sentence = sentence.replace("python", "javascript")
print(new_sentence)  # Output: "This is a javascript code."

# Converting a string to uppercase:

message = "your selenium version is 4.9!"
uppercase_message = message.upper()
print(uppercase_message)  # Output: "YOUR SELENIUM VERSION IS 4.9!"

# Converting a string to lowercase:

message = "YOUR SELENIUM VERSION IS 4.9!"
uppercase_message = message.lower()
print(uppercase_message)  # Output: "your selenium version is 4.9!"
