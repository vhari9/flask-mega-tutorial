from myapp import app
import config

if __name__ == '__main__':
    app.run('0.0.0.0')
    print "Navigate in your browser to", config.DevelopmentConfig.SERVER_NAME