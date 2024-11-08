from app.app import create_app
from app.config_app import get_logger


PORT = 10000
DEBUG = False
HOST = "0.0.0.0"

flask_app = create_app()

logger = get_logger()

if __name__ == "__main__":
    bar = "-" * 40
    print(f"{bar}\n   Running {HOST}:{PORT} Debug: {DEBUG}\n{bar}")
    flask_app.run(host=HOST, debug=DEBUG, port=PORT)
