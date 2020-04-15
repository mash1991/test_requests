from api.department_manage import DepartmentManege

class TestDepartmentManage:

    @classmethod
    def setup_class(cls):
        cls.department = DepartmentManege()

    #测试创建部门
    def test_department_create(self):
        r = self.department.create(name="研发一部",parentid=1)
        assert r["errcode"] == 0

    #测试更新部门
    def test_department_update(self):
        r = self.department.update(id=2,name="研发总部")
        assert r["errcode"] == 0

    #测试删除部门
    def test_department_delete(self):
        r = self.department.delete(id=2)
        assert r["errcode"] == 0

    #测试获取部门列表
    def test_department_list(self):
        r = self.department.list(id=1)
        assert r["errcode"] == 0