import pytest
from StringUtils import StringUtils

@pytest.mark.parametrize("string, result",
                        [("welcome", "Welcome"),
                         ("Welcome", "Welcome"),
                         ("123", "123"),
                         ("добро пожаловать", "Добро пожаловать"),
                         ("", ""),
                         ])
def test_positive_capitilize(string, result):
    capitilize = StringUtils()
    res = capitilize.capitilize(string)
    assert res == result

@pytest.mark.parametrize("string",
                         [None,
                          123,
                          [1,2,3],
                          True
                          ])
def test_negative_capitilize(string):
    capitilize = StringUtils()
    with pytest.raises(AttributeError):
        capitilize.capitilize(string)

@pytest.mark.parametrize("string, result",
                        [("  привет", "привет"),
                         ("Добрый день!", "Добрый день!"),
                         ("   HELLO", "HELLO"),
                         (" 123", "123"),
                         ("  ", "")
                         ])
def test_positive_trim(string, result):
    trim = StringUtils()
    res = trim.trim(string)
    assert res == result

@pytest.mark.parametrize("string",
                         [None,
                          123,
                          ["1","2","3"],
                          True
                          ])
def test_negative_trim(string):
    trim = StringUtils()
    with pytest.raises(AttributeError):
        trim.trim(string)


@pytest.mark.parametrize("string, symbol, bool",
                         [("Hello", "H", True),
                          ("приВЕТ", "О", False),
                          ("hello32", "3", True),
                          ("", "H", False),
                          ("Добро пожаловать", " ", True)
                          ])
def test_positive_contains(string, symbol, bool):
    contains = StringUtils()
    res = contains.contains(string, symbol)
    assert res == bool

@pytest.mark.parametrize("string, symbol",
                         [(987, "c"),
                          (None, "H"),
                          ("May", 12),
                          ("Утро", ["1","2","3"]),
                          ])
def test_negative_contains(string, symbol):
    contains = StringUtils()
    with pytest.raises((AttributeError, TypeError)):
        contains.contains(string, symbol)

@pytest.mark.parametrize("string, symbol, result",
                         [("Ночь", "ь", "Ноч"),
                          ("heLLO", "LL", "heO"),
                          ("123", "3", "12"),
                          ("Добрый день", " ", "Добрыйдень"),
                          (".?%", ".?%", ""),
                          ("", "", "")
                          ])
def test_positive_delete_symbol(string, symbol, result):
    delete_symbol = StringUtils()
    res = delete_symbol.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, symbol",
                         [("Нет", None),
                          (None, "Нет"),
                          (123, "Да"),
                          ("lf", [2,3]),
                          ("lf", 23)
                          ])
def test_negative_delete_symbol(string, symbol):
    delete_symbol = StringUtils()
    with pytest.raises((AttributeError, TypeError)):
        delete_symbol.delete_symbol(string, symbol)


@pytest.mark.parametrize("string, symbol, bool",
                         [("Сова", "С", True),
                          ("pinK", "p", True),
                          ("1,2,3", " ", False),
                          ("", "", True),
                          (".&#", "1", False),
                          ("Добро пожаловать!", "!", False)
                          ])
def test_positive_start_with(string, symbol, bool):
    start_with = StringUtils()
    res = start_with.starts_with(string, symbol)
    assert res == bool

@pytest.mark.parametrize("string, symbol",
                         [("Нет", None),
                          (None, "т"),
                          (123, "Д"),
                          (["1","2","3"], "d"),
                          ("lf", [2,3]),
                          ("lf", 2)
                          ])
def test_negative_start_with(string, symbol):
    start_with = StringUtils()
    with pytest.raises((AttributeError, TypeError)):
        start_with.starts_with(string, symbol)

@pytest.mark.parametrize("string, symbol, bool",
                         [("Утро", "о", True),
                          ("monday", "Y", False),
                          ("Priвет!!!", "!", True),
                          (" hello ", "o", False),
                          ("", "", True),
                          ("123%@$", " ", False)
                          ])
def test_positive_end_with(string, symbol, bool):
    end_with = StringUtils()
    res = end_with.end_with(string, symbol)
    assert res == bool

@pytest.mark.parametrize("string, symbol",
                         [("Нет", None),
                          (None, "т"),
                          (123, "Д"),
                          (["1","2","3"], "d"),
                          ("lf", [2,3]),
                          ("lf", 2),
                          ("book", ["1","2"])
                          ])
def test_negative_end_with(string, symbol):
    end_with = StringUtils()
    with pytest.raises((AttributeError, TypeError)):
        end_with.end_with(string, symbol)

@pytest.mark.parametrize("string, bool",
                         [("", True),
                          ("  ", True),
                          ("Vы", False),
                          ("1 ! ", False),
                          ("Всем hello!", False)
                          ])
def test_positive_is_empty(string, bool):
    is_empty = StringUtils()
    res = is_empty.is_empty(string)
    assert res == bool

@pytest.mark.parametrize("string",
                         [None,
                          123,
                          [1, 2, 3],
                          ])
def test_negative_is_empty(string):
    is_empty = StringUtils()
    with pytest.raises(AttributeError):
        is_empty.is_empty(string)


@pytest.mark.parametrize("string, delimiter, result",
                          [("H,e,l,l,o", ",", ["H","e","l","l","o"]),
                          ("1/2/3/4", "/", ["1","2","3","4"]),
                          ("4,5,6", ",", ["4","5","6"]),
                          ("4,5,6", None, ["4","5","6"]),
                          ("", ",", [])
                           ])
def test_pozitive_to_list(string, delimiter, result):
    to_list = StringUtils()
    if delimiter is None:
      res = to_list.to_list(string)
    else:
      res = to_list.to_list(string,delimiter)
    assert res ==result

@pytest.mark.parametrize("string, delimiter",
                         [(None, ","),
                          (123, ","),
                          ([1, 2, 3], "-"),
                          ("POI", 123),
                          ("флаг", ["1","2","3"])
                          ])
def test_negative_to_list(string, delimiter):
    to_list = StringUtils()
    with pytest.raises((AttributeError, TypeError)):
      to_list.to_list(string, delimiter)


@pytest.mark.parametrize("lst, joiner, result",
                         [(["Pi", 3], "-", "Pi-3"),
                          (["Ты мне", "я тебе."], " ", "Ты мне я тебе."),
                          ([1234567, "Dog"], "", "1234567Dog"),
                          (["ехал", "приехал"], "да", "ехалдаприехал")
                          ])
def test_positive_list_to_string(lst, joiner, result):
    list_to_string = StringUtils()
    res = list_to_string.list_to_string(lst, joiner)
    assert res == result

@pytest.mark.parametrize("lst, joiner",
                         [(None, "a"),
                          (["a", "b"], None),
                          (567, "v"),
                          (["!", "33", "100"], 1)
                           ])
def test_negative_list_to_string(lst, joiner):
        list_to_string = StringUtils()
        with pytest.raises((AttributeError, TypeError)):
         list_to_string.list_to_string(lst, joiner)







