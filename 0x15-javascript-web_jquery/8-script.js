// Lists all Star Wars movies from api fetch
$('document').ready(() => {
  const movies = $('ul#list_movies');
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    movies.html(data.results.map((res) => `<li>${res.title}</li>`));
  });
});
