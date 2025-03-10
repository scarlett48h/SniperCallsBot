import logging

class StrategyDeltaZ(StrategyBase):
    def scan_market_signals(self, market_data, indicators_data):
        detected_signals = []
        sensitivity_level = self.config.getfloat('sensitivity_level', 0.8)
        for data_point in market_data:
            signal = data_point['price']
            if signal > sensitivity_level:
                detected_signals.append(signal)
        return detected_signals
