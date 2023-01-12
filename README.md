<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://zsy.juncikeji.xyz/i/img/icon_cici.png" width="200" height="200" alt="辞辞bot"></a>
</p>


<div align="center">
    <h1 align="center">✨萌新源 辞辞机器人</h1>
     <h1 align="center">🎂生日:2022-2-28</h1>
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
	</a>&emsp;
	<!-- py版本 -->
	<img src="https://img.shields.io/badge/python-3.7.3+-blue" alt="python">&emsp;
	<img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT">&emsp;
</p></br>



<div align="center">
    <img src="https://gitee.com/yevin_bot/cici-bot/raw/master/img/virtual_01.png" width="200px" alt="辞辞bot">
<img src="https://gitee.com/yevin_bot/cici-bot/raw/master/img/virtual_02.png" width="200px" alt="辞辞bot">
<img src="https://gitee.com/yevin_bot/cici-bot/raw/master/img/virtual_03.png" width="200px" alt="辞辞bot">
</div>


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
│  yuanshen_search.py		原神角色查询
|  system_type.py			查看系统信息
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
├─stamp
|		__init__.py
├-------tem[该文件夹请移动到bot根目录下]
|	   |	mxy.html(邮件模板)
```

## 贡献
本仓库由萌新源制作，以及sevin、张时贰共同维护

QQ群：934541995

## 更新日志

**注**:本日志从v2.2版本开始记录，过往版本就不记录了

------

2022/11/5  v2.2

- 修复诸多问题，例如疫情查询的“目前”这类用词不当，修改为累计

- 修复禁言，用户可以自定义禁言时间例如 禁@某某 【禁言时间】


2022/12/22  v2.3

- 修复疫情查询，更换为萌新源API


2022/12/22  v2.4

- 修复ICP备案查询

2022/12/28  v2.5

- 更新stamp发信模块
- 更新查看系统信息插件

2023/1/11  v2.6

- 更新退群通报

2023/1/12  v2.7

- 更新原神公告