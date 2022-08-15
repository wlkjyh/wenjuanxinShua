# 基于selenium刷问卷星

## 如何安装？
```
conda install selenium
conda install requests
conda install faker
```

## 如何运行？

先在代码第10行proxyUrl设置代理接口获取代理IP
在11行设置url设置要刷的问卷星
38-49行设置填表信息即可
```
python start.py
```

## 这和其他项目有什么区别
这个项目用了selenium实现，完美实现反爬虫，并且能过滑块、点击验证码，只需简单配置就能刷问卷星


## 注意
这里需要你去购买代理IP配置，否则问卷星会限制IP提交。
