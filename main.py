import os
import requests
from bs4 import BeautifulSoup
from supabase import create_client, Client

SUPABASE_URL = "https://minkahnqqkilodlbbvlw.supabase.co"
SUPABASE_KEY = "Sb_publishable_xhEmJWSXEaG4fEdR8sLH5g_718YiiXM"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def crawl_and_save():
    print("開始抓取與更新包棟民宿資料...")
    
    homestays_data = [
        {
            "name": "宜蘭綠意包棟 Villa",
            "city": "宜蘭縣",
            "max_guests": 20,
            "price": 16000,
            "has_ktv": True,
            "has_bbq": True,
            "has_mahjong": True,
            "url": "https://example.com/yilan-villa"
        },
        {
            "name": "南投清境雲海包棟木屋",
            "city": "南投縣",
            "max_guests": 12,
            "price": 12000,
            "has_ktv": False,
            "has_bbq": True,
            "has_mahjong": True,
            "url": "https://example.com/nantou-cabin"
        },
        {
            "name": "墾丁陽光海景包棟會館",
            "city": "屏東縣",
            "max_guests": 16,
            "price": 18000,
            "has_ktv": True,
            "has_bbq": True,
            "has_mahjong": False,
            "url": "https://example.com/kenting-resort"
        },
        {
            "name": "苗栗山城星空包棟莊園",
            "city": "苗栗縣",
            "max_guests": 10,
            "price": 9800,
            "has_ktv": False,
            "has_bbq": True,
            "has_mahjong": False,
            "url": "https://example.com/miaoli-manor"
        }
    ]
    
    for item in homestays_data:
        supabase.table("homestays").upsert(item).execute()
        
    print(f"成功更新 {len(homestays_data)} 筆民宿資料！")

if __name__ == "__main__":
    crawl_and_save()
