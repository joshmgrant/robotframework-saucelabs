*** Settings ***
Library  AppiumLibrary  plugins=${CURDIR}/../src/SauceLabs

*** Test Cases ***

Start Real Android Device
    Start Sauce RDC Android Device
    [Teardown]  Stop Sauce Session

Start Real iOS Device
    Start Sauce RDC iOS Device
    [Teardown]  Stop Sauce Session
