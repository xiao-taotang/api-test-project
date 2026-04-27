import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# 表单页面的fixture
@pytest.fixture
def form_driver():
    driver = webdriver.Chrome()
    driver.get("https://sahitest.com/demo/formTest.htm")
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    yield driver
    driver.quit()


# 链接页面的fixture
@pytest.fixture
def link_driver():
    driver = webdriver.Chrome()
    driver.get("https://sahitest.com/demo/linkTest.htm")
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    yield driver
    driver.quit()


def test_text_input(form_driver):
    """文本框输入验证"""
    text_input = form_driver.find_element(By.NAME, "t1")
    text_input.send_keys("hello caden")
    assert text_input.get_attribute("value") == "hello caden"


def test_select_dropdown(form_driver):
    """下拉框选择验证"""
    select_element = form_driver.find_element(By.ID, "s1Id")
    select = Select(select_element)
    select.select_by_value("o2")
    try:
        form_driver.switch_to.alert.accept()
    except:
        pass
    assert select.first_selected_option.text == "o2"


def test_checkbox(form_driver):
    """复选框勾选验证"""
    checkbox = form_driver.find_element(By.CSS_SELECTOR, "input[value='cv1']")
    checkbox.click()
    assert checkbox.is_selected()


def test_radio_button(form_driver):
    """单选按钮选中验证"""
    radio = form_driver.find_element(By.CSS_SELECTOR, "input[value='rv1']")
    radio.click()
    assert radio.is_selected()


def test_link_jump(link_driver):
    """点击链接跳转后操作验证"""
    link = link_driver.find_element(By.XPATH, "/html/body/a[4]")
    link.click()
    try:
        link_driver.switch_to.alert.accept()
    except:
        pass
    textarea = link_driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    textarea.send_keys("hello caden")
    assert textarea.get_attribute("value") == "hello caden"