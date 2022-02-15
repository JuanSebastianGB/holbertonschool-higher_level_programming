const $ = window.jQuery;
$('document').ready(function () {
  translate();
});
const translate = async () => {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('input#btn_translate').click(async () => {
    const response = await $.get(url + $.param({ lang: $('input#language_code').val() }));
    $('div#hello').html(response.hello);
  });
};
