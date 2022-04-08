from peewee import Model, MySQLDatabase, SqliteDatabase, CharField, AutoField, IntegerField, DatabaseProxy
from sanic import Sanic
from app import config

# Create a proxy for our db.
db = DatabaseProxy()


# Use proxy for our DB.
class BaseModel(Model):
    class Meta:
        database = db


class EmployeeInfo(BaseModel):
    class Meta:
        table_name = 'employee_table'

    id = IntegerField(null=False, primary_key=True)
    name = CharField(null=False)
    position = CharField()
    telephonenumber = CharField()
    salary = IntegerField()

    @classmethod
    def filters(cls, employee_id=None, name=None, page=1, per_page_num=10):
        """
        通过员工编号或者姓名查询信息
        默认返回第一页数据，每页最多10条记录
        """
        if not employee_id and not name:
            q = cls.select()
        elif employee_id:
            q = cls.select().where(cls.id.contains(employee_id)).order_by(cls.id)
        else:
            q = cls.select().where(cls.name.contains(name)).order_by(cls.id)

        cls.result = q.paginate(page, per_page_num)
        cls.num_records = q.count()
        return cls.result

    @classmethod
    def total(cls):
        return cls.num_records


if config.DEBUG:
    database = SqliteDatabase('local.db')
elif config.TESTING:
    database = SqliteDatabase(':memory:')
else:
    database = MySQLDatabase('info_db')

db.initialize(database)
