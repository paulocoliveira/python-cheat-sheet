# List Functions

# Checking if an element exists in a list

test_cases = ["login", "register", "checkout"]
exists = "login" in test_cases
print(exists)  # Output: True

# Removing duplicates from a list

test_cases = ["login", "login", "register", "checkout", "register", "register"]
unique_data = list(set(test_cases))
print(unique_data)  # Output: ["login", "checkout", "register"]

# Counting the occurrences of an element in a list

test_cases = ["login", "login", "register", "checkout", "register", "register"]
count = test_cases.count("register")
print(count)  # Output: 3

# Sorting a list in ascending order

test_cases = ["login", "login", "register", "checkout", "register", "register"]
test_cases.sort()
print(test_cases)  # Output: ["checkout", "login", "login", "register", "register", "register"]

# Extending a list by appending elements from another list

test_cases_1 = ["login", "register", "checkout"]
test_cases_2 = ["logout", "profile", "cancel"]
test_cases_1.extend(test_cases_2)
print(test_cases_1)  # Output: ["login", "register", "checkout", "logout", "profile", "cancel"]