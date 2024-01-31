# Kartify
This is a flask web application that is intended to provide a one-stop browsing point for desktop and laptops across different sites.
There is also an api that runs alongside the application.

You can filter the results by vendor or price. Once You have found the item, the web app will direct you to the seller site where a purchase can be completed
![Kartify Screen Short](https://github.com/bion-slmn/Kartify/assets/122830539/a5c3874e-f48d-45de-9b68-dc00e7b1775a)

The application scrapes specific website at given intervals and stores the data in a mysql database. 
This allows ease on manipulation of data, reducing the number of requests and preventing the app from being blocked but also makes the application faster

The backend uses flask to create api and template for somepages
 The application runs on port 5001 and the api runs on port 5000
All this api have hypermedia pagination and they return content as show in the example 

```json
{
  "data": "content",
  "next_page": 3,
  "page": 2,
  "page_size": 10,
  "prev_page": 1,
  "total_pages": 8
}
```

## APIs and Methods
This methods are for the web_Client:
### api/v1/laptop/vendor/?page=int
GET: Return the all laptops from a specific vendor
### api/v1/desktop/vendor/?page=int
GET: Return all the desktop from a specific vendor
### api/v1/all/?page=int
GET: Return all computers both laptops and desktops in the storage
### api/v1/all/vendor/?page=int
GET: Return all items from the specified vendor
### api/v1/laptops/?page=int
GET: return all laptops in the storage
### api/v1/desktops/?page=int
GET: Return all desktops  in storage
### api.v1/search/name/vendor/?page=int
GET: Return all items  whose name has the value name match the name specified in the api from the vendor specified
### api.v1/search/name/?page=int
GET: Return all items whose name has the value name match the name specified in the api from all vendors

## How to Install and Run the Project
The application was built with ubuntu 20.04 , python3.8, sqlachemy version 2.0.21,
MySQLdb module version 2.2.0 and MySQL 8.0


### Installing MySQL 8.0
$ ```sudo apt update```

$ ```sudo apt install mysql-server```

### Installing MySQLdb
$ ```sudo apt-get install python3-dev```

$ ```sudo apt-get install libmysqlclient-dev```

$ ```sudo apt-get install zlib1g-dev```

$ ```sudo pip3 install mysqlclient```

### Install aiohttp
$ ```pip install aiohttp```

### Installing SQLALchemy
$ ```sudo pip3 install SQLAlchemy```

### Installing requests and BeautifulSoup
$ ```pip install requests```

$ ```pip3 install beautifulsoup4```

### Starting Mysql database
$ ```sudo service mysql start```

$ ```cat setup_db.sql | mysql -u root -p```

### set environmental variable for DABATABASE
$ ```export PROJECT_USER="name of the user that was set in setup_db.sql"```

$ ```export PROJECT_PWD="password of the user that was set in setup_db.sql"```

$ ```export PROJECT_USER="bion_dev" PROJECT_PWD="bion_dev_pwd"```

### Scrape data and Load the database.
$ ```python3 load_data.py```

### START THE FLASK APP AND API
$ ```python3 -m flask_app.views```

$ ```python3 -m api.v1.app```
## USAGE
The application will be running on http://localhost:5001 when not deployed on 
remote server. 
You can view the deployed site on Github here https://bion-slmn.github.io/Kartify/flask_app/templates/home.html
However, that is just part of the website as Github only accepts static files.

The application start at the home_page. As shown below.

![home_page kartigy](https://github.com/bion-slmn/Kartify/assets/122830539/4cb7c385-28e3-499c-b2f7-b308cff63301)

To start your journey, click the BEGIN SHOPPING NOW BUTTON, this will take you where you shop both laptops
and desktops by brand, as shown in the images below

![begin shopping](https://github.com/bion-slmn/Kartify/assets/122830539/0ff378be-9c27-4576-abac-83b081ed5f57)

When you click the BEGIN SHOPPING NOW !! button
![Shop_by_brand](https://github.com/bion-slmn/Kartify/assets/122830539/dbf43638-78ce-4280-b6f8-ed3ac81d893f)

Select any brand that you would like to view the items on sale.
In this example ASUS brand in selected . This should display all the ASUS laptops and desktops from all vendors.
By default they will be arranged from the lowest priced to the highest priced computer.
As shown in the image below.
![Display Page](https://github.com/bion-slmn/Kartify/assets/122830539/13149efa-df64-41d6-a08e-bc8e1d514a82)

You could also filter the results by vendor. This chooses all computers from a specific vendor

## Contributing
Bion Solomon - bionsol25@gmail.com

Lucas Owen - sanguraowens@gmail.com

Ambrose Kol - kolus7381@gmail.com



