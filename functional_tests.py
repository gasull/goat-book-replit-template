import socket

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

hostname = socket.gethostname()

# Hostname of your local machine for when running the tests locally
is_local_machine = "YOUR-HOSTNAME" in hostname

# Configure Firefox WebDriver
if is_local_machine:
    # Running on your local machine (virtual machine)
    browser = webdriver.Firefox()
    dev_domain = "http://localhost:8000/" 
else:
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    dev_domain = ("https://83a4be34-00a1-4161-b902-5cd071ee95be-00-" 
                  "2c0cs3xz0oqim.sisko.replit.dev/")
    
browser.get(dev_domain)
assert "Congratulations!" in browser.title
print("OK")
browser.quit()
