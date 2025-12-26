class Config:
    SECRET_KEY = "dev_secret_key_change_later"
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://admin:123@localhost:3306/dashboard_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
