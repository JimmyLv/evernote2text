import html2text
import os
import codecs

for root, dirs, files in os.walk('./My Notes'):
	for file in files:
		if file.find('.html') != -1:
			short_name = file[0:6]+".html"
			filename = os.path.join(root,file).split(".html")[0]
			with codecs.open(os.path.join(root,file[0:6])+'.md', 'w', 'utf-8') as outfile, codecs.open(filename+".html", 'r', 'utf-8') as infile:
				html_data = infile.read()
				md_data = html2text.html2text(html_data)
				outfile.write(md_data)
