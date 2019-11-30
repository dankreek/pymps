from pymps.charsets import mps801


def test_us_uk_charset_len():
    assert len(mps801.US_UK_GRAPHIC_MODE) == 256
    assert len(mps801.US_UK_BUSINESS_MODE) == 256

