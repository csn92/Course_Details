import scrapy
from Tutorial.items import ColumItem


# Applicable only for MS CS students. Import has been directly done from CS department website.

class DepartmentSpider(scrapy.Spider):
	name="dept"
	allowed_domains = ["www.columbia.edu"]
	start_urls = ["http://www.cs.columbia.edu/education/courses/list?yearterm=20143"]

	def parse(self, response):
		term="Fall2014"
		item = ColumItem()
		for sel in response.xpath('//div[@id="content"]/table'):
			item['title'] = sel.xpath('//tr/td[@valign="top"]//text()').extract()
			item['timing'] = sel.xpath('//tr/td[position()=5]/text()').extract()
			item['date'] = sel.xpath('//tr/td[position()=4]/text()').extract()
			yield item

# class DepartSpider(scrapy.Spider):
# 	name="dep"
# 	allowed_domains = ["www.columbia.edu/"]
# 	start_urls = ["http://www.columbia.edu/cu/bulletin/uwb/sel/dept-A.html"]

# 	def parse(self,response):
# 		term="Fall2014"
# 		for sel in response.xpath('//tr'): 
# 		 		title= sel.xpath('td/text()[1]').extract()
# 		 		term1 = sel.xpath('td/a/text()').extract()
# 		 		link1 = sel.xpath('td/a/@href').extract()
# 		 		for i in range(len(term1)):
# 		 			term2 = term1[i]
# 		 			if(term2 == term):
# 		 				link = link1[i]
# 		 				print link
# 		 				print term2
# 		 			else:
# 		 				continue
		 	
# 		 		print title
# 		 		print '\n'


		 		
# class CourseSpider(scrapy.Spider):
# 	name="course"
# 	allowed_domains = ["wwww.columbia.edu/"]
# 	start_urls = ["http://www.columbia.edu/cu/bulletin/uwb/sel/ACCT_Summer2014.html"]

# 	def parse(self,response):
# 		course="Summer 2014 Accounting B5001"
# 		course_name_list = []
# 		course_name_element = []
# 		for sel in response.xpath('//table'):
# 			course_name=sel.xpath('.//tr[@valign="top" and position()>2]/td[@colspan="2"]//text()').extract()
			
# 			for i in range(1,len(course_name),3):
# 				course_name_element = course_name[i]
# 				if course_name_element!='\n':
# 					course_name_element=course_name[i]+" "+course_name[i+1]
# 					course_name_list.append(course_name_element)
# 		# print course_name_list
# 				course_timing = sel.xpath('.//tr[@valign="top" and position()>2]/td[@colspan="2"]//text()[.="Summer 2014 Accounting B5001"]/*').extract()
# 				print course_timing
# 		for i in range(len(course_name_list)):
# 			if course_name_list[i]==course:
# 				print course_name_list[i]
					
			
			


