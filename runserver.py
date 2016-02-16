from myapp import app, init_for
from os import path, walk

extra_dirs = ['myapp/templates',]
extra_files = extra_dirs[:]

if __name__ == '__main__':
    init_for('dev')
    for extra_dir in extra_dirs:
        for dirname, dirs, files in walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)
    app.run('0.0.0.0', port=5000, extra_files=extra_files)