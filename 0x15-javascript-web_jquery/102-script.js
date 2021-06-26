// Fetches lang-specified translation of "hello"
$('document').ready(() => {
    const lang_code_input = $('input#language_code');
    $('input#btn_translate').click(() => {
    $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/',
        type: 'get',
            data: { 
        'lang': lang_code_input.val()
        },
        success: (data) => $('div#hello').text(data.hello)
        });
  });
});
