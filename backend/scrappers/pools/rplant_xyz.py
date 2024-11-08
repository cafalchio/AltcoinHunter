import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from app.config_app import get_logger
from backend.data.models import AllCoins
from backend.utils.scrappers import scrap_website_driver
from backend.utils.utils import update_all_coins

logger = get_logger()


def rplant():
    with scrap_website_driver("https://pool.rplant.xyz/") as driver:
        coins_page = "//*[@id='tbs-table']"

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, coins_page))
        )
        time.sleep(2)
        name_elements = driver.find_elements(By.XPATH, "//tbody/tr/td")
        name_elements = [
            td for td in name_elements if "sorting_1" in td.get_attribute("class")
        ]
        new_coins = {}
        for name in name_elements:
            new_coins[name.text] = AllCoins(
                id=name.text, symbol="", name=name.text, source="pool", is_shit=False
            )
    logger.info(f"-Got {len(new_coins.keys())} coins from rplantxyz")
    update_all_coins(new_coins)


if __name__ == "__main__":
    rplant()
