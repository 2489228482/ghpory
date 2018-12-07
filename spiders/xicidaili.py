import requests
from lxml import etree

def xicidaili():
    headers ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Host":"www.xicidaili.com",
            "If-None-Match":'W/"1db68a2a8fa8e3ee485aceebbe4fd60b',
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (X11; Ltinux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.106 Chrome/68.0.3440.106 Safari/537.36"}
    seedList =['http://www.xicidaili.com/nn/1','http://www.xicidaili.com/nn/2']
    proxyList = []
    for url in seedList:
        resp = requests.get(url,headers)
        if resp.status_code==200:
            html = etree.HTML(resp.text)
            tr = html.xpath('//table[@id="ip_list"]/tr')
            if tr:
                for tag in tr[1:]:
                    ip = tag.xpath('string(./td[2])')
                    htype = tag.xpath('string(./td[6])')
                    port = tr[3].xpath('string(./td[3])')
                    proxyList.append(htype.lower()+r'://'+ip+':'+port)
    return proxyList

if __name__ == '__main__':
    main()
    