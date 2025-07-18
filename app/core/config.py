import os

PROJECT_NAME = "aurora-admin-panel"

BACKEND_VERSION = os.getenv("BACKEND_VERSION", '0.1.0')
ENVIRONMENT = os.getenv("ENVIRONMENT", "PROD")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
ENABLE_SENTRY = os.getenv("ENABLE_SENTRY", False)
SECRET_KEY = os.getenv("SECRET_KEY", "aurora-admin-panel")
TRAFFIC_INTERVAL_SECONDS = os.getenv("TRAFFIC_INTERVAL_SECONDS", 600)
DDNS_INTERVAL_SECONDS = os.getenv("DDNS_INTERVAL_SECONDS", 120)
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

V2BOARD_API_HOST = os.getenv("V2BOARD_API_HOST", "")
if V2BOARD_API_HOST.endswith("/"):
    V2BOARD_API_HOST = V2BOARD_API_HOST[:-1]

V2BOARD_API_KEY = os.getenv("V2BOARD_API_KEY", "")
V2BOARD_NODE_ID = os.getenv("V2BOARD_NODE_ID", 1)
V2BOARD_NODE_TYPE = os.getenv("V2BOARD_NODE_TYPE", "v2ray")

API_V1_STR = "/api/v1"
