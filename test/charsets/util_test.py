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


def test_tuplize_col():
    col_len = 16
    tuplized_col = util.tuplize_col([[], []], col_len)
    assert len(tuplized_col) == 16


def test_tuplize_charset():
    col_len = 16
    tuplized_charset = util.tuplize_charset([[[]], [[]]], line_len=col_len)
    assert len(tuplized_charset) == 2*16

