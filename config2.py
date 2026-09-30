from dotenv import load_dotenv
import os

load_dotenv()

S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_REGION = os.getenv("S3_REGION")
S3_SIGNATURE_VERSION = os.getenv("S3_SIGNATURE_VERSION")

REDIS_HOST = os.getenv("REDIS_HOST")
# Added default values as strings so int() doesn't fail on None
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWD = os.getenv("DB_PASSWD")

# Corrected from JavaScript to Python
print(os.getenv("PORT")) 

DB_DATABASE = os.getenv("DB_DATABASE")

DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
DUMMY_PASS = os.getenv("DUMMY_PASS")

REDIS_JOB_LIST = os.getenv("REDIS_JOB_LIST")
REDIS_RESULT_CHANNEL = os.getenv("REDIS_RESULT_CHANNEL")
SHUTDOWN_KEY = os.getenv("SHUTDOWN_KEY")
WORKER_PREFIX = os.getenv("WORKER_PREFIX")

WARM_QUEUE_PREFIX = os.getenv("WARM_QUEUE_PREFIX")

CONTAINER_POOL_THRESHOLD = int(os.getenv("CONTAINER_POOL_THRESHOLD", "5"))

CONTAINER_WORKER_COUNT = int(os.getenv("CONTAINER_WORKER_COUNT", "2"))
MINIMUM_JUDGE_WORKER = int(os.getenv("MINIMUM_JUDGE_WORKER", "1"))
MAXIMUM_JUDGE_WORKER = int(os.getenv("MAXIMUM_JUDGE_WORKER", "5"))

JUDGE_WORKER_TIMEOUT = int(os.getenv("JUDGE_WORKER_TIMEOUT", "60"))
ACQUIRE_TIMEOUT_SECONDS = int(os.getenv("ACQUIRE_TIMEOUT_SECONDS", "10"))

MAX_MEMCAP_GB = int(os.getenv("MAX_MEMCAP_GB", "1"))
MAX_PIDS = int(os.getenv("MAX_PIDS", "64"))

WORKSPACE_DIR = os.getenv("WORKSPACE_DIR")

TESTCASE_BUCKET = os.getenv("TESTCASE_BUCKET")
SUBMISSION_BUCKET = os.getenv("SUBMISSION_BUCKET")
