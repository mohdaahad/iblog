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
    $(this).css("color", get_random_color());
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




const body=document.querySelector("body"),
    nav=document.querySelector("nav"),
    modeToggle=document.querySelector(".dark-light"),
    searchToggle=document.querySelector(".searchToggle"),
    sidebarOpne=document.querySelector(".sidebarOpne"),
    siderbarClose=document.querySelector(".siderbarClose");
    
    let getMode =localStorage.getItem("mode");
        if(getMode &&getMode === "dark-mode"){
            body.classList.add("dark");

        }
    
//js codee to toggle dark and light
   modeToggle.addEventListener("click",() =>{
        modeToggle.classList.toggle("active");
        body.classList.toggle("dark");

        if(!body.classList.contains("dark")){
            localStorage.setItem("mode","light-mode");

        }
        else{
            localStorage.setItem("mode","dark-mode");
        }
    }) ;
//js codee to toggle search box 

    searchToggle.addEventListener("click",() =>{
        searchToggle.classList.toggle("active")
    });


//js code to toggle sidebar
sidebarOpne.addEventListener("click",() =>{
    nav.classList.add("active");
}) ;  

body.addEventListener("click",e =>{
    let clickedElm=e.target;
    if(!clickedElm.classList.contains("sidebarOpne") && !clickedElm.classList.contains("menu")){
        nav.classList.remove("active");
    }
}) ;  