from selenium import webdriver as wd
import os

s = wd.Chrome()
s.maximize_window()
s.get("https://sbis.ru/")
s.find_element_by_css_selector('[href="/support"]').click()
s.find_element_by_css_selector('[href="/download"]').click()
Get_DownloadNew_loadLink = s.find_elements_by_xpath('//div[@data-for="ereport25"]//div[@class="sbis_ru-DownloadNew-loadLink"]/a')
print(Get_DownloadNew_loadLink)
file_Get_DownloadNew_loadLink = open('file_Get_DownloadNew_loadLink.txt', 'w')
for i in Get_DownloadNew_loadLink:
    file_Get_DownloadNew_loadLink.write(i.get_attribute('href'))
    file_Get_DownloadNew_loadLink.write('\n')
file_Get_DownloadNew_loadLink.close()
print(os.getcwd())
print('')



