import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), 
                       (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], 
                        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), 
                       (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], 
                        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_missingTopBid(self):
    quote = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'id': '0.109974697771', 'stock': 'ABC'}
    with self.assertRaises(KeyError):
      getDataPoint(quote) 

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_missingTopAsk(self):
    quote = {'top_bid': {'price': 120.48, 'size': 109}, 'timestamp': '2019-02-11 22:06:30.572453', 'id': '0.109974697771', 'stock': 'DEF'}
    with self.assertRaises(KeyError):
      getDataPoint(quote)

  def test_getDataPoint_invalidPriceType(self):
    quote = {'top_ask': {'price': '121.2', 'size': 36}, 'top_bid': {'price': '120.48', 'size': 109}, 'timestamp': '2019-02-11 22:06:30.572453', 'id': '0.109974697771', 'stock': 'ABC'}
    with self.assertRaises(TypeError):
      getDataPoint(quote)


if __name__ == '__main__':
    unittest.main()
