from flask import Blueprint, jsonify, request
import requests
from utils import extract_http_link, send_headers, extract_image_list

api_bp = Blueprint('api', __name__)


@api_bp.route('/getImageUrls', methods=['POST'])
def get_image_urls():
    share_text = request.form.get('share_text')

    if not isinstance(share_text, str):
        return jsonify({
            'message': 'share_text is not string',
            'code': 1,
        })

    http_link = extract_http_link(share_text)

    if not http_link:
        return jsonify({
            'message': 'share_text is invalid',
            'code': 2,
        })

    html = requests.get(http_link, headers=send_headers).text

    if html is None:

        return jsonify({
            'message': 'cannot get html content',
            'code': 3,
        })

    image_list = extract_image_list(html)

    if image_list is None:

        return jsonify({
            'message': 'cannot extract image list',
            'code': 4,
        })

    return jsonify({
        'image_list': image_list,
        'code': 0,
    })
