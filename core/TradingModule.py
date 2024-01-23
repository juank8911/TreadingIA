from TradingModel import TradingModel


class TradingModule:

    def __init__(self):
        self.trading_models = []

    def add_trading_model(self, trading_model):
        self.trading_models.append(trading_model)

    def get_trading_models(self):
        return self.trading_models

    def open_trading_position(self, trading_model):
        trading_model.open_position()

    def close_trading_position(self, trading_model):
        trading_model.close_position()

    def get_trading_positions(self):
        trading_positions = []
        for trading_model in self.trading_models:
            if trading_model.state == "open":
                trading_positions.append(trading_model)
        return trading_positions
