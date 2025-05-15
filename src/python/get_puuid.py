import requests

API_KEY = "RGAPI-f29fc59a-e478-45b9-ab2a-feed4934d21a"
REGION = "kr"
SUMMONER_NAME = "Hide on bush"

url = f"https://{REGION}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{SUMMONER_NAME}"
headers = {
    "X-Riot-Token": API_KEY
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print("puuid:", data["puuid"])
else:
    print("请求失败，状态码：", response.status_code)
    print("返回内容：", response.text) 