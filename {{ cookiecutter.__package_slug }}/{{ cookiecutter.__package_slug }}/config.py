from pathlib import Path

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

PROJECT_PATH = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_PATH.joinpath("data", "raw")
PROCESSED_DATA_PATH = PROJECT_PATH.joinpath("data", "processed")
