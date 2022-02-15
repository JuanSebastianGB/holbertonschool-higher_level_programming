const $ = window.jQuery;

window.onload = function () {
  appendLiToUl();
};
function appendLiToUl () {
  $('div#add_item').click(function () {
    $('ul.my_list').append($('<li>item</li>'));
  });
}
