import sqlite3, os, subprocess

import db
from server import run as server_run


def create_db(db_file, schema_file):
	return db.create_db(db_file, schema_file)

def load_db(db_file):
	conn = db.connect_db(db_file)
	db.Cjkfonts.insert(conn)
	db.Cjkblocks.insert(conn)
	db.Ideographs.insert(conn)

def run_server(db_file):
	return server_run(db.connect_db(db_file))

def capture_image(phantomjs_path, capture_js, urls, image_dir):
	for key in sorted(urls.keys()):
		item_dir = os.path.join(image_dir, key)
		if not os.path.exists(item_dir):
			os.makedirs(item_dir)
		url = urls[key]
		selector = '.u span'
		zoomfactor = '6'
		try:
			output = subprocess.check_output(
				[phantomjs_path, capture_js, url, selector, item_dir, zoomfactor],
				stderr=subprocess.STDOUT, 
				shell=True)
		except subprocess.CalledProcessError as e:
			output = e.output
			raise e

def run_spider(spider_main, spider_name):
	output = subprocess.check_out(
		['python', spider_main, '-n', spider_name],
		stderr=subprocess.STDOUT,
		shell=True
	)
	return output