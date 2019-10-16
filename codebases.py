"""连接mysql数据库。

1、密码的保存
2、密码的取出

数据库类：Databases_deal
    方法1：use_mysql
    方法2：code_save (code_unsave,pertain_unsave)
    方法3：code_take (serch_pertain)
"""

import pymysql
from CodeChanger import base64_code

class Databases_deal(object):
    """定义数据库，执行存储与取出"""
    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # self.args = args
        self.base64_bases = base64_code()

    def use_mysql(self,*args):
        conn = pymysql.connect(
        host='localhost',
        port=3306,
        database='useself',
        user='root',
        password='root',
        charset='utf8',
        )
        # 获得Cursor对象
        cs1 = conn.cursor()
        # sql_execute = args[0] + 
        result = 0
        count = 0
        if len(args) > 3:
            #insert
            count = cs1.execute(args[0],(args[1], args[2], args[3], args[4]))
        else:
            #select
            # result = cs1.execute('select * from encryptcode')
            cs1.execute(args[0],(args[1]))
        

        result = cs1.fetchall()
        # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
        conn.commit()
        #输出结果

        if result:
            return result 
        else:
            return count

        # 关闭Cursor对象
        cs1.close()
        # 关闭Connection对象
        conn.close()

    def code_save(self,code_unsave,pertain_unsave,*args):
        # 加密并储存
        coded = self.base64_bases.encrypt(code_unsave)
        pertained = self.base64_bases.encrypt(pertain_unsave)
        E_username = self.base64_bases.encrypt(args[0])
        E_web_remark = self.base64_bases.encrypt(args[1])
        
        sql = 'insert into encryptcode(pertain,code,username,web_remark) values(%s,%s,%s,%s)'
            
        #写入参数，防止sql注入
        flag = self.use_mysql(sql, pertained, coded, E_username, E_web_remark)
        # print(flag)
        if flag:
            print('success')
    
    def code_bringout(self,search_pertain): 
        #加密以便查询
        pertained = self.base64_bases.encrypt(search_pertain)
        #code
        sql = 'select pertain,code,username,web_remark from encryptcode where pertain = %s'
        # sql = 'select * from encryptcode where code = %s'
        #写入                                                                                                                                                                                                                                                 
        encrypted = self.use_mysql(sql,pertained)
        # print(encrypted)
        #解码
        try:
            pertain = self.base64_bases.declassified(encrypted[0][0])
            codes = self.base64_bases.declassified(encrypted[0][1])
            username = self.base64_bases.declassified(encrypted[0][2])
            web_remark = self.base64_bases.declassified(encrypted[0][3])
        except:
            print('未找到对应条目，请检查拼写后重试。')
            return 0
        #将值返回
        return pertain,codes,username,web_remark
        

if __name__ == "__main__":
    test = Databases_deal() 
    # test.code_save('123456as','QQ','empty','none')
    usetuple = test.code_bringout('QQ')
    if usetuple:
        print(' %s : %s'%(usetuple[0].decode(),usetuple[1].decode()))
        print('username : %s , web_remark : %s'%(usetuple[2].decode(), usetuple[3].decode()))

    

    



