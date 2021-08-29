# Robotframework - Sauce Labs Plugin

This is a plugin for the SeleniumLibrary to help with using Sauce Labs. 

This library is a [plugin extension](https://github.com/robotframework/SeleniumLibrary/blob/master/docs/extending/extending.rst) of the SeleniumLibrary. That means you can (in theory!) use all the keywords in the SeleniumLibrary _in addition to_ the keywords added here. The keywords added are specifically meant for use with Sauce Labs.

## Installation

You can install this package using `pip`: 

```bash
pip install robotframework-saucelabs
```

Currently, there are two other dependencies you need to install for this package as well:

```bash
pip install saucebindings sa11y
```

This library is powered by the Python [Sauce Bindings](https://opensource.saucelabs.com/sauce_bindings/) to connect and use Sauce Labs. 

A requirement of using this library is to [set environment variables](https://opensource.saucelabs.com/sauce_bindings/getting-started#universal-prerequisites) for your Sauce username and access key.

Note that you must have the [SeleniumLibrary](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html) installed as well. 

## Examples

Since this library is a plugin for the SeleniumLibrary, you need to add this as a plugin where you define using the SeleniumLibrary:

```robot

*** Settings ***
Library  SeleniumLibrary  plugins=SauceLabs

```

After defining this plugin, you can then use SauceLabs keywords in addition to SeleniumLibrary keywords:

```robot
*** Test Cases ***

Web Workflow Test
    # Use a SauceLabs keyword
    Start Latest Chrome On Sauce  https://www.saucedemo.com
    # Then you can use standard SeleniumLibrary keywords
    Input text  id:user-name  standard_user
    Input text  id:password  secret_sauce
    Click button  class:btn_action
    Page should contain element  id:shopping_cart_container
    # End with closing the session on Sauce
    [Teardown]  Stop Sauce Session  ${TEST_STATUS}

```

See [the acceptance test](https://github.com/joshmgrant/robotframework-saucelabs/blob/main/atest/acceptance.robot) for an example of usage, and the other tests for more examples. 

## Contribution

Contributors welcome! We need keywords, and if you are a robot and Sauce Labs user, please open pull requests and/or issues as needed!