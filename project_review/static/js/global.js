function w3_open() {
    if(document.getElementById("mySidebar").style.display == "none") {
      document.getElementById("mySidebar").style.display = "block";
    } else {
      document.getElementById("mySidebar").style.display = "none"
    }
  }

  function w3_open2() {
    if(document.getElementById("Profile").style.display == "none") {
      document.getElementById("Profile").style.display = "block";
    } else {
      document.getElementById("Profile").style.display = "none"
    }
  }


function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) =>{
    console.log(entry)
    if(entry.isIntersecting) {
      entry.target.classList.add('show');
    } else {
      entry.target.classList.remove('show');
    }
  });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach( (el) => observer.observe(el) );