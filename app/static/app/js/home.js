// Add active class to the current button (highlight it)
var header = document.getElementById("myDIV");
var btns = header.getElementsByClassName("btnn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
  var current = document.getElementsByClassName("active");
  current[0].className = current[0].className.replace(" active", "");
  this.className += " active";
  });
}
function myFunction3() {
    document.getElementById("top").style.display = "block";
    document.getElementById("relevant").style.display = "none";
    document.getElementById("latest").style.display = "none";
    document.getElementById("mydiv").style.display = "block";


  }
function myFunction1() {
    document.getElementById("top").style.display = "none";
    document.getElementById("relevant").style.display = "block";
    document.getElementById("latest").style.display = "none";
    document.getElementById("mydiv").style.display = "none";



  }
  function myFunction2() {
    document.getElementById("top").style.display = "none";
    document.getElementById("relevant").style.display = "none";
    document.getElementById("latest").style.display = "block";
    document.getElementById("mydiv").style.display = "none";



  }  
  var header = document.getElementById("mydiv");
  var btns = header.getElementsByClassName("btnn");
  for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("activ");
    current[0].className = current[0].className.replace(" activ", "");
    this.className += " activ";
    });
  }
 
 