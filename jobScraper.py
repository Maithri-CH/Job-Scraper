from selenium import webdriver
import time
import csv
driver = webdriver.Chrome()
driver.get('https://google.com')
#searchKeyword="software engineer new grad jobs"
searchKeyword=input("enter your job search keyword ,ex: software engineer new grad : ")

searchBar=driver.find_element_by_xpath("//input[@title='Search']")
searchBar.send_keys(searchKeyword)
submitSearch=driver.find_element_by_xpath("//input[@value='Google Search']").submit()
driver.implicitly_wait(5)
openJobList= driver.find_element_by_xpath("//span[contains(text(),'more jobs')]").click()
driver.implicitly_wait(5)
datesPosted=driver.find_element_by_xpath("//span[contains(text(),'Date posted')]").click()
driver.implicitly_wait(5)
datesPosted=driver.find_element_by_xpath("//div[@class='eNr05b GbaVB WGYX8'][@data-name='week']").click()
driver.implicitly_wait(5)

jobTitlesElement=driver.find_elements_by_xpath("//div[@role='heading']")
jobTitlesList=[]

for jobTitle in jobTitlesElement:
    jobTitlesList.append(jobTitle.text)
#print("jobTitlesList=",jobTitlesList)


companiesElement=driver.find_elements_by_class_name("vNEEBe")
companyList=[]
for company in companiesElement:
    companyList.append(company.text)
#print(companyList)

locationApplyElement=driver.find_elements_by_xpath("//div[@class='Qk80Jf']")
locationApplyList=[]
for locationApply in locationApplyElement:
    locationApplyList.append(locationApply.text.strip("via"))
#print(locationApplyList)
locationList=locationApplyList[0::2]
applyPortalList=locationApplyList[1::2]
#print("locationList= ", locationList)
#print("Application Portal= " , applyPortalList)

jobTitlesElement[0].click()
applyLinkElements=driver.find_elements_by_xpath("//a[@class='pMhGee Co68jc j0vryd']")


driver.implicitly_wait(5)

applicationPortalLinks=[]
#print(applyLinkElements)

for applyLinkElement in applyLinkElements:
    applyLink=applyLinkElement.get_attribute('href')
    applicationPortalLinks.append(applyLink)
    print(applyLink)


applicationPortalLinks = applicationPortalLinks[-1:] + applicationPortalLinks[:-1]


#converting each list element to a list
'''
jobTitlesList=list(map(lambda el:[el],jobTitlesList))
companyList=list(map(lambda el:[el],companyList))
locationList=list(map(lambda el:[el],locationList))
applyPortalList=list(map(lambda el:[el],applyPortalList))
'''


allRows=[]
for i in range(len(jobTitlesList)):
    row=[]
    row.append(jobTitlesList[i])
    row.append(companyList[i])
    row.append(locationList[i])
    row.append(applyPortalList[i])
    row.append(applicationPortalLinks[i])
    #print(row)
    allRows.append(row)
    #print(allRows)

file = open('jobScraper.csv', 'w+', newline ='')

fields = ['Job Title', 'Company', 'Location', 'Application Portal','Application link']

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerow(fields)
    write.writerows(allRows)

print("success-check csv")
