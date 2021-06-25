$("document").ready((e) => {
    $("DIV#toggle_header").click((e) => {
        const cls = $("#red_header").hasClass("red") ? "green" : "red";
        e.target.removeClass(cls === "red" ? "red" : "green");
        e.target.addClass(cls);
    });
});
