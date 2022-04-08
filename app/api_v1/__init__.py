from sanic import Blueprint


api_bp = Blueprint('api_bp_v1', url_prefix='/api/v1')


from .views import employee_info