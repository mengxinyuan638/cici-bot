from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER


matcher = on_command("测试权限")


@matcher.handle()
async def _(event: GroupMessageEvent):
    if await GROUP_ADMIN(event):
        await matcher.send("管理员测试成功")
    elif await GROUP_OWNER(event):
        await matcher.send("群主测试成功")
    else:
        await matcher.send("群员测试成功")