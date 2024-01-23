from distutils import config
from typing import Self
import requests
import json
import pandas as pd

class DataService:

    def __init__(self):
        self.api_key = config["binance"]["api_key"]
        self.api_secret = config["binance"]["api_secret"]
        self.base_url = config["binance"]["api3"]
        self.exchange_info = None

def get_exchange_info(self):
    """Obtiene la información del exchange, filtrando los símbolos relevantes."""

    url = f"{self.base_url}/api/v3/exchangeInfo"  # Endpoint correcto para información general
    response = requests.get(url)
    response.raise_for_status()

    data = json.loads(response.text())

    # Filtra los símbolos que se encuentran en estado "TRADING"
    symbols = [symbol for symbol in data["symbols"] if symbol["status"] == "TRADING"]

    # Extrae los campos relevantes para la selección de monedas
    filtered_symbols = []
    for symbol in symbols:
        filtered_symbol = {
            "symbol": symbol["symbol"],
            "baseAsset": symbol["baseAsset"],
            "quoteAsset": symbol["quoteAsset"],
            "minPrice": symbol["minPrice"],
            "maxPrice": symbol["maxPrice"],
            "filters": symbol["filters"],
            "orderTypes": symbol["orderTypes"],
            "marginTradingEnabled": symbol["marginTradingEnabled"],
            "isSpotTradingAllowed": symbol["isSpotTradingAllowed"],
        }
        filtered_symbols.append(filtered_symbol)

    return filtered_symbols

def get_historical_klines(self, symbol, interval, start_time, end_time):

    url = f"{self.base_url}/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&endTime={end_time}"
  # Realiza la solicitud a la API
    response = requests.get(url)
  # Verifica el estado de la respuesta
    if response.status_code != 200:
        raise Exception(f"Error al obtener los datos históricos de kline: {response.status_code}")
  # Decodifica la respuesta
    data = response.json()
  # Procesa los datos
    for candle in data:
      # Calcula la ganancia potencial
        candle["ganancia_potencial"] = candle["close"] - candle["open"]
      # Calcula el riesgo de stop-loss
        candle["riesgo_stop_loss"] = candle["close"] * (1 - self.stop_loss)
      # Calcula el precio máximo
        candle["precio_maximo"] = candle["high"]
      # Calcula el precio mínimo
        candle["precio_minimo"] = candle["low"]
      # Calcula la cantidad de transacciones necesarias
        candle["cantidad_transacciones"] = candle["ganancia_potencial"] / candle["riesgo_stop_loss"]
      # Calcula el apalancamiento posible
        candle["apalancamiento_posible"] = candle["cantidad_transacciones"] / self.capital

    return data
        
