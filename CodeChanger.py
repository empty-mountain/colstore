"""本模块用于完成密码的加密解密功能

1.随机密码构成
    根据输入选择密码构成
    加入密码对象，日期
    随机插入字符

2.暂时选用加密程度较低的base64加密
"""
import base64
class base64_code(object):
    """base64加密解密程序"""
    def __init__(self):
        # self.code = real_code
        pass
        
    def encrypt(self,code_unencrypt):
        #base64加密程序
        # 编译为byte类型
        code = code_unencrypt.encode('utf8')
        #加密
        encrypt_code = base64.b64encode(code)
        return encrypt_code

    def declassified(self,encrypt_code):
        # base64解密程序
        decode = base64.b64decode(encrypt_code)
        return decode

if __name__ == "__main__":
    #实例化一个对象
    code = input('input your code here')

    coding = base64_code(code)
    
    coded = coding.encrypt()
    print(coded)
    mid = coding.declassified(coded)
    mids = str(mid,encoding='utf-8')
    print(mids)
    