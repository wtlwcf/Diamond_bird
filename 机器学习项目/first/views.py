from django.shortcuts import render,redirect
from django import views
from first.forms import *
from first.face_baidu import *
import pymysql
from django.db.models import Sum
'''
搜索页面的物品数量与页面数量灵活对应
将购物车添入订单后，购物车内相对应的该商品自动删除
可多项选择购物车内的商品并且选择商品填写订单时，对应商品会传到填写订单的页面
每个页面均可看到登录状态以及购物车内的商品数量
手动完成数据挖掘和所有页面设计以及Django与数据库页面两者的交互
逻辑明确，页面的衔接与所有链接之间的跳转完整且准确
完美利用Django与前端后台的交互，商品的详情页面所有数据都来自于数据库，并且一一对应，准确无误
'''

# 连接数据库
conn=pymysql.connect(user="root",password="123456",db="bank")
cursor=conn.cursor()
cursor1=conn.cursor()

# 注册
class Register(views.View):
    def get(self,request):
        return render(request,'first/register.html')
    def post(self,request):
        f=RegisterForm(request.POST)
        if f.is_valid():
            username = f.cleaned_data.get("user_name")
            password = f.cleaned_data.get("user_password")
            phone=f.cleaned_data.get("user_phone")
            User.objects.create(user_name=username,user_password=password,user_phone=phone)
            u1=User.objects.get(user_name=username)
            request.session['uid'] = u1.id
            return redirect('isface1')
        else:
            print(f.get_simple())

            return redirect('register')


# 登录
class Login(views.View):
    def get(self,request):
        return render(request,'first/login.html')
    def post(self,request):
        f = LoginForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data.get("user_name")
            pw = f.cleaned_data.get("user_password")
            if User.objects.filter(user_name=name, user_password=pw).exists():
                u2 =User.objects.get(user_name=name, user_password=pw)
                request.session['u_id'] = u2.id
            else:
                try:
                    u2 = User.objects.get(user_phone=name, user_password=pw)
                    request.session['u_id'] = u2.id
                except:
                    return redirect('login')
            return redirect('index')
        else:
            print(f.errors.get_json_data())
            return redirect('register')


# 是否注册人脸
class IsFace(views.View):
    def get(self,request):
        return render(request, 'first/is_face.html')
    def post(self,request):
        answer=request.POST.get("button")
        if answer=="是":
            return render(request,'first/face_register.html')
        else:
            return redirect('login')


# 人脸注册
class Faceregister(views.View):

    def get(self,request):
        return render(request,'first/face_register.html')

    def post(self,request):
        uid = request.session.get('uid')
        u3 = User.objects.get(id=uid)
        img = request.POST.get('face_l')
        face = Registerss(img=img)
        face.face_register(group_id=1,user_id=u3.id)
        return redirect('login')


# 【人脸登录】
class FaceLogin(views.View):
    def get(self,request):
        return render(request,'first/face_login.html')
    def post(self,request):
        img=request.POST.get("face_l")
        face = Search(img=img)
        r=face.get_search(group_id_list="1,2,3,4")

        if r['error_code']==0:
            if r['result']['user_list'][0]['score']<=80:
                print("面部检测不成功，登录失败")
                return redirect('login')
            else:
                try:
                    user_id=r['result']['user_list'][0]['user_id']
                    u2=User.objects.get(id=user_id)
                    request.session['u_id'] = u2.id
                    return redirect('index')
                except:
                    return redirect('login')
        else:
            return redirect('login')


# 退出登录
def exit_login(request):
    request.session.flush()
    return redirect('index')


# 首页
def index(request):
    u_id = request.session.get("u_id")
    if u_id:
        try:
            u=User.objects.get(id=u_id)
            shop_number=Shoppings.objects.filter(user_id=u.id).count()
            return render(request,'first/index.html',{"u":u,'u_id':u_id,"number":shop_number})
        except:
            return render(request,'first/index.html')
    else:
        return render(request,'first/index.html')


# 商品页面
def weding_detail(request):
    u_id = request.session.get("u_id")
    imgs_dict = {}
    all_info = AllDiamonds.objects.all()[:12]
    all_img = cursor.execute('''select good_img from all_diamonds''')
    imgs = cursor.fetchall()[:12]
    url_list = []
    for i in imgs:
        img = eval(i[0])[0]
        img2 = eval(i[0])[1]
        imgs_dict[img] = img2
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/weding_detail.html', {"all_info": all_info, "imgs_dict": imgs_dict,'urls':url_list,"u_id":u_id,"u":u,'number':shop_number})
    else:
        return render(request, 'first/weding_detail.html',{"all_info": all_info, "imgs_dict": imgs_dict, 'urls': url_list})


