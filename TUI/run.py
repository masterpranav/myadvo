from selenium import webdriver
from selenium.webdriver.support import ui
import time
state=input("Enter the State:  ")
city=input("Enter the City:  ")
start_date=input("Start Date(dd/mm/yyyy):  ")
end_date=input("End Date(dd/mm/yyyy):  ")
respondent_name=input("Name of Respondent:  ")
driver = webdriver.Firefox()
driver.get("http://cms.nic.in/ncdrcusersWeb/login.do?method=caseStatus")
'''
wait = ui.WebDriverWait(driver,10)
wait.until(page_is_loaded)

usertype=driver.find_element_by_name("userType")
driver.findElement(By.cssSelector("input[value='']")).click()
'''
driver.find_element_by_xpath("//input[@value='E']").click()

location=driver.find_element_by_name("state_idD")
for option in location.find_elements_by_tag_name('option'):
	if option.text == state:
		option.click()
		break
#print("1")	
time.sleep(3)
	
loc=driver.find_element_by_name("dist_id")
for option in loc.find_elements_by_tag_name('option'):
	if option.text == city:
		option.click()
		break	
#print("1")

'''
driver.find_element_by_xpath("//img[@class='ui-datepicker-trigger']").click()
wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='ui-datepicker-div']"))
driver.find_element_by_xpath("//div[@id='ui-datepicker-div']//select[@class='ui-datepicker-month'][text()='HERE_IS_DATE_LIKE_10']")).click()
'''
#driver.find_element_by_xpath("//img[@class='ui-datepicker-trigger']").click()

driver.find_element_by_name("dtFrom").clear()
driver.find_element_by_name("dtFrom").send_keys(start_date)

driver.find_element_by_name("dtTo").clear()
driver.find_element_by_name("dtTo").send_keys(end_date)

loc=driver.find_element_by_name("condition")
for option in loc.find_elements_by_tag_name('option'):
	if option.text == 'Respondent':
		option.click()
		break	
#print("1")

driver.find_element_by_name("searchTxt").send_keys(respondent_name)

'''
form={'state_idD':'Jharkhand','dist_id':'Gumla'}
for key, value in form.items():
    element = driver.find_element_by_name(key)
    if element.tag_name == "select":
       select = select(element)
       select.select_by_visible_text(value)
    else:
       element.send_keys(value)

'''
driver.find_element_by_name('advs').click()
