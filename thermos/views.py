from flask import Flask,render_template,url_for,request,redirect,flash
from logging import DEBUG
from datetime import datetime
from forms import BookmarkForm, MyForm
import os 

import models 
from sqlalchemy import desc

from thermos import app,db

from models import User,Bookmark



class User:
	"""docstring for 
User"""
	def __init__(self, firstname,lastname):
		self.firstname= firstname
		self.lastname= lastname

	def initials(self):
		return "{}. {}.".format(self.firstname[0],self.lastname[0])


bookmarks=[]

def store_bookmark(url,description):
	bookmarks.append(dict(url=url,user="Rohit1",date = datetime.utcnow(),description= description))



def new_bookmarks(num):
	return  models.Bookmark.query.order_by(desc(Bookmark.date)).limit(num)
	# return sorted(bookmarks, key=lambda kv: kv['date'],reverse=True)[:num]


#fakeuser
def logged_in_user():
    return models.User.query.filter_by(username='Rohit1').first()

@app.route('/')
@app.route('/index')
def index():
	# return render_template('index.html',title="This is the title",
	# 						user=User("rohit","vyas"))
	#Do not display more then two recently added books
	return render_template('index.html',new_bookmarks=models.Bookmark.newest(2))

@app.route('/add',methods=['GET','POST'])
def add():
	
	form = BookmarkForm()
	if form.validate_on_submit():
		url = form.url.data
		# description = form.description.data
		description = form.description.data
		bm = models.Bookmark(url=url,description=description,user=logged_in_user())
		print bm.url
		db.session.add(bm)
		db.session.commit()
		# store_bookmark(url,description)
		
		flash("Stored '{}'".format(description))
		return redirect(url_for('index'))
	return render_template('add.html',form=form)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404


@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'),500

@app.route('/user/<username>')
def user(username):
	user = models.User.query.filter_by(username=username).first_or_404()
	# user = "Rohit1"
	return render_template('user.html',user=user)


######## Test function################

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
    	name = form.name.data
    	print name
    	store_bookmark(name,name)
        return 'success data'
    return render_template('submit.html', form=form)

@app.route('/success', methods=('GET', 'POST'))
def success():
	return ("Data saved !!!")






