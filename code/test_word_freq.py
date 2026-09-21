"""word_freq.py 的自动化测试（标准库 unittest，无需第三方依赖）。

运行方法：
    python -m unittest test_word_freq -v     # 详细输出
或
    python test_word_freq.py                 # 简洁输出
"""
import unittest

from word_freq import count_words, format_result, tokenize


class TestTokenize(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(tokenize(''), [])
        self.assertEqual(tokenize('   '), [])

    def test_english_lowercase_and_split(self):
        self.assertEqual(tokenize('Hello, World! Hello.'), ['hello', 'world', 'hello'])

    def test_numbers_and_letters(self):
        self.assertEqual(tokenize('v2 v3 42'), ['v2', 'v3', '42'])

    def test_chinese_single_char(self):
        self.assertEqual(tokenize('你好，世界'), ['你', '好', '世', '界'])


class TestCountWords(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_words('a b a c a'), {'a': 3, 'b': 1, 'c': 1})


class TestFormatResult(unittest.TestCase):
    def test_sorted_by_freq_then_alphabet(self):
        self.assertEqual(format_result(count_words('b a a c')), 'a: 2\nb: 1\nc: 1')

    def test_tie_uses_alphabetical_order(self):
        self.assertEqual(format_result(count_words('c b a')), 'a: 1\nb: 1\nc: 1')


if __name__ == '__main__':
    unittest.main()
