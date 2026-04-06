import requests
import json

# 桃園市公車站牌資料 API
url = "https://data.tycg.gov.tw/api/v1/rest/datastore/86364028-2f1d-44a6-9812-3211516e88e2?format=json"

def get_data():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # 儲存成 JSON 檔案符合作業要求 [cite: 4466]
            with open('taoyuan_bus.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("資料抓取成功並已儲存為 taoyuan_bus.json")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    get_data()
