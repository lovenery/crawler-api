import unittest

import ptt

class TestPttCrawler(unittest.TestCase):
    def test_ptt_start(self):
        next_url, results = ptt.start('https://www.ptt.cc/bbs/Beauty/index2.html')
        self.assertEqual(results[0][0], '[情報] 我的電車男大變身')
        self.assertEqual(next_url, 'https://www.ptt.cc/bbs/Beauty/index1.html')

if __name__ == '__main__':
    unittest.main()