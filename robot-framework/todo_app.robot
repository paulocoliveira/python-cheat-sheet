*** Settings ***
Resource    common.robot
Test Setup  common.Open test browser
Test Teardown  common.Close test browser

*** Test Cases ***
Verify Todo App Functionality
    ${checkbox}    Get WebElement    name=li1
    Select Checkbox    ${checkbox}
    Checkbox Should Be Selected    ${checkbox}
    Input Text  id=sampletodotext   New Item
    Click Button    id=addbutton
    ${todos}    Get WebElements    css=ul.list-unstyled li
    Length Should Be    ${todos}    6
    Close Browser