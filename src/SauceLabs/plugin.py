from typing import Optional
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords.element import ElementKeywords
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
        self.session = {}
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
    def platform_version_should_be_windows_10(self):
        assert self.session.options.platform_name == "Windows 10"

    """Keywords"""
    @keyword
    def start_sauce_browser(self, url: Optional[str] = None, alias: Optional[str] = None):
        index = self.drivers.get_index(alias)
        if index:
            self.info(f"Using existing browser from index {index}.")
            self.switch_browser(alias)
            if url:
                self.go_to(url)
            return index
        self.session = SauceSession()
        driver = self.session.start()
        index = self.ctx.register_driver(driver, alias)
        if url:
            driver.get(url)
        return index
    
    @keyword
    def stop_sauce_session(self):
        if self.session:
            self.session.stop(True)
        self.ctx.close_all_browsers()

