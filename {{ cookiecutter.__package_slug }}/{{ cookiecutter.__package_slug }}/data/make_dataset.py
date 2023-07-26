import logging

from {{ cookiecutter.__package_slug }}.config import RAW_DATA_PATH, PROCESSED_DATA_PATH

logger = logging.getLogger(__name__)


def main():
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger.info("making final data set from raw data")
