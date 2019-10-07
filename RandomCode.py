"""本文档为主函数，用于调用及交互等功能。

1、密码管理器访问权限
2、根据用户输入调用相关功能

"""

import random


class InputManage():
    """用于生成与管理输入输出"""
    
    def __init__(self,middle_linked):
        self.middle_linked = middle_linked

    def DealInput(self):
        #使用split分割输入
        command_list = self.middle_linked.split('.',1)
        #调用方法处理
        pass_permit = self.is_user(command_list[0])
        if pass_permit == 1 and command_list[1] !=0:
            pass_word = self.add_symbol()
            return pass_word

        elif pass_permit == 1 :
            pass
        
        else: 
            print('password error')
            return 0
            

    def is_user(self,password):
        #验证密码，正确返回1
        if password == 'aaa':
            return 1
        else: return 0

    def add_symbol(self):
        #随机加入符号
        symbol_list = ['#','$','!','@','*','*']
        pass_code = 'co'
        while len(pass_code) < 12:
            num_1 = random.randrange(1, 30, 1)
            num_2 = random.randrange(1, 30, 1)
            nums_all = num_1*num_2

            symbol_choice = random.choice(symbol_list)
            pass_code = pass_code + str(nums_all) + symbol_choice
        
        return pass_code

if __name__ == "__main__":
    
    print('1、请输入密码\n')
    print('2、是否加入符号\n')
    # print('如果需要')
    
    #实例化循环执行
    while True:
        #获得输入
        middle_link = input('请输入指令')
        middle_object = InputManage(str(middle_link))
        pass_code = middle_object.DealInput()
        #判断，执行成功则输出
        if pass_code !=0:
            print(pass_code)
            break

