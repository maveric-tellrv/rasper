from flask import Flask, render_template,url_for,request,redirect,flash
from logging import DEBUG
from datetime import datetime

app = Flask(__name__)
# app.logger.setLevel(DEBUG)

app.config['SECRET_KEY'] = '\x13R\xa7\x1d\xa3\x96vuQ2\xca\x11\xf4h\xc6,%\xa3-g[D\xda^' 



class User:
	"""docstring for 
User"""
	def __init__(self, firstname,lastname):
		self.firstname= firstname
		self.lastname= lastname

	def initials(self):
		return "{}. {}.".format(self.firstname[0],self.lastname[0])

def name(*f):
	print f
	return (f)

bookmarks=[]

def store_bookmark(url):
	bookmarks.append(dict(url=url,user="Rohit",date = datetime.utcnow()))


  
def new_bookmarks(num):
	return sorted(bookmarks, key=lambda kv: kv['date'],reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
	# return render_template('index.html',title="This is the title",
	# 						user=User("rohit","vyas"))
	#Do not display more then two recently added books
	return render_template('index.html',new_bookmarks=new_bookmarks(2))

@app.route('/add',methods=['GET','POST'])
def add():
	if request.method == "POST":
		url = request.form['url']
		store_bookmark(url)
		# app.logger.debug('store url: '+url)
		print("Store url '{}'".format(url))
		flash("Stored the url: '{}'".format(url))
		return redirect(url_for('index'))
	return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404


@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'),500


if __name__ == "__main__":
    app.run(debug=True)



