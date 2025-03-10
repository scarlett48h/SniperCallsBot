import logging

class IndicatorBase:
    def __init__(self, config, indicator_name):
        self.logger = logging.getLogger(f"{self.__class__.__name__}-{indicator_name}")
        self.config = config
        self.indicator_name = indicator_name

    def calculate(self, market_data):
        raise NotImplementedError("Method calculate must be overridden in subclasses.")

class SimpleMovingAverageIndicator(IndicatorBase):
    def __init__(self, config, indicator_name="SMA"):
        super().__init__(config, indicator_name)
        self.period = self.config.getint('indicators', indicator_name + '_period', fallback=20)

    def calculate(self, market_data):
        self.logger.debug("Calculating SMA...")
        prices = market_data.get_historical_prices(period=self.period)
        if not prices:
            self.logger.warning("Not enough data to calculate SMA.")
            return None
        return sum(prices) / len(prices) if prices else None

class RSIIndicator(IndicatorBase):
    def __init__(self, config, indicator_name="RSI"):
        super().__init__(config, indicator_name)
        self.period = self.config.getint('indicators', indicator_name + '_period', fallback=14)

    def calculate(self, market_data):
        self.logger.debug("Calculating RSI...")
        prices = market_data.get_historical_prices(period=self.period * 2)
        if not prices:
            self.logger.warning("Not enough data to calculate RSI.")
            return None
        return random.uniform(30, 70)

class IndicatorManager:
    def __init__(self, config):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config = config
        self.indicators = self.load_indicators(config)

    def load_indicators(self, config):
        indicators_config = config.get('indicators', 'enabled_indicators').split(',')
        loaded_indicators = {}
        for indicator_name in indicators_config:
            indicator_name = indicator_name.strip()
            if not indicator_name:
                continue
            try:
                indicator_class_name = config.get('indicators', indicator_name + '_class')
                if not indicator_class_name:
                    self.logger.warning(f"No class specified for indicator: {indicator_name}")
                    continue

                indicator_class = globals().get(indicator_class_name)
                if not indicator_class or not issubclass(indicator_class, IndicatorBase):
                    self.logger.error(f"Invalid indicator class '{indicator_class_name}' for '{indicator_name}'.")
                    continue

                indicator_instance = indicator_class(config, indicator_name)
                loaded_indicators[indicator_name] = indicator_instance
                self.logger.info(f"Indicator '{indicator_name}' loaded: {indicator_class_name}")
            except Exception as e:
                self.logger.exception(f"Error loading indicator '{indicator_name}': {e}")

        return IndicatorCollection(loaded_indicators)

    def calculate_indicators(self, market_data):
        indicators_data = {}
        for indicator_name, indicator in self.indicators.indicators.items():
            try:
                indicator_value = indicator.calculate(market_data)
                if indicator_value is not None:
                    indicators_data[indicator_name] = indicator_value
            except Exception as e:
                self.logger.exception(f"Error calculating indicator '{indicator_name}': {e}")
        return indicators_data

class IndicatorCollection:
    def __init__(self, indicators):
        self.indicators = indicators

    def get_indicator(self, indicator_name):
        return self.indicators.get(indicator_name)

    def get_all_indicators(self):
        return list(self.indicators.values())

def load_indicators(config):
    return IndicatorManager(config)
