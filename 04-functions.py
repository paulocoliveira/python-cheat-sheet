#Basic function sample

def latest_selenium_version():
    print("Latest Selenium version is 4.9!")

# Calling the latest_selenium_version() function
latest_selenium_version()

#Basic function with parameter sample

def selenium_version_with_parameter(version):
    print(f"Your Selenium version is {version}!")

# Calling the selenium_version_with_parameter() function with an argument
selenium_version_with_parameter("4.9")

#Basic function with return sample

def calculate_total_execution_time(testcase_quantity, execution_time_sec):
    total_time = testcase_quantity * execution_time_sec
    return total_time

# Calling the calculate_total_execution_time() function and storing the result in a variable
result = calculate_total_execution_time(5, 35)
print("Total Execution Time in seconds:", result)

#Basic function with multiple returns sample

def calculate_total_execution_time_and_average(testcase_quantity, execution_time_sec):
    total_time = testcase_quantity * execution_time_sec
    average = total_time / testcase_quantity
    return total_time, average

# Calling the calculate_total_execution_time_and_average() function and storing the results in variables
total_time_result, average_result = calculate_total_execution_time_and_average(12, 25)
print("Total Execution Time in seconds:", total_time_result)
print("Average Execution Time in seconds:", average_result)