# 商品页面二
def weding_detail_page2(request):
    u_id = request.session.get("u_id")
    imgs_dict = {}
    all_info = AllDiamonds.objects.all()[12:24]
    all_img = cursor.execute('''select good_img from all_diamonds''')
    imgs = cursor.fetchall()[12:24]
    url_list = []
    for i in imgs:
        img = eval(i[0])[0]
        img2 = eval(i[0])[1]
        imgs_dict[img] = img2
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/weding_detail.html', {"all_info": all_info, "imgs_dict": imgs_dict,'urls':url_list,"u_id":u_id,"u":u,'number':shop_number})
    else:
        return render(request, 'first/weding_detail.html',{"all_info": all_info, "imgs_dict": imgs_dict, 'urls': url_list})


# 商品页面三
def weding_detail_page3(request):
    u_id = request.session.get("u_id")
    imgs_dict = {}
    all_info = AllDiamonds.objects.all()[24:36]
    all_img = cursor.execute('''select good_img from all_diamonds''')
    imgs = cursor.fetchall()[24:36]
    url_list = []
    for i in imgs:
        img = eval(i[0])[0]
        img2 = eval(i[0])[1]
        imgs_dict[img] = img2
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/weding_detail.html', {"all_info": all_info, "imgs_dict": imgs_dict,'urls':url_list,"u_id":u_id,"u":u,'number':shop_number})
    else:
        return render(request, 'first/weding_detail.html',{"all_info": all_info, "imgs_dict": imgs_dict, 'urls': url_list})


# 商品页面四
def weding_detail_page4(request):
    u_id = request.session.get("u_id")
    imgs_dict = {}
    all_info = AllDiamonds.objects.all()[36:48]
    all_img = cursor.execute('''select good_img from all_diamonds''')
    imgs = cursor.fetchall()[36:48]
    url_list = []
    for i in imgs:
        img = eval(i[0])[0]
        img2 = eval(i[0])[1]
        imgs_dict[img] = img2
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/weding_detail.html', {"all_info": all_info, "imgs_dict": imgs_dict,'urls':url_list,"u_id":u_id,"u":u,'number':shop_number})
    else:
        return render(request, 'first/weding_detail.html',{"all_info": all_info, "imgs_dict": imgs_dict, 'urls': url_list})


# 商品页面五
def weding_detail_page5(request):
    u_id = request.session.get("u_id")
    imgs_dict = {}
    all_info = AllDiamonds.objects.all()[48:60]
    all_img = cursor.execute('''select good_img from all_diamonds''')
    imgs = cursor.fetchall()[48:60]
    url_list = []
    for i in imgs:
        img = eval(i[0])[0]
        img2 = eval(i[0])[1]
        imgs_dict[img] = img2
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/weding_detail.html', {"all_info": all_info, "imgs_dict": imgs_dict,'urls':url_list,"u_id":u_id,"u":u,'number':shop_number})
    else:
        return render(request, 'first/weding_detail.html',{"all_info": all_info, "imgs_dict": imgs_dict, 'urls': url_list})


# 商品页面六
def weding_detail_page6(request):
    u_id = request.session.get("u_id")
    imgs_dict = {}
    all_info = AllDiamonds.objects.all()[60:72]
    all_img = cursor.execute('''select good_img from all_diamonds''')
    imgs = cursor.fetchall()[60:72]
    url_list = []
    for i in imgs:
        img = eval(i[0])[0]
        img2 = eval(i[0])[1]
        imgs_dict[img] = img2
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/weding_detail.html', {"all_info": all_info, "imgs_dict": imgs_dict,'urls':url_list,"u_id":u_id,"u":u,'number':shop_number})
    else:
        return render(request, 'first/weding_detail.html',{"all_info": all_info, "imgs_dict": imgs_dict, 'urls': url_list})


