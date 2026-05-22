import requests
import random
import time

# ==================================================
# OFFER URL CPAGRIP
# ==================================================
OFFER_URL = "https://singingfiles.com/show.php?l=0&u=2528939&id=74819"

# ==================================================
# 5 PROXY GRATIS WEBSHARE (IP US)
# GANTI PASSWORD DENGAN PASSWORD ASLI DARI DASHBOARD!
# ==================================================
proxy_list = [
    {
        "host": "23.95.150.145",
        "port": "6114",
        "user": "cdvfpydm",
        "pass": "t792h11n03va"  # Ganti dengan password asli
    },
    {
        "host": "38.154.203.95",
        "port": "5863",
        "user": "cdvfpydm",
        "pass": "t792h11n03va"  # Ganti dengan password asli
    },
    {
        "host": "198.23.243.226",
        "port": "6361",
        "user": "cdvfpydm",
        "pass": "t792h11n03va"  # Ganti dengan password asli
    },
    {
        "host": "209.127.138.10",
        "port": "5784",
        "user": "cdvfpydm",
        "pass": "t792h11n03va"  # Ganti dengan password asli
    },
    {
        "host": "38.154.185.97",
        "port": "6370",
        "user": "cdvfpydm",
        "pass": "t792h11n03va"  # Ganti dengan password asli
    }
]

# ==================================================
# USER AGENT (BERBEDA AGAR TIDAK TERDETEKSI)
# ==================================================
user_agents = [
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36",
]

# ==================================================
# GENERATE EMAIL (TERLIHAT REAL)
# ==================================================
first_names = ["john", "james", "robert", "michael", "william", "david", 
               "joseph", "thomas", "charles", "daniel", "matthew", "anthony"]
last_names = ["smith", "johnson", "williams", "brown", "jones", "garcia", 
              "miller", "davis", "rodriguez", "martinez", "wilson", "anderson"]
domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]

def generate_email():
    first = random.choice(first_names)
    last = random.choice(last_names)
    number = random.randint(1, 9999)
    domain = random.choice(domains)
    return f"{first}.{last}{number}@{domain}"

# ==================================================
# SUBMIT OFFER DENGAN PROXY RANDOM
# ==================================================
def submit_offer(submit_num):
    # Pilih proxy secara acak dari daftar
    proxy = random.choice(proxy_list)
    email = generate_email()
    
    # Format proxy untuk requests
    proxies = {
        "http": f"http://{proxy['user']}:{proxy['pass']}@{proxy['host']}:{proxy['port']}",
        "https": f"http://{proxy['user']}:{proxy['pass']}@{proxy['host']}:{proxy['port']}"
    }
    
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://singingfiles.com",
        "Referer": OFFER_URL,
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
    }
    
    payload = {
        "email": email,
        "submit": "Submit"
    }
    
    print(f"\n[+] Submit #{submit_num}")
    print(f"    Email: {email}")
    print(f"    Proxy IP: {proxy['host']}:{proxy['port']}")
    print(f"    User Agent: {headers['User-Agent'][:50]}...")
    
    try:
        res = requests.post(OFFER_URL, data=payload, headers=headers, 
                           proxies=proxies, timeout=30)
        print(f"    Response: {res.status_code} ✅")
        
        # Jeda random 60-120 detik
        delay = random.randint(60, 120)
        print(f"    Jeda {delay} detik sebelum submit berikutnya...")
        time.sleep(delay)
        return True
        
    except Exception as e:
        print(f"    Error: {e} ❌")
        return False

# ==================================================
# MAIN LOOP
# ==================================================
if __name__ == "__main__":
    print("="*60)
    print("  CPAGRIP BOT - 5 PROXY US (ROTASI OTOMATIS)")
    print("="*60)
    print(f"[*] Total Proxy: {len(proxy_list)}")
    print(f"[*] Target: {OFFER_URL}")
    print("="*60)
    
    success_count = 0
    total_submit = 20  # Bisa diubah sesuai keinginan
    
    for i in range(total_submit):
        if submit_offer(i+1):
            success_count += 1
    
    print("\n" + "="*60)
    print(f"  BOT SELESAI! {success_count}/{total_submit} submit berhasil")
    print("  Cek dashboard CPAGrip dalam 1-2 jam")
    print("="*60)
