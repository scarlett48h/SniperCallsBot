import logging

class StrategyBravoRev1(StrategyBase):
    def process_data_feed(self, market_data, indicators_data):
        processed_value = 0
        model_weights = self.config.get('model_weights', [0.1, 0.9, 10])
        for item in market_data: # Using market_data
            processed_value += item['price'] * random.uniform(model_weights[0], model_weights[1]) # Using market_data
        if processed_value > model_weights[2]:
            return 'LONG'
        else:
            return 'SHORT'
