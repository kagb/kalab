# -*- coding: utf-8 -*-

import jieba.analyse
import numpy
from PIL import Image
from wordcloud import WordCloud
from xarticle.xarticle import XFetcher


FONT_PATH = 'static/fonts/jiaotong.ttf'
MASK_PATH = 'static/img/weibo.png'
WEIBO_IMG_FILE_PATH = 'static/img/weibo/'
BACKGROUND_COLOR = "#FFFFFF"
STOPWORDS = [u'什么', u'为什么', u'这么', u'这个', u'那天', u'还要' u'这位']


def weibo_article_word_cloud(weibo_url, filename='weibo.jpg'):
    url = normalize_weibo_article_url(weibo_url)
    content = fetch_content(url, x_path='string(//div[@class="m-feed"])', check_xpath='//div[@class="m-feed"]')
    generate_weibo_img(content, filename)


def normalize_weibo_article_url(url):
    return url


def fetch_content(url, x_path='normalize-space(string(//body))', check_xpath=''):
    fetcher = XFetcher()
    fetcher.fetch(url, x_path)
    content = fetcher.doc.xpath(x_path)
    fetcher.quit()
    return content


def generate_weibo_img(content, filename, mask_path=MASK_PATH,
                       file_path=WEIBO_IMG_FILE_PATH, topk=100, font_path=FONT_PATH,
                       background_color=BACKGROUND_COLOR, width=400, height=400):
    if not (content and filename):
        return
    tags = jieba.analyse.extract_tags(content, topK=topk)
    if not tags:
        return
    text = ' '.join(tags)
    alice_mask = numpy.array(Image.open(mask_path)) if mask_path else None
    stopwords = set(STOPWORDS)
    wdcloud = WordCloud(font_path=font_path,
                        background_color=background_color,
                        mask=alice_mask,
                        max_words=topk,
                        width=width,
                        stopwords=stopwords,
                        height=height).generate(text)
    image = wdcloud.to_image()
    file_path = file_path + filename
    image.save(file_path)
    return filename


def _color_func(*args, **kwargs):
    return 'white'
