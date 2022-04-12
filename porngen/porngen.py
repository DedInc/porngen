from lxml import html
from requests import get
from requests_html import HTMLSession

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

def getVideo(link):
	r = HTMLSession().get(link, headers=headers)
	r.html.render()
	tree = html.fromstring(r.content)
	for i in range(2):
		tree = html.fromstring(get(tree.xpath('//iframe/@src')[0], headers=headers).content)
	return tree.xpath('//video/@src')[0]

def scanVideos(link):
	videos = []
	tree = html.fromstring(get(link, headers=headers).content)
	urls = tree.xpath('//a/@href')
	if len(urls) > 0:
		for url in urls:
			if 'rt-' in url and not 'page' in url:
				videos.append(url)
	return videos

def getVideos(search, allPages=False, maxVideos=-1):
	videos = []
	if ' ' in search:
		search = search.lower().replace(' ', '-')
	tree = html.fromstring(get(f'http://nonzenon.ru/{search}/', headers=headers).content)
	urls = tree.xpath('//a/@href')
	i = 0
	if len(urls) > 0:
		for url in urls:
			if 'page' in url:
				if not allPages and i > 0:
					break
				else:
					for video in scanVideos(url):
						if maxVideos != -1 and len(videos) != maxVideos:
							videos.append(getVideo(video))
						else:
							break
				i += 1
	return videos

def getCategories():
	categories = []
	tree = html.fromstring(get('http://nonzenon.ru/', headers=headers).content)
	for i in range(1, 100):
		categories.append(tree.xpath(f'/html/body/div[2]/div[2]/div[1]/div[{i}]/div/a/@href')[0].split('.ru/')[1].split('/')[0])
	return categories