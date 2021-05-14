from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *

symbol_test_list = ["xrpusdt"]
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
for symbol_test in symbol_test_list:
    list_obj = trade_client.get_history_orders(symbol=symbol_test, start_time=None, end_time=None, size=200, direct=None)
    LogInfo.output_list(list_obj)















