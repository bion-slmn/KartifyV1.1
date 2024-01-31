from flask import Flask, abort, render_template, request
from vendors.phonex_vendor import Phonex
from vendors.smartbuy_vendor import Smartbuy
from vendors import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


def seller_class(vendor):
    '''perform common logic to all view function
    and return a class that matches the vendor
    '''
    vendor_class = {'phonex': Phonex, 'smartbuy': Smartbuy}
    vendor_lower = vendor.lower()
    return vendor_class.get(vendor_lower, None)


@app.route('/count/', defaults={'vendor': None})
@app.route('/count/<vendor>')
def count(vendor):
    ''' counts the number of items that a vendor has
    - parameter:
    vendor:(string) this the name of the vendor it can eiter be
                    Phonex or Smartbuy

    if vendor is none it will return the total items of all vendors
    '''
    if vendor:
        vend = seller_class(vendor)
        if vend:
            all_laptops = vend.item('laptop', vendor)
            all_desktops = vend.item('desktop', vendor)
            return str(len({**all_laptops, **all_desktops})), 200
        return 'Seller Not available', 404
    # if nor vendor is specified
    phonex = Phonex()
    all_items_g = phonex.all()

    smartbuy = Smartbuy()
    all_items_k = smartbuy.all()

    return str(len({**all_items_g, **all_items_k}))


@app.route('/laptop/', defaults={'vendor': None})
@app.route('/laptop/<vendor>')
def laptop(vendor):
    '''return the laptops owned by specific vendor

    -parameter
    vendor:(string) this the name of the vendor it can eiter be
                        Phonex or Smartbuy

    if vendor is none it will return the total items of all vendors
    '''
    if vendor and seller_class(vendor):
         all_items = storage.items('laptop', vendor)
    elif  vendor and not seller_class(vendor):
        abort('404', 'Seller not avialable')
    else:
        all_items = storage.items('laptop')
    return render_template('display.html', item_dict=all_items, items='Laptop')


@app.route('/desktop/', defaults={'vendor': None})
@app.route('/desktop/<vendor>')
def desktop(vendor):
    '''return the desktops owned by specific vendor

    -parameter
    vendor:(string) this the name of the vendor it can eiter be
    Phonex or Smartbuy

    if vendor is none it will return the total items of all vendors
    '''
    if vendor:
        vend = seller_class(vendor)
        if vend:
            all_items = storage.items('desktop', vendor)
        abort('404', 'Seller not avialable')
    # return all desktops from all vendors 
    else:
        all_items = storage.items('desktop')
    return render_template('display.html', item_dict=all_items, items='Desktop')



@app.route('/search/', methods=["GET"])
def search():
    '''this is a search function that searches the data by name
    it searches the item from ll vendors
    '''
    searchName = request.args.get('searchName')
    return render_template('search.html', searchName=searchName)


@app.route('/')
def home1():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)
