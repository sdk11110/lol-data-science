# 英雄联盟玩家行为分析

本仓库是《英雄联盟玩家行为分析》的源代码。项目旨在通过机器学习方法，基于英雄联盟（League of Legends, LoL）历史对局数据，分析和刻画玩家行为与表现的关系，帮助玩家提升策略和技能。

## 数据来源

本项目使用 [Riot Games](http://www.riotgames.com/) 官方 API 提供的历史对局数据。每场对局包含模式、类型、唯一编号及每位玩家的基础统计信息。详细字段可参考 [Riot API 文档](https://developer.riotgames.com/api/methods#!/1064)。

## 环境配置与依赖安装

1. **安装 Anaconda（推荐）**
   - 前往 [Anaconda 官网](https://www.anaconda.com/products/distribution) 下载并安装 Anaconda。

2. **创建独立 Python 环境（可选但推荐）**
   在命令行（Anaconda Prompt 或终端）输入：
   ```bash
   conda create -n lol python=3.10
   conda activate lol
   ```

3. **进入项目目录**
   ```bash
   cd /你的项目路径/src/python/
   ```

4. **安装 Python 依赖**
   使用国内清华镜像加速安装：
   ```bash
   pip install -r requeriments.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```
   > 依赖说明：
   > - `riotwatcher`：用于访问英雄联盟官方API
   > - `pymongo`：用于与MongoDB数据库交互（如需）

5. **申请并配置 Riot API Key**
   - 登录 [Riot Developer Portal](https://developer.riotgames.com/)，申请开发者 API Key。
   - 打开 `src/python/config.py`，将 `API_KEY` 设置为你申请到的 Key。

## 数据采集流程

1. **配置 API Key**
   - 在 `src/python/config.py` 文件中，将 `API_KEY` 设置为你申请到的 Riot API Key。

2. **获取召唤师 puuid**
   - 运行 `get_puuid.py` 脚本，输入目标召唤师名，获取对应的 puuid。
   - 命令示例：
     ```bash
     python get_puuid.py
     ```
   - 复制输出的 puuid，后续采集用。

3. **采集比赛数据**
   - 在 `raw.py` 中填入目标 puuid，或根据脚本逻辑自动采集。
   - 运行采集脚本：
     ```bash
     python raw.py
     ```
   - 采集到的原始对局数据将保存在 `src/dump/` 目录下。

4. **批量采集建议**
   - 如需采集多个召唤师的数据，可维护一个召唤师名列表，循环获取 puuid 并采集。
   - 可调整采集脚本中 `count` 参数，获取更多比赛。

5. **异常与限流处理**
   - 若遇到 429（限流）等错误，脚本会自动等待后重试。
   - 建议合理控制采集频率，避免 API Key 被封禁。