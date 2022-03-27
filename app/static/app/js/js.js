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
});  



mybutton = document.getElementById("myBtn");

// When the user s  rolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

 $(document).ready(function(){
    $(".heart").click(function(){
      if($(".heart").hasClass("like")){
        $(".heart").removeClass("like");
        $(".heart").addClass("liked");
        $(".heart").html('<i class="fa-solid fa-heart"></i>');
      }
      else{
        $(".heart").removeClass("liked");
        $(".heart").addClass("like");
        $(".heart").html('<i class="fa-regular fa-heart"></i>');
      }
    });
  });


  function myFunctioninfo() {
    var element = document.getElementById("moreinfo");
    element.classList.add("mystyle");
    var element = document.getElementById("infomore");
    element.classList.add("mystyle1");
 }
  