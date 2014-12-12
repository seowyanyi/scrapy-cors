import scrapy

from AverageBidPoints.items import ABPItem

class CORSSpider(scrapy.Spider):
    name = "cors1314"
    allowed_domains = ["nus.edu.sg/cors"]
    start_urls = [
        "http://www.nus.edu.sg/cors/Archive/201314_Sem2/avgbidinfo_3B_1808_20132014s2.html",
        "http://www.nus.edu.sg/cors/Archive/201314_Sem1/avgbidinfo_3B_2104_20132014s1.html",
    ]

    def parse(self, response):
    	item = ABPItem()
    	temp = response.xpath('//h2/text()').re('(\d+)')
    	year = temp[0] + '/' + temp[1]
    	sem = temp[2]

        for sel in response.xpath('//tr'):
        	item['AcadYear'] = year
        	item['Semester'] = sem
        	item['ModuleCode'] = sel.xpath('td[2]/text()').extract()
        	item['ModuleTitle'] = sel.xpath('td[3]/text()').extract()
        	item['StudentAcctType'] = sel.xpath('td[4]/text()').extract()
        	item['AveragePoints'] = sel.xpath('td[5]/text()').extract()
        	yield item

