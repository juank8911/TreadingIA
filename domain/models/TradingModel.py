class TradingModel:

    def __init__(self, type, symbol, quantity, price, side, timestamp, state, gain_loss, leverage, max_price, min_price):
        self.type = type
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.side = side
        self.timestamp = timestamp
        self.state = state
        self.gain_loss = gain_loss
        self.leverage = leverage
        self.max_price = max_price
        self.min_price = min_price

    def __repr__(self):
        return f"TradingModel(type={self.type}, symbol={self.symbol}, quantity={self.quantity}, price={self.price}, side={self.side}, timestamp={self.timestamp}, state={self.state}, gain_loss={self.gain_loss}, leverage={self.leverage}, max_price={self.max_price}, min_price={self.min_price})"
