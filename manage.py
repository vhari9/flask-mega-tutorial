from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from myapp import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.run()
