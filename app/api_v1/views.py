from sanic import json
from . import api_bp
from app.api_v1.models import EmployeeInfo
from playhouse.shortcuts import model_to_dict


@api_bp.route('/info')
async def employee_info(request):
    per_page_num = request.app.config['MAX_PER_PAGE']
    page = int(request.args.get('page', 1))
    word = request.args.get('q')

    if not word:
        q = EmployeeInfo.filters(page=page, per_page_num=per_page_num)
    elif word.isdigit():
        q = EmployeeInfo.filters(employee_id=word, page=page, per_page_num=per_page_num)
    else:
        q = EmployeeInfo.filters(name=word, per_page_num=per_page_num)

    results = [model_to_dict(row) for row in q.iterator()]
    total = EmployeeInfo.total()

    return json(
        {
            'results': results,
            'pageSize': per_page_num,
            'page': page,
            'total': total
        }
        , ensure_ascii=False)
