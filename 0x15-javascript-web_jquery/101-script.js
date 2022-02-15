$('document').ready(() => {
  addItem();
  removeItem();
  clearList();
});
const addItem = () => {
  $('div#add_item').click(() => {
    $('ul.my_list').append($('<li>Item</li>'));
  });
};
const removeItem = () => {
  $('div#remove_item').click(() => {
    const lastChild = $('ul.my_list li:last');
    lastChild.remove();
  });
};
const clearList = () => {
  $('div#clear_list').click(() => {
    $('ul.my_list').empty();
  });
};
