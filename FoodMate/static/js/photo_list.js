//let counter = 0;

$(document).ready(function(){
    $.noConflict();
    init_slick();
    init_hover();
    init_see_more_btn();
});
function init_slick(){
    $('.image_list').slick({
        autoplay: true,
        autoplaySpeed: 5000,
        dots: false, // 하단 paging버튼 노출 여부
        infinite: true, // 양방향 무한 모션
        speed: 300, // 모션 스피드
        cssEase: 'linear', //css easing 모션 함수

    });
}
function init_hover(){
    $('.bg_parent')
    .mouseover(function(){
        $(this).children('div.bg').show();
        $(this).children('div.show_count').hide();
    })
    .mouseout(function(){
        $(this).children('div.bg').hide();
        $(this).children('div.show_count').show();
    });
}
function init_see_more_btn(){
    let counter = $('.article_board').children().length;
    $('.article_board').append('<div class="article" id="see_more_btn_container"><img id="see_more_btn" src="static/img/see_more_btn.png"></div>')
    $("#see_more_btn").click(function(){
        counter = counter + 10;
        info = {"counter": counter}
        $.ajax({
            type: "POST",
            url: "call_ajax/",
            data: info,
            dataType: "json",
            statusCode: {
                // 더 이상 읽어 올 글이 존재하지 않을 때
                404: function(response){
                    $('#see_more_btn_container').remove();
                    console.log(response.responseJSON.message)
                },
                // POST 이외의 방식으로 호출
                400: function(response){
                    console.log(response.responseJSON.message)
                }
            },
            success: function(response){ // 호출 성공시
                articles = JSON.parse(response.articles)
                img_urls =  response.img_urls
                console.log(articles)
                for(var i = 0; i < articles.length; i++){
                    console.log(articles[i].pk)
                    $(".article_board").append(
                    '<div style=\"margin-left: 0px; margin-right:25px; z-index: 1; position:relative; cursor:pointer;\" class=\"article\" onclick =\"location.href=\"{% url '
                    + 'photo:detail ' + articles[i].pk  + ' %}\">'
                    + '<img src=\"' + img_urls[i] + '\" class=\"article\">'
                    + '<p class=\"area\" style=\"z-index: 3; position: absolute; right: 12px; top: 10px;\">' + articles[i].fields.area + '</p>'
                        + '<div class=\"bg_parent\">'
                            + '<div class=\"bg\">'
                                + '<div style=\"margin-top: 172px; width: 240px; height: 404px; text-align: center; \">'
                                    + '<p class=\"title\">' + articles[i].fields.title + '</p>'
                                        + '<div>'
                                            + '<span class=\"yellow_font\">' + articles[i].fields.count + '</span>'
                                            + '<span style=\"margin-left:5px;\" class=\"white_font\">개</span>'
                                            + '<span style=\"margin-left:16px;\" class=\"yellow_font\">' + articles[i].fields.money + '</span>'
                                            + '<span style=\"margin-left:13px;\"class=\"white_font\">원</span>'
                                        + '</div>'
                                + '</div>'
                            + '</div>'
                            + '<div class=\"show_count\" style=\"z-index: 3; position: absolute; right:0; bottom: 0px; width: 100px; height: 30px;\">'
                                + '<img style=\"display: inline-block;\" src=\"static/img/comment_white.png\"\"/>'
                                + '<p class=\"white\" style=\"display: inline-block; margin-left: 4px;\"> 0 </p>'
                                + '<img style=\"margin-left:12px; display: inline-block;\" src=\"static/img/heart_white.png\"\"/>'
                                + '<p class=\"white\" style=\"margin-left:4px; display: inline-block;\">' + articles[i].fields.like + '</p>'
                            + '</div>'
                        + '</div>'
                    + '</div>')
                }
                $('#see_more_btn_container').remove();
                init_hover() // 다시 호출해줘야 호버 효과 적용됨
                init_see_more_btn();
            }
        })
    })
}