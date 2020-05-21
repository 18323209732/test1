import os
from Common.ReadYaml import ConfigYaml
from Common.Template import html_all,html_all_case,html_all_end,html_body,html_button,html_head,html_sum__end,html_other
# from Common.GetPath import second_path
from Common.Route import Any_Path
class GetReport:
    def __init__(self, data, dir, filename, encoding = "utf-8"):
        '''

        :param data:  传入数据
        :param dir:   目录名称
        :param filename:    文件名称
        :param encoding:
        '''
        self.encoding = encoding
        self.data = data
        self.report_path = Any_Path(dir)
        self.report = Any_Path(dir, filename)
        self.html_head = html_head
        self.senum = len(self.data.get("success"))                                          #成功用例集
        self.ernum = len(self.data.get("error"))                                            #错误用例集
        self.fanum = len(self.data.get("fail"))                                           #失败用例集
        self.tinum = len(self.data.get("timeout"))                                       #超时用例集
        self.sknum = len(self.data.get("skip"))                                          # 跳过用例集
        self.info = self.data.get("info")                                               #概况数据
        self.alnum = self.senum + self.ernum + self.fanum + self.tinum + self.sknum     #总执行用例数
        self.succrate = round(self.senum/(self.alnum - self.sknum)*100,2)                      #成功率
        self.html_butt = html_button.format(self.alnum, self.senum,
                         self.fanum, self.ernum, self.tinum, self.sknum)             #数据连接

        self.sestr = ''                        #成功用例报告字符
        self.fastr = ''                        #失败用例报告字符
        self.erstr = ''                        #错误用例报告字符
        self.skstr = ''                        #跳过用例报告字符
        self.tistr = ''                        #超时用例报告字符
        self.alstr = ''                        #所有用例报告字符

    def get_str(self, status: str, case: dict):

        '''
        用例字符串拼接，返回
        :param case:
        :return:
        '''

        case_str = html_all_case.format(
                        case.get('funname'), case.get('describe'), case.get('priority'),
                        case.get('address'),case.get('status'), case.get('writer'),
                        round(case.get('usetime'), 2), status,case.get('funname'),
                        status, case.get('funname'), status, case.get('funname'), status,
                        case.get('funname'), case.get('summary')
                        )

        return case_str

    def generate_report(self):
        '''
        获取并拼接所有字符串
        :return:
        '''
        for success in self.data.get("success"):
            self.sestr += self.get_str("su", success)

            self.alstr += self.get_str("al", success)

        for error in self.data.get("error"):
            self.erstr += self.get_str("er", error)

            self.alstr += self.get_str("al", error)

        for fail in self.data.get("fail"):
            self.fastr += self.get_str("fa", fail)

            self.alstr += self.get_str("al", fail)

        for timeout in self.data.get("timeout"):
            self.tistr += self.get_str("ti", timeout)

            self.alstr += self.get_str("al", timeout)

        for skip in self.data.get("skip"):
            self.skstr += self.get_str("sk", skip)

            self.alstr += self.get_str("al", skip)

        sum_alstr = self.html_butt + html_all + self.alstr + html_all_end
        sum_sestr = html_other.format("success") + self.sestr + html_all_end
        sum_fastr = html_other.format("fail") + self.fastr + html_all_end
        sum_erstr = html_other.format("error") + self.erstr + html_all_end
        sum_tistr = html_other.format("timeout") + self.tistr + html_all_end
        sum_skstr = html_other.format("skip") + self.skstr + html_all_end

        all_case_str = sum_alstr + sum_sestr + sum_erstr + sum_fastr + sum_tistr + sum_skstr + html_sum__end

        return all_case_str

    def splicing(self):
        '''
        :return:
        '''
        all_case_str = self.generate_report()
        self.html_body =html_body.format(
                        self.info.get('title'),self.info.get('edition'),
                        self.info.get('science'),self.alnum,
                        self.info.get('sumtime'),self.info.get('startdata'),
                        self.info.get('enddata'),self.info.get('maxtime'),
                        self.info.get('mintime'),self.info.get('avgtime'),
                        self.succrate,self.senum,
                        self.fanum,self.ernum,
                        self.tinum,self.sknum,
                        )

        report = self.html_head + self.html_body + all_case_str

        return report

    def write_report(self):
        '''
        生成报告
        :return:
        '''
        if not os.path.exists(self.report_path):
            os.makedirs(self.report_path)
        with open(self.report, "w", encoding=self.encoding) as f:
            f.write(self.splicing())
            f.close()
            return True


# if __name__=="__main__":





