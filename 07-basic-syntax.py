# Variable assignment for test data
username = "testuser"
password = "secretpassword"

# Login test scenario
# This test verifies the login functionality by entering valid credentials

"""
Steps:
1. Enter the username
2. Enter the password
3. Click on the Login button
4. Verify successful login
"""


# Test case for adding items to the cart
# Steps:
# 1. Navigate to the product page
# 2. Select the desired item
# 3. Click on the Add to Cart button
# 4. Verify item is added to the cart
if item_available():
    navigate_to_product_page()
    select_item()
    add_to_cart()
    if verify_item_added():
        print("Item added to cart successfully")
    else:
        print("Failed to add item to cart")
else:
    print("Item is not available")
