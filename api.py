import requests
import json
import os
import urllib3

# 關閉因跳過驗證而產生的警告訊息
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_bus_data():
    url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=343a3583-8d35-42bc-9d41-0ca2d039578f&rid=5d49f64a-251a-466d-8a4c-d10243467657"
    
    try:
        # 【核心修正】加入 verify=False 跳過 SSL 驗證
        response = requests.get(url, verify=False)
        response.raise_for_status() 
        
        data = response.json()
        
        file_name = 'taoyuan_bus.json'
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print(f"✅ 成功跳過 SSL 驗證！檔案已儲存至: {os.path.abspath(file_name)}")
        
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    fetch_bus_data()
