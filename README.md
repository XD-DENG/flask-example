# flask-example

A minimal web app developed in [Flask](http://flask.pocoo.org/). 

The main purpose is to introduce how to implement the essential elements in web application with Flask framework, including

- URL Building

- Authentication with Sessions

- Template & Template Inheritance

- Error Handling

- Integrating with *Bootstrap*

- Interaction with Database (SQLite)

For more basic knowledge of Flask, you can refer to [a tutorial on Tutorialspoint](https://www.tutorialspoint.com/flask/).


## Details

There are three tabs in this toy app

- **Public**: this is a page which can be accessed by anyone, no matter if the user has logged in or not.

- **Private**: Only logged-in user can access this page. Otherwise the user will get a 401 error page.

- **Admin Page**: This part is only open to the user who logged in as "Admin". In this tab, the administrator can manage accounts (list, delete, or add).


A few accounts were set for testing, like ***admin*** (password: admin), ***test_1*** (password: 123456), etc. You can also delete or add accounts after you log in as ***admin***.


## References

- http://flask.pocoo.org/

- https://www.tutorialspoint.com/flask/



## Credict
Image private.jpg: https://commons.wikimedia.org/wiki/File:(315-365)_Locked_(6149414678).jpg

Image public.jpg: https://commons.wikimedia.org/wiki/File:Drown%3F!_(131380682).jpg