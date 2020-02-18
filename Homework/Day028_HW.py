import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Japan_Travel/M.1581775130.A.22C.html',
        'https://www.ptt.cc/bbs/Japan_Travel/M.1581915527.A.CDB.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('JPCrawler2', start_urls=target_urls, filename='testjp.json')
    process.start()


if __name__ == '__main__':
    main()
