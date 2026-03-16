from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://www.bing.com")

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "sb_form_q"))
)
search_box.send_keys("软件测试")
search_box.submit()

# 验证标题里包含"软件测试"
assert "软件测试" in driver.title
print("测试通过！标题是：", driver.title)

driver.quit()