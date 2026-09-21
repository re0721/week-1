"""文本词频统计程序。

统计一段文本中每个"词"出现的次数，按频率降序（同频按字典序升序）输出。

分词规则：
  - 英文/数字：按连续字母数字串切分（统一转小写），如 "Hello, World" -> hello, world
  - 中文：按单个汉字切分（如 "你好" -> 你, 好）
    （中文真正分词需用 jieba 等工具，这里用单字切分作为简化。）

用法：
  python word_freq.py <输入文件>      # 从文件读文本
  echo "some text" | python word_freq.py   # 从标准输入读文本
"""
import re
import sys
from collections import Counter


def tokenize(text: str) -> list[str]:
    """把文本切成词列表。空文本返回空列表。"""
    if not text:
        return []
    # [a-z0-9]+ 匹配英文单词/数字；[一-鿿] 匹配单个汉字
    return re.findall(r'[a-z0-9]+|[一-鿿]', text.lower())


def count_words(text: str) -> Counter:
    """统计词频，返回 Counter（词 -> 出现次数）。"""
    return Counter(tokenize(text))


def format_result(counter: Counter) -> str:
    """把词频格式化成字符串：频率降序，同频按字典序升序，每行 "词: 次数"。"""
    items = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
    return '\n'.join(f'{word}: {count}' for word, count in items)


def main(argv=None) -> None:
    """入口：从文件（第一个参数）或标准输入读取文本，打印词频统计。"""
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        with open(argv[0], encoding='utf-8') as handle:
            text = handle.read()
    else:
        text = sys.stdin.read()
    print(format_result(count_words(text)))


if __name__ == '__main__':
    main()
