import requests
import json

def fetch_bus_data():
    url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=343a3583-8d35-42bc-9d41-0ca2d039578f&rid=5d49f64a-251a-466d-8a4c-d10243467657"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # 直接寫檔名，不加任何路徑
        with open('taoyuan_bus.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print("✅ 檔案 taoyuan_bus.json 已成功產出！")
        
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    fetch_bus_data()
