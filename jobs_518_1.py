import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import threading
import time


def get_links(total_page):
    for page in range(1,total_page):
        url="http://www.518.com.tw/job-index-P-{}.html?i=1&am=1&ai=1,".format(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'lxml')
        a_list=soup.select('li.title > a')
        links= []
        for a in a_list:
            links.append(a['href'])
    return links


def get_tools(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'lxml')
    job_detail = soup.select_one('.job-detail-box > dl').text
    tools=[]
    tools_raw = job_detail.split('擅長工具：\n')[1].split('\n')[0].split('、')
    for tool in tools_raw:
        tools.append(tool.upper())

    min_max_position = re.findall(r'[0-9]+', job_detail.split('需求人數：\n')[1].split('\n')[0])
    if min_max_position:
        position = int(min_max_position[0])
    else:
        position = 1
    for i in range(1, position):
        tools += tools
    return tools

# link='https://www.518.com.tw/%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB-%E6%A1%83%E5%9C%92%E5%B8%82-%E4%B8%AD%E5%A3%A2%E5%8D%80-job-965162.html?kw=&pi=3'
# res = requests.get(link)
# soup = BeautifulSoup(res.text, 'lxml')
#
# job_detail = soup.select_one('.job-detail-box > dl').text
# tools = job_detail.split('擅長工具：\n')[1].split('\n')[0].split('、')
# min_max_position = re.findall(r'[0-9]+', job_detail.split('需求人數：\n')[1].split('\n')[0])
# if min_max_position:
#     position = int(min_max_position[0])
# else:
#     position = 1
# for i in range(1, position):
#     tools += tools
# print(min_max_position)
# print(tools)