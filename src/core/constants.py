from pathlib import Path


# caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# caminho do .env
ENV_PATH = BASE_DIR / 'src' / '.env'

# logs
LOG_PATH = BASE_DIR / 'logs'

