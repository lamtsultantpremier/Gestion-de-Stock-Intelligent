from dotenv import dotenv_values

venv = dotenv_values(".env")

USERNAME = venv.get("USERNAME")
PASSWORD = venv.get("PASSWORD")
HOST = venv.get("HOST")
PORT = venv.get("PORT")

DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/stockage_intelligent"
