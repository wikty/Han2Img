import json

from .client import insert_many, get_all

data = [(
	'新细明体',
	'PMingLiU',
	'PMingLiU, PMingLiu-ExtB',
	"[BabelStone Han](http://www.babelstone.co.uk/Fonts/Han.html) 字体支持 Unicode 10.0，包含超过 3 万个 CJK 字符，同时支持简体和繁体汉字。字体作者是通过合并由 [Arphic Technology](http://www.arphic.com.tw/)（文鼎科技）制作的两个字体来生成 BabelStone Han 字体的。BabelStone Han 字体支持常用 Unicode 字符以及 CJK, CJK-A, CJK-B, CJK-C, CJK-D, CJK-E, CJK-F 中的大部分字符，该字体还在持续更新，作者将主要精力集中在 CJK-C 之后字符的支持，当前字体对字符的支持情况如下：CJK(100%), CJK-A(36.6%), CJK-B(17.5%), CJK-C(100%), CJK-D(100%), CJK-E(67.1%), CJK-F(61.8%)。并且该字体的字形遵从 Unicode 发布的 [Charts](http://www.unicode.org/charts/) 文档中所列字形，这些字形是由国家标准化管理委员会监制的，因此适合在中国使用。"
),(
	'中易宋体',
	'SimSun',
	'SimSun, SimSun-ExtB',
	"由 [SimSun](https://www.microsoft.com/typography/fonts/font.aspx?FMID=2165) 和 [SimSun-ExtB](https://www.microsoft.com/typography/fonts/font.aspx?FMID=1648) 两部分组成。该字体内置于 Windows，其中 SimSun 支持 CJK Symbols And Punctuation, CJK Compatibility, CJK Unified Ideographs, CJK Radicals Supplement, Kangxi Radicals, Ideographic Description Characters, CJK Unified Ideograph Extension A, CJK Unified Ideographs Extension B, CJK Compatibility Ideographs, CJK Compatibility Ideographs Supplement CJK Compatibility Forms 等，SimSun-ExtB 支持 [Unicode Plane 0]((http://www.unicode.org/roadmaps/bmp/)) 范围以外的字符，而 CJK 字符主要分布在 Unicode Plane 0 和 [Unicode Plane 2](http://www.unicode.org/roadmaps/sip/) 中，因此结合 SimSun 和 SimSun-ExtB 理论上可以显示 CJK 所有字符，而事实上经过测试 CJK Unified Ideograph Extension C 到 F 的字符仍然无法显示。"
),(
	'花园明朝',
	'HanaMin',
	'HanaMinA, HanaMinB',
	"[花园明朝字体](http://fonts.jp/hanazono/) 对 Unicode 的支持十分全面，大概支持 10 万个字符的显示，可以从官网下载该字体，由 HanaMinA 和 HanaMinB 两个字体文件构成，HanaMinA 主要支持常用字符、CJK 常用字符以及 HKSCS 字符等，HanaMinB 则支持 CJK-B, CJK-C, CJK-D, CJK-E 的所有字符。该字体被古籍网站[中国哲学书电子化计划](http://ctext.org/zhs)推荐作为浏览网站的预装字体。不过该字体有一个缺点在于，字形符合日本的使用方式，因此字符显示看起来跟中文会有点不一样。"
),(
	'BabelStone Han',
	'BabelStone',
	'BabelStone Han',
	"由 [MingLiU](https://www.microsoft.com/typography/fonts/font.aspx?FMID=2140) 和 [MingLiU-ExtB](https://www.microsoft.com/typography/fonts/font.aspx?FMID=1772) 两部分组成。其中 MingLiU 支持 CJK Compatibility, CJK Unified Ideographs, CJK Radicals Supplement, Kangxi Radicals, Ideographic Description Characters, CJK Unified Ideograph Extension A, CJK Unified Ideographs Extension B, CJK Compatibility Ideographs, CJK Compatibility Ideographs Supplement, CJK Compatibility Forms 等字符，MingLiU-ExtB 支持 [Unicode Plane 0]((http://www.unicode.org/roadmaps/bmp/)) 范围以外的字符，而 CJK 字符主要分布在 Unicode Plane 0 和 [Unicode Plane 2](http://www.unicode.org/roadmaps/sip/) 中，因此结合 MingLiU 和 MingLiU-ExtB 理论上可以显示 CJK 所有字符，经过测试后发现 CJK Unified Ideograph Extension C 到 F 的字符仍然无法显示。"
),(
	'香港增補字符集',
	'MingLiUHKSCS',
	'MingLiU_HKSCS, MingLiU_HKSCS-ExtB',
	"由 [MingLiU_HKSCS](https://www.microsoft.com/typography/fonts/font.aspx?FMID=1771) 和 [MingLiU_HKSCS-ExtB](https://www.microsoft.com/typography/fonts/font.aspx?FMID=1774) 两部分组成。"
)]

def get_data():
	fonts = []
	for item in data:
		fonts.append({
			'name': item[0],
			'abbr': item[1],
			'family': item[2],
			'description': item[3]
		})
	return fonts

class Cjkfonts(object):

	tblname = 'cjkfonts'

	fields = {
		'name': '',
		'abbr': '',
		'family': '',
		'description': ''
	}

	insert_sql = '''INSERT INTO {tblname}
	(name, abbr, family, description)
	VALUES
	(
		"{font_name}",
		"{font_abbr}",
		"{font_family}",
		"{font_description}"
	);'''

	@classmethod
	def generate(cls, output='list', tblname=''):
		'''
		output = dict or json or sql
		'''
		tblname = tblname if tblname else cls.tblname
		fonts = get_data()
		if output == 'json':
			return json.dumps(fonts, ensure_ascii=False)
		elif output == 'sql':
			sqls = []
			for font in fonts:
				sql = cls.insert_sql.format(
					tblname=tblname,
					font_name=font['name'],
					font_abbr=font['abbr'],
					font_family=font['family'],
					font_description=font['description']
				)
			return '\n'.join(sqls)
		else:
			return fonts

	@classmethod
	def insert(cls, conn):
		return insert_many(conn, cls.generate(), cls.tblname)

	@classmethod
	def get_all(cls, conn, sort_by='abbr'):
		return get_all(conn, cls.tblname, sort_by)