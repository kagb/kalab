# -*- coding: utf-8 -*-

from urlparse import urlparse, urlunsplit

import jieba.analyse
import numpy
from PIL import Image
from wordcloud import WordCloud
from xarticle.xarticle import XArticle

FONT_PATH = 'static/fonts/jiaotong.ttf'
MASK_PATH = 'static/img/weibo.png'
WEIBO_IMG_FILE_PATH = 'static/img/weibo/'
BACKGROUND_COLOR = "#FFFFFF"
STOPWORDS = [u'什么', u'为什么', u'这么', u'这个', u'那天', u'还要' u'这位']


def weibo_article_word_cloud(weibo_url, filename='weibo.jpg'):
    url = normalize_weibo_article_url(weibo_url)
    if not url:
        return (1, u'非法的微博地址', url)
    content = fetch_content(url, x_path='string(//div[@class="m-feed"])', check_xpath='//div[@class="m-feed"]')
    if not content:
        return (2, u'内容抓取失败', url)
    img_file = generate_weibo_img(content, filename)
    if img_file:
        return (0, u'图片生成成功', img_file)
    return (3, u'未知失败')


def normalize_weibo_article_url(url):
    scheme, netloc, path, params, qs, fg = urlparse(url)
    if scheme not in ['http', 'https']:
        return ''
    if netloc in ['media.weibo.cn', 'weibo.com', 'www.weibo.com']:

        if '/ttarticle/' in url:
            return urlunsplit((scheme, 'media.weibo.cn', 'article', qs, ''))
        elif 'media.weibo.cn/article?id' in url:
            return url
        else:
            return ''
    return ''


def fetch_content(url, x_path='normalize-space(string(//body))', check_xpath=''):
    x = XArticle()
    x.site_conf = {'content': x_path}
    x.extract(url)
    x.quit()
    return x.content[0] if x.content else ''


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
