function get_random_color() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.round(Math.random() * 15)];
    }
    return color;
}

// document.getElementsByClassName('bg-custom').style.backgroundColor = get_random_color()
$(document).ready($(".bg-custom ").each(function() {
    $(this).css("background-color", get_random_color());
}))

// $(function() {
//     $(".bg-custom").each(function() {
//         var hue = 'rgb(' + (Math.floor((256-199)*Math.random()) + 200) + ',' + (Math.floor((256-199)*Math.random()) + 200) + ',' + (Math.floor((256-199)*Math.random()) + 200) + ')';
//          $(this).css("background-color", hue);
//     });
// });
$('.owl-carousel').owlCarousel({
    loop:true,
    margin:0,
    // nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:3
        }
    }
})