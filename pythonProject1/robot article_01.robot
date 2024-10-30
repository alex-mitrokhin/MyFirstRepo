# Created by aleksey.mitrokhin at 12.07.2024
*** Settings ***
Documentation    Applying for a loan at ParaBank
Library    SeleniumLibrary

*** Test Cases ***
Applying for a loan with a too low down payment sees the application denied
    Open Browser  https://www.google.ru/  Chrome
    Maximize Browser Window
    Input Text    css:textarea#APjFqb.gLFyf   футбол
    Sleep   1
    Click Button    css:input.gNO89b
    Sleep   2
    Close Browser

