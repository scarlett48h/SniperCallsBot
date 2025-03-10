import logging
import random

class RiskManager:
    def __init__(self, config):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config = config
        self.max_risk_per_trade = self.config.getfloat('risk_management', 'max_risk_per_trade', fallback=0.01)

    def manage_risks(self, signals):
        trades = []
        for strategy_name, signal in signals.items():
            trade = self.create_trade_from_signal(strategy_name, signal)
            if trade:
                trades.append(trade)
        return trades

    def create_trade_from_signal(self, strategy_name, signal):
        if signal == "BUY":
            trade_type = "LONG"
        elif signal == "SELL":
            trade_type = "SHORT"
        else:
            return None

        position_size = random.uniform(0.01, 0.1)
        stop_loss_level = random.uniform(0.95, 0.99)

        trade = TradeOrder(
            strategy_name=strategy_name,
            trade_type=trade_type,
            position_size=position_size,
            )
        self.logger.info(f"Trade created: {trade}")
        return trade

class TradeOrder:
    def __init__(self, strategy_name, trade_type, position_size, stop_loss_level):
        self.strategy_name = strategy_name
        self.trade_type = trade_type
        self.position_size = position_size
        self.stop_loss_level = stop_loss_level

    def __str__(self):
        return (f"TradeOrder(strategy='{self.strategy_name}', type='{self.trade_type}', "
                f"size={self.position_size:.2f}, stop_loss={self.stop_loss_level:.4f})")