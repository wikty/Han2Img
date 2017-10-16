CREATE TABLE IF NOT EXISTS ideographs (
	id INTEGER PRIMARY KEY autoincrement,
	ideograph TEXT NOT NULL,
	codepoint TEXT UNIQUE NOT NULL,
	html TEXT NOT NULL,
	block TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS cjkblocks (
	id INTEGER PRIMARY KEY autoincrement,
	name TEXT NOT NULL,
	abbr TEXT UNIQUE NOT NULL,
	range TEXT NOT NULL,
	chart_url TEXT NOT NULL,
	wikipedia_url TEXT NOT NULL,
	ref_url TEXT NOT NULL,
	description TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS cjkfonts (
	id INTEGER PRIMARY KEY autoincrement,
	name TEXT NOT NULL,
	abbr TEXT NOT NULL,
	family TEXT NOT NULL,
	description TEXT NOT NULL
);