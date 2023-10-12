from utils import fun


def test_read_json():
    assert isinstance(fun.read_json(), list)


def test_delete_void_list_():
    assert fun.delete_void_list_({"id"}) == ["id"]
    assert fun.delete_void_list_({}) == []


def test_check_sorting():
    assert fun.check_sorting([{'date': '2019-07-12T08:11:47.735774'},
                              {'date': '2018-03-22T01:40:19.984219'},
                              {'date': '2018-04-21T00:10:28.317704'}
                              ]) == ([{'date': '2018-03-22T01:40:19.984219'},
                                      {'date': '2018-04-21T00:10:28.317704'},
                                      {'date': '2019-07-12T08:11:47.735774'}
                                      ])


def test_get_executed():
    assert fun.get_executed({"id": 634356296}) == []
