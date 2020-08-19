//let counter = 0;
let counter = $('.article_board').length;
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
    $("#see_more_btn").click(function(){
        console.log("ajax call")
        counter = counter + 4;
        info = {"counter": counter}
        $.ajax({
            type: "POST",
            url: "call_ajax/",
            data: info,
            dataType: "json",
            success: function(response){
                articles = JSON.parse(response.articles)
                img_urls =  response.img_urls
//                console.log(articles)
//                console.log(urls)

                for(var i=0; i<articles.length; i++){
                    $(".article_board").append(
                    "<div style=\"cursor:pointer;\" class=\"article\" onclick =\"location.href=\'{% url \'photo:detail\' article.id %}\'\">"
                    + "<img src=\"" + img_urls[i] + "\" style=\"object-fit: contain; width:100px; height:100px\"/>"
                    + "<div>" + articles[i].fields.title + "</div>"
                    + "<span>" + articles[i].fields.count + "개</span>"
                    + "<span>" + articles[i].fields.money + "원</span>"
                    + "</div>")
                }
            }
        })
    })
});