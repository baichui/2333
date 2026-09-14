# -*- coding: utf-8 -*-
from nonebot import on_command, logger
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    MessageEvent,
    MessageSegment,
    PrivateMessageEvent,
)
from nonebot.plugin import PluginMetadata

from .image import get_image

__plugin_meta__ = PluginMetadata(
    name="WuWaLuck|今日运势",
    description="鸣潮主题白底今日运势图",
    usage="/luck 或 /今日运势",
    type="application",
    homepage="https://github.com/Kuro-Game/WutheringWaves",
    supported_adapters={"~onebot.v11"},
)

wuwa_luck = on_command(
    "luck",
    aliases={"今日运势"},
    priority=5,
    block=True,
)


@wuwa_luck.handle()
async def _(event: MessageEvent, bot: Bot):
    user_id = event.user_id
    nickname = ""

    if isinstance(event, PrivateMessageEvent):
        nickname = event.sender.nickname or str(user_id)
    elif isinstance(event, GroupMessageEvent):
        try:
            info = await bot.get_group_member_info(group_id=event.group_id, user_id=user_id)
            nickname = info.get("card") or info.get("nickname") or str(user_id)
        except Exception as e:  # noqa: BLE001 — 群名片拉取失败时回退
            logger.warning(f"wuwa_luck: get group member info failed: {e}")
            nickname = event.sender.nickname or str(user_id)
    else:
        nickname = str(user_id)

    try:
        image = get_image(nickname=nickname, uid=user_id)
    except Exception as e:  # noqa: BLE001
        logger.exception("wuwa_luck: render failed")
        await wuwa_luck.finish(f"运势图生成失败：{e}")

    if isinstance(event, PrivateMessageEvent):
        await wuwa_luck.send(MessageSegment.image(image))
    else:
        await wuwa_luck.send(MessageSegment.at(user_id) + MessageSegment.image(image))
