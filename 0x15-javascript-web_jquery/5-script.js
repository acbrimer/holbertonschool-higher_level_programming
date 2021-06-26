// Adds <li> to <ul class="my_list"> on DIV#add_item.click
$('document').ready(() => {
    const my_list = $('UL.my_list');
    $('DIV#add_item').click(() => {
        my_list.append('<li>Item</li>');
    });
});
