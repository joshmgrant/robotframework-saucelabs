*** Settings ***
Library  SeleniumLibrary  plugins=${CURDIR}/../src/SauceLabs

*** Test Cases ***

Web Workflow Test
    Start Latest Chrome  https://www.saucedemo.com
    Input text  id:user-name  standard_user
    Input text  id:password  secret_sauce
    Click button  class:btn_action
    Page should contain element  id:shopping_cart_container
    [Teardown]  Stop Sauce Session

