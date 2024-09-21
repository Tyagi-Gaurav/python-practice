pip install MetaTrader5
pip install pandas matplotlib
pip install jupyterlab
pip install notebook


aJob()
 .triggerEvery()
 .when(condition(), then(apply(strategy1)), closeItself())
 .when(condition(), then(apply(strategy2)), closeInTime())
