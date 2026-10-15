import pytest
from week04.solutions.python_core_22 import first_adjacent_duplicate

@pytest.mark.parametrize(
    'data, expected',
    [
        (
            ['API', 'modern', 'NET', 'NET'], (3, 'NET')
        ),
        (
            ['API', 'NET','modern', 'NET'], None
        ),
        (
            ['API', 'modern', 'NET', 'DB'], None
        ),
        (
            ['API'], None
        ),
        (
            ['API', 'NET', 'NET', 'NET'], (2, 'NET')
        ),
        (
            ['API', 'api', 'NET', 'NET'], (3, 'NET')
        ),
        (
            ['', '', 'NET', 'NeT'], (1, '')
        ),
    ]
)
def test_adjacent_duplicates(data, expected):
    assert first_adjacent_duplicate(data) == expected
