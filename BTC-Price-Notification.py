import requests
# Make sure that your key is in the URL
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
# You should change "name" and "key" with your own values.
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/{name}/with/key/{key}'
response = requests.get(bitcoin_api_url)
response_json = response.json()
# Converts the price to a floating point number
value = float(response_json[0]['price_usd'])
# The payload that will be sent to IFTTT service
data = {'value1': value}
# Sends a HTTP POST request to the webhook URL
requests.post(ifttt_webhook_url, json=data)