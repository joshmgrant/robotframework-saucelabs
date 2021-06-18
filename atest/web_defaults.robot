*** Settings ***
Library  SeleniumLibrary  plugins=${CURDIR}/../src/SauceLabs

*** Test Cases ***

Verify Default Browser
    Start Sauce Browser
    Browser Should Be Chrome
    [Teardown]  Stop Sauce Session

Verify Default Browser Version
    Start Sauce Browser
    Browser Version Should Be Latest
    [Teardown]  Stop Sauce Session

Verify Default Platform Version
    Start Sauce Browser
    Platform Version Should Be Windows 10
    [Teardown]  Stop Sauce Session

Verify Firefox Session
    Start Latest Firefox
    Browser Should Be Firefox
    [Teardown]  Stop Sauce Session