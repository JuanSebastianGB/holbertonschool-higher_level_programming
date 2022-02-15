const $ = window.jQuery;

window.onload = function () {
  setRedHeaderClass();
};
function setRedHeaderClass () {
  $('div#red_header').click(function () {
    $('header').addClass('red');
  });
}
