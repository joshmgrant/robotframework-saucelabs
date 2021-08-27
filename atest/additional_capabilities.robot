*** Settings ***
Library  SeleniumLibrary  plugins=${CURDIR}/../robotframework-saucelabs/SauceLabs

*** Test Cases ***

Set Test Name
    Start Sauce Browser  name=Robotframework Rocks
    Browser Should Be Chrome
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

Set Sauce Timeouts
    Start Sauce Browser  idleTimeout=300  commandTimeout=100
    Browser Should Be Chrome
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}