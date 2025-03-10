class StrategyFusionV3(StrategyBase):
    def process_binary_input(self, market_data, indicators_data):
        current_state = 0
        logic_gates = self.config.get('logic_gates', ['AND', 'OR'])
        binary_data = [1, 0, 1]
        for gate in logic_gates:
            if gate == 'AND':
                current_state &= binary_data.pop(0)
            elif gate == 'OR':
                current_state |= binary_data.pop(0)
        return current_state
