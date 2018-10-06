#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : chrome_headless_request_demo.py
 @Time       : 2018/10/05 0011 22:14
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : MIT
"""
import requests as req
import json


if __name__ == '__main__':
    data = {
        "url": "https://cn.bing.com",
        "operation": [{
            "input": {
                "dom": "#sb_form_q",
                "value": "冰菓",
                "type": "css"
            },
            "wait": 20
        }, {
            "click": {
                "dom": "#sb_form_go",
                "type": "css"
            },
            "wait": 2
        }, {
            "scroll": {
                "height": 1000
            },
            "wait": 10
        }, {
            "window": {
                "size": "800x600"
            },
            "wait": 10
        }],
        "result": "page & cookies"
    }
    print(json.dumps(data))
    dat = json.dumps(data)
    # 重要的一步,用json的头来确保提交的内容是json的内容类型
    header = {"Content-Type": "application/json"}
    res = req.post('http://localhost:5000', data=dat, headers=header)
    print(res.content.decode('utf-8'))
