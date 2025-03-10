import logging
import random
import os
import importlib

import src.indicators as indicators

class StrategyBase:
    def __init__(self, config, strategy_name):
        self.logger = logging.getLogger(f"{self.__class__.__name__}-{strategy_name}")
        self.config = config
        self.strategy_name = strategy_name

    def generate_signal(self, market_data, indicators_data):
        raise NotImplementedError("Method generate_signal must be overridden in subclasses.")

class StrategyManager:
    def __init__(self, config):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config = config
        self.strategies = self.load_strategies(config)

    def load_strategies(self, config):
        return
        for filename in os.listdir("strategies"):
            if filename.startswith("strategy_") and filename.endswith(".py"):
                module_name = filename[:-3]
                module_path = os.path.join('strategies', filename)
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and obj.__name__.startswith("Strategy") and obj.__base__.__name__ == "StrategyBase":
                        strategy_name = obj.__name__
                        strategies[strategy_name] = obj

class StrategyCollection:
    def __init__(self, strategies):
        self.strategies = strategies

    def get_strategy(self, strategy_name):
        return self.strategies.get(strategy_name)

    def get_all_strategies(self):
      return list(self.strategies.values())

def load_strategies(config):
    return StrategyManager(config)