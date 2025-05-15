'''
Raw  matches from LOL API using RiotWatcher.

Deprecated. Use `collector.py` instead.
'''
import os
import os.path
import time
import logging
import json
from riotwatcher import LolWatcher, ApiError
import config

# 召唤师名和region
SUMMONER_NAME = 'Hide on bush'  # 你可以换成任意存在的召唤师名
REGION = 'br1'
MATCH_REGION = 'americas'

# Minimal log setting
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 确保 dump 目录存在
if not os.path.exists(config.DUMP_DIR):
    os.makedirs(config.DUMP_DIR)

# LOL api wrapper
wrapper = LolWatcher(config.API_KEY)

try:
    # 1. 获取召唤师信息
    summoner = wrapper.summoner.by_name(REGION, SUMMONER_NAME)
    puuid = summoner['puuid']
    logger.info(f"召唤师 {SUMMONER_NAME} 的 puuid: {puuid}")

    # 2. 获取最近10场比赛ID
    match_ids = wrapper.match.matchlist_by_puuid(MATCH_REGION, puuid, count=10)
    logger.info(f"最近10场比赛ID: {match_ids}")

    # 3. 依次获取每场比赛详情并保存
    for match_id in match_ids:
        try:
            match = wrapper.match.by_id(MATCH_REGION, match_id)
            filename = os.path.join(config.DUMP_DIR, f"{match_id}.json")
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(match, f, ensure_ascii=False, indent=2)
            logger.info(f"{match_id}: Match saved.")
        except ApiError as e:
            logger.info(f"ApiError: {match_id}: {e}")
            if hasattr(e, 'response') and getattr(e.response, 'status_code', None) == 429:
                logger.info('Too many requests, sleeping...')
                time.sleep(10)
        except Exception as e:
            logger.info(f"Other Error: {match_id}: {e}")
except Exception as e:
    logger.error(f"主流程异常: {e}")
