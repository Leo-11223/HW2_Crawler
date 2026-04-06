import requests
import json
import os
import urllib3

# 關閉 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_bus_data():
    # 桃園公車站牌 API 網址
    url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=343a3583-8d35-42bc-9d41-0ca2d039578f&rid=5d49f64a-251a-466d-8a4c-d10243467657"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # allow_redirects=True 確保處理網址跳轉，verify=False 跳過憑證錯誤
        response = requests.get(url, headers=headers, verify=False, allow_redirects=True)
        response.raise_for_status()
        
        # 檢查內容是否為空
        if not response.text.strip():
            print("❌ 錯誤：伺服器回傳了空內容")
            return

        # 嘗試解析 JSON
        data = response.json()
        
        file_name = 'taoyuan_bus.json'
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print(f" 成功！檔案已儲存至: {os.path.abspath(file_name)}")
        print(f" 檔案大小: {os.path.getsize(file_name)} bytes")
        
    except json.JSONDecodeError:
        print("❌ 錯誤：抓到的內容不是 JSON 格式。")
        print("回傳內容前 100 字：", response.text[:100])
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    fetch_bus_data()
