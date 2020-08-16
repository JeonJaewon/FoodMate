$(document).ready(function(){
    $('.nav_font').click(function(){
        $(this).css("background-color", "#FFBE00");
        $(this).css("border","2px solid #FFBE00");
    })
    .mouseover(function(){
        $(this).css("background-color", "#FFBE00");
        $(this).css("border","2px solid #FFBE00");
    })
    .mouseout(function(){
        $(this).css("background-color", "white");
        $(this).css("border","2px solid white");
    });
});