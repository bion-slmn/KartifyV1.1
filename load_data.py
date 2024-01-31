#!/usr/bin/python3
from vendors.phonex_vendor import Phonex
from vendors.smartbuy_vendor import Smartbuy
import time
import asyncio


from vendors import storage
# clear all the data from the daables
storage.drop()

start = time.time()
# loading items into databse

async def main():
    phonex = (Phonex.get_html('desktop'), Phonex.get_html('laptop'))
    smartbuy = (Smartbuy.get_html('desktop'), Smartbuy.get_html('laptop'))
    return await asyncio.gather(*phonex, *smartbuy)

pdesktop, plaptop, sdesktop, slaptop = asyncio.run(main())
mid = time.time()
print(mid - start)
Smartbuy.load_items('desktop', sdesktop)
Phonex.load_items('desktop', pdesktop)
Smartbuy.load_items('laptop', slaptop)
Phonex.load_items('laptop', plaptop)
end = time.time()
print(end - mid)