# 商品页面七
def weding_detail_page7(request):
    u_id = request.session.get("u_id")
    imgs_dict = {}
    all_info = AllDiamonds.objects.all()[72:84]
    all_img = cursor.execute('''select good_img from all_diamonds''')
    imgs = cursor.fetchall()[72:84]
    url_list = []
    for i in imgs:
        img = eval(i[0])[0]
        img2 = eval(i[0])[1]
        imgs_dict[img] = img2
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/weding_detail.html', {"all_info": all_info, "imgs_dict": imgs_dict,'urls':url_list,"u_id":u_id,"u":u,'number':shop_number})
    else:
        return render(request, 'first/weding_detail.html',{"all_info": all_info, "imgs_dict": imgs_dict, 'urls': url_list})


# 商品页面八
def weding_detail_page8(request):
    u_id = request.session.get("u_id")

    imgs_dict = {}
    all_info = AllDiamonds.objects.all()[84:96]
    all_img = cursor.execute('''select good_img from all_diamonds''')
    imgs = cursor.fetchall()[84:96]
    url_list = []
    for i in imgs:
        img = eval(i[0])[0]
        img2 = eval(i[0])[1]
        imgs_dict[img] = img2
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/weding_detail.html', {"all_info": all_info, "imgs_dict": imgs_dict,'urls':url_list,"u_id":u_id,"u":u,'number':shop_number})
    else:
        return render(request, 'first/weding_detail.html',{"all_info": all_info, "imgs_dict": imgs_dict, 'urls': url_list})


# 商品页面九
def weding_detail_page9(request):
    u_id = request.session.get("u_id")
    imgs_dict = {}
    all_info = AllDiamonds.objects.all()[96:108]
    all_img = cursor.execute('''select good_img from all_diamonds''')
    imgs = cursor.fetchall()[96:108]
    url_list = []
    for i in imgs:
        img = eval(i[0])[0]
        img2 = eval(i[0])[1]
        imgs_dict[img] = img2
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/weding_detail.html', {"all_info": all_info, "imgs_dict": imgs_dict,'urls':url_list,"u_id":u_id,"u":u,'number':shop_number})
    else:
        return render(request, 'first/weding_detail.html',{"all_info": all_info, "imgs_dict": imgs_dict, 'urls': url_list})


# 商品详情页面
def shop_detail(request,good_id):
    u_id = request.session.get("u_id")
    good = AllDiamonds.objects.get(id=good_id)
    print(good_id)
    img = eval(good.good_img)[0]
    detail_img = eval(good.detail_img)
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request,'first/shop_detail.html',{"good":good,"img":img,"detail_img":detail_img,"u_id":u_id,"u":u,"number":shop_number})
    else:
        return render(request, 'first/shop_detail.html',{"good": good, "img": img, "detail_img": detail_img})


# 填入购物车
def insert_good(request,shop_id):
    u_id = request.session.get("u_id")
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        shop=AllDiamonds.objects.get(id=shop_id)
        Shoppings.objects.get_or_create(good_id=shop.id,good_name=shop.good_name,main_diamond=shop.main_diamond,assitant_diamond=shop.assitant_diamond,good_size=shop.good_size,good_number=1,first_price=shop.good_price,good_price=shop.good_price,user_id=u_id)
        return redirect('my_shops2')
    else:
        return redirect('login')


# 购物车（处于空状态显示的页面）
def my_shops(request):
    u_id = request.session.get("u_id")
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request,'first/my_shops.html',{"u":u,"u_id":u_id,"number":shop_number})
    else:
        return render(request,'first/my_shops.html')


# 购物车（处于未登陆状态显示的页面）
def my_shops3(request):
    u_id = request.session.get("u_id")
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        return render(request, 'first/my_shops3.html', {"u": u, "u_id": u_id,"number":shop_number})
    else:
        return render(request, 'first/my_shops3.html')


# 购物车（处于有商品状态）
def my_shops2(request):
    u_id = request.session.get("u_id")
    if u_id:
        imgs_list = []
        id_list=[]
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        all_shops=Shoppings.objects.filter(user_id=u.id)
        all_price = Shoppings.objects.filter(user_id=u.id).aggregate(sum=Sum('good_price'))
        for shop in all_shops:
            id_list.append(shop.good_id)
        if len(id_list) == 0:
            return redirect('my_shops3')
        elif len(id_list) ==1:
            all_img = cursor1.execute('select good_img from all_diamonds where id in (%s)'%id_list[0])
        elif len(id_list) > 1:
            all_img = cursor1.execute('''select good_img from all_diamonds where id in {}'''.format(tuple(id_list)))
        imgs = cursor1.fetchall()
        for i in imgs:
            img = eval(i[0])[0]
            imgs_list.append(img)
        return render(request,'first/my_shops2.html',{"all_shops":all_shops,"u_id":u_id,"u":u,"imgs_list":imgs_list,"number":shop_number,'all_price':all_price['sum']})

    else:
        return redirect('my_shops')


