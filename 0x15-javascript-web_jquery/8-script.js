const $ = window.jQuery;

window.onload = () => {
  printTitles();
};
const getMovies = async () => {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  const movies = await $.get(url);
  return movies;
};
const printTitles = async () => {
  const movies = (await getMovies()).results;
  movies.map((movie, index) => {
    $('ul#list_movies').append(`<li>${movie.title}</li>`);
    return true;
  });
};
