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
        command_list = self.middle_linked.split('.',5)
        print(command_list)
        #调用方法处理
        #验证密码正确与否，正确pass_permit返回1
        pass_permit = self.is_user(command_list[0])
        # try:
        if pass_permit == 1 and command_list[1] == '1':
            # 假如密码正确并且要添加
            try:
                # 2 是否加入符号 ；3 密码位数 ; 4 是否加入用户名和备注
                pass_word = self.code_birth(command_list[2],command_list[3], command_list[4])
                return pass_word
                
            except IndexError: 
                pass_word = self.code_birth()
    

        elif pass_permit == 1 and command_list[1] == '0':
            # 密码正确，查询
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

    def code_birth(self,symbol_flag='0',code_nums=12, use_remark='0'):
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
        if use_remark == '1':
            usename = input('输入用户名')
            web_remark = input('输入备注')
            # self.code_copy(birth_word, usename)
        else:
            usename = web_remark = 'none'
        self.base_deal.code_save(birth_word,code_pertain,usename,web_remark)
        print('%s : %s'%(code_pertain,birth_word))
        print('已复制密码')
        pyperclip.copy(birth_word)
        return birth_word


    def code_search(self):
        #密码查询
        search_peitain = input('查询 ：输入密码归属 :')

        usetuple = self.base_deal.code_bringout(search_peitain)
        if usetuple:
            # print('密码归属 ：%s'%usetuple[0].decode())
            print('%s : %s'%(usetuple[2].decode(),usetuple[1].decode()))
            print('username : %s')
            self.code_copy(usetuple[1].decode(), usetuple[2].decode())
            # print('\n已复制密码')
            # pyperclip.copy(usetuple[1].decode())
        else:
            print('无法查询到对应密码，请检查拼写后重试')
    
    def code_copy(self,passcode,username=None):
        # 密码复制进剪贴板
        if username:
            pyperclip.copy(username)
            continued = input('已复制用户名，按c继续复制密码')
            print('iii')
            if continued == 'c':
                pyperclip.copy(passcode)
                print('已复制密码，结束')
            else:
                pyperclip.copy(passcode)
                print('已结束复制')

if __name__ == "__main__":
    
    
    #实例化循环执行
    while True:
        #获得输入
        print('密码 。 添加1 . 是否加入符号1 . 密码位数')
        middle_link = input('请输入密码+指令')

        middle_object = InputManage(str(middle_link))
        middle_object.DealInput()
        # #判断，执行成功则输出
        # if pass_code !=0:
        #     print(pass_code)
        #     break


