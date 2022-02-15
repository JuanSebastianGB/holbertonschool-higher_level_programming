window.onload = function () {
  setRedHeader();
};
function setRedHeader () {
  $('div#red_header').click(function () {
    $(this).css('color', '#FF0000');
  });
}
