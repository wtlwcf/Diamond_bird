import base64,json,requests

class AccessToken:
    def __init__(self,ak,sk,img=None,img_path=None):
        self.ak=ak
        self.sk=sk

        r = requests.post('https://aip.baidubce.com/oauth/2.0/token'
                          '?'
                          'grant_type=client_credentials'
                          '&'
                          'client_id=%s'
                          '&'
                          'client_secret=%s'%(ak,sk))

        self.access_token = r.json().get("access_token")
#
#
        #img!=None:上传了一张拍照的照片，已经经过base64编码
        if img!=None:
            self.img=img[23:]

        #img_path!=None：上传了一个文件照片，文件的存储路径
        if img_path!=None:
            f=open(img_path,"rb")
            self.img=base64.b64encode(f.read())


class FaceRegister(AccessToken):
    # 人脸注册
    def face_register(self,user_id):
        url = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add?access_token=%s' % (self.access_token)

        header = {'Content-Type': 'application/json'}
        body = {
            'image': self.img,
            'image_type': 'BASE64',
            'group_id':1,
            'user_id': user_id
        }
        r = requests.post(url=url, headers=header, data=body)

        return r.json()


class Face(AccessToken):
    # 人脸搜索
    def face_search(self,group_id_list):
        url = 'https://aip.baidubce.com/rest/2.0/face/v3/search?access_token=%s' % (self.access_token)
        header = {"Content-Type": "application/json"}
        body = {
            'image': self.img,
            'image_type': 'BASE64',
            'group_id_list': group_id_list,
        }
        r = requests.post(url=url, headers=header, data=body)

        return r.json()