# 清空购物车
def clear(request):
    Shoppings.objects.all().delete()
    u_id = request.session.get("u_id")
    u = User.objects.get(id=u_id)
    return render(request,'first/my_shops3.html',{'u_id':u_id,'u':u})

def delete_one(request,one_id):
    if Shoppings.objects.all().count()>1:
        Shoppings.objects.get(id=one_id).delete()
        return redirect('my_shops2')
    elif Shoppings.objects.all().count() == 1:
        Shoppings.objects.get(id=one_id).delete()
        return redirect('my_shops3')


# 搜索商品实现翻页
def skip_page(request,everypage=None):
    u_id = request.session.get("u_id")
    try:
        keyword = request.POST.get("find")

        if AllDiamonds.objects.filter(good_name__contains=keyword).exists()or AllDiamonds.objects.filter(type_name__contains=keyword).exists() or AllDiamonds.objects.filter(material__contains=keyword).exists() or AllDiamonds.objects.filter(belong_name__contains=keyword).exists():
            img_list=[]
            page_list=[]
            if AllDiamonds.objects.filter(good_name__contains=keyword).exists():
                goods=AllDiamonds.objects.filter(good_name__contains=keyword)
            elif AllDiamonds.objects.filter(type_name__contains=keyword).exists():
                goods=AllDiamonds.objects.filter(type_name__contains=keyword)
            elif AllDiamonds.objects.filter(material__contains=keyword).exists():
                goods=AllDiamonds.objects.filter(material__contains=keyword)
            elif AllDiamonds.objects.filter(belong_name__contains=keyword).exists():
                goods=AllDiamonds.objects.filter(belong_name__contains=keyword)
            count=goods.count()
            count1 = count - ((everypage - 1) * 12)
            if count1 <= 12:
                goods = goods[:count1]
            else:
                goods = goods[count1 - 12:count - ((everypage - 1) * 12)]
            page = count // 12
            if page == 0 or page==1:
                page_list = [1]
            elif page > 1:
                for i in range(1, page + 1):
                    page_list.append(i)
            else:
                pass
            for good in goods:
                good_img = eval(good.good_img)[0]
                img_list.append(good_img)
            if u_id:
                u = User.objects.get(id=u_id)
                shop_number = Shoppings.objects.filter(user_id=u.id).count()
                return render(request, 'first/select_diamonds.html',{"goods": goods, "img_list": img_list, "page_list": page_list,"keyword":keyword,"u":u,"u_id":u_id,'page':page,'count':count,'number':shop_number})
            else:
                return render(request, 'first/select_diamonds.html',{"goods": goods, "img_list": img_list, "page_list": page_list, "keyword": keyword,'page':page,'count':count})
        else:
            return redirect('index')
    except:
        return redirect('index')


# 搜索商品
def skip_goods(request,keyword,everypage):
    u_id = request.session.get("u_id")
    img_list = []
    page_list = []
    if AllDiamonds.objects.filter(good_name__contains=keyword).exists()or AllDiamonds.objects.filter(type_name__contains=keyword).exists() or AllDiamonds.objects.filter(material__contains=keyword).exists() or AllDiamonds.objects.filter(belong_name__contains=keyword).exists():

        if AllDiamonds.objects.filter(good_name__contains=keyword).exists():
            goods=AllDiamonds.objects.filter(good_name__contains=keyword)
        elif AllDiamonds.objects.filter(type_name__contains=keyword).exists():
            goods=AllDiamonds.objects.filter(type_name__contains=keyword)
        elif AllDiamonds.objects.filter(material__contains=keyword).exists():
            goods=AllDiamonds.objects.filter(material__contains=keyword)
        elif AllDiamonds.objects.filter(belong_name__contains=keyword).exists():
            goods=AllDiamonds.objects.filter(belong_name__contains=keyword)
        count=goods.count()
        count1 = count - ((everypage - 1) * 12)
        if count1<=12:
            goods=goods[:count1]
        else:
            goods = goods[count1 - 12:count - ((everypage - 1) * 12)]
        page = count // 12
        if page == 0 or page == 1:
            page_list=[1]
        elif page > 1:
            for i in range(1, page + 1):
                page_list.append(i)
        for good in goods:
            good_img = eval(good.good_img)[0]
            img_list.append(good_img)
        if u_id:
            u = User.objects.get(id=u_id)
            return render(request, 'first/select_diamonds.html', {"goods": goods, "img_list": img_list,"page_list":page_list,"keyword":keyword,"u":u,"u_id":u_id,"page":page,'count':count})
        else:
            return render(request, 'first/select_diamonds.html',{"goods": goods, "img_list": img_list, "page_list": page_list, "keyword": keyword,'page':page,'count':count})
    else:
        return redirect('index')


