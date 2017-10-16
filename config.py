import os

SPIDER_MAIN = os.path.abspath(os.path.join('crawlword', 'main.py'))
SQLITE_DB = os.path.abspath(os.path.join('data', 'dump.db'))
SQLITE_SCHEMA = os.path.abspath(os.path.join('data', 'schema.sql'))
CJK_IMAGE_DIR = os.path.abspath(os.path.join('data', 'cjkimages'))
PHANTOMJS_PATH = os.path.abspath(os.path.join('bin', 'phantomjs-2.1.1-windows', 'bin', 'phantomjs.exe'))
CAPTURE_JS = os.path.abspath(os.path.join('data', 'js', 'capture_element.js'))
CJK_SERVER_URLS = {
	'cjk': 'http://localhost:8888/unicode/list/cjk-ideo',
	'cjka': 'http://localhost:8888/unicode/list/cjk-ideo-a',
	'cjkb': 'http://localhost:8888/unicode/list/cjk-ideo-b',
	'cjkc': 'http://localhost:8888/unicode/list/cjk-ideo-c?font=HanaMin',
	'cjkd': 'http://localhost:8888/unicode/list/cjk-ideo-d?font=HanaMin', # 'cjkd': 'http://localhost:8888/unicode/list/cjk-ideo-d?font=BabelStone',
	'cjke': 'http://localhost:8888/unicode/list/cjk-ideo-e?font=HanaMin',
	'cjkf': 'http://localhost:8888/unicode/list/cjk-ideo-f?font=BabelStone'
}