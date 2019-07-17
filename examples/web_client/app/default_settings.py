from flask import make_response
from flask_socketio import SocketIO

from ctpbee import ExtAbstract
from ctpbee.constant import LogData, AccountData, ContractData, BarData, OrderData, PositionData, TickData, SharedData, \
    TradeData


class DefaultSettings(ExtAbstract):

    def __init__(self, name, app, socket_io: SocketIO):
        super().__init__(name, app)
        self.io = socket_io

    def on_log(self, log: LogData):
        data = {
            "type": "log",
            "data": log
        }
        self.io.send(data)

    def on_account(self, account: AccountData) -> None:
        data = {
            "type": "account",
            "data": account._to_dict()
        }
        self.io.send(data)

    def on_contract(self, contract: ContractData):
        data = {
            "type": "contract",
            "data": contract._to_dict()
        }
        self.io.send(data)

    def on_bar(self, bar: BarData) -> None:
        data = {
            "type": "bar",
            "data": bar._to_dict()
        }
        self.io.send(data)

    def on_order(self, order: OrderData) -> None:
        data = {
            "type": "order",
            "data": order._to_dict()
        }
        self.io.send(data)

    def on_position(self, position: PositionData) -> None:
        data = {
            "type": "position",
            "data": self.app.recorder.get_all_positions()
        }
        self.io.send(data)

    def on_tick(self, tick: TickData) -> None:
        data = {
            "type": "tick",
            "data": tick._to_dict()
        }
        self.io.send(data)

    def on_shared(self, shared: SharedData) -> None:
        data = {
            "type": "shared",
            "data": shared._to_dict()
        }
        self.io.send(data)

    def on_trade(self, trade: TradeData) -> None:
        data = {
            "type": "trade",
            "data": trade._to_dict()
        }
        self.io.send(data)


def true_response(data="", message="操作成功执行"):
    true_response = {
        "result": "success",
        "data": data,
        "message": message
    }
    return make_response(true_response)


def false_response(data="", message="出现错误, 请检查"):
    false_response = {
        "result": "error",
        "data": data,
        "message": message
    }
    return make_response(false_response)


def warning_response(data="", message="警告"):
    warning_response = {
        "result": "warning",
        "data": data,
        "message": message
    }
    return make_response(warning_response)