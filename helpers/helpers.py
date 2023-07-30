from selenium import webdriver
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep
from helpers.logg_helper import logger


url = "https://scrapeme.live/shop/"


def get_soup(url_):
    options = Options()
    options.add_argument('--headless')
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent:{user_agent}')
    logger.info(f"the useragent is {user_agent}.")
    with webdriver.Firefox(service=Service('/Users/geckodriver'), options=options) as driver:
        driver.get(url_)
        sleep(2)
        driver.maximize_window()
        driver.save_screenshot("data/homepage.png")
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        return soup


def parse_soup(soup):
    items = soup.findAll('li', class_="product")
    logger.info(f"there are {len(items)} items.")
    results = []
    for item in items:
        result = {
            'name': item.find('h2').text,
            'price': item.find('span', class_="woocommerce-Price-amount amount").text[1:],
            'image_link': item.find('img', class_="wp-post-image")['srcset'].split(' ')[0],
            'product_link': item.find('a')['href']
        }
        results.append(result)
    return results


def set_url(page: int) -> str:
    return f"https://scrapeme.live/shop/page/{page}/"


if __name__ == '__main__':
    get_soup(url)
