import os, subprocess, sqlite3
from optparse import OptionParser

import config
import services


if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option('-a', '--action', dest='action', help='action')
	parser.add_option('-e', '--extra', dest='extra', help='extra arguments for the action')
	(options, args) = parser.parse_args()

	if options.action == 'create-db':
		services.create_db(config.SQLITE_DB, config.SQLITE_SCHEMA)
	elif options.action == 'load-db':
		services.load_db(config.SQLITE_DB)
	elif options.action == 'run-server':
		services.run_server(config.SQLITE_DB)
	elif options.action == 'capture-image':
		# please start server in another process first
		services.capture_image(
			config.PHANTOMJS_PATH, 
			config.CAPTURE_JS, 
			config.CJK_SERVER_URLS,
			config.CJK_IMAGE_DIR
		)
	elif options.action == 'run-spider':
		services.run_spider(config.SPIDER_MAIN)
	else:
		print('Bye!')

	print('\a\a\a')