from flask import Flask, abort, jsonify, request
from vendors.phonex_vendor import Phonex
from vendors.smartbuy_vendor import Smartbuy
from vendors import storage
from api.v1.views import app_views
from api.v1.views.pagination import Pagination


def seller_class(vendor):
    '''perform common logic to all view function
    and return a class that matches the vendor
    '''
    vendor_class = {'phonex': Phonex, 'smartbuy': Smartbuy}
    vendor_lower = vendor.lower()
    return vendor_class.get(vendor_lower, None)


@app_views.route('/laptop/', defaults={'vendor': None})
@app_views.route('/laptop/<vendor>')
def laptop(vendor):
    '''return the laptops owned by specific vendor

    -parameter
    vendor:(string) this the name of the vendor it can eiter be
                        Phonex or Smartbuy

    if vendor is none it will return the total items of all vendors
    '''
    page_no = request.args.get('page', default=1, type=int)

    if vendor and seller_class(vendor):
         all_items = storage.items('laptop', vendor)
    elif  vendor and not seller_class(vendor):
        abort('404', 'Seller not avialable')
    else:
        all_items = storage.items('laptop')
    page = Pagination(all_items)
    return jsonify(page.get_hyper(page_no))


@app_views.route('/desktop/', defaults={'vendor': None})
@app_views.route('/desktop/<vendor>')
def desktop(vendor):
    '''return the desktops owned by specific vendor

    -parameter
    vendor:(string) this the name of the vendor it can eiter be
    Phonex or Smartbuy

    if vendor is none it will return the total items of all vendors
    '''
    page_no = request.args.get('page', default=1, type=int)
    if vendor:
        vend = seller_class(vendor)
        if vend:
            all_items = storage.items('desktop', vendor)
        else:
            abort('404', 'Seller not avialable')
    # return all desktops from all vendors 
    else:
        all_items = storage.items('desktop')
    page = Pagination(all_items)
    return jsonify(page.get_hyper(page_no))


@app_views.route('/all/', defaults={'vendor': None})
@app_views.route('/all/<vendor>')
def all_items(vendor):
    '''return all items owned by the vendor

        -parameter
     vendor:(string) this the name of the vendor it can eiter be
     Phonex or Smartbuy
     if vendor is none it will return the total items of all vendors
    '''
    page_no = request.args.get('page', default=1, type=int)
    if vendor:
        vend = seller_class(vendor)
        if vend:
            data = storage.all(vendor)
            print(data)
            page = Pagination(data)
            return jsonify(page.get_hyper(page_no))
        abort(404, 'Seller Not available')

    # if nor vendor is specified
    data = storage.all()
    page = Pagination(data)
    return jsonify(page.get_hyper(page_no))

@app_views.route('/search/<name>/<vendor>', methods=["GET"])
@app_views.route('/search/<name>', methods=["GET"])
def search(name, vendor=None,):
    '''this is a search function that searches the data by name
    it searches the item from ll vendors if the name of the vendor
    is not sprcified
    -parameter:w
         name (string): name of the items to be searched
         vendor (string): name of the vendor it can be either be phonex or 
         smartbuy
    '''
    page_no = request.args.get('page', default=1, type=int)
    searchN = name
    search_items = storage.search(searchN, vendor)
    if search_items is None:
        abort(404)
    page =  Pagination(search_items)
    return jsonify(page.get_hyper(page_no))


@app_views.route('/compare/<item_1>/<item_2>')
def compare(item_1, item_2):
    searchitem_1 = storage.search(item_1)
    searchitem_2 = storage.search(item_2)
    search_items = {**searchitem_1, **searchitem_2}
    return jsonify(search_items)
