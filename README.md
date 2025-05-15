# 英雄联盟玩家行为分析

本仓库为硕士研究课题《英雄联盟玩家行为分析》的源代码。项目旨在通过机器学习方法，基于英雄联盟（League of Legends, LoL）历史对局数据，分析和刻画玩家行为与表现的关系，帮助玩家提升策略和技能。

* 项目作者：你的名字
* 指导老师：你的导师
* 所属单位：你的学校/研究所

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

1. 在 `