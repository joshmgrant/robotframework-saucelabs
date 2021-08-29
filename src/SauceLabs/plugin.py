from typing import Optional
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary import SeleniumLibrary
from saucebindings.options import SauceOptions
from saucebindings.session import SauceSession

from robot.utils import is_truthy


class SauceLabs(LibraryComponent):

    def __init__(self: "SauceLabs",
        ctx: SeleniumLibrary,
        automatic_wait: bool = True,
        timeout: str = "30 seconds",
        error_on_timeout: bool = True,
        automatic_injection: bool = True) -> None:
        LibraryComponent.__init__(self, ctx)
        self.sauce_options = SauceOptions()
        self.session = SauceSession()
        self.sauce_data_centre = "us-west"
        self.automatic_wait = is_truthy(automatic_wait)
        self.automatic_injection = is_truthy(automatic_injection)
        self.error_on_timeout = is_truthy(error_on_timeout)
        self.timeout = timeout  # type: ignore

    """Testing/assertion keywords."""
    @keyword
    def browser_version_should_be_latest(self):
        assert self.session.options.browser_version == "latest"

    @keyword
    def browser_should_be_chrome(self):
        assert self.session.options.browser_name == "chrome"

    @keyword
    def browser_should_be_firefox(self):
        assert self.session.options.browser_name == "firefox"

    @keyword
    def platform_version_should_be_windows_10(self):
        assert self.session.options.platform_name == "Windows 10"

    @keyword
    def browser_should_be_safari(self):
        assert self.session.options.browser_name == "safari"


    """Keywords"""
    @keyword
    def start_sauce_browser(self,
        url: Optional[str] = None,
        alias: Optional[str] = None,
        browserName: Optional[str] = 'chrome',
        browserVersion: Optional[str] = None,
        platformName: Optional[str] = None,
        **kwargs):
        """Start a browser on Sauce. Defaults to starting the latest Chrome on Windows 10"""
        index = self.drivers.get_index(alias)
        if index:
            self.info(f"Using existing browser from index {index}.")
            self.switch_browser(alias)
            if url:
                self.go_to(url)
            return index
        if not any([browserVersion, platformName]):
            self.options = SauceOptions(**kwargs)
        else:
            self.options = SauceOptions(browserName=browserName, browserVersion=browserVersion, platformName=platformName, **kwargs)
        
        self.session = SauceSession(self.options, data_center=self.sauce_data_centre)
        driver = self.session.start()
        index = self.ctx.register_driver(driver, alias)
        if url:
            driver.get(url)
        return index
    
    @keyword
    def stop_sauce_session(self, passed: bool):
        if self.session:
            self.session.stop(passed)
        self.ctx.close_browser()

    @keyword
    def start_latest_chrome_on_sauce(self,
        url: Optional[str] = None,
        alias: Optional[str] = None):
        index = self.drivers.get_index(alias)
        if index:
            self.info(f"Using existing browser from index {index}.")
            self.switch_browser(alias)
            if url:
                self.go_to(url)
            return index
        self.options = SauceOptions('chrome')
        self.session = SauceSession(self.options, data_center=self.sauce_data_centre)
        driver = self.session.start()
        index = self.ctx.register_driver(driver, alias)
        if url:
            driver.get(url)
        return index

    @keyword
    def start_latest_firefox_on_sauce(self,
        url: Optional[str] = None,
        alias: Optional[str] = None):
        index = self.drivers.get_index(alias)
        if index:
            self.info(f"Using existing browser from index {index}.")
            self.switch_browser(alias)
            if url:
                self.go_to(url)
            return index
        self.options = SauceOptions('firefox')
        self.session = SauceSession(self.options, data_center=self.sauce_data_centre)
        driver = self.session.start()
        index = self.ctx.register_driver(driver, alias)
        if url:
            driver.get(url)
        return index

    @keyword
    def set_data_centre(self, data_centre: str="us-west-1"):
        self.sauce_data_centre = data_centre
