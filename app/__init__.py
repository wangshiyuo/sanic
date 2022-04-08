from sanic import Sanic, response
from . import config
from sanic.exceptions import NotFound
from .api_v1 import api_bp
from sanic_cors import CORS


# 注册app
app = Sanic('employee')

# 跨域
CORS(app, automatic_options=True)

# 注册api蓝图
app.blueprint(api_bp)

# 导入配置文件
app.config.update_config(config)



# 处理404
@app.exception(NotFound)
async def ignore_404s(request, exception):
    return response.text("404. Oops, That page couldn't found.")


# 根路由指向主页文件
@app.route('/')
async def handle_request(request):
    return await response.file('app/frontend/index.html')


from app.api_v1.models import EmployeeInfo, db

db.create_tables([EmployeeInfo], safe=True)
