#Integers

x = 13
y = -3

#Floating-Point Numbers

pi = 3.14159
radius = 2.5

#Complex Numbers

z = 3 + 4j

#Strings

name = "Paulo Oliveira"
message = 'Hello, Paulo!'

#String concatenation

greeting = "Hello"
name = "Paulo"
full_greeting = greeting + " " + name
print(full_greeting)  # Output: Hello Paulo

#Booleans

is_raining = True
is_sunny = False

#Lists

test_cases = ["login", "register", "search", "checkout"]

usernames = ["user1", "user2", "user3"]
passwords = ["pass123", "pass456", "pass789"]

#List Operations

test_cases = ["login", "register", "search"]
test_cases.append("checkout")
print(test_cases) # Output: ['login', 'register', 'search', 'checkout']

test_cases.remove("register")
print(test_cases) # Output: ['login', 'search', 'checkout']

#Tuples

test_case = ("login", "user1", "pass123", True)

credentials = (
    ("admin", "admin123"),
    ("user", "user123"),
    ("guest", "guest123")
)

#Tuples Access

test_case = ("login", "user1", "pass123", True)
print(test_case[0])  # Output: login

#Tuple Subset

credentials = ("admin", "user", "guest", "tester")
print(credentials[1:3])  # Output: ("user", "guest")

#Tuple Unpack

user, password = ("admin", "admin123")
print(user)      # Output: admin
print(password)  # Output: admin123

#Sets

test_tags = {"smoke", "regression", "functional"}
test_case_1_tags = {"smoke", "regression"}
test_case_2_tags = {"functional", "performance"}

#Set Operations: Union

test_tags = {"smoke", "regression"}
additional_tags = {"functional", "performance"}

all_tags = test_tags.union(additional_tags)
print(all_tags)  # Output: {"smoke", "regression", "functional", "performance"}

#Set Operations: Intersection

test_tags = {"smoke", "regression", "functional"}
selected_tags = {"functional", "performance"}

common_tags = test_tags.intersection(selected_tags)
print(common_tags)  # Output: {"functional"}

#Set Operations: Difference

test_tags = {"smoke", "regression", "functional"}
excluded_tags = {"regression", "performance"}

remaining_tags = test_tags.difference(excluded_tags)
print(remaining_tags)  # Output: {"smoke", "functional"}

#Set membership tests and operations

test_tags = {"smoke", "regression", "functional"}

print("regression" in test_tags)  # Output: True
print({"functional", "performance"}.issubset(test_tags))  # Output: False
print({"functional", "performance"}.isdisjoint(test_tags))  # Output: True

#Dictionaries

test_case_1 = {
    "name": "Login",
    "input": {"username": "testuser", "password": "password123"},
    "expected_output": "Success",
    "tags": ["smoke", "regression"]
}

test_environment = {
    "url": "https://example.com",
    "browser": "Chrome",
    "timeout": 10,
    "headless": True
}

test_data = {
    "TC001": {"input": 5, "expected_output": 25},
    "TC002": {"input": 10, "expected_output": 100},
    "TC003": {"input": -2, "expected_output": 4}
}

test_results = {
    "TC001": "Pass",
    "TC002": "Fail",
    "TC003": "Pass"
}

#Dictionaries Access and Manipulation

test_case = {"name": "Login", "status": "Pass", "tags": ["smoke", "regression"]}

print(test_case["name"])  # Output: "Login"

test_case["status"] = "Fail"
print(test_case)  # Output: {"name": "Login", "status": "Fail", "tags": ["smoke", "regression"]}

test_case["timeout"] = 10
print(test_case)  # Output: {"name": "Login", "status": "Fail", "tags": ["smoke", "regression"], "timeout": 10}

del test_case["tags"]
print(test_case)  # Output: {"name": "Login", "status": "Fail", "timeout": 10}
