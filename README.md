# nonebot-plugin-wuwa-luck

NoneBot2 插件：鸣潮主题「今日运势」白底卡片。

## 指令

| 指令 | 说明 |
|------|------|
| /luck | 生成今日运势图 |
| /今日运势 | 同上 |

## 安装

**只需要把插件放进 NoneBot 的插件目录。**

假设你的 NoneBot 工程（含 pyproject.toml / ot.py）在 C:\Y\BOT\onebot，
且 pyproject.toml 里已配置 plugin_dirs = ["src/plugins"]：

`powershell
cd C:\Y\BOT\onebot
git clone https://github.com/baichui/2333.git src/plugins/wuwa_luck
`

目录结构应如下：

`	ext
onebot/
  src/
    plugins/
      wuwa_luck/          ← clone 下来的本仓库
        __init__.py
        data.py
        image.py
        assets/
          bg.png
`

然后重启 NoneBot 即可（例如 
b_cli run 或你的启动脚本）。

### 其它插件目录

若你的 plugin_dirs 不是 src/plugins，改成对应路径即可，例如：

`powershell
git clone https://github.com/baichui/2333.git src/plugins/wuwa_luck
# 或
git clone https://github.com/baichui/2333.git plugins/wuwa_luck
`

### 依赖

- 
onebot2
- 
onebot-adapter-onebot
- Pillow（一般随环境已有）

字体优先使用系统字体（Windows：C:\Windows\Fonts），无需额外装字体。

## 说明

- 同一 UID + 昵称 + 日期，当天结果固定。
- 共鸣指引：小爱（爱弥斯）约 80%，其余角色均分。
- 宜/忌默认各 2 条；大吉/大凶特判缩为 1 条。
- 鸣潮相关文案全卡最多 1 条。
