# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# Categories to be scrapied:
# - properties for sale
# - properties for rent
# - agencies
# - funda for business


import scrapy


class FundaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    href = scrapy.Field()
    address = scrapy.Field()
    label = scrapy.Field()
    house_num = scrapy.Field() 
    post_code = scrapy.Field()
    city = scrapy.Field()
    num_photos = scrapy.Field()
    num_360_photos = scrapy.Field()
    description = scrapy.Field()

    #Transfer of Ownership
    asking_price = scrapy.Field()
    listed_since = scrapy.Field()
    status = scrapy.Field()
    acceptance = scrapy.Field()

    #Construntion
    kind_of_house = scrapy.Field()
    building_type = scrapy.Field()
    year_of_construction = scrapy.Field()
    type_of_roof = scrapy.Field()
    specific = scrapy.Field()  # Optinal

    #Surface areas and volume
    #Areas
    living_area = scrapy.Field()
    exterior_sapce_attached_to_the_building = scrapy.Field()
    external_storage_space = scrapy.Field()
    plot_size = scrapy.Field()
    volume = scrapy.Field()

    #Layout
    num_rooms = scrapy.Field()
    num_bedrooms = scrapy.Field()
    num_bath_rooms = scrapy.Field()
    bathroom_facilities = scrapy.Field()
    num_stories = scrapy.Field()

    #Energy
    energy_label = scrapy.Field()
    insulation = scrapy.Field()
    heating =scrapy.Field()
    hot_water =scrapy.Field()
    ch_boiler = scrapy.Field()

    #Cadastral data
    kadaster_title = scrapy.Field()
    ownership_situation = scrapy.Field()

    #Exterior space
    location = scrapy.Field()
    garden = scrapy.Field()
    back_garden = scrapy.Field()
    garden_location = scrapy.Field()

    #Storage space
    storage = scrapy.Field()
    facilities = scrapy.Field()
    
    #Parking
    type_parking = scrapy.Field()

    #Neighbourhood
    neighbourhood = scrapy.Field()

    #Agency
    agency_name = scrapy.Field()
    agency_phone = scrapy.Field()
    

    #VVE (Owners Association) checklist - Only for appartments
    registration_with_KvK = scrapy.Field()
    annual_meeting = scrapy.Field()
    periodic_contribution = scrapy.Field()
    reserve_fund_present = scrapy.Field() 
    maintenance_plan = scrapy.Field()
    building_insurance = scrapy.Field()
    
    
    
    pass
