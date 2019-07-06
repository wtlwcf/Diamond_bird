 $(function show() {
        var isClick = true;

        if (isClick) {

            document.getElementById('show').style.display = "block";
            isClick = false
        } else {

            document.getElementById('show').style.display = "none";
            isClick = true
        }
    });



var isClick = true;
function shwo() {
    if(isClick)
    {
        document.getElementById('shwo').style.display = "block"
        isClick = false
    }else{
        document.getElementById('shwo').style.display = "none"
        isClick = true
    }
}



var isClick = true;
function swoh() {
    if(isClick)
    {
        document.getElementById('swoh').style.display = "block"
        isClick = false
    }else{
        document.getElementById('swoh').style.display = "none"
        isClick = true
    }
}


$(function () {
    $('.v1101').click(function () {
        $('.v7').hide(1);
        $('.v8').hide(1);
        $('.v9').hide(1);
        $('.v10').hide(1);
        $('.v1102').show(1);
        $('.v1101').hide(1)
    });
    $('.v1102').click(function () {
        $('.v7').show(1);
        $('.v8').show(1);
        $('.v9').show(1);
        $('.v10').show(1);
        $('.v1102').hide(1);
        $('.v1101').show(1)
    });


});








