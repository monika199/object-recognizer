import os
from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import mechanize
import re

import time
from lxml import html  
import xlwt 
import xlrd 
from django.utils.http import urlquote 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

#change location here, download chrome driver
search_string = "books"
@app.route("/amazon", methods=["POST"])
def amazon():
    driver = webdriver.Chrome('C:\Users\Dev\Downloads\chromedriver_win32\chromedriver.exe')
    #change location here, download selenium chrome driver
    #driver.maximize_window() 
    static_search_amazon = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='
    driver.get(static_search_amazon+urlquote(search_string).encode('utf8'))
    return "searching amazon"
@app.route("/walmart", methods=["POST"])
def walmart():
    driver = webdriver.Chrome('C:\Users\Dev\Downloads\chromedriver_win32\chromedriver.exe')
    #driver.maximize_window() 
    static_search_walmart1 = 'https://www.walmart.com/search/?query='
    static_search_walmart2 = '&cat_id=0'
    driver.get(static_search_walmart1+urlquote(search_string).encode('utf8')+static_search_walmart2)
    return "searching walmart"

@app.route("/")
def index():
    print "in index call..calling upload"
    return render_template("upload.html")

def object_recognizer():
    f = open("temp.txt","w+")
    f.write("Line 1 \n")
    f.write("Line 2 \n")
    f.close();
    print "called object rec"
    delete_line()
def delete_line():
    f = open("temp.txt","r+")
    lines = f.readlines()
    f.seek(0)
    print "called delete line"
    #get the line you want no need to delete line
    # for line in lines:
    #     if some condition:
    #         get line
    #set global search string value here and when crawler is called it will search for that string value
    #search_string = ? 


@app.route("/login", methods=["POST"])
def login():
    #call object recognzer here
    #string = object_recognizer()
    string = "output of object recognizer goes here"
    #set search string valu
    return render_template('login.html',detect=string)

@app.route("/upload", methods=["POST"])
def upload():
    print "in upload now"
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    '''
    target = os.path.join(APP_ROOT, 'static')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, "temp.jpg"])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    print "heyho"
    return render_template('login.html', detect=0)


if __name__ == "__main__":
    app.run(port=4555, debug=True)
