
$(function () {
    $('.box03_1_2').mouseenter(function () {
        $('.box03_1_2_c').stop().show(1)
    });
    $('.box03_1_2_c').mouseenter(function () {
        $('.box03_1_2_c').stop().show(1)
    });
    $('.box03_1_2_c').mouseleave(function () {
        $('.box03_1_2_c').stop().hide(1)
    });
    $('.box03_1_2').mouseleave(function () {
        $('.box03_1_2_c').stop().hide(1)
    });

    $('.box03_1_3').mouseenter(function () {
        $('.box03_1_3_c').stop().show(1)
    });
    $('.box03_1_3_c').mouseenter(function () {
        $('.box03_1_3_c').stop().show(1)
    });
    $('.box03_1_3_c').mouseleave(function () {
        $('.box03_1_3_c').stop().hide(1)
    });
    $('.box03_1_3').mouseleave(function () {
        $('.box03_1_3_c').stop().hide(1)
    });

    $('.box03_1_4').mouseenter(function () {
        $('.box03_1_4_c').stop().show(1)
    });
    $('.box03_1_4_c').mouseenter(function () {
        $('.box03_1_4_c').stop().show(1)
    });
    $('.box03_1_4_c').mouseleave(function () {
        $('.box03_1_4_c').stop().hide(1)
    });
    $('.box03_1_4').mouseleave(function () {
        $('.box03_1_4_c').stop().hide(1)
    });

    $('.box03_1_5').mouseenter(function () {
        $('.box03_1_5_c').stop().show(1)
    });
    $('.box03_1_5_c').mouseenter(function () {
        $('.box03_1_5_c').stop().show(1)
    });
    $('.box03_1_5_c').mouseleave(function () {
        $('.box03_1_5_c').stop().hide(1)
    });
    $('.box03_1_5').mouseleave(function () {
        $('.box03_1_5_c').stop().hide(1)
    });

    $('.box03_1_6').mouseenter(function () {
        $('.box03_1_6_c').stop().show(1)
    });
    $('.box03_1_6_c').mouseenter(function () {
        $('.box03_1_6_c').stop().show(1)
    });
    $('.box03_1_6_c').mouseleave(function () {
        $('.box03_1_6_c').stop().hide(1)
    });
    $('.box03_1_6').mouseleave(function () {
        $('.box03_1_6_c').stop().hide(1)
    });

    $('.box03_1_7').mouseenter(function () {
        $('.box03_1_7_c').stop().show(1)
    });
    $('.box03_1_7_c').mouseenter(function () {
        $('.box03_1_7_c').stop().show(1)
    });
    $('.box03_1_7_c').mouseleave(function () {
        $('.box03_1_7_c').stop().hide(1)
    });
    $('.box03_1_7').mouseleave(function () {
        $('.box03_1_7_c').stop().hide(1)
    });



    $('.box06_2_1_1 span').mouseenter(function () {
        $('.box06_2_2_1').stop().show(1)
    });
    // $('.box06_2_1_1 span').mouseleave(function () {
    //     $('.box06_2_2_1').stop().hide(1)
    // });
    $('.box06_2_1_2 span').mouseenter(function () {
        $('.box06_2_2_2').stop().show(1)
    });
    $('.box06_2_1_2 span').mouseleave(function () {
        $('.box06_2_2_2').stop().hide(1)
    });
    $('.box06_2_1_3 span').mouseenter(function () {
        $('.box06_2_2_3').stop().show(1)
    });
    $('.box06_2_1_3 span').mouseleave(function () {
        $('.box06_2_2_3').stop().hide(1)
    });
    $('.box06_2_1_4 span').mouseenter(function () {
        $('.box06_2_2_4').stop().show(1)
    });
    $('.box06_2_1_4 span').mouseleave(function () {
        $('.box06_2_2_4').stop().hide(1)
    });
    $('.box06_2_1_5 span').mouseenter(function () {
        $('.box06_2_2_5').stop().show(1)
    });
    $('.box06_2_1_5 span').mouseleave(function () {
        $('.box06_2_2_5').stop().hide(1)
    });

});
$(function () {
    $('.box07_2_1 ul').html($('.box07_2_1 ul').html() + $('.box07_2_1 ul').html());
            aaa=0;
            bbb=1;
            function ccc() {
                $('.box07_2_1 ul').css({"right":aaa+=bbb});
                if(aaa<-1100){
                    aaa=0
                }if(aaa>0){
                    aaa=-1100
                }
            }
            ddd=setInterval(ccc,10);
            $('.box07_2_1 ul').mouseenter(function () {
                clearInterval(ddd)
                }
            );
            $('.box07_2_1 ul').mouseleave(function () {
                ddd=setInterval(ccc,10);
                }
            );

            $(".left1").click(function () {
                bbb=1
            });
            $(".right1").click(function () {
                bbb=-1
            })
});

$(function () {

    var a=$(".picture li").length;
    var f=$(".picture li");
    var c=$(".tu_li");
    var k=$(".box04_1");
    for(var i=1;i<=a;i++){
        var li=$("<li>");
        c.append(li);
        if(i==0){
            c.addClass("active")
        }
    }
    var iiii = 0;
    tttt = setInterval(move,1500);
    function move(){
        var f=$(".picture li");
        iiii ++;
        if (iiii == a){
            iiii = 0;
        }
        $('.tu_li li').eq(iiii).addClass('active').siblings().removeClass('active');
        f.eq(iiii).addClass("active").siblings().removeClass("active");
        f.eq(iiii).fadeIn(1).siblings().fadeOut(1);
    }
});

$(function () {
    var a1 = $('.box05_1_2 li').length;
    var a2 = $('.box05_1_2 li');
    var a3 = 0;
    time2 = setInterval(move1,1000);
    function move1() {
        a3++;
        if (a3==a1){
            a3=0;
        }
        a2.eq(a3).fadeIn(500).siblings().fadeOut(500)
    }
});





