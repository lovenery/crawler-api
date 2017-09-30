import unittest

import ptt

class TestPttCrawler(unittest.TestCase):
    def test_ptt_start(self):
        next_url, results = ptt.start('https://www.ptt.cc/bbs/Beauty/index2.html')
        self.assertEqual(results[0][0], '[猜題] 猜古代美女 (11)')
        self.assertEqual(next_url, 'https://www.ptt.cc/bbs/Beauty/index1.html')
    def test_ptt_start_at_the_end(self):
        next_url, results = ptt.start('https://www.ptt.cc/bbs/Beauty/index1.html')
        self.assertEqual(next_url, 'https://www.ptt.cc/bbs/Beauty/index1.html')

if __name__ == '__main__':
    unittest.main()