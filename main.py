from flask import Flask, request

password = []
email = []

marach = Flask(__name__, static_url_path='/static')

@marach.route('/register', methods=['POST'])
def register():
  global email, password 
  response = ''
  a = request.form
  email.append(a['email'])
  password.append(a['password'])
  file = open('static/response.html', 'r')
  response = file.read()
  file.close()
  response = response.replace('{response}', 'Registration Succesful')
    
  return response

  
@marach.route('/login', methods=['POST'])
def login():
  global email, password 
  response = ''
  a = request.form
  file = open('static/response.html', 'r')
  
  if a['email'] in email and a['password'] in password:
    response = file.read()
    file.close()
    response = response.replace('{response}', 'Login Succesful🎉✨')

  else:
    response = file.read()
    file.close()
    response = response.replace('{response}', 'Incorrect email or password!!!😢😢')
    
  return response


@marach.route('/')
def home ():
  homepage = ''
  file = open('static/homepage.html', 'r')
  homepage = file.read()
  file.close()
  return homepage

@marach.route('/register')
def registration():
  page = ''
  file = open('static/template.html', 'r')
  page = file.read()
  file.close()
  page = page.replace('{name}', 'Registration')
  page = page.replace('{action}', 'register')
  page = page.replace('{title}', 'Registration page')
  return page


@marach.route('/login')
def log_in():
  page = ''
  file = open('static/template.html', 'r')
  page = file.read()
  file.close()
  page = page.replace('{name}', 'Login')
  page = page.replace('{action}', 'login')
  page = page.replace('{title}', 'Login page')
  return page


marach.run(host='0.0.0.0', port=81)
  