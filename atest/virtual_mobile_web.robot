*** Settings ***
Library  AppiumLibrary  plugins=${CURDIR}/../src/SauceLabs

*** Test Cases ***

Start Android Emulator Device
    Start Sauce Android Emulator
    [Teardown]  Stop Sauce Session

Start iOS Simulator Device
    Start Sauce iOS Emulator
    [Teardown]  Stop Sauce Session
