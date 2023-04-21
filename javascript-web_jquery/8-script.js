$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  const movies = data.results;
  const $list = $('#list_movies');
  for (let movie of movies) {
    $list.append(`<li>${movie.title}</li>`);
  }
});
