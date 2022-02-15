const $ = window.jQuery;

$('document').ready(() => {
  printData();
});
const getData = async () => {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const data = $.get(url);
  return data;
};
const printData = async () => {
  const data = await getData();
  $('div#hello').text(data.hello);
};
