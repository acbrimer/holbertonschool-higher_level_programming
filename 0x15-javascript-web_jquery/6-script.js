// Updates <header> text to "New Header!!!" on DIV#update_header.click
$('document').ready(() => {
    const header = $('header');
  $('DIV#update_header').click(() => {
    header.text('New Header!!!');
  });
});
