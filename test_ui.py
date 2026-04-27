import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://sahitest.com/demo/formTest.htm")
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    yield driver
    driver.quit()

def test_text_input(driver):
    # 找到第一个文本框，输入内容，验证输入成功
    text_input = driver.find_element(By.NAME, "t1")
    text_input.send_keys("hello caden")
    assert text_input.get_attribute("value") == "hello caden"        # 验证输入框value属性，查看是否是预料结果

def test_select_dropdown(driver):
    select_element = driver.find_element(By.ID, "s1Id")
    select = Select(select_element)                                  # 包成下拉框对象，能够使用下拉框的操作用法
    select.select_by_value("o2")
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    assert select.first_selected_option.text == "o2"

def test_checkbox(driver):
    # 找到第一个复选框，点击勾选，验证是选中状态
    checkbox = driver.find_element(By.CSS_SELECTOR, "input[value='cv1']")
    checkbox.click()
    assert checkbox.is_selected()

def test_radio_button(driver):
    # 找到第一个单选按钮，点击，验证选中
    radio = driver.find_element(By.CSS_SELECTOR, "input[value='rv1']")
    radio.click()
    assert radio.is_selected()