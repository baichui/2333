# nonebot-plugin-wuwa-luck

NoneBot2 插件：鸣潮主题「今日运势」白底卡片。

## 指令

- /luck
- /今日运势

## 安装

放到 NoneBot 的 plugin_dirs 下，例如：

`	ext
src/plugins/wuwa_luck/
  __init__.py
  data.py
  image.py
  assets/bg.png
`

依赖：
onebot2、
onebot-adapter-onebot、Pillow。

## 说明

- 同一 UID + 昵称 + 日期，当天结果固定。
- 共鸣指引：小爱（爱弥斯）约 80%，其余角色均分。
- 宜/忌默认各 2 条；大吉/大凶特判缩为 1 条。
- 鸣潮相关文案全卡最多 1 条。
- 字体优先使用系统字体（C:\Windows\Fonts）。
