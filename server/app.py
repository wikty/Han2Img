# -*- coding: utf-8 -*-
import os
import tornado.ioloop
import tornado.web

# from db import get_ideograph_by_codepoint, get_all_of_ideographs, get_ideographs_by_block, get_all_of_blocks, get_all_of_fonts
from db import Cjkfonts, Cjkblocks, Ideographs

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('Hello World!')

class UnicodeHandler(tornado.web.RequestHandler):
	def initialize(self, db):
		self.db = db

	def get(self, codepoint):
		codepoint = codepoint.upper()
		ideo = Ideographs.get_one_by_codepoint(self.db, codepoint)
		# ideograph = get_ideograph_by_codepoint(self.db, codepoint)
		if not ideo:
			content = ''
		else:
			content = ideo['ideograph']
		self.render('unicode.html', title='CJK - Unicode', content=content, width='300px')

class UnicodeListHandler(tornado.web.RequestHandler):
	def initialize(self, db, view):
		self.db = db
		self.view = view

	def get(self, block=''):
		font = self.get_query_argument('font', '').lower()
		if not font:
			font = None
		else:
			fonts = {}
			for item in Cjkfonts.get_all(self.db):
				fonts[item['abbr'].lower()] = (item['name'], item['family'])
			font = fonts.get(font, None)
		blockabbr = self.get_query_argument('block', '') if not block else block
		if not blockabbr:
			items = Ideographs.get_all(self.db)
		else:
			items = Ideographs.get_many_by_block(self.db, blockabbr)
		if not items:
			items = []
		ideographs = []
		for item in items:
			ideographs.append((item['ideograph'], item['codepoint']))
		blocks = []
		blockrange = ''
		blockname = ''
		for item in Cjkblocks.get_all(self.db):
			blocks.append((item['abbr'], item['name'], item['range']))
			if blockabbr == item['abbr']:
				blockrange = item['range']
				blockname = item['name']

		if self.view:
			self.render('unicode-list-display.html', **{
				'title': 'CJK - Unicode View List',
				'ideographs': ideographs,
				'blocks': blocks,
				'blockabbr': blockabbr,
				'blockname': blockname,
				'blockrange': blockrange,
				'font': font
			})
		else:
			self.render('unicode-list.html', **{
				'title': 'CJK - Unicode List',
				'ideographs': ideographs,
				'font': font
			})

def run(db, port=None):
	port = 8888 if not port else port
	currentdir = os.path.dirname(os.path.abspath(__file__))
	settings = {
		'template_path': os.path.join(currentdir, 'templates')
	}
	app = tornado.web.Application([
		(r"/", MainHandler),
		(r"/unicode/u([0-9a-fA-F]+)", UnicodeHandler, dict(db=db)),
		(r"/unicode/list", UnicodeListHandler, dict(db=db, view=False)),
		(r"/unicode/list/([-\w]*)", UnicodeListHandler, dict(db=db, view=False)),
		(r"/unicode/view/list", UnicodeListHandler, dict(db=db, view=True)),
		(r"/unicode/view/list/([-\w]*)", UnicodeListHandler, dict(db=db, view=True)),
	], **settings)
	app.listen(port)
	print('Start server listening on: http://localhost:%d' % port)
	tornado.ioloop.IOLoop.current().start()