
from app import create_app
from flask_script import Manager,Server
from app import db





app = create_app('development')
manager = Manager(app)

manager.add_command('server', Server)


@manager.shell
def create_shell_context():
  return dict(app=app, db=db)






if __name__ == '__main__':
  manager.run()