# 填写订单页面
def fill_form(request):
    return render(request,'first/fill_form.html')


# 购物车商品数量设置（减少）
def reduce(request,p_id):
    u_id = request.session.get("u_id")
    if u_id:
        imgs_list = []
        id_list = []
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        shops = Shoppings.objects.get(id=p_id)
        first_price = shops.first_price
        shop_num = shops.good_number
        shop_num -= 1
        cursor.execute('update shoppings set good_number={} where id ={}'.format(shop_num, p_id))
        conn.commit()
        shops.good_price -= first_price
        cursor.execute('update shoppings set good_price={} where id={}'.format(shops.good_price, p_id))
        conn.commit()
        all_shops = Shoppings.objects.filter(user_id=u.id)
        all_price = Shoppings.objects.filter(user_id=u.id).aggregate(sum=Sum('good_price'))
        for shop in all_shops:
            id_list.append(shop.good_id)
        if len(id_list) ==0:
            return redirect('my_shops3')
        elif len(id_list) == 1:
            all_img = cursor1.execute('select good_img from all_diamonds where id in (%s)' % id_list[0])
        elif len(id_list) >1:
            all_img = cursor1.execute('''select good_img from all_diamonds where id in {}'''.format(tuple(id_list)))
        imgs = cursor1.fetchall()
        for i in imgs:
            img = eval(i[0])[0]
            imgs_list.append(img)
        return render(request, 'first/my_shops2.html',
                          {"all_shops": all_shops, "u_id": u_id, "u": u, "imgs_list": imgs_list, "number": shop_number,
                           'all_price': all_price['sum'], 'num': shop_num})
    else:
        return redirect('my_shops')


# 购物车商品数量设置（增加）
def puls(request,p_id):
    u_id = request.session.get("u_id")
    if u_id:
        imgs_list = []
        id_list = []
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        shops = Shoppings.objects.get(id=p_id)
        first_price = shops.first_price
        shop_num = shops.good_number
        shop_num += 1
        cursor.execute('update shoppings set good_number={} where id ={}'.format(shop_num,p_id))
        conn.commit()
        shops.good_price += int(first_price)
        cursor.execute('update shoppings set good_price={} where id={}'.format(shops.good_price,p_id))
        conn.commit()
        all_shops = Shoppings.objects.filter(user_id=u.id)
        all_price = Shoppings.objects.filter(user_id=u.id).aggregate(sum=Sum('good_price'))
        for shop in all_shops:
            id_list.append(shop.good_id)
        if len(id_list) ==0:
            return redirect('my_shops3')
        elif len(id_list) ==1:
            all_img = cursor1.execute('select good_img from all_diamonds where id in (%s)' % id_list[0])
        elif len(id_list) >1:
            all_img = cursor1.execute('''select good_img from all_diamonds where id in {}'''.format(tuple(id_list)))
        imgs = cursor1.fetchall()
        for i in imgs:
            img = eval(i[0])[0]
            imgs_list.append(img)
        return render(request, 'first/my_shops2.html',{"all_shops": all_shops, "u_id": u_id, "u": u, "imgs_list": imgs_list, "number": shop_number,'all_price': all_price['sum'],'num':shop_num})
    else:
        return redirect('my_shops')


