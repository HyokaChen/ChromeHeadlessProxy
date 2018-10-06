# ChromeHeadlessProxy

Use Chrome headless mode to redirect HTTP request

## 基本环境安装：

1. [nodejs](https://nodejs.org/en/)安装，目前本机装的是10的LTS版本。
2. 确保```npm```已经包含。
3. 确保安装了```Chrome```浏览器。
4. 使用命令```npm i```安装当前路径下的```packge.json```中依赖的包。
5. 运行```start_chrome_server.bat```启动中间服务。

## post的格式和注意事项

1. 使用```requests```的```post```模块进行中转请求的数据格式。

``` json
{
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
            "wait": 5
        }, {
            "window": {
                "size": "800x600"
            },
            "wait": 5
        }],
        "result": "page & cookies"
    }
```

> - url代表着最终请求的链接。
> - operation代表着需要的页面的操作（针对于一些需要滚动啊等等的网页）。里面支持的操作有```click, input, scroll, window```分别代表着点击，输入内容，滚动，和缩放窗口的视图大小。所有的参数就如上面所示，其中```dom```节点支持```XPATH```和```CSS```选择器两种。
> - result代表着需要返回的结果，一般是两种，```page```和```cookies```。两者可同时返回，返回的格式是```json```。大致是```{"result": xxx, "cookies": xxx}```。

每次请求都会打开一次浏览器和关闭一次浏览器，后续就考虑复用打开的浏览器。

注意事项：在```chrome_serve.js```中```debug```变量，如果需要观看浏览器的界面，请设置为```true```，否则会以无头浏览器的形式在后台运行。

## 示例请见```chrome_headless_request_demo.py```。