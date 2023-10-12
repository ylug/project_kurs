from utils.main import Check


def test_count_now():
    item_date = Check("2021-11-21T23:10:37.456751", "2313456712345423", "54623671321533123567")
    assert item_date.mask_account() == "****************3567"
    assert item_date.count_now("Visa Gold 3589276410671603") == "Visa Gold xxxx xx  "


def test_mask_account():
    item = Check("24.09.2002", "2313456712345423", "54623671321533123567")
    assert item.mask_card() == "2313 45xx xxxx 5423"


def test_mask_card():
    item = Check("24.09.2002", "2313456712345423", "54623671321533123567")
    assert item.mask_card() == "2313 45xx xxxx 5423"


def test_format_date():
    item = Check("2021-11-21T23:10:37.456751", "2313456712345423", "54623671321533123567")
    assert item.mask_card() == "2313 45xx xxxx 5423"
