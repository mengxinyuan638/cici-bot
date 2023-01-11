import psutil
import platform
import time
from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message

'''
writen by 萌新源 at 2022/12/24
本插件需要psutil拓展库，没有的请使用命令 pip install psutil 进行安装
本插件主要功能是获取系统各项指标状态，以及硬件信息，操作系统等
命令：系统状态
'''
system_msg = on_regex(pattern = r'^系统信息$')

mem = psutil.virtual_memory()
# 系统总计内存
zj = round(float(mem.total) / 1024 / 1024 / 1024, 1)
# 系统已经使用内存
ysy = round(float(mem.used) / 1024 / 1024 / 1024, 1)
# 系统空闲内存
kx = round(float(mem.free) / 1024 / 1024 / 1024, 1)
# CPU逻辑核心数量
core = psutil.cpu_count()
# CPU物理核心数量
core2 = psutil.cpu_count(logical=False)
# 内存占用量
percent = mem.percent

#网速获取
sent_before = psutil.net_io_counters().bytes_sent  # 已发送的流量
recv_before = psutil.net_io_counters().bytes_recv  # 已接收的流量
time.sleep(1)
sent_now = psutil.net_io_counters().bytes_sent
recv_now = psutil.net_io_counters().bytes_recv
sent = (sent_now - sent_before) / 1024  # 算出1秒后的差值
recv = (recv_now - recv_before) / 1024

run_time = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
upload_speed = "上传：{0}KB/s".format("%.2f" % sent)
download_speed = "下载：{0}KB/s".format("%.2f" % recv)
core_1 = f'CPU逻辑核心数：{core}'
core_2 = f'CPU物理核心数：{core2}'
total_nc = f'系统总计内存：{zj}GB'
used_nc = f'系统已使用内存：{ysy}GB'
free_nc = f'系统空闲内存：{kx}GB'
percent_nc = f'内存占比{percent}'

#获取操作系统
system = platform.platform()
system = f'操作系统:{system}'

result = f'{run_time}\n{upload_speed}\n{download_speed}\n{core_1}\n{core_2}\n{total_nc}\n{used_nc}\n{free_nc}\n{percent_nc}\n{system}'


@system_msg.handle()
async def yy(bot: Bot, event: GroupMessageEvent, state: T_State):

    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await system_msg.send(Message(result))


