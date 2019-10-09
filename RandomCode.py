"""本文档为主函数，用于调用及交互等功能。

1、密码管理器访问权限。is_user
2、根据用户输入调用相关功能。DealInput
3、生成对应密码。code_birth

"""

import random
import string
import pyperclip
from codebases import Databases_deal


class InputManage():
    """用于生成与管理输入输出"""
    
    def __init__(self,middle_linked):
        self.middle_linked = middle_linked
        #实例化数据库类
        self.base_deal = Databases_deal()

    def DealInput(self):
        #使用split分割输入
        command_list = self.middle_linked.split('.',3)
        print(command_list)
        #调用方法处理
        #验证密码正确与否，正确pass_permit返回1
        pass_permit = self.is_user(command_list[0])
        # try:
        if pass_permit == 1 and command_list[1] == '1':
            try:
                pass_word = self.code_birth(command_list[2],command_list[3])
                return pass_word
            except IndexError: 
                pass_word = self.code_birth()
    

        elif pass_permit == 1 and command_list[1] == '0':
            self.code_search()
        
        else: 
            print('password error')
            return 0
        # except:
        #     print('命令输入错误，请重新输入')
            

    def is_user(self,password):
        #验证密码，正确返回1
        #排出干扰项，查询序列中是否存在此密码
        if 'aaa' in password:
            return 1
        else: return 0

    def code_birth(self,symbol_flag='0',code_nums=12):
        #密码生成
        #0表示只有数字和字母，1表示包括符号
        code_pertain = input('添加 ：输入密码归属或网址 :')
        code_chdict = {
            '0' : string.ascii_letters + string.digits,
            '1' : string.printable[:-6],
        }
        birth_word = ''
        #根据输入选择
        for i in range(1,int(code_nums)+1):
            #根据是否加入symbol，选择密码字典，再随机选择
            birth_word += random.choice(code_chdict[symbol_flag])
        
        self.base_deal.code_save(birth_word,code_pertain)
        print('%s : %s'%(code_pertain,birth_word))
        return birth_word


    def code_search(self):
        #密码查询
        search_peitain = input('查询 ：输入密码归属 :')

        usetuple = self.base_deal.code_bringout(search_peitain)
        if usetuple:
            print(' %s : %s'%(usetuple[0].decode(),usetuple[1].decode()))
        else:
            print('无法查询到对应密码，请检查拼写后重试')

if __name__ == "__main__":
    
    
    #实例化循环执行
    while True:
        #获得输入
        print('密码 。 添加1 . 是否加入符号1 . 密码位数')
        middle_link = input('请输入密码+指令')

        middle_object = InputManage(str(middle_link))
        pass_code = middle_object.DealInput()
        # #判断，执行成功则输出
        # if pass_code !=0:
        #     print(pass_code)
        #     break


