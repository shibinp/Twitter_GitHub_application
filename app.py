from flask import render_template,request,session,flash,redirect,url_for
from time import *
from functools import wraps
import os
from flask import Flask
app = Flask(__name__)
import requests
import json
import oauth2 as oauth

@app.route('/')
@app.route('/home2')
def home2():
	header= {'h1':''}
	return render_template('home2.html',
				title='home',
				header=header)


@app.route('/github',methods = ['GET','POST'])	
def github():
   
   l=[]
   if request.form.get('submit'):
	API_TOKEN='****************************'
	GIT_API_URL='https://api.github.com'

	import requests


	#url1='https://api.github.com'
	username=request.form.get('github')

	url='https://api.github.com/users/'+username+'/repos'
	#print url
	#fields = "id,name,birthday"
	fields = "id"
	limit=4

	url = '%s?access_token=%s' % \
	    (url,API_TOKEN,)
#print url
	r = requests.get(url).json()
#print r
#print type(r)
	l = []
	i = 1
	for data in r:
		l.append(str(i) + data['full_name'] + 	'\n')
		i += 1
   return render_template('github.html',data=l)




@app.route('/twitter',methods = ['GET','POST'])
def twitter():
   a=[]
   if request.form.get('submit'):
	name=request.form.get('twitter')
		 
  	Consumer_Key = "***************************"
	Consumer_Secret = "***************************"
	Access_Key = "*********************************"
	Access_Secret = "***************************"

	consumer = oauth.Consumer(key=Consumer_Key, secret=Consumer_Secret)
	access_token = oauth.Token(key=Access_Key, secret=Access_Secret)
	client = oauth.Client(consumer, access_token)

	


	post = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count=10"

	response, data = client.request(post)

	tweets = json.loads(data)
	for tweet in tweets:
   		 a.append(tweet['text'])
	       
   return render_template('twitter.html',a=a)
def HOME():
	render_template('home2.html')

__name__ == '__main__';
app.run(debug=True)
