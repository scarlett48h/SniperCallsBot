class StrategyEchoBeta(StrategyBase):
    def calculate_flow_index(self, market_data, indicators_data):
        flow_value = 0
        momentum_factor = self.config.getfloat('momentum_factor', 2.0)
        for data_point in market_data:
            value = data_point['volume']
            flow_value += value * math.log(momentum_factor + 2)
        if flow_value > momentum_factor * 20:
            return 'INITIATE_FLOW'
        else:
            return 'MAINTAIN_STATE'
