const $ = window.jQuery;

window.onload = () => {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  printCharacter(url);
};
const printCharacter = async (url = '') => {
  const character = await $.get(url);
  setName(character.name);
};
const setName = async (name = '') => {
  await $('div#character').html(name);
};
