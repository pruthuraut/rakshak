import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def download_images(query, limit, output_directory):
    # Set ChromeDriver path
    chromedriver_path = "/usr/bin/chromedriver"  # Replace with the actual path
    service = Service(chromedriver_path)

    # Set Chrome options to download images without opening browser window
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_settings.popups": 0, "download.default_directory": output_directory}
    chrome_options.add_experimental_option("prefs", prefs)

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to Google Images
    driver.get(f"https://www.google.com/search?q={query}&tbm=isch")

    # Scroll to load more images
    for _ in range(10):  # Adjust based on the number of scrolls needed to load images
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)  # Wait for images to load

    # Find and save image URLs
    image_urls = driver.find_elements_by_css_selector("img.rg_i")
    for i, image in enumerate(image_urls[:limit]):
        image_url = image.get_attribute("src")
        if image_url:
            image_url = image_url.split("?")[0]  # Remove extra parameters
            os.system(f"wget -P {output_directory} {image_url}")  # Download image using wget

    # Quit the WebDriver
    driver.quit()

query = "long gun"  # Set your desired search query here
limit = 500  # Number of images to download
output_directory = "/home/nigga/Documents/rajasthan hackthon/Weapon-Detection-And-Classification/train/KnivesImagesDatabase/long gun"  # Set the path to your desired folder

# Create the folder if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

download_images(query, limit, output_directory)
