import requests
import random
import time
import json
from datetime import datetime

class CPABotAdvanced:
    def __init__(self, proxies):
        self.session = requests.Session()
        self.proxies = proxies
        self.success = 0
        self.failed = 0
        
        self.session.headers.update({
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        })
    
    def random_user_agent(self):
        ua_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 Version/15.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 Chrome/118.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/16.1 Safari/605.1.15",
            "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 Chrome/119.0.0.0 Mobile Safari/537.36",
        ]
        return random.choice(ua_list)
    
    def generate_lead_data(self):
        first_names = ["John", "James", "Robert", "Michael", "William", "David", "Joseph", "Thomas", "Charles", "Daniel"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "Austin"]
        zips = ["10001", "90210", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "78701"]
        
        first = random.choice(first_names)
        last = random.choice(last_names)
        
        return {
            "email": f"{first.lower()}.{last.lower()}@gmail.com",
            "first_name": first,
            "last_name": last,
            "city": random.choice(cities),
            "zipcode": random.choice(zips),
            "state": random.choice(["CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI"]),
            "phone": f"({random.randint(200,999)}) {random.randint(100,999)}-{random.randint(1000,9999)}",
            "submit": "Submit"
        }
    
    def submit(self, url, proxy, submit_num):
        try:
            # Random User Agent
            ua = self.random_user_agent()
            self.session.headers.update({"User-Agent": ua})
            
            # Generate data
            data = self.generate_lead_data()
            
            # GET request dulu (dapat cookie)
            print(f"[{submit_num}] GET: {proxy['host']}")
            get_resp = self.session.get(url, proxies=proxy, timeout=15)
            
            if get_resp.status_code != 200:
                raise Exception(f"GET failed: {get_resp.status_code}")
            
            time.sleep(random.uniform(2, 5))
            
            # POST dengan data
            print(f"[{submit_num}] POST: {data['email']}")
            post_resp = self.session.post(url, data=data, proxies=proxy, timeout=30)
            
            if post_resp.status_code == 200:
                self.success += 1
                print(f"✅ SUCCESS: {data['email']}")
                return True
            else:
                self.failed += 1
                print(f"❌ FAILED: {post_resp.status_code}")
                return False
                
        except Exception as e:
            self.failed += 1
            print(f"❌ ERROR: {str(e)[:60]}")
            return False
    
    def run(self, url, target_submits):
        print("="*60)
        print(f"  CPAGRIP BOT - START: {datetime.now()}")
        print("="*60)
        print(f"Target: {url}")
        print(f"Target submits: {target_submits}")
        print(f"Proxies: {len(self.proxies)}")
        print("-"*60)
        
        for i in range(target_submits):
            proxy = random.choice(self.proxies)
            print(f"\n[Lead {i+1}/{target_submits}] Proxy: {proxy['host']}")
            
            self.submit(url, proxy, i+1)
            
            # Jeda random 45-120 detik
            delay = random.randint(45, 120)
            print(f"[*] Jeda {delay} detik...")
            time.sleep(delay)
        
        print("-"*60)
        print(f"  SELESAI: {datetime.now()}")
        print(f"  Success: {self.success}, Failed: {self.failed}")
        print("="*60)
        return self.success

# ==================================================
# KONFIGURASI
# ==================================================
OFFER_URL = "https://singingfiles.com/show.php?l=0&u=2528939&id=74819"

# 5 PROXY WEBSHARE (ganti password asli)
proxies = [
    {"host": "23.95.150.145", "port": "6114", "user": "cdvfpydm", "pass": "t792h11n03va"},
    {"host": "38.154.203.95", "port": "5863", "user": "cdvfpydm", "pass": "t792h11n03va"},
    {"host": "198.23.243.226", "port": "6361", "user": "cdvfpydm", "pass": "t792h11n03va"},
    {"host": "209.127.138.10", "port": "5784", "user": "cdvfpydm", "pass": "t792h11n03va"},
    {"host": "38.154.185.97", "port": "6370", "user": "cdvfpydm", "pass": "t792h11n03va"},
]

# Format proxy untuk requests
formatted_proxies = []
for p in proxies:
    formatted_proxies.append({
        "http": f"http://{p['user']}:{p['pass']}@{p['host']}:{p['port']}",
        "https": f"http://{p['user']}:{p['pass']}@{p['host']}:{p['port']}"
    })

# ==================================================
# JALANKAN
# ==================================================
if __name__ == "__main__":
    bot = CPABotAdvanced(formatted_proxies)
    bot.run(OFFER_URL, target_submits=30)  # 30 submit per eksekusi
