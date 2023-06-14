//search for groups
$('[data-search]').on('keyup', function() {
    var searchVal = $(this).val();
    var filterItems = $('[data-filter-item]');

    if ( searchVal != '' ) {
        filterItems.addClass('hidden');
        $('[data-filter-item][data-filter-name*="' + searchVal.toLowerCase() + '"]').removeClass('hidden');
    } else {
        filterItems.removeClass('hidden');
    }
});

//add group table => for each group its content into//
function this_group_info(nameId) {
    var $pre = $('pre');
    $('.group_info_container').children().css('display', 'none');
    var thisGroup = $($('.group_info_container').find('#' + nameId));
    thisGroup.css('display', 'table-caption');
}
//endadd group table => for each group its content into//

//loading first .5 sec//
var load;
function loader_function() {
    load = setTimeout(show_page, 1);
}
function show_page() {
    document.getElementById('main').style.opacity = '1';
    document.getElementById('loader').style.display = 'none';
}
//end loading first .5 sec//
