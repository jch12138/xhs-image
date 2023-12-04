from app import create_app

# 创建Flask应用实例
app = create_app()

if __name__ == '__main__':
    # 启动应用
    app.run(debug=False)

