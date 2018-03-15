var throttle = require('lodash.throttle');
var $navigationLinks = $('#fh5co-menu-wrap > ul > li > a');
var $sections = $($(".section").get().reverse());
var sectionIdTonavigationLink = {};


$sections.each(function() {
    var id = $(this).attr('id');
    sectionIdTonavigationLink[id] = $('#fh5co-menu-wrap > ul > li > a[href=#' + id + ']');
});

function highlightNavigation() {
    // get the current vertical position of the scroll bar
    var scrollPosition = $(window).scrollTop();
    // iterate the sections
    $sections.each(function() {
        var currentSection = $(this);
        // get the position of the section
        var sectionTop = currentSection.offset().top;

        // if the user has scrolled over the top of the section  
        if (scrollPosition >= sectionTop) {
            // get the section id
            var id = currentSection.attr('id');
            // get the corresponding navigation link
            var $navigationLink = sectionIdTonavigationLink[id].parent();
            // if the link is not active
            if (!$navigationLink.hasClass('active')) {
                // remove .active class from all the links
                $navigationLinks.parent().removeClass('active');
                // add .active class to the current link
                $navigationLink.addClass('active');
            }
            // we have found our section, so we return false to exit the each loop
            return false;
        }
    });
}

$(document).ready(function(){
	$(window).on('scroll', throttle(highlightNavigation, 200));
})
