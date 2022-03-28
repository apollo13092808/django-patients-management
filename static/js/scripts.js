$(document).ready(function () {

    let verify = $("#check-id").length;

    if (verify == 0) {
        $("#no-data").text("No Patient Found.");
    };

});

setInterval(() => {
    let date = new Date();
    $('#clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ':' +
        (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ':' +
        (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);

