#!/Users/michael/Documents/Demo/Sanic_venv/bin/env python
from sanic import Sanic
from sanic.response import text
from config import CONFIG

app = Sanic(__name__)
app.config.from_object(CONFIG)


@app.route("/")
async def index_handler(request):
    return text("Welcome to my python world! Current Mode is : " +
                str(app.config['DEBUG']))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=app.config['DEBUG'])
