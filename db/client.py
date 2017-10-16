import sqlite3

def create_db(db_file, schema_file, insert_db=False):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		with open(schema_file, 'r', encoding='utf8') as f:
			conn.executescript(f.read())
			conn.commit()
	except sqlite3.Error as e:
		print('SQLite3 Error: %s' % str(e))
		return False
	except Exception as e:
		print(e)
		return False
	if conn:
		conn.close()
	return True

def connect_db(db_file):
	return sqlite3.connect(db_file)

def insert_many(conn, items, tblname):
	'''
	items: list of dict, dict should match database table field
	'''
	keys = ', '.join(list(items[0].keys()))
	values = ', '.join([':%s' % k for k in items[0].keys()])
	conn.executemany('INSERT INTO {tblname} ({keys}) VALUES ({values});'.format(
			tblname=tblname,
			keys=keys,
			values=values
	), items)
	conn.commit()

def get_one(conn, tblname, where_condition):
	conn.row_factory = sqlite3.Row
	cursor = conn.execute('SELECT * FROM {tblname} WHERE {where_condition}'.format(
		tblname=tblname,
		where_condition=where_condition
	))
	return cursor.fetchone()

def get_many(conn, tblname, where_condition):
	conn.row_factory = sqlite3.Row
	cursor = conn.execute('SELECT * FROM {tblname} WHERE {where_condition}'.format(
		tblname=tblname,
		where_condition=where_condition
	))
	return cursor.fetchall()

def get_all(conn, tblname, orderby='id'):
	conn.row_factory = sqlite3.Row
	cursor = conn.execute('SELECT * FROM {tblname} ORDER BY {orderby}'.format(
		tblname=tblname,
		orderby=orderby
	))
	return cursor.fetchall()