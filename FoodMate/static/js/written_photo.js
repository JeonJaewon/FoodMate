$(document).ready(function(){
    $('.bg_parent')
    .mouseover(function(){
        $(this).children('div.bg').show();
        $(this).children('div.show_count').hide();
    })
    .mouseout(function(){
        $(this).children('div.bg').hide();
        $(this).children('div.show_count').show();
    });
});
