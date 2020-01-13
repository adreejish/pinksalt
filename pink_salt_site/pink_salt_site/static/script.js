var slideindex=0;
slides=document.getElementsByClassName("slide")
setInterval(changeslide,5000)
//console.log($('#title'))


console.log("js works");

/*for(i=0;i<slides.length;i++)
    {
        console.log(i);
        slides[i].style.visibility="hidden"
      //  slides[3].style.visibility="visible"
    }*/

function changeslide(){
    //hide all slides
    for(i=0;i<slides.length;i++){
        slides[i].style.visibility="hidden";
        
    }
    
    if (slideindex==slides.length-1)
        {
            slideindex=0;
        }
    
   slides[slideindex].style.visibility="visible";
    //slides[slideindex].fadeIn();
    slideindex++
}

