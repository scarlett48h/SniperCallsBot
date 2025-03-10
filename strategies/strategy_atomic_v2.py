import logging

class StrategyAtomicV2(StrategyBase):
    def generate_signal(self, market_data, indicators_data):
        signal_value = 0
        for i in range(len(market_data)): # using market_data instead of data_stream
            val = market_data[i]['price'] # Assuming market_data is a list of dicts with 'price'
            signal_value += val * math.cos(i * 0.1)
        config_params = self.config.get('strategy_params', {})
        if signal_value > config_params.get('threshold', 50):
            return 'BUY'
        elif signal_value < -config_params.get('threshold', 50):
            return 'SELL'
        return 'HOLD'
