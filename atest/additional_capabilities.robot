*** Settings ***
Library  SeleniumLibrary  plugins=${CURDIR}/../src/SauceLabs

*** Test Cases ***

Set Test Name
    Start Sauce Browser  name=Robotframework Rocks
    Browser Should Be Chrome
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

Set Sauce Timeouts
    Start Sauce Browser  idleTimeout=300  commandTimeout=100
    Browser Should Be Chrome
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

Use A Sauce Connect Tunnel
    [Documentation] This assumes there is a tunnel running called myTunnel
    Start Sauce Browser  name=Robotframework Rocks  tunnelIdentifier=myTunnel
    Browser Should Be Chrome
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}
