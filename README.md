# PDD_28_hw
Python: Deploying sites on Django. wsgi, gunicorn, nginx
## update 2022.06.14 Deploying
### service nginx status

![img_15.png](img_15.png)

### sudo systemctl status gunicorn
![img_16.png](img_16.png)

### Rusult:

![img_17.png](img_17.png)

## update 2022.06.10 Site optimization

![img_14.png](img_14.png)

![img_12.png](img_12.png)

![img_13.png](img_13.png)

## update 2022.06.09
Added Paginator for the function ‘history’ and page ‘history.html’.

Added Paginator for the class ‘Hh_RequestListView’ and page req_list.html.

Added filter ‘|date:"SHORT_DATETIME_FORMAT"’at the page ‘req_detail.html’.


![img_11.png](img_11.png)

## update 2022.06.07
Added tests for the  views and its response codes.

Added tests for permissions and response pages for different users

## update 2022.06.06
Implemented user model: added new application 'usersapp'.

The menu items “Data management” (req_list.html), "Start searching" (form.html) and "History" (history.html) are available only for logged in users.

If user attribute is_dbAdmin = True than it’s possible to change data at the pages:

* req_detail.html
* req_update.html
* req_create.html
* req_delete.html

## Project
Project name is kvblog.

## Aplication:
Aplication name is 'blogapp'.

## Pages:
Implemented the base page (base.html):

![img_1.png](img_1.png)

Static is here:

![img_9.png](img_9.png)

Implemented pages inherited from the base page:

![img.png](img.png)

### index.html
index.html - the first page of the aplication;

![img_2.png](img_2.png)

### form.html
form.html - the page with the form used for search at HH.RU;

![img_3.png](img_3.png)

### result.html
result.html - the page with current result of the request at HH.RU;

![img_4.png](img_4.png)

### history.html
history.html - the page with all saved request at the db;

![img_5.png](img_5.png)

### contacts.html
contacts.html - the page with my contacts.

![img_6.png](img_6.png)

### 2022.06.06 Updated:
Added new navigation link ‘Управление данными’.

Added new pages:

* req_list.html
* req_detail.html
* req_update.html
* req_create.html
* req_delete.html

For these pages added class base views classes based on different view classes.

Added Mixin for the view classes

* Hh_RequestDetailView
* Hh_RequestUpdateView



### urls
Internal urls described here:

![img_10.png](img_10.png)

## Models:
Models names are:
* Hh_Request
* Hh_Response

![img_7.png](img_7.png)

## Django commands:
Implemented two commands:
1. fill_db - to fill database with test data;
2. fill_db_parser - to fill databsse with parsed data from HH.RU

Examples:

python manage.py fill_db

python manage.py fill_db_parser

![img_8.png](img_8.png)