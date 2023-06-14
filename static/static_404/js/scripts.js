$(document).ready(function() {

  // const animItems = document.querySelectorAll('.animate');

  // if(animItems.length > 0){
  //   function animOnScroll(params){
  //     for(let index = 0; index < animItems.length; index++){
  //       const animItem = animItems[index];
  //     }
  //   }
  // }

  // if ( window.innerWidth>0 ) {
	// 	$('.main_section').toggleClass("hidden");
	// 	//$('#header').addClass('animated');
	// }; 

  // animation
	$(window).on('load scroll', function(){
	    $('.main_section').each(function(){
		if ( $(this).offset().top < ($(document).scrollTop() + window.innerHeight*0.5 ) ) {
		    $(this).addClass('animated');
		}
	    });
	});

       // языки
	$('.language').click(function(){
        if ($('.language').hasClass("show")) {
            $('.language').removeClass('show');
        }else{
            $('.language').addClass('show');
        }
    });

    // menu button
        $('.menu_btn').click(function(){
            if($('.menu_btn').hasClass('active')){
                $('.menu_btn').removeClass('active');
                $('.navigation').removeClass('slid_active');
            }else{
                $('.menu_btn').addClass('active');
                $('.navigation').addClass('slid_active');
            }
        });

    // services block
        $(window).on('load resize', function() {
          if ($(window).width() < 750) {
            $('.services_block').slick({
              centerMode: true,
              arrows: false,
              slidesToShow: 1,
            });
          } else {
            $('.services_block').slick('unslick');
          }
      });

  // partners
      $('.our_partners_slider').slick({
        // centerMode: true,
        arrows: true,
        slidesToShow: 4,
        responsive: [
          {
            breakpoint: 1000,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
            }
          },
          {
            breakpoint: 730,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
            }
          },
          {
            breakpoint: 540,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              centerMode: true,
              // arrows:false,
              
            }
          }
        ]
      });

  // category
      $(window).on('load resize', function() {
        if ($(window).width() < 967) {
          $('.category').slick({
            // centerMode: true,
            arrows: true,
            slidesToShow: 3,
            responsive: [
              {
                breakpoint: 355,
                settings: {
                  slidesToShow: 2,
                  slidesToScroll: 1,
                }
              }
            ]
          });
        } else {
          $('.category').slick('unslick');
        }
    });

    $('.products_slider').slick({
      infinite:true,
      autoplay:true,
      autoplaySpeed: 2000,
      slidesToShow: 3,
      arrows: true,
      responsive: [
        {
          breakpoint: 1230,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            centerMode: true,
          }
        },
        {
          breakpoint: 960,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            centerMode: true,
          }
        },
        {
          breakpoint: 630,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            centerMode: false,
          }
        }
      ]
    });
});
