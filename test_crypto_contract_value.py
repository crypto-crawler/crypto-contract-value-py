#!/usr/bin/env python3

from crypto_contract_value import MarketType, get_contract_value


def test_binance():
    assert get_contract_value("binance", MarketType['spot'], 'BTCUSDT') == 1.0
    assert get_contract_value(
        "binance", MarketType['inverse_swap'], 'BTCUSD') == 100.0
    assert get_contract_value(
        "binance", MarketType['inverse_swap'], 'ETHUSD') == 10.0
    assert get_contract_value(
        "binance", MarketType['linear_swap'], 'BTCUSDT') == 1.0
    assert get_contract_value(
        "binance", MarketType['linear_swap'], 'ETHUSDT') == 1.0
