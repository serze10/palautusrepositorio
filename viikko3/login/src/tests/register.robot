*** Settings ***
Resource        resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Input Text    username    user_valid
    Input Text    password    kalle123
    Input Text    password_confirmation    kalle123
    Click Button    Register
    Wait Until Page Contains    Welcome to Ohtu Application!    timeout=5s

Register With Too Short Username And Valid Password
    Input Text    username    ab
    Input Text    password    ValidPass123
    Input Text    password_confirmation    ValidPass123
    Click Button    Register
    Wait Until Page Contains    Username must be at least 3 characters long    timeout=5s

Register With Valid Username And Too Short Password
    Input Text    username    user_short
    Input Text    password    short
    Input Text    password_confirmation    short
    Click Button    Register
    Wait Until Page Contains    Password must be at least 8 characters long    timeout=5s

Register With Valid Username And Invalid Password
    Input Text    username    user_letters
    Input Text    password    onlyletters
    Input Text    password_confirmation    onlyletters
    Click Button    Register
    Wait Until Page Contains    Password cannot consist of only letters    timeout=5s

Register With Nonmatching Password And Password Confirmation
    Input Text    username    user_mismatch
    Input Text    password    kalle123
    Input Text    password_confirmation    DifferentPass123
    Click Button    Register
    Wait Until Page Contains    Passwords do not match    timeout=5s

Register With Username That Is Already In Use
    Input Text    username    kalle
    Input Text    password    kalle123
    Input Text    password_confirmation    kalle123
    Click Button    Register
    Wait Until Page Contains    Username already exists    timeout=5s
