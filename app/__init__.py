from flask import Flask


def create_app():
    # 创建Flask应用实例
    app = Flask(__name__)

    # 注册路由
    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
