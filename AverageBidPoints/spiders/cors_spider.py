import scrapy

from AverageBidPoints.items import ABPItem

class CORSSpider(scrapy.Spider):
    name = "cors"
    allowed_domains = ["nus.edu.sg/cors"]
    start_urls = [
        "http://www.nus.edu.sg/cors/Archive/201415_Sem1/avgbidinfo_3B_1753_20142015s1.html",
        "http://www.nus.edu.sg/cors/Archive/201314_Sem2/avgbidinfo_3B_1808_20132014s2.html",
        "http://www.nus.edu.sg/cors/Archive/201314_Sem1/avgbidinfo_3B_2104_20132014s1.html",
        "http://www.nus.edu.sg/cors/Archive/201213_Sem2/avgbidinfo__1847_20122013s2.html",
        "http://www.nus.edu.sg/cors/Archive/201213_Sem1/avgbidinfo__1915_20122013s1.html",
        "http://www.nus.edu.sg/cors/Archive/201112_Sem2/avgbidinfo__1743_20112012s2.html",
        "http://www.nus.edu.sg/cors/Archive/201112_Sem1/avgbidinfo__1800_20112012s1.html",
        "http://www.nus.edu.sg/cors/Archive/201011_Sem2/avgbidinfo__1804_20102011s2.html",
        "http://www.nus.edu.sg/cors/Archive/201011_Sem1/avgbidinfo__1742_20102011s1.html",
        "http://www.nus.edu.sg/cors/Archive/200910_Sem2/avgbidinfo__1758_20092010s2.html",
        
        #"http://www.nus.edu.sg/cors/Archive/200910_Sem1/avgbidinfo__1728_20092010s1.html",
        #"http://www.nus.edu.sg/cors/Archive/200809_Sem2/avgbidinfo__1848_20082009s2.html",
        #"http://www.nus.edu.sg/cors/Archive/200809_Sem1/avgbidinfo__1745_20082009s1.html",
        #"http://www.cors.nus.edu.sg/Archive/200708_Sem2/avgbidinfo_3C_1803_20072008s2.html",
        #"http://www.cors.nus.edu.sg/Archive/200708_Sem1/avgbidinfo_3C_1740_20072008s1.html",
        #"http://www.cors.nus.edu.sg/Archive/200607_Sem2/avgbidinfo_3C_20062007s2.html",
        #"http://www.cors.nus.edu.sg/Archive/200607_Sem1/avg_bid_point_info_3C.html",
        #"http://www.cors.nus.edu.sg/Archive/200506_Sem2/averagepoints_20052006S2_3E.html",
        #"http://www.cors.nus.edu.sg/Archive/200506_Sem1/avg_bid_pts_info_20052006S1_3F.html"
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

