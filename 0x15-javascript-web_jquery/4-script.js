// Toggles header between red and green text on #toggle_header.click
$("document").ready((e) => {
    const header = $('header');
    $("DIV#toggle_header").click((e) => {
        header.toggleClass('green');
        header.toggleClass('red');
    });
});
