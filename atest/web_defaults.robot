*** Settings ***
Library  SeleniumLibrary  plugins=${CURDIR}/../src/SauceLabs

*** Test Cases ***

Verify Default Browser
    Start Sauce Browser
    Browser Should Be Chrome
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

Verify Default Browser Version
    Start Sauce Browser
    Browser Version Should Be Latest
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

Verify Default Platform Version
    Start Sauce Browser
    Platform Version Should Be Windows 10
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

Verify Firefox Session
    Start Latest Firefox On Sauce
    Browser Should Be Firefox
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

Verify Selecting Browser Using Params
    Start Sauce Browser  browserName=chrome  browserVersion=90.0  platformName=Windows 10
    Browser Should Be Chrome
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

Verify Selecting Safari Using Params
    Start Sauce Browser  browserName=safari  browserVersion=13.1  platformName=MacOS 10.15
    Browser Should Be Safari
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

Verify Selecting Edge Using Params
    Start Sauce Browser  browserName=MicrosoftEdge  browserVersion=latest  platformName=Windows 10
    Browser Should Be Microsoft Edge
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}