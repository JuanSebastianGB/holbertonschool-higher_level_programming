const $ = window.jQuery;

window.onload = function () {
  toggleRedBlueHeader();
};
function toggleRedBlueHeader () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
}
