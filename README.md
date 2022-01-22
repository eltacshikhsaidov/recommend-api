# recommend-api
Book recommender api written in flask framework. The ```API``` is written for solving my diplom project work. I wanted this kind of ```API```, but not found.
So, I decided to write my own. It is free to use. You can apply this api to your own recommendation projects. Good luck!
<br><br>
For building this ```API```, I used ```sklearn```, ```pandas```, ```numpy``` and ```flask```. 

# How API works

- recommendation for books works based on user ratings
- using ```sklearn.neighbors.NearestNeighbors``` we find best suited books 
- in future I'll try to add other advanced recommendation techniques

# project link

https://bookrecommenderapi.herokuapp.com/

# Endpints
- ```api/books/all``` - returns all books 
- ```api/books?title=BookTitle``` - returns the book (or multiple books) based on search. If not found then returns empty ```JSON``` array
- ```api/books/recommend?title=BookTitle``` returns ```JSON ARRAY``` recommended books based on searched book.

# Support
 <strong>follow me :)</strong>

# Examples

- ## Example 1: finding books based on title

<img src="https://github.com/eltacshikhsaidov/recommend-api/blob/main/image2.png?raw=true" alt="Example 1">

- ## Example 2: finding recommended books based on title

<img src="https://github.com/eltacshikhsaidov/recommend-api/blob/main/image1.png?raw=true" alt="Example 1">
