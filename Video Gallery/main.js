function scrollContent() {
    $('html,body').animate({
        scrollTop: $(".video-content").offset().top},
        'slow');
}

function searchGoogle() {
    window.open("http://google.com/search?q=" + document.getElementsByName("google search")[0].value)
}