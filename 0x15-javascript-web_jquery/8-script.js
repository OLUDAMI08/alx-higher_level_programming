url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function(data, status){
  const movies = data.results;
  for (let i = 0; i < movies.length; i++){
	$('UL#list_movies').append("<li>" + movies[i].title + "<li>");
  }
});
