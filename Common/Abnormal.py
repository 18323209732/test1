import warnings

class RepeatClass(Warning):
    """
    检查重复类名
    """
    def __init__(self,class_name):
        self.class_name = class_name

    def __str__(self):
        return (f"用例中存在重复的类名:{self.class_name},请修改确认后，再执行操作....")


class RepeatCase(Warning):
    """
    检查重复方法名
    """
    def __init__(self,case_name):
        self.case_name = case_name


    def __str__(self):
        return (f"用例中存在重复的方法名:{self.case_name},请修改确认后，再执行操作....")


class DataException(Exception):
    """
    检查数据异常
    """
    def __init__(self,class_name):
        self.class_name = class_name

    def __str__(self):
        return f"{self.class_name}:该数据类型对象错误,请修确认改后，再执行操作...."


class SqlException(Exception):
    """
    检查数据异常
    """
    def __init__(self,case_name):
        self.case_name = case_name

    def __str__(self):
        return f"{self.case_name}:用例插入数据库错误，未插入成功...."


class Assert(Exception):
    """
    断言抛出异常
    """
    def __init__(self,expect,actual):
        self.expect = expect
        self.actual = actual
        if expect:
            self.expect = expect
        else:
            self.expect = "Null"
        if actual:
            self.actual = actual
        else:
            self.actual = "Null"

    def __str__(self):
        return f"AssertionError: 预期值:'{self.expect}'与实际值:'{self.actual}',二者不对应异常...."

class KeyException(Exception):
    """
    检查数据异常
    """
    def __init__(self,key):
        self.key = key

    def __str__(self):
        return f"未找到{self.key}键,请检查数据,再执行操作...."