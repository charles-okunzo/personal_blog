
from app import create_app
# from flask_script import Manager,Server
from app import db, models
from flask_migrate import Migrate




app = create_app('development')
# manager = Manager(app)
migrate = Migrate(app,db)

# manager.add_command('server', Server)



# @manager.shell
# def create_shell_context():
#   return dict(app=app, db=db, User=User)

if __name__ == '__main__':
  app.run()