*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Fill Data Entry Form Using Robot Framework
    Open Browser    https://testautomationpractice.blogspot.com    chrome[span_1](start_span)[span_1](end_span)
    Maximize Browser Window
    Input Text    id=name    Robot Mawa
    Input Text    id=email    robotmawa@gmail.com
    Input Text    id=phone    9123456789
    Input Text    id=textarea    Bangalore, India
    Sleep    2s
    Close Browser