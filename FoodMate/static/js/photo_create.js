$(document).ready(function(){
    $("#label1").click(function(){
        $("#label2").show();
        $("#img_count").text("1/4");
    });
    $("#label2").click(function(){
        $("#label3").show();
        $("#img_count").text("2/4");
    });
    $("#label3").click(function(){
        $("#label4").show();
        $("#img_count").text("3/4");
    });
    $("#label4").click(function(){
        $("#img_count").text("4/4");
    });

});