import requests,base64, json
class AccessToken:
    def __init__(self, ak='DWSK1htCSbLa1hdlXj8m7Lup', sk='QnxBk75l5N3WR3gFwZApj4wD5e2eyZWK', img=None, img_path=None):
        self.ak = ak
        self.sk = sk
        r = requests.post('https://aip.baidubce.com/oauth/2.0/token'
                          '?'
                          'grant_type=client_credentials'
                          '&'
                          'client_id=%s'
                          '&'
                          'client_secret=%s' % (ak, sk))
        self.access_token = r.json().get('access_token')
        if img != None:
            self.img = img[23:]
        if img_path != None:
            f = open(img_path,'rb')
            self.img = base64.b64encode(f.read())



# class Face_Register(AccessToken):
#     def get_register(self, group_id, user_id,info):
#         url = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add?access_token=%s' % self.access_token
#         header = {'Content-Type': 'application/json'}
#         dic = {
#             '姓名': '%s' % info[0],
#             '密码': '%s' % info[1],
#             '性别': '%s' % info[2],
#
#
#         }
#         dic = json.dumps(dic)
#         Body = {
#             'image': self.img,
#             'group_id': group_id,
#             'user_id': user_id,
#             'image_type': 'BASE64',
#             'user_info':dic
#         }
#         Body=json.dumps(Body)
#         r = requests.post(url=url, headers=header, data=Body)
#         return r.json()
class Registerss(AccessToken):

    def face_register(self,group_id,user_id):

        url = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add?access_token=%s' % self.access_token
        header = {
            "Content-Type": "application/json"
        }
        # dic = {
        #         "姓名": "%s"%info[0],
        #         "性别": "%s"%info[1],
        #         "年龄": "%s"%info[2],
        #         "密码": "%s"%info[3],
        #     }
        # dic = json.dumps(dic)
        # print(dic)
        body = {
            "image": self.img,
            "group_id": group_id,
            "user_id": user_id,
            # "user_info": dic,
            "image_type": "BASE64",
        }
        body=json.dumps(body)
        r = requests.post(url=url, headers=header, data=body)
        return r.json()

class Search(AccessToken):
    def get_search(self, group_id_list):
        url = 'https://aip.baidubce.com/rest/2.0/face/v3/search?access_token=%s' % self.access_token
        header = {'Content-Type': 'application/json'}
        Body = {'image': self.img,
                'group_id_list': group_id_list,
                'image_type': 'BASE64',
                }
        r = requests.post(url=url, headers=header, data=Body)
        return r.json()

class Live(AccessToken):
    def face_live(self,img_list):
        url = 'https://aip.baidubce.com/rest/2.0/face/v3/faceverify?access_token=%s' % self.access_token
        header = {'Content-Type': 'application/json'}
        body = []
        for img in img_list:
            img_dic = {}
            img_dic['image'] = str(img[23:])
            img_dic['image_type'] = 'BASE64'
            body.append(img_dic)
        a = json.dumps(body)
        r = requests.post(url=url, headers=header, data=a)
        return r.json()

class Live1(AccessToken):
    def face_live(self,img_list):
        url = 'https://aip.baidubce.com/rest/2.0/face/v3/faceverify?access_token=%s' % self.access_token
        header = {'Content-Type': 'application/json'}
        body = []
        for img_path in img_list:
            f = open(img_path, 'rb')
            imgs = base64.b64encode(f.read())
            img_dic = {}
            img_dic['image'] = str(imgs, "utf-8")
            img_dic['image_type'] = 'BASE64'
            body.append(img_dic)
        a = json.dumps(body)
        r = requests.post(url=url, headers=header, data=a)
        return r.json()











