
import random
# 将测试数据以字典的形式存放在列表中
login_data_success = [
    {'username': 'yyhtest', 'pwd': '123456789', 'expected': '欢迎，小袁'},
]

organization_data_info = [
    {'main_menu':2, 'module_menu':1, 'organization_name': '测试' + str(random.randint(1,99999999)), 'province_num': '3','city_num':'1','contact_person': '测试',
     'phone_number':'13212121212','status_num':'2',}
]
