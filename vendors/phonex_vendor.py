#!/usr/bin/python3
'''this module define a vendor call Glantix'''
from vendors.vendor import Vendor, Base
from bs4 import BeautifulSoup
import requests
import aiohttp
import asyncio


class Phonex(Vendor, Base):
    ''' this class defines a vendor called kilimall'''
    __tablename__ = 'phonex'
    
    # using classmethod as a factory method to create objects
    @staticmethod
    async def get_html(item: str) ->str:
        '''fetch the html of from phenox site that match the item 

        Parameter:
        - item (str, optional): Type of items to load.
        Can be 'laptop' or 'desktop'.

        Return the html string of the website
        '''
        url_laptop = 'https://www.phone-x.co.ke/product-category/computing/laptops/'
        url_desktop = 'https://www.phone-x.co.ke/product-category/computing/computers-and-desktops/'
        url = url_laptop if item.lower() == 'laptop' else url_desktop
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.text()

    

    @classmethod
    def load_items(cls, item: str, html: str) -> None:
        '''it loads all the item of the vendor from the
        file and stores in database

        Parameter
        - item (str, optional): Type of items to load.
        - html (str): html from the website that.
        Can be 'laptop' or 'desktop'.
        '''
        from vendors import storage
        try:
            soup = BeautifulSoup(html, 'html.parser')
            all_div = soup.find_all('div', {'class': 'col-inner'})
            for laptop in all_div:
                new = {}
                name = laptop.a.get('aria-label')
                if not name:
                    continue
                new['name'] = name
                new['link'] = laptop.a.get('href')
                new['img_link'] = laptop.img.get('src')
                new['price'] = laptop.find('bdi').text.strip('KSH \h')
                new['vendor'] = cls.__name__
                new['catergory'] = 'laptop' if item == 'laptop' else 'desktop'

                obj = cls(**new)
                storage.new(obj)
                storage.save()
            print("Successfully loaded", item)
        except Exception as e:
            print(e)
