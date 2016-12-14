var i = 20;
var interval;
var orig_url;

function printSeconds() {
    $('#show_time').empty();
    $('#show_time').append('The ad will be closed in ' + i + ' seconds');
    i -= 1;
    if (i < 0) {
        clearInterval(interval);
        window.location = orig_url;
    }
}

function changeImages() {

}

$(window).load(function() {
    interval = setInterval(printSeconds, 1000);
});

$(document).ready(function() {
    orig_url = $('#orig_url').val();
    $('#orig_url').remove();
});