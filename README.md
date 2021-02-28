# Bookstore 
App which let's users save their books, import new ones, delete and update already existing ones.

### Technologies
Project is created with:
* Django
* Bootstrap
* Python 3.8.5
* Django REST framework 3.12.2
* Google Books API https://developers.google.com/books/docs/v1/getting_started


##Endpoints 
https://bookstore-stx.herokuapp.com/books/ - allows user to search through their books. <br/><br/>
https://bookstore-stx.herokuapp.com/manage/ - lists all books in our library and allows to add additional ones <br/><br/>
https://bookstore-stx.herokuapp.com/import/ - allows user to import new books to theirs library by searching through Google Books API <br/><br/>
https://bookstore-stx.herokuapp.com/api/view - REST API view for our project - By sending GET request to it, it returns JSON format of our books

