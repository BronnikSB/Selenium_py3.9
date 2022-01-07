# # Task 1
#
# from selenium import webdriver as wd
#
# s = wd.Chrome()
# s.maximize_window()
# s.get("https://sbis.ru/")
# s.find_element_by_css_selector('[href="/support"]').click()
# s.find_element_by_css_selector('[href="/download"]').click()
# Get_DownloadNew_loadLink = s.find_elements_by_xpath('//div[@data-for="ereport25"]'
#                                                     '//div[@class="sbis_ru-DownloadNew-loadLink"]/a')
# file_Get_DownloadNew_loadLink = open('file_Get_DownloadNew_loadLink.txt', 'w')
# for i in Get_DownloadNew_loadLink:
#     file_Get_DownloadNew_loadLink.write(i.get_attribute('href'))
#     file_Get_DownloadNew_loadLink.write('\n')
# file_Get_DownloadNew_loadLink.close()

## Task 2
#
# import os
#
# counter_folder = 0
# counter_file_py = 0
# counter_file_exe = 0
# counter_file_full = 0
#
# path = r'C:\Users\bronn\AppData\Local\Programs\Python\Python310'
#
# for root, dirs, files in os.walk(path):
#     for folder in dirs:
#         counter_folder += 1
#     for file in files:
#         counter_file_full += 1
#         if file.endswith('.exe'):
#             counter_file_exe += 1
#         elif file.endswith('.py'):
#             counter_file_py += 1
# Quantity_file_pathPy = open('Quantity_file_pathPy.txt', 'w')
# Quantity_file_pathPy.write(f'Количество папок: {counter_folder}\n'
#                            f'Количество файлов: {counter_file_full}\n'
#                            f'Количество файлов с расширением ".exe": {counter_file_exe}\n'
#                            f'Количество файлов с расширением ".py": {counter_file_py}')
# Quantity_file_pathPy.close()
