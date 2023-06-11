# msedgedriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.quit()