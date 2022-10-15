<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
    <h1 align="center">✨萌新源 辞辞机器人</h1>
</div>

<p align="center">
	<!-- 萌新源API -->
	<a style="margin-inline:5px" target="_blank" href="https://api.juncikeji.xyz/">
		<img src="https://img.shields.io/badge/API-萌新源-blue?style=flat&logo=PHP" title="萌新源API">
	</a>&emsp;
	<!-- Gitee主页 -->
	<a style="margin-inline:5px" target="_blank" href="https://gitee.com/meng-xinyuan-mxy">
		<img src="https://img.shields.io/badge/Gitee-Home-blue?style=flat&logo=Gitee" title="Gitee主页">
	</a>&emsp;
	<!-- CSDN博客 -->
	<a style="margin-inline:5px" target="_blank" href="https://blog.csdn.net/m0_66648798">
		<img src="https://img.shields.io/badge/CSDN-博客-c32136?style=flat&logo=C" title="CSDN博客主页">
	</a>&emsp;
	<!-- 萌新源的小窝 -->
	<a style="margin-inline:5px" target="_blank" href="http://blog.juncikeji.xyz/">
		<img src="https://img.shields.io/badge/Blog-个人博客-FDE6E0?style=flat&logo=Blogger" title="萌新源的小窝">
	</a>&emsp;
	<!-- QQ群 -->
	<a style="margin-inline:5px" target="_blank" href="https://jq.qq.com/?_wv=1027&k=5Ot4AUXh">
		<img src="https://img.shields.io/badge/腾讯-QQ群-0cedbe?style=flat&logo=Tencent QQ" title="QQ">
	</a>
	<!-- py版本 -->
	<img src="https://img.shields.io/badge/python-3.7.3+-blue" alt="python">
</p></br>

## 描述

一款基于[NoneBot2](https://v2.nonebot.dev/)的群管机器人，请先参考官方文档下载安装Nonebot2

本仓库仅提供插件源码，并未打包pip，但也不允许私自打包。转载或打包前请联系作者。本仓库版权属于萌新源

## 使用
由于本仓库并未打包pip，所以请复制源代码至`./nb2/src/plugins`路径下

## 插件目录
```
│  cartoon_wallpapers.py	随机卡通壁纸
│  chicken_soup.py			心灵鸡汤
│  covid_query.py			疫情查询
│  dog_diary.py				舔狗日记
│  enter_group_welcome.py	入群欢迎
│  firexN.py				QQ续火花(pnonebot_plugin_firexN)
│  get_music.py             网易云点歌(返回歌曲或语音)
│  jrys.py					今日运势
│  menu.py					菜单	
│  qunguan.py				群管(违禁词撤回、全员禁言、成员禁言、踢人、同意/拒绝入群申请、入群欢迎、定时推送群消息(支持enjoy表情))
│  random_chat.py			随机聊天
│  random_head.py			随机头像
│  random_joke.py			随机笑话
│  random_love.py			土味情话
│  random_music.py			随机歌曲
│  random_sentence.py		随机一言
│  random_talk.py			随机一句
│  translate.py				翻译
│  view advertise.py		公告
│  xingzuo_luck.py			星座运势
│  yuanshen_search.py		元神角色查询
│
├─choujiang					抽奖
│      __init__.py
│
├─qiandao					签到
│      login.py
│      read.py
│      write.py
│      __init__.py
│
├─store						金币商城
│       search.py
│       source.py
│       success.py
│       use.py
│       write.py
│       __init__.py
├─  CS_search.py			测试类，未完成功能
├─  CS_抽奖.py				测试类，未完成功能        
├─  Test.py					Test为测试文件
├─  Test_权限测试.py
├─  Test_禁言测试.py
└─  Test_私聊权限.py        
```

## 贡献
本仓库由萌新源制作，以及sevin、张时贰共同维护

QQ群：934541995

