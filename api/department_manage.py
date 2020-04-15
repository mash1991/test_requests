import requests
from api.wework import WeWork

class DepartmentManege(WeWork):
    #部门管理
    secret = "ATvrnjJTv6Qu3zqUSDLXUJzmsPSBT_lHHd8pW68SVUs"

    #创建部门
    def create(self,name,parentid,**kwargs):
        data = {"name":name,"parentid":parentid}
        data.update(kwargs)
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        r = requests.post(
            url,
            params={'access_token':self.get_token(self.secret)},
            json=data
        )
        self.format(r)
        return r.json()

    #更新部门
    def update(self,id,**kwargs):
        data = {"id":id}
        data.update(kwargs)
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        r = requests.post(
            url,
            params={'access_token': self.get_token(self.secret)},
            json=data
        )
        self.format(r)
        return r.json()

    #删除部门
    def delete(self,id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        params = {'access_token': self.get_token(self.secret),"id":id}
        r = requests.get(url,params=params)
        self.format(r)
        return r.json()

    #获取部门列表
    def list(self,id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        params = {'access_token': self.get_token(self.secret), "id": id}
        r = requests.get(url, params=params)
        self.format(r)
        return r.json()