# 填写订单页面
def info_id(request):
    sum_price = 0
    imgs_list = []
    id_list = []
    u_id = request.session.get("u_id")
    u = User.objects.get(id=u_id)
    all_info = []
    res = request.POST.getlist('box')
    shop_number = Shoppings.objects.filter(user_id=u.id).count()
    for i in res:
        shopss = Shoppings.objects.get(id=i)
        all_info.append(shopss)
        id_list.append(shopss.good_id)
        dan_price = shopss.good_price
        sum_price += dan_price
    if len(id_list)==0:
        return redirect('my_shops3')
    elif len(id_list)==1:
        all_img = cursor1.execute('''select good_img from all_diamonds where id in(%s)'''%id_list[0])
    elif len(id_list)>0:
        all_img = cursor1.execute('''select good_img from all_diamonds where id in {}'''.format(tuple(id_list)))
    imgs = cursor1.fetchall()
    for i in imgs:
        img = eval(i[0])[0]
        imgs_list.append(img)
    return render(request, 'first/fill_form.html',{'res': res, 'all_info': all_info, "u_id": u_id, "u": u, "imgs_list": imgs_list,'sum_price':sum_price,'number':shop_number})


# 将订单填入数据库
def insert_order(request,res):
    u_id = request.session.get("u_id")
    u = User.objects.get(id=u_id)
    try:
        sender_name = request.POST.get("sender_name")
        sender_phone = request.POST.get("sender_phone")
        sender_address1 = request.POST.get("sender_address1")
        sender_address2 = request.POST.get("sender_address2")
        sender_address3 = request.POST.get("sender_address3")

        sender_post = request.POST.get("sender_post")
        sender_postcode = request.POST.get("sender_postcode")

        receiver_name = request.POST.get("receiver_name")
        receiver_phone = request.POST.get("receiver_phone")
        receiver_address1 = request.POST.get("receiver_address1")
        receiver_address2 = request.POST.get("receiver_address2")
        receiver_address3 = request.POST.get("receiver_address3")
        print(receiver_address1)
        receiver_postcode = request.POST.get("receiver_postcode")
        id_list=[]
        for ids in eval(res):
            id_list.append(ids)
        for i in id_list:
            shopping=Shoppings.objects.get(id=i)
            orders=OrderForms.objects.create(sender_name=sender_name,sender_phone=sender_phone,sender_address=sender_address1,sender_post=sender_post,sender_postcode=sender_postcode,receiver_name=receiver_name,receiver_phone=receiver_phone,receiver_address=receiver_address1,receiver_postcode=receiver_postcode,shop_id=shopping.good_id,user_id=u_id)
            shopping.delete()
        return redirect('orders')
    except:
        return redirect('my_shops2')


# 显示订单页面
def ordering(request):
    u_id = request.session.get("u_id")
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        id_list = []
        if OrderForms.objects.filter(user_id=u.id).exists():
            ordersss=OrderForms.objects.filter(user_id=u.id)
            print(ordersss)
            for order in ordersss:
                id_list.append(order.shop_id)
            orders = AllDiamonds.objects.filter(id__in=id_list)
            return render(request,'first/order_form1.html',{"orders":orders,"u_id":u_id,"u":u,'number':shop_number})
        else:
            return render(request,'first/order_form.html',{"u_id":u_id,"u":u,'number':shop_number})
    else:
        return redirect('login')


# 订单页面（无订单状态）
def order_from(request):
    u_id = request.session.get("u_id")
    u = User.objects.get(id=u_id)
    shop_number = Shoppings.objects.filter(user_id=u.id).count()
    return render(request, 'first/order_form.html', {'u_id': u_id, 'u': u, 'number': shop_number})


# 订单页面（有订单状态）
def order_from1(request):
    u_id = request.session.get("u_id")
    u = User.objects.get(id=u_id)
    shop_number = Shoppings.objects.filter(user_id=u.id).count()
    return render(request,'first/order_form1.html',{'u_id':u_id,'u':u,'number':shop_number})


# 删除订单
def delete_order(request,d_id):
    OrderForms.objects.get(shop_id=d_id).delete()
    u_id = request.session.get("u_id")
    if u_id:
        u = User.objects.get(id=u_id)
        shop_number = Shoppings.objects.filter(user_id=u.id).count()
        id_list = []
        if OrderForms.objects.filter(user_id=u.id).exists():
            ordersss = OrderForms.objects.filter(user_id=u.id)
            print(ordersss)
            for order in ordersss:
                id_list.append(order.shop_id)
            orders = AllDiamonds.objects.filter(id__in=id_list)
            return render(request, 'first/order_form1.html',
                          {"orders": orders, "u_id": u_id, "u": u, 'number': shop_number})
        else:
            return render(request, 'first/order_form.html',{ "u_id": u_id, "u": u, 'number': shop_number})





