from datetime import datetime, timedelta
import os

def utf8len(s):
	return len(s.encode('utf-8')) + s.count("\n")

HEADER = '<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee</title><link>http://t.ly</link><description>Eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee</description>\n'
FOOTER = '</channel></rss>'
ITEM = '<item><title></title><link></link><description>E</description><pubDate>{cnt}</pubDate></item>\n'
DATE_FORMAT = '%Y%m%d'

size_limit = 5 * 1024**2 #thats MiB not MB
date_counter = datetime(1900, 1, 1)

item_size = utf8len(ITEM.format(cnt=date_counter.strftime(DATE_FORMAT)))
num_items = (size_limit - utf8len(HEADER + FOOTER)) // item_size
num_files = 1
force = True

for n in range(num_files):
	file_name = f'../rss.xml'
	# file_name = f'../rss{n+1:02}.xml'
	if not force and os.path.exists(file_name):
		date_counter += timedelta(days=num_items)
		continue

	with open(file_name, 'w', encoding='utf-8') as f:
		f.write(HEADER)
		for i in range(num_items):
			f.write(ITEM.format(cnt=date_counter.strftime(DATE_FORMAT)))
			date_counter += timedelta(days=1)
		f.write(FOOTER)
