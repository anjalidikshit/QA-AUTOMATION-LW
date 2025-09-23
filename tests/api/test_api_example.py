import requests
from utils import config, logger

log = logger.get_logger(__name__)


def test_api_get_posts():
    url = f"{config.API_URL}/posts/1"
    log.info(f"Sending GET request to {url}")
    response = requests.get(url)

    assert response.status_code == 200, f"Unexpected status: {response.status_code}"
    data = response.json()
    assert "id" in data and data["id"] == 1, "Invalid response data"

    log.info("API GET /posts/1 validated successfully.")
