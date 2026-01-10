from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_snapdeal_reviews(product_url, max_reviews=50):
    """
    Scrape reviews from a Snapdeal product page using Selenium.
    Returns a list of review texts.
    """
    options = Options()
    options.add_argument("--headless")  # run Chrome in background
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(product_url)
    time.sleep(3)  # wait for page to load

    # Click "See all reviews" if button exists
    try:
        see_all = driver.find_element(By.XPATH, "//a[contains(text(),'See All Reviews')]")
        see_all.click()
        time.sleep(2)
    except:
        pass  # maybe already on review section

    reviews = []
    page = 1
    while len(reviews) < max_reviews:
        review_elements = driver.find_elements(By.CSS_SELECTOR, ".user-review p")  # Snapdeal review text
        for r in review_elements:
            text = r.text.strip()
            if text and text not in reviews:
                reviews.append(text)
            if len(reviews) >= max_reviews:
                break

        # Click next page if available
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, ".next.i-next")
            next_btn.click()
            page += 1
            time.sleep(2)
        except:
            break  # no more pages

    driver.quit()
    print(f"DEBUG → Fetched {len(reviews)} reviews from Snapdeal page")
    return reviews
