# coding=utf-8
import re
import requests

def ip66():
    url = 'http://www.66ip.cn/mo.php?sxb=&tqsl=1000&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=http%3A%2F%2Fwww.66ip.cn%2F%3Fsxb%3D%26tqsl%3D1000%26ports%255B%255D2%3D%26ktip%3D%26sxa%3D%26radio%3Dradio%26submit%3D%25CC%25E1%2B%2B%25C8%25A1'
    resp = requests.get(url)
    proxyList =[]
    if resp.status_code ==200:
        ipList = re.findall("\t(.+?)<br />",resp.text)
        proxyList.extend(["http://'"+x.replace("\t","") for x in i])
    return proxyList

if __name__ == '__main__':
    ip66()
    
    