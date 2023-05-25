from app import app
from app.controllers import posts, users, likes, profiles

from app.models import user
from app.models import post



if __name__ == '__main__':
    app.run(debug=True)