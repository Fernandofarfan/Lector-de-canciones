from backend import app

if __name__ == '__main__':
    print("Starting songs application.")
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)

import os

mongodb_service = os.environ.get('MONGODB_SERVICE')
print(f"The value of MONGODB_SERVICE is: {mongodb_service}")
