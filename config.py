import os

SPIDER_MAIN = os.path.abspath(os.path.join('crawlword', 'main.py'))
SQLITE_DB = os.path.abspath(os.path.join('data', 'dump.db'))
SQLITE_SCHEMA = os.path.abspath(os.path.join('data', 'schema.sql'))
CJK_IMAGE_DIR = os.path.abspath(os.path.join('data', 'cjkimages'))
PHANTOMJS_PATH = os.path.abspath(os.path.join('bin', 'phantomjs-2.1.1-windows', 'bin', 'phantomjs.exe'))
CAPTURE_JS = os.path.abspath(os.path.join('data', 'js', 'capture_element.js'))
CJK_SERVER_URLS = {
	# 'cjk': 'http://localhost:8888/unicode/list/cjk-ideo',
	# 'cjk-a': 'http://localhost:8888/unicode/list/cjk-ideo-a',
	# 'cjk-b': 'http://localhost:8888/unicode/list/cjk-ideo-b',
	# 'cjk-c': 'http://localhost:8888/unicode/list/cjk-ideo-c?font=HanaMin',
	# 'cjk-d': 'http://localhost:8888/unicode/list/cjk-ideo-d?font=HanaMin', # 'cjkd': 'http://localhost:8888/unicode/list/cjk-ideo-d?font=BabelStone',
	# 'cjk-e': 'http://localhost:8888/unicode/list/cjk-ideo-e?font=HanaMin',
	# 'cjk-f': 'http://localhost:8888/unicode/list/cjk-ideo-f?font=BabelStone'
    # 'cjk-radical': 'http://localhost:8888/unicode/list/cjk-radical?font=BabelStone',
    # 'cjk-radical-sup': 'http://localhost:8888/unicode/list/cjk-radical-sup?font=BabelStone',
    # 'cjk-stroke': 'http://localhost:8888/unicode/list/cjk-stroke?font=BabelStone',
    # 'cjk-punctuation': 'http://localhost:8888/unicode/list/cjk-punctuation?font=BabelStone',
    # 'cjk-ido-desc': 'http://localhost:8888/unicode/list/cjk-ideo-desc?font=BabelStone',
    # 'cjk-cmpt': 'http://localhost:8888/unicode/list/cjk-cmpt?font=BabelStone',
    # 'cjk-cmpt-form': 'http://localhost:8888/unicode/list/cjk-cmpt-form?font=BabelStone',
    # 'cjk-cmpt-ideo': 'http://localhost:8888/unicode/list/cjk-cmpt-ideo?font=BabelStone',
    # 'cjk-cmpt-ideo-sup': 'http://localhost:8888/unicode/list/cjk-cmpt-ideo-sup?font=BabelStone',
    # 'cjk-enclosed': 'http://localhost:8888/unicode/list/cjk-enclosed?font=BabelStone',
    # 'cjk-enclosed-sup': 'http://localhost:8888/unicode/list/cjk-enclosed-sup?font=BabelStone',
    'private-use-area': 'http://localhost:8888/unicode/list/private-use-area?font=MingLiUHKSCS',
}