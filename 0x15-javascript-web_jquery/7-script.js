// Fetches data and displays name field in DIV#character
$('document').ready(() => {
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
    $('DIV#character').text(data.name);
  });
});
