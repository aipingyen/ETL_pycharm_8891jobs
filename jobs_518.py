import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import threading
import time

url = "https://www.518.com.tw/%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB-%E6%A1%83%E5%9C%92%E5%B8%82-%E4%B8%AD%E5%A3%A2%E5%8D%80-job-965162.html?kw=&pi=3"
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')

content = soup.select_one('.JobDescription > p').text
job_detail=soup.select_one('.job-detail-box > dl').text

# print(content)
print(job_detail)

key_words=re.match(r'[A-Za-z]+(\s[A-Za-z]+)*\s?(.NET|.net)?', job_detail)
print(key_words.group())