// Fetches and displays French translation for "hello"
$('document').ready(() => {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  console.log(data);
  });
});
