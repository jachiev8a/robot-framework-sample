*** Settings ***
Documentation    Suite description
Library          test_python.py

*** Test Cases ***
Test is OK
    test ok

Test is NOK
    test failure

*** Keywords ***