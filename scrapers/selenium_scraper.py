from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumScraper:

    def __init__(self, headless: bool = True):
        self.options = Options()

        if headless:
            self.options.add_argument("--headless=new")

        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(
            options=self.options
        )

        self.wait = WebDriverWait(
            self.driver,
            15
        )

    def open_page(self, url: str):
        self.driver.get(url)

    def get_title(self) -> str:
        return self.driver.title

    def get_html(self) -> str:
        return self.driver.page_source

    def close(self):
        self.driver.quit()