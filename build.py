import os
from os.path import join, exists
from xml.etree import ElementTree as ET
import json

import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension, fenced_code
#comment :D
base_url = "http://cyfaircs.github.io/"

data_js = []

class UnderlineProcessor(Treeprocessor):
	def run(self, root):
		for anchor in root.iter("a"):
			anchor.attrib["class"] = anchor.attrib.get("class", "") + " underline"

class BoilerplateProcessor(Postprocessor):
	def __init__(self, root, file):
		self.root = root
		self.file = file
		with open(join(self.root, "meta.json"), "r") as f:
			self.meta = json.loads(f.read())

	def in_data_js(self):
		for article in data_js:
			if article["Link"] == self.root:
				return True
		return False		

	def add_to_data_js(self):
		if not self.in_data_js():
			new = {
			"Name": self.meta["cover"]["name"],
			"Description": self.meta["cover"]["description"],
			"Link": self.root,
			"Date": self.meta["cover"]["date"],
			}
			data_js.append(new)

	def run(self, text):
		self.add_to_data_js()
		return self.generate_html(text)

	def generate_table_of_contents(self):
		if self.meta.get("series") == None:
			return ""
		html = "<ul id='tableOfContents'>"
		for v, k in self.meta["series"].items():
			if k == self.file:
				html += "<li><a class='selected'>" + v + "</a></li>"
			else:
				html += f"<li><a href='{k}' class='underline'>" + v + "</a></li>"				
		html += "</ul>"
		return html

	def get_file_title(self):
		if self.meta.get("series") == None:
			return self.meta["cover"]["name"]
		for title, file in self.meta["series"].items():
			if self.file == file:
				return title

	def generate_html(self, text):
		return f"""<!DOCTYPE html>
<html>
{self.generate_head()}
<body>
<header>
<a class="underline" href="../../index.html">←</a>
</header>
{self.generate_table_of_contents()}
<article>
{text}
</article>
</body>
</html>"""

	def generate_head(self):
		return f"""<head><meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>LSC CS</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<meta content="{self.get_file_title()}" property="og:title">
<meta content="{self.meta["cover"]["description"]}" property="og:description">
<meta content="{base_url + f"{self.root}/{self.file}"}" property="og:url">
<meta content="{base_url + f"{self.root}/cover.png"}" property="og:image">
<meta content="#32CCFF" property="theme-color">
<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="../../base.css">
<link rel="stylesheet" media="screen" type="text/css" href="../monokai.css">
<link rel="stylesheet" media="print" type="text/css" href="../friendly.css">
<link rel='stylesheet' type='text/css' href='../article.css'>
</head>"""

class MyExtensions(Extension):
	def __init__(self, root, file):
		self.root = root
		self.file = file

	def extendMarkdown(self, md):
		md.postprocessors.register(BoilerplateProcessor(self.root, self.file), "bp", 1)
		md.treeprocessors.register(UnderlineProcessor(), "underline", 1)

def build():	
	for root, _, files in os.walk("articles/"):
		for file in files:
			if file.endswith(".md"):
				file_path = join(root, file)
				with open(file_path, "r", encoding="utf-8") as md_file:
					html_file_name = file.replace(".md", ".html")
					with open(join(root, html_file_name), "w+", encoding="utf-8") as html_file:
						extension_configs = {
							"codehilite": {
								"guess_lang": False,
							},
						}
						html_file.write(markdown.markdown(md_file.read(), extensions=[MyExtensions(root, html_file_name), "toc", "codehilite", "tables", "md_in_html"], extension_configs=extension_configs, output_format="html5"))
	with open("data.js", "w+") as f:
		f.write(f"let Articles = {json.dumps(data_js)}")
if __name__ == "__main__":
	build()
	print("Site built")
