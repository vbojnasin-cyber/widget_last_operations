from unittest.mock import patch

import pytest
@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2026-07-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2026-07-03T15:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2026-06-30T09:15:00"},
        {"id": 4, "state": "PENDING", "date": "2026-07-02T18:45:00"},
    ]
# Фикстура, которая автоматически отключает создание реальных файлов логов во всех тестах этого модуля
@pytest.fixture(autouse=True)
def mock_logger():
    with patch("src.loggers.create_logger") as mock:
        yield mock