# -*- coding: UTF-8 -*-
import time
import unittest
import requests
import json
from zbh_manage_requests import tools_requests

host = "https://dev.est.cicccapital.cn"

class login_testCase(unittest.TestCase):
    def setUp(self):
        print("执行开始")

    def testUserlogin(self):
        # 用户登录验证
        request = tools_requests.tools_requests()
        url = host + "/amarth/api/sysUser/public/Login"
        heards = {"Content-Type":"application/json"}
        param = {"account":"15510161574", "pwd":"123456", "requestSource":"SYSTEM"}
        response = request.request(url, 'post',params=json.dumps(param), headers=heards)
        print(response)
        self.assertTrue(len(response['data']) > 0, "异常：无数据返回")
        token = response.get("data").get("token")
        # token = response.json()['token']
        print("当前的token值="+token)
        print("用户登录成功")
        return token


    # def getToken(self):
    #     return  token

