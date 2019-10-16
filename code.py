"""用于调动各模块的主函数。

"""
from codemanageII.RandomCode import InputManage


class main_cotrol():
    """尝试用于调用各模块"""
    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        pass

    def __call__(self):
        #实例化循环执行
        while True:
            #获得输入
            print('密码 . \n添加1(查询0) .\n加入符号1(默认为0) . \n密码位数(默认为12) . \n用户名与备注')
            middle_link = input('\n请输入密码+指令 : ')
            #退出条件

            middle_object = InputManage(str(middle_link))
            pass_code = middle_object.DealInput()
            print('\n')
            print('--'*20)
            continue_flag = input('输入c继续操作，输入其他字符退出 : ')
            print('\n')
            if continue_flag != 'c':
                break


if __name__ == "__main__":
    user = main_cotrol()
    user()


