from thermos import app,db
# import views
from flask_script import Manager, prompt_bool


manager = Manager(app)



@manager.command
def initdb():
	db.create_all()
	print ('initialize the database')


@manager.command
def dropdb():
	if prompt_bool(
		"Are you sure deleting Db"):
		db.dropdb()
		db.drop_all()
		print ("Dropped DB")




if __name__ == '__main__':
	manager.run()