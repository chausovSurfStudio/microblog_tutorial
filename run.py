#!flask/bin/python
from app import create_app
from app import initFuckingViews

app = create_app('config')
app = initFuckingViews()


app.run(debug = True)
