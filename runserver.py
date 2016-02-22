from myapp import app, init_for

if __name__ == '__main__':
    init_for('dev')
    app.run('0.0.0.0', port=9000)