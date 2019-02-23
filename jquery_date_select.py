from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.maximize_window()
driver.implicitly_wait(30)

e_d = "22"
e_m = "2"
e_y = "2020"

f_x = "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a[text()="
s_x = "'"
t_x = "'"
ff_x = "]"
final_xpath = f_x+s_x+e_d+t_x+ff_x

ele = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(ele)
driver.find_element_by_id("datepicker").click()
year_ele = Select(driver.find_element_by_xpath("//select[@class='ui-datepicker-year']"))
year_ele.select_by_visible_text(e_y)
month_ele = Select(driver.find_element_by_xpath("//select[@class='ui-datepicker-month']"))
month_ele.select_by_value(e_m)

print(final_xpath)
driver.find_element_by_xpath(final_xpath).click()
driver.close()