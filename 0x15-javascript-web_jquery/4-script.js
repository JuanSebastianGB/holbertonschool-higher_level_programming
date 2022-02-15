window.onload = function () {
  setRedHeaderClass();
};
function setRedHeaderClass () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
}
