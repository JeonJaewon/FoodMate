$(document).ready(function(){
    $.noConflict();
    $('.image_list').slick({
        autoplay: true,
        autoplaySpeed: 5000,
        dots: false, // 하단 paging버튼 노출 여부
        infinite: true, // 양방향 무한 모션
        speed: 300, // 모션 스피드
        cssEase: 'linear', //css easing 모션 함수

    });
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