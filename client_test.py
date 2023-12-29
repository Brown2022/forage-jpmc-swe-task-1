import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    result1 = getDataPoint(quotes)
    self.assertEqual(result1, {'stock': 'ABC', 'bid_price': 120.48, 'ask_price': 121.2, 'price': (120.48 + 121.2) / 2})

    self.assertEqual(result1, {'stock': 'DEF', 'bid_price': 117.87, 'ask_price': 121.68, 'price': (117.87 + 121.68) / 2})

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    result2 = getDataPoint(quotes)
    self.assertEqual(result2, {'stock': 'ABC', 'bid_price': 128.48, 'ask_price': 119.2, 'price': (128.48 + 119.2) / 2})

    self.assertEqual(result2, {'stock': 'DEF', 'bid_price': 117.87, 'ask_price': 121.68, 'price': ( 117.87 + 121.68 ) / 2})


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
