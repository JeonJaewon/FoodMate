$(document).ready(function(){
    // 모든 약관 동의 확인

    //모두 동의 눌렀을 경우
    $('#check_all').click(function(){
        var checked = $(this).is(":checked");
        if(checked){
            $("#check_1").prop("checked", true);
            $("#check_2").prop("checked", true);
            $("#check_3").prop("checked", true);
        }else{
            $("#check_1").prop("checked", false);
            $("#check_2").prop("checked", false);
            $("#check_3").prop("checked", false);
        }
    });

    //하나라도 체크가 되어있지 않을 경우, 모두 동의 체크 해제
    $("#check_1").click(function(){
        if($(this).is(":checked") == false){
            $("#check_all").prop("checked", false);
        }else{
            if($("#check_2").is(":checked") == true && $("#check_2").is(":checked") == true){
                $("#check_all").prop("checked", true);
            }
        }
    });
    $("#check_2").click(function(){
        if($(this).is(":checked") == false){
            $("#check_all").prop("checked", false);
        }else{
            if($("#check_1").is(":checked") == true && $("#check_3").is(":checked") == true){
                $("#check_all").prop("checked", true);
            }
        }
    });
    $("#check_3").click(function(){
        if($(this).is(":checked") == false){
            $("#check_all").prop("checked", false);
        }else{
            if($("#check_1").is(":checked") == true && $("#check_2").is(":checked") == true){
                $("#check_all").prop("checked", true);
            }
        }
    });
});