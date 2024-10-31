from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

from backend.data.models import NewCoins
from backend.scrappers.pools.tools import scrap_website_driver
from backend.scrappers.run_scrappers import update_new_coins

logger = logging.getLogger(__name__)


def rplant():
    new_coins = []
    with scrap_website_driver("https://pool.rplant.xyz/") as driver:
        coins_page = "//*[@id='tbs-table']"

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, coins_page))
        )
        name_elements = driver.find_elements(By.XPATH, '//tbody/tr/td')
        name_elements = [
            td for td in name_elements if 'sorting_1' in td.get_attribute('class')]
        logger.info(name_elements)
        new_coins = {}
        for name in name_elements:
            new_coins[name.text] = NewCoins(
                id=name.text,
                symbol="",
                name=name.text,
                is_shit=False
            )
    logger.info(f"{'-'*30}\nGot {len(new_coins.keys())} coind from rplantxyz")
    update_new_coins(new_coins)


if __name__ == "__main__":
    rplant()
