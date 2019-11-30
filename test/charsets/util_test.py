import pytest

from pymps.charsets import util


tuplize_char_cases = [
    ([], ((False, False, False, False, False, False),
          (False, False, False, False, False, False),
          (False, False, False, False, False, False),
          (False, False, False, False, False, False),
          (False, False, False, False, False, False),
          (False, False, False, False, False, False),
          (False, False, False, False, False, False))),

    (['# # #'], ((True, False, True, False, True, False),
                 (False, False, False, False, False, False),
                 (False, False, False, False, False, False),
                 (False, False, False, False, False, False),
                 (False, False, False, False, False, False),
                 (False, False, False, False, False, False),
                 (False, False, False, False, False, False))),

    (['# # # ',
      ' # # #',
      '# # # ',
      ' # # #',
      '# # # ',
      ' # # #',
      '# # # '], ((True, False, True, False, True, False),
                  (False, True, False, True, False, True),
                  (True, False, True, False, True, False),
                  (False, True, False, True, False, True),
                  (True, False, True, False, True, False),
                  (False, True, False, True, False, True),
                  (True, False, True, False, True, False)))
]


@pytest.mark.parametrize("test_input,expected", tuplize_char_cases)
def test_tuplize_char(test_input, expected):
    assert util.tuplize_char(test_input) == expected
