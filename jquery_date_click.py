from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.maximize_window()
driver.implicitly_wait(30)

framename = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(framename)
driver.find_element_by_id("datepicker").click()
driver.switch_to.parent_frame()
# driver.switch_to.default_content()
driver.find_element_by_xpath("//a[text()='Draggable']").click()
driver.close()