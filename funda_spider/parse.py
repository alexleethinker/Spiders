from scrapy.selector import Selector
from pprint import pprint

with open('sold.html','r') as f:
    html = f.read()

html = html.replace('\n','')
selector = Selector(text = html)


full_address = selector.xpath('//h1[contains(@class, "object-header__address")]//text()').extract()
full_address = list(map(lambda s : s.strip(), full_address))
street = full_address[0].split(' ')[0]
house_number = full_address[0].split(' ')[1]
postal = full_address[1].split(' ')[0] + full_address[1].split(' ')[1]
city = ' '.join(full_address[1].split(' ')[2:])  ### there are exceptions

labels = selector.xpath('//ul[contains(@class, "labels")]//li//text()').extract_first()

num_photo = selector.xpath('//a[contains(@data-interaction, "Object.Fotos")]//span[contains(@class, "object-media-teaser-count")]//text()').extract_first()
num_360_photo = selector.xpath('//a[contains(@data-interaction, "Object.Fotos360")]//span[contains(@class, "object-media-teaser-count")]//text()').extract_first()

agency_name = selector.xpath('//a[contains(@class, "object-contact-aanbieder-link")]//text()').extract_first()
agency_link = selector.xpath('//a[contains(@class, "object-contact-aanbieder-link")]//@href').extract_first()
agency_call = selector.xpath('//a[starts-with(@href, "tel:")]//@href').extract_first().split(':')[1]
neighbourhood = selector.xpath('//p[contains(@class, "object-buurt__name")]//text()').extract_first()

price = selector.xpath('//strong[contains(@class, "object-header__price")]//text()').extract_first()

description = selector.xpath('//div[contains(@class, "object-description-body")]//text()').extract()
description = '\n'.join(description)




# store feature as json dict
schema = selector.xpath('//div[contains(@class, "object-kenmerken-body")]//dl[contains(@class, "object-kenmerken-list")]//dt[not(@class)]//text()').extract()
schema = list(map(lambda s : s.strip(), schema))
schema = [s for s in schema if s]
values = selector.xpath('//div[contains(@class, "object-kenmerken-body")]//dl[contains(@class, "object-kenmerken-list")]//dd[not(@class)]//text()[not(parent::a)]').extract()
values = list(map(lambda s : s.strip(), values))
values = [s for s in values if s]

features = dict(zip(schema,values)) 



pprint(neighbourhood)