
import requests
import re
from bs4 import BeautifulSoup

# 以上作为基本引用


# 全局变量
start_url = "https://www.121du.net/59763/554785.html"  # 小说第一章对应的URL
base_url = "https://www.121du.net"
file_name = "长生武道：我有一具玄水蛇分身.txt"  # 设置保存的文件名字

# 使用的时候只需要更改上面两个变量的值即可


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


# function： 获取每章节的小说文字并写入文件中
def getContent(content_url):
    print("下载url "+content_url)
    res = requests.get(content_url, headers=header, timeout=10)
    res.encoding = 'utf-8'

    soup = BeautifulSoup(res.text, 'html.parser')

    BeautifulSoup(res.text, 'html.parser')
    title = soup.select('title')[0].text  # 获取章节题目 ok
    # content = soup.get_text()
    # test =soup.select('#BookText');
    content = soup.select('#BookText')[0].text.lstrip('style5();').rstrip('style6();')  # 获取章节内容
    both = title + content

    print(both, file=f)  # 写入文件
    print("已下载 " + title)  # 输出到屏幕提示 状态
    # 获取所有的a标签
    a_all = soup.select('a')
    if len(a_all) > 1:
        url = a_all[len(a_all) - 2].attrs.get("href")
        next_url = base_url + url  # 获取下个章节URL
        return getContent(next_url)



# MAIN
if __name__ == '__main__':
    f = open(file_name, 'a+', encoding='utf-8')
    getContent(start_url)
    f.close()
    print('小说下载完成!')
