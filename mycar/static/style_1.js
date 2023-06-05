$(document).ready(function() {
    $("#do_login").click(function() { 
       closeLoginInfo();
       $(this).parent().find('span').css("display","none");
       $(this).parent().find('span').removeClass("i-save");
       $(this).parent().find('span').removeClass("i-warning");
       $(this).parent().find('span').removeClass("i-close");
       
        var proceed = true;
        $("#login_form input").each(function(){
            
            if(!$.trim($(this).val())){
                $(this).parent().find('span').addClass("i-warning");
            	$(this).parent().find('span').css("display","block");  
                proceed = false;
            }
        });
       
        if(proceed) //everything looks good! proceed...
        {
            $(this).parent().find('span').addClass("i-save");
            $(this).parent().find('span').css("display","block");
        }
    });
    
    //reset previously results and hide all message on .keyup()
    $("#login_form input").keyup(function() { 
        $(this).parent().find('span').css("display","none");
    });
 
  openLoginInfo();
  setTimeout(closeLoginInfo, 1000);
});

function openLoginInfo() {
    $(document).ready(function(){ 
    	$('.b-form').css("opacity","0.01");
      $('.box-form').css("left","-37%");
      $('.box-info').css("right","-37%");
    });
}

function closeLoginInfo() {
    $(document).ready(function(){ 
    	$('.b-form').css("opacity","1");
    	$('.box-form').css("left","0px");
      $('.box-info').css("right","-5px"); 
    });
}

$(window).on('resize', function(){
      closeLoginInfo();
});


// carousel js

// var multipleCardCarousel = document.querySelector(
//     "#carouselExampleControls"
//   );
//   if (window.matchMedia("(min-width: 768px)").matches) {
//     var carousel = new bootstrap.Carousel(multipleCardCarousel, {
//       interval: false,
//     });
//     var carouselWidth = $(".carousel-inner")[0].scrollWidth;
//     var cardWidth = $(".carousel-item").width();
//     var scrollPosition = 0;
//     $("#carouselExampleControls .carousel-control-next").on("click", function () {
//       if (scrollPosition < carouselWidth - cardWidth * 4) {
//         scrollPosition += cardWidth;
//         $("#carouselExampleControls .carousel-inner").animate(
//           { scrollLeft: scrollPosition },
//           600
//         );
//       }
//     });
//     $("#carouselExampleControls .carousel-control-prev").on("click", function () {
//       if (scrollPosition > 0) {
//         scrollPosition -= cardWidth;
//         $("#carouselExampleControls .carousel-inner").animate(
//           { scrollLeft: scrollPosition },
//           600
//         );
//       }
//     });
//   } else {
//     $(multipleCardCarousel).addClass("slide");
//   }