import os
import random
import time
from binance.client import Client

# Вместо ТВОЙ_API_KEY и ТВОЙ_API_SECRET введите API Key и Secret Key со страницы
# https://www.binance.com/ru/my/settings/api-management сохраняя ковычки

API_KEY = 'ТВОЙ_API_KEY'
API_SECRET = 'ТВОЙ_API_SECRET'

# Инициализация клиента Binance
client = Client(API_KEY, API_SECRET)

def withdraw_crypto(asset, amount, address, network):
    """
    Это функция для вывода крипту с Binance на указанный Вами адрес.

    Используемые параметры:
    asset (str): Символы криптовалюты, например, 'BTC', 'ETH'
    amount (float): Значение криптовалюты для вывода
    address (str): Адрес назначения для вывода средств
    network (str): Сеть, используемая для вывода средств, например, 'ETH', 'BNB'

    Возвращает:
    dict: Ответ от API Binance
    """
    try:
        response = client.withdraw(coin=asset, address=address, amount=amount, network=network)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

# Замените BTC на нужную крипту и сеть для вывода, сохраняя ковычки.

ASSET_TO_WITHDRAW = 'BTC'
NETWORK = 'BTC'

print("=" * 44, "Сryptotyk", "=" * 44 + '\nПодпишись: https://t.me/cryptotyk\n' + "=" * 99)


# Считывание адресов из текстового файла "addresses.txt"
with open("addresses.txt", "r") as file:
    addresses = file.readlines()

#Перемешивает адреса в случайном порядке
random.shuffle(addresses)

# Обработка вывода средств по каждому адресу
for address in addresses:
    address = address.strip()
    # Значение ниже генерирует случайное число (сумму для вывода) от 2 до 2,5, округленное до 8 знаков после запятой.
    # Поэтому установите нужный вам диапазон и число знаков после запятой, заменив 2, 2.5 на свой диапазон, а 8 на нужное количество знаков после запятой.
    amount_to_withdraw = round(random.uniform(2, 2.5), 8)
    print(f"Processing withdrawal for address: {address} with amount: {amount_to_withdraw}")
    response = withdraw_crypto(ASSET_TO_WITHDRAW, amount_to_withdraw, address, NETWORK)

    if response:
        print(f"Withdrawal successful! Response: {response}")
    else:
        print("Withdrawal failed.")
    
    time.sleep(random.randint(5, 9))  # Сон в интервале от 5 до 9 секунд между снятиями, можете указать свой для ускорения или замедления процесса
