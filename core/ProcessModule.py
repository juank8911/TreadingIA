from ProcessModel import ProcessModel


class ProcessModule:

    def __init__(self):
        self.trading_module = TradingModule()

    def start_trading(self):
        for trading_model in self.trading_module.get_trading_models():
            trading_model.open_position()

    def stop_trading(self):
        for trading_model in self.trading_module.get_trading_models():
            trading_model.close_position()

    def update_trading_positions(self):
        for trading_model in self.trading_module.get_trading_models():
            trading_model.update_position()