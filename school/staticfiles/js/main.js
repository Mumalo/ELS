/**
 * Created by JUSTICE on 9/11/2016.
 */

$(document).ready(function() {
var owl = $("#owl");
  owl.owlCarousel({
    transitionStyle: "fade",
    singleItem: true,
    pagination: true,
    autoPlay: 5000,
    stopOnHover:true,
    navigation: true,
    addClassActive: true,
    afterMove: previousslide,
    beforeMove: nextslide,


  });
    //     determine when an animation ends and remove the class
    $.fn.extend({
           animateCss: function (animationName) {
               var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
               $(this).addClass('animated ' + animationName).one(animationEnd, function() {
                   $(this).removeClass('animated ' + animationName);
               });
           }
         });

    // First Slide
        $(".owl-item.active .heading").addClass('fadeInDown');
         $(".owl-item.active .detail_desc").addClass('fadeInUp');

        // Other Slides
        function previousslide() {
          $(".owl-item.active .heading").addClass('fadeInDown');
          $(".owl-item.active .detail_desc").addClass('fadeInUp');
        }
        function nextslide() {
           $(".owl-item.active .heading").addClass('fadeInDown');
          $(".owl-item.active .detail_desc").addClass('fadeInUp');
        }


});
