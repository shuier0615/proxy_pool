import re
import time

from fake_useragent import UserAgent
from util.webRequest import WebRequest

# 创建一个UserAgent对象
ua = UserAgent()
# 获取随机的浏览器用户代理
random_user_agent = ua.random
headers = {
    'User-Agent': random_user_agent
}


class ProxyFetcher(object):

    @staticmethod
    def freeProxy01():
        for page in range(0, 7):
            # http: // www.ip3366.net / free /?stype = 2
            target_url = 'http://www.ip3366.net/free/?stype=1&page=' + str(page)
            html = WebRequest().get(target_url, verify=False, header=headers).tree
            for tr in html.xpath("//table//tr")[1:]:
                ip = "".join(tr.xpath("./td[1]/text()")).strip()
                port = "".join(tr.xpath("./td[2]/text()")).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy02():
        for page in range(0, 7):
            target_url = 'http://www.ip3366.net/free/?stype=2&page=' + str(page)
            html = WebRequest().get(target_url, verify=False, header=headers).tree
            for tr in html.xpath("//table//tr")[1:]:
                ip = "".join(tr.xpath("./td[1]/text()")).strip()
                port = "".join(tr.xpath("./td[2]/text()")).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy03():

        """ 小幻代理 """
        base_url = 'https://ip.ihuan.me/'
        html = WebRequest().get(base_url, timeout=10, header=headers).tree
        urls = html.xpath("//div[@class='col-md-10']//nav//a/@href")
        print(urls)
        for url in urls:
            # 1https://ip.ihuan.me/?page=4ce63706
            r = WebRequest().get('https://ip.ihuan.me/' + url, timeout=10, header=headers)
            proxies = re.findall(r'>\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*?</a></td><td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)

    @staticmethod
    def freeProxy04():
        """ 89免费代理 """
        for page in range(0, 6):
            target_url = 'https://www.89ip.cn/index_{%s}.html' % (page)
            html = WebRequest().get(target_url, verify=False, header=headers).tree
            for tr in html.xpath("//table//tr")[1:]:
                ip = "".join(tr.xpath("./td[1]/text()")).strip()
                port = "".join(tr.xpath("./td[2]/text()")).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy05():
        """ 稻壳代理 https://www.docip.net/ """
        r = WebRequest().get("https://www.docip.net/data/free.json", timeout=10, header=headers)
        try:
            for each in r.json['data']:
                yield each['ip']
        except Exception as e:
            print(e)

    @staticmethod
    def freeProxy06():
        for page in range(0, 6):
            target_url = f'https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-{page}'
            proxy = {
                'http': "http://110.77.134.112:8080"
            }
            html = WebRequest().get(target_url, verify=False, header=headers, timeout=10).tree
            for tr in html.xpath("//table[2]//tr")[2:]:
                ip = "".join(tr.xpath("./td[2]/text()")).strip()
                port = "".join(tr.xpath("./td[3]/text()")).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy07():
        """  极光HTTP免费代理IP   """
        for page in range(1, 20):
            print('*' * 50 + f'正在爬取{page}页' + '*' * 50)
            target_url = 'http://ip.jghttp.com/%s/' % (page)
            html = WebRequest().get(target_url, verify=False, header=headers, timeout=10).tree
            # print(WebRequest().get(target_url, verify=False, header=headers, timeout=10).text)
            for tr in html.xpath("//div[@class='table']/div")[1:]:
                ip = "".join(tr.xpath("./div/div[1]/text()")).strip()
                # print(ip)
                port = "".join(tr.xpath("./div/div[2]/text()")).strip()
                yield "%s:%s" % (ip, port)
            time.sleep(3)

if __name__ == '__main__':
    p = ProxyFetcher()
    for _ in p.freeProxy05():
        print(_)
