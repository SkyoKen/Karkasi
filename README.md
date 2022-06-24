<div align="center">
  <h1>Karkasi</h1>
  <p>方便朋友之间的记账相互确认</p>
  <p>基于<a href="https://www.pyweb.io/">PyWebio</a>框架</p>
  <p>
  <a href="https://github.com/SkyoKen/Karkasi"><img src="https://img.shields.io/github/forks/SkyoKen/Karkasi.svg" alt="forks"></a>
  <a href="https://github.com/SkyoKen/Karkasi"><img src="https://img.shields.io/github/stars/SkyoKen/Karkasi.svg" alt="stars"></a>
  <a href="https://github.com/SkyoKen/Karkasi"><img src="https://img.shields.io/github/license/SkyoKen/Karkasi.svg" alt="license"></a>
  </p>
</div>

## 目录
1. [更新进度](#更新进度)  
2. [食用方法](#食用方法)  
3. [可能用到的小知识](#可能用到的小知识)  
    - [如何保持后台运行](#如何保持后台运行)  
    - [如何关闭这个程序](#如何关闭这个程序)  

## 界面
<br/>
<img src="./images/head.jpg">
<br/>

## 基本功能
- [x] 简单的登录验证
- [x] 新增记录
- [x] 修改记录
- [x] 删除记录
- [x] 更新记录
- [ ] 记录排序
- [ ] 输入不同密码进入不同账本（即多人，多情况对应可能）

## 食用方法
```shell
git clone https://github.com/SkyoKen/Karkasi
sudo pip3 install pywebio pandas
cd Karkasi
python app.py
```

## 可能用到的小知识
### 如何保持后台运行
```
nohup python app.py & 
```
### 如何关闭这个程序
1. 通过端口反查进程号'netstat -nlp | grep 端口'
2. 根据命令查找进程'ps -ef|grep python'

然后'kill 进程号'


