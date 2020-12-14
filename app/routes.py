from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Execution Test Line 1"