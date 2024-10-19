import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Access values from the configuration file
trading_direction = config.get('Trading', 'Direction')

# Return a dictionary with the retrieved values
cfg = {
    'trading_type': trading_direction
}


def allowed_sell_trading(_):
    return cfg['trading_type'] == 'SELL' or cfg['trading_type'] == 'BOTH'


def allowed_buy_trading(_):
    return cfg['trading_type'] == 'BUY' or cfg['trading_type'] == 'BOTH'
