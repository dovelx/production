#2020-6-29

from case.case16 import *
#from case.case38 import  case38
from htmlreporter import HtmlReport
from sendmail import MyMail
import configparser
from runners import runner3
from runners import runner2
from globalpkg.global_var import *
#from runners import pc_login
import sys
testsuitex = []
testsuitrul = []

# 临时cookies
#cookies = {'JSESSIONID': '743109AE5B44B3A5208A69FE52A4EF0BLKmKYh'}

#cookies = pc_login.cookies

# 记录测试开始时间
start_time = datetime.datetime.now()

#执行测试

#mobile-手机端预约
#runner2.runmobile(testsuitm33)
#PC-安全分析
runner3.runcase_changqing(testsuit14)
#mobile-安全分析确认
runner2.runmobile(testsuit15)
#mobile-作业任务添加
#runner2.runmobile(testsuitm37)
#pc-作业票提交

runner3.runcase_changqing(testsuit16)
#mobile-现场确认作业票
#runner2.runmobile(testsuitm39)
#mobile-作业票关闭
#runner2.runmobile(testsuitm40)
# 记录测试结束时间
end_time = datetime.datetime.now()
# 构造测试报告
html_report = HtmlReport('test report', 'ushayden_interface_autotest_report')
html_report.set_time_took(str(end_time - start_time))  # 计算测试消耗时间

# 读取测试报告路径及文件名
config = configparser.ConfigParser()
config.read('./config/report.conf', encoding='utf-8')
dir_of_report = config['REPORT']['dir_of_report']
report_name = config['REPORT']['report_name']

# 设置报告生成路
html_report.mkdir_of_report(dir_of_report)

# 生成测试报告
html_report.generate_html(report_name)

logger.info('生成测试报告成功%s',name)
# if sys.argv[1] == '1':
#     # 记录测试结束时间
#     end_time = datetime.datetime.now()
#     # 构造测试报告
#     html_report = HtmlReport('test report', 'ushayden_interface_autotest_report')
#     html_report.set_time_took(str(end_time - start_time))  # 计算测试消耗时间
#
#     # 读取测试报告路径及文件名
#     config = configparser.ConfigParser()
#     config.read('./config/report.conf', encoding='utf-8')
#     dir_of_report = config['REPORT']['dir_of_report']
#     report_name = config['REPORT']['report_name']
#
#     # 设置报告生成路
#     html_report.mkdir_of_report(dir_of_report)
#
#     # 生成测试报告
#     html_report.generate_html(report_name)
#
#     logger.info('生成测试报告成功')
#
#     mymail = MyMail('./config/mail.conf')
#     mymail.connect()
#     mymail.login()
#     mail_content = 'Hi，附件为接口测试报告，烦请查阅'
#     mail_tiltle = '【测试报告】接口测试报告' + str(executed_history_id)
#     logger.info(html_report.get_filename())
#     attachments = set([html_report.get_filename()])
#
#     logger.info('正在发送测试报告邮件...')
#     mymail.send_mail(mail_tiltle, mail_content, attachments)
#     mymail.quit()
#
#     logger.info('发送邮件成功')
#     logger.info("-------------------------------------THE_END----------------------------------------------------------------------")