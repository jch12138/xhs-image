from flask import Blueprint, jsonify, request
import requests
from utils import extract_http_link, send_headers, extract_image_list

api_bp = Blueprint('api', __name__)


