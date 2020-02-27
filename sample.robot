*** Settings ***
Documentation    Suite description
Library          robot-lib.py

*** Test Cases ***
Test Addition
    [Tags]          MATH
    ${RES} =        keyword_add     1   2


Test Subtraction
    [Tags]          MATH
    keyword_sub     1   4

Test Multiplication
    [Tags]          MATH
    keyword_mult    1   2

Test Division
    [Tags]          MATH
    keyword_div     1   5

Test Case 1
    [Tags]          OTHER
    run test case 1

Test Turn Off System
    [Tags]          OTHER
    turn off system

*** Keywords ***