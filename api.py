import requests
import json
import os

def fetch_bus_data():
    url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=343a3583-8d35-42bc-9d41-0ca2d039578f&rid=5d49f64a-251a-466d-8a4c-d10243467657"
    
    try:

        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'taoyuan_bus.json')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print(f"✅ 資料抓取成功！檔案已儲存至: {file_path}")
        
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    fetch_bus_data()
