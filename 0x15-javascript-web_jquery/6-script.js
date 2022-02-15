const $ = window.jQuery;

window.onload = function () {
  updateHeader();
};
const updateHeader = () => {
  $('div#update_header').click(function () {
    $('header').html('New Header!!!');
  });
};
