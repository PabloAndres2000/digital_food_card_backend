from flask import Flask
from app.config import DevelopmentConfig
from app.extensions import db, migrate
# from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    # app.register_blueprint(user_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
