#!/usr/bin/node
/* script that prints the title of a Star Wars movie where the episode number matches a given integer. */

const request = require('request');
const id = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
