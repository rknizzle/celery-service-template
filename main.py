"""
Run Flask's bundled web server

"""
from proj import app
import config

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=config.PORT)
