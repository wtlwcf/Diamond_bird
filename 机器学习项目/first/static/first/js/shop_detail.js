

$(function () {
    var l_top = document.getElementById('shop_detail_4').offsetTop;
    // alert(l_top)
    var l_top2 =document.getElementById('shop_detail_4').offsetHeight;
    // alert(l_top2);
    var l_top3 = document.getElementById('box100').offsetHeight;
    // alert(l_top3)
        $('#box100').css({
            'top': l_top + l_top2
    });
        $('#box1111').css({
            'position':'absolute',
            'top':l_top+l_top2+l_top3 +60
    });


});