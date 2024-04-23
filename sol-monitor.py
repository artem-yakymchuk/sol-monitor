import requests
import time

def get_latest_block():
    url = "https://api.mainnet-beta.solana.com"
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSlot",
        "params": ["finalized"]
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data['result']

def get_block_details(slot):
    url = "https://api.mainnet-beta.solana.com"
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBlock",
        "params": [slot, {"encoding": "json"}]
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data['result']

def check_for_new_tokens(block_data):
    # Ищем транзакции, создающие новые токены (это простой пример и может потребовать настройки)
    new_tokens = []
    transactions = block_data['transactions']
    for txn in transactions:
        if 'createAccount' in txn['transaction']['message']['instructions'][0]['parsed']['type']:
            new_tokens.append(txn['transaction']['message']['instructions'][0]['parsed'])
    return new_tokens

def main():
    print("Starting to monitor Solana blocks...")
    while True:
        latest_slot = get_latest_block()
        print(f"Checking slot: {latest_slot}")
        block_data = get_block_details(latest_slot)
        if block_data:
            new_tokens = check_for_new_tokens(block_data)
            if new_tokens:
                print(f"New tokens found in slot {latest_slot}: {new_tokens}")
        time.sleep(60)  # Проверяем каждую минуту

if __name__ == "__main__":
    main()
