# -*- coding: utf-8 -*-
"""
Purpose: This is spider to get the products info from Teradek.
Domain: https://teradek.com/
Author: Mounika Konduru
Date: 19-01-2022
"""

import requests
from  datetime import datetime
import json


class Test_Products():
	"""
        This class is to get products information from Teradek.
    """
	def __init__(self):
		self.current_date = datetime.now().strftime("%d-%m-%Y")
		self.final_data = []

	def Data_Extract(self):
		
		url = "https://teradek.com/products/anton-bauer-digital-battery.oembed"
		response = requests.get(url)
		res_data = json.loads(response.text)
		dict_data = res_data['offers']
		
		for data in dict_data:
			offer_id = data['offer_id']
			sku = data['sku']
			title = data['title']
			price = data['price']
			
			self.final_data.append({'offer_id': offer_id,
								'product_title': title,
								'sku': sku,
								'price':price})

		json_object = json.dumps(self.final_data, indent = 4)
  
		# Writing to Output.json
		with open("Output.json", "w") as outfile:
		    outfile.write(json_object)
		
	def run(self):
		self.Data_Extract()

ob = Test_Products()
ob.run()