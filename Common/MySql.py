
from pymysql.connections import Connection
import sqlite3
# from Common.GetPath import second_path
from Common.ReadYaml import ConfigYaml
from Common.Route import Any_Path


class Sql:
    def __init__(self,sql=None,db='Sqlite.db',encoding="utf-8"):
        '''

        :param sql:  sql语句
        :param db:  数据库名称
        '''
        self.sql = sql
        self.db = db
        self.encoding = encoding
        self.mysql = ConfigYaml('mysql').base_config
        self.sqlite_path = Any_Path('Config', self.db)
        self.sqlite = ConfigYaml('sqlite').base_config
        self.host = ConfigYaml('host').base_config
        self.port = ConfigYaml('port').base_config
        self.pwd = ConfigYaml('pwd').base_config
        self.sqlname = ConfigYaml('sqlname').base_config
        self.user = ConfigYaml('user').base_config
        if self.sqlite:
            try:
                self.conn = sqlite3.connect(self.sqlite_path)
            except:
                raise ConnectionError("sqlite connect error,please check configuration ....")
        else:
            try:
                self.conn = Connection(host=self.host,user=self.user,password=self.pwd,database=self.sqlname,
                                        port=self.port,charset='utf8')
            except:
                raise ConnectionError("mysql connect error,please check configuration ....")

    def execute_sql(self):
        '''
        执行sql语句
        :return:
        '''
        cursor = self.conn.cursor()
        cursor.execute(self.sql)
        values = cursor.fetchall()
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return values


if __name__=="__main__":
    m="SELECT *  FROM result WHERE funname='test_product_getlistsss';"
    s = "update result set totalnumber=totalnumber+1,passnumber=passnumber+1,passrate=(passnumber/totalnumber) where funname='test_fun';"
    sql = "INSERT INTO result(funname) VALUES ('test_fun');"
    j = """CREATE TABLE IF NOT EXISTS result(id INTEGER primary key NOT NULL,funname varchar (100),totalnumber int default 0,
      passnumber int default 0, errornumber int default 0,failnumber int default 0,passrate float default 0,
      errorrate float default 0,failrate float default 0,modular varchar (30));"""
    hh = "select max(usetime) from response;"
    ff = """SELECT modular,funname  FROM result where errorrate >0.7 or failrate >0.8;"""
    tt="""CREATE TABLE IF NOT EXISTS response(id INTEGER primary key NOT NULL,funname varchar (100),describes varchar(1000),priority varchar(50),address varchar(1000),result varchar(30), writer varchar(30),usetime float ,summary nvarchar(10000));"""
    da = Sql(ff).execute_sql()
    print(da)







