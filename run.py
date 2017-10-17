from sanic import Sanic
from sanic.response import text


app = Sanic(__name__)


@app.route("/")
async def index_handler(request):
    return text("Welcome to my python world!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
