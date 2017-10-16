import json

from .client import insert_many, get_one, get_many, get_all
from .cjkblocks import get_range

class Ideographs(object):

	tblname = 'ideographs'

	fields = {
		'ideograph': '',
		'codepoint': '',
		'html': '',
		'block': ''
	}

	insert_sql = '''INSERT INTO {tblname}
	(ideograph, codepoint, html, block)
	VALUES
	(
		"{ideograph}",
		"{codepoint}",
		"{html}",
		"{block}"
	);'''

	@classmethod
	def generate(cls, output='list', tblname=''):
		'''
		output = list or json or sql
		'''
		tblname = tblname if tblname else cls.tblname
		cjk_blocks = get_range()
		ideographs = []
		for block, block_range in cjk_blocks:
			block_low, block_high = block_range.split('-')
			for i in range(int(block_low, 16), int(block_high, 16)+1):
				ideo = cls.fields.copy()
				ideo['ideograph'] = chr(i)
				ideo['codepoint'] = hex(i)[2:].upper()
				ideo['html'] = '&#%d;' % i
				ideo['block'] = block
				ideographs.append(ideo)
		
		if output == 'json':
			return json.dumps(ideographs, ensure_ascii=False)
		elif output == 'sql':
			sqls = []
			for ideo in ideographs:
				sql = cls.insert_sql.format(
					tblname=tblname,
					ideograph=ideo['ideograph'],
					codepoint=ideo['codepoint'],
					html=ideo['html'],
					block=ideo['block']
				)
				sqls.append(sql)
			return '\n'.join(sqls)
		else:
			return ideographs

	@classmethod
	def insert(cls, conn):
		return insert_many(conn, cls.generate(), cls.tblname)

	@classmethod
	def get_one_by_codepoint(cls, conn, codepoint):
		where_condition = "codepoint='{}'".format(codepoint)
		return get_one(conn, cls.tblname, where_condition)

	@classmethod
	def get_many_by_block(cls, conn, block):
		where_condition = "block='{}'".format(block)
		return get_many(conn, cls.tblname, where_condition)

	@classmethod
	def get_all(cls, conn, sort_by='codepoint'):
		return get_all(conn, cls.tblname, sort_by)