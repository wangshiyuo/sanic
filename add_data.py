from app.api_v1.models import EmployeeInfo, db
import random


def add_data():
    data_list = [
        {'id': random.randint(10000, 99999), 'name': '李园园', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 50000},
        {'id': random.randint(10000, 99999), 'name': '黄俊才', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 20000},
        {'id': random.randint(10000, 99999), 'name': '赵小莽', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 8000},
        {'id': random.randint(10000, 99999), 'name': '李大牛', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 12000},
        {'id': random.randint(10000, 99999), 'name': '王二小', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 7000},
        {'id': random.randint(10000, 99999), 'name': '陈从周', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '周其仁', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '蒋孝慈', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '王拱辰', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '陈省身', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '陈是知', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '张纯如', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '陈毅', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '于凤至', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '王尽美', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '李宗仁', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '孙立人', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '陈友谅', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '柳永', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '张若虚', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000},
        {'id': random.randint(10000, 99999), 'name': '萧炎', 'position': '销售', 'telephonenumber': random.randint(13000000000, 19000000000), 'salary': 5000}
    ]

    EmployeeInfo.insert_many(data_list).execute()
    print('导入职员数据成功！')


if __name__ == '__main__':
    add_data()
