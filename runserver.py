import config
from myapp import app

print app.url_map
if __name__ == '__main__':
    app.run(config.DevelopmentConfig.SERVER_NAME, port=8080)