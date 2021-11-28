from program import calc , input_func

def test_input_func1():
    test_list = ["program.py","a","b","c","b","a","."]
    test_output = input_func(test_list)
    assert test_output == ["a","b","c","b","a"]

def test_input_func2():
    test_list = ["program.py","a","3","c","1","2","."]
    test_output = input_func(test_list)
    assert test_output == ["a","3","c","1","2"]

def test_input_func3():
    test_list = ["program.py","a","b","c","B","A","."]
    test_output = input_func(test_list)
    assert test_output == ["a","b","c","B","A"]

def test_input_func4():
    test_list = ["program.py","a","b","."]
    test_output = input_func(test_list)
    assert test_output == ["a","b"]

def test_input_func5():
    test_list = ["program.py","1","2","3","b","6","99999","C","x","/","=","."]
    test_output = input_func(test_list)
    assert test_output == ["1","2","3","b","6","99999","C","x","/","="]

def test_input_func6():
    test_list = ["program.py","a","b","c","b","a",".","a","b","c","d","e"]
    test_output = input_func(test_list)
    assert test_output == ["a","b","c","b","a"]



def test_calc1():
    test_list = ["a","b","c","b","a"]
    test_output = calc(test_list)
    assert test_output == ["c"]

def test_calc2():
    test_list = ["a","3","c","1","2"]
    test_output = calc(test_list)
    assert test_output == ["a","3","c","1","2"]

def test_calc3():
    test_list = ["a","b","c","B","A"]
    test_output = calc(test_list)
    assert test_output == ["a","b","c","B","A"]

def test_calc4():
    test_list = ["a", "a", "b", "b"]
    test_output = calc(test_list)
    assert test_output == []
def test_calc5():
    test_list = ["a","b","c","b","a","e","a","b","c","b","a"]
    test_output = calc(test_list)
    assert test_output == ["e"]
def test_calc6():
    test_list = ["ab","c","ab"]
    test_output = calc(test_list)
    assert test_output == ["c"]

def test_calc7():
    test_list = ["a","b","c","b","a","e","="]
    test_output = calc(test_list)
    assert test_output == ["a","b","c","b","a","e","="]
