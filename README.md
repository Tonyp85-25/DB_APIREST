# DB_APIREST

A simple RESTful API coded in Python with flask and Mongo Db for storing data

## Principle

You are a user who wants to save some special sentence.
- So first register , and send POST request with  this JSON {"username": *your_username*, "password": *your password*} to "/register" route
- With this registration, you will be granted 10 tokens
- To store your sentence, send POST request with  this JSON {"username": *your_username*, "password": *your password*,"sentence": *your_sentence*} to "/store" route,it will cost you one token
- To get your sentence, send POST request with  this JSON {"username": *your_username*, "password": *your password*} to "/get" route, it will cost you one token
- To update your sentence, send PUT request {"username": *your_username*, "password": *your password*, "sentence": *your_sentence*} }to "/update" route, it will cost you one token
- To delete your sentence, send DELETE request {"username": *your_username*, "password": *your password*, "fullDeletion": False} , set fullDeletion key to True if you want to delete your account as well, for free

## Installation

- Make sure you have Docker installed on your OS
- Download this repo
- do a `docker-compose build` at the root of the downloaded repo, then `docker-compose up`
- api available locally at http://0.0.0.0:5000


You can test this API using Postman or others tools