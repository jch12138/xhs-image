import re
import requests
from lxml import etree
import json


def extract_http_link(share_link: str) -> str:
    if not isinstance(share_link, str):
        return ''

    pattern = re.compile(r'http://xhslink.com/\w+')
    result = pattern.findall(share_link)

    if len(result) == 0:
        return ''

    return result[0]


def extract_image_list(html: str) -> list:
    selector = etree.HTML(html)
    content = selector.xpath('//script')
    page_content = content[-1].text.replace('window.__INITIAL_STATE__=', '').replace('undefined', '\"\"')
    page_content = json.loads(page_content)
    key = list(page_content['note']['noteDetailMap'].keys())[0]
    image_list = page_content['note']['noteDetailMap'][key]['note']['imageList']
    image_list = [image['infoList'][1]['url'] for image in image_list]

    return image_list


send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
}
