$('document').ready(function () {
  translate();
  translateByEnter();
});
const fetchResponse = async () => {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  const response = $.get(url + $.param({ lang: $('input#language_code').val() }));
  return response;
}
const translate = async () => {
  $('input#btn_translate').click(async () => {
    const response = await fetchResponse();
    $('div#hello').html(response.hello);
  });
};
const applyEnter = async () => {
  const response = await fetchResponse();
  $('div#hello').html(response.hello);
};
const translateByEnter = () => {
  $('input#language_code').focus(() => {
    $(this).keydown((e) => {
      if (e.keyCode === 13)
        applyEnter();
    });
  });
}