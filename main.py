from website import create_app

app = create_app()

if __name__ == '__main__': # run the web server if run this file 
  app.run(debug=True) # debug=True means that everytime make a change in python code, it auto rerun the web server
