
$(function () {
    var l_top = document.getElementById('shop_have').offsetTop;
    var l_top2 =document.getElementById('shop_have').clientHeight;
        $('#box111').css({
        'margin-top':l_top+l_top2
    });
        $('#end').css({
        'margin-top':l_top+l_top2 -('120')
    });
        $('.clear_shop').click(function () {
            $('#clear_car').stop().show(1)
        });
        $('.cancle').click(function () {
            $('#clear_car').stop().hide(1)
        });
    // var va = document.getElementsByTagName('input');
    // var va = document.getElementById('shop_num');
    var va = $('#shop_num').val();
    if  (va==1){
        $('.shop_have_6_1 a').stop().hide(1)
    }
    if (va>1){
        $('.shop_have_6_1 a').stop().show(1)
    }

    $('.checks').click(function () {
    $('.go_pay').stop().show(1);

});



});





