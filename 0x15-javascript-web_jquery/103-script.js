// Fetches lang-specified translation of "hello"
// Translates on keycode 13 in input#language_code
$('document').ready(() => {
    const lang_code_input = $('input#language_code');
    const getTranslation = () => {
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/',
            type: 'get',
            data: {
                'lang': lang_code_input.val()
            },
            success: (data) => $('div#hello').text(data.hello)
        });
    };
    $('input#btn_translate').click(getTranslation);
    $('input#language_code').keypress((e) => {
        const keycode = (e.keyCode ? e.keyCode : e.which);
        if (keycode === 13) {
            getTranslation();
        }
    });
});
