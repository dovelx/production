#from globalpkg.global_var import sql_query_jsa_step_harm_id
from tools import tool
# from globalpkg.global_var import tsi
# from globalpkg.global_var import workticketid
# from globalpkg.global_var import worktaskid
# from globalpkg.global_var import worktaskid1
# from globalpkg.global_var import jsaid
# from globalpkg.global_var import safeclarid
# from globalpkg.global_var import sql_query_work_appointid
# from globalpkg.global_var import sql_query_jsastepid
# from globalpkg.global_var import sql_query_jsa_step_measure_id
# from tools import getdata
#
case = '长岭项目作业许可-PC-作业统计'
#
# #times
# starttime = tool.starttime
# endtime = tool.endtime
# now = tool.now
#
#作业预约名称
name = tool.ran_name_with_str()
print("作业预约名称：",name)


#用例信息变量定义
testsuit81 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

count =0

#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '作业统计-作业票统计'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'gh'
caseinfo['exresult'] =  {"条件":[{"模式":"用火作业", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORKTICKET_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522workstatus_name%2522%253A%2522%25E7%258E%25B0%25E5%259C%25BA%25E7%25A1%25AE%25E8%25AE%25A4%2522%252C%2522workstatus%2522%253A%2522sceneConfirm%2522%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-07-01%2522%257D&0.06904107842711249
#url = 'http://192.168.6.156/hse/HSE_WORKTICKET_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522workstatus_name%2522%253A%2522%25E7%258E%25B0%25E5%259C%25BA%25E7%25A1%25AE%25E8%25AE%25A4%2522%252C%2522workstatus%2522%253A%2522sceneConfirm%2522%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-07-01%2522%257D&0.06904107842711249http://192.168.6.156/hse/HSE_WORKTICKET_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522workstatus_name%2522%253A%2522%25E7%258E%25B0%25E5%259C%25BA%25E7%25A1%25AE%25E8%25AE%25A4%2522%252C%2522workstatus%2522%253A%2522sceneConfirm%2522%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-07-01%2522%257D&0.06904107842711249'
url = "http://192.168.6.156/hse/HSE_WORKTICKET_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522workstatus_name%2522%253Anull%252C%2522workstatus%2522%253Anull%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-07-01%2522%257D&0.5619507386663365"
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit81.append(caseinfo.copy())

caseinfo['id'] = 2
caseinfo['name'] = '作业统计-作业任务耗时统计'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'gh'
caseinfo['exresult'] = {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORK_TASK_TIME_CONSUME/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK_TIME_CONSUME&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522territorialunitid%2522%253A2000000004016%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-07-01%2522%257D&0.885418189987921
url = 'http://192.168.6.156/hse/HSE_WORK_TASK_TIME_CONSUME/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK_TIME_CONSUME&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522territorialunitid%2522%253A2000000004016%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-07-01%2522%257D&0.885418189987921http://192.168.6.156/hse/HSE_WORK_TASK_TIME_CONSUME/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK_TIME_CONSUME&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522territorialunitid%2522%253A2000000004016%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-07-01%2522%257D&0.885418189987921'
url = 'http://192.168.6.156/rqreports/hse/HSE_WORK_TASK_TIME_CONSUME/reportCommonShow?rpx=HSE_WORK_TASK_TIME_CONSUME.rpx&scroll=no&territorialunitid=1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%2C40%2C41%2C42%2C43%2C44%2C45%2C46%2C47%2C48%2C2000000004965%2C2000000004966%2C2000000004967%2C2000000004968%2C2000000005061%2C2000000005062%2C2000000005063%2C2000000005064%2C2000000005065%2C2000000005066%2C2000000005067%2C2000000005068%2C2000000005069%2C2000000005070%2C2000000005071%2C2000000005072%2C2000000005073%2C2000000005074%2C2000000005075%2C2000000005076%2C2000000005077%2C2000000005078%2C2000000005079%2C2000000005080%2C2000000005081%2C2000000005082%2C2000000005083%2C2000000005084%2C2000000005085%2C2000000005086%2C2000000005087%2C2000000005088%2C2000000005089%2C2000000005090%2C2000000005091%2C2000000005092%2C2000000005093%2C2000000005094%2C2000000005095%2C2000000005096%2C2000000005097%2C2000000005098%2C2000000005099%2C2000000005100%2C2000000005101%2C2000000005102%2C2000000005566%2C2000000004016&pcContext=http%3A%2F%2F192.168.6.156%3A80&endtime=2020-07-31&territorialunitname=%E4%B8%AD%E7%9F%B3%E5%8C%96%E9%95%BF%E5%B2%AD%E5%88%86%E5%85%AC%E5%8F%B8&starttime=2020-06-01&uuid=1639ecb2851e41a68cd5fe2ad8e530c6ljrERRefcojAGrDCmkSuGLqbgUblILhttp://192.168.6.156/rqreports/hse/HSE_WORK_TASK_TIME_CONSUME/reportCommonShow?rpx=HSE_WORK_TASK_TIME_CONSUME.rpx&scroll=no&territorialunitid=1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%2C40%2C41%2C42%2C43%2C44%2C45%2C46%2C47%2C48%2C2000000004965%2C2000000004966%2C2000000004967%2C2000000004968%2C2000000005061%2C2000000005062%2C2000000005063%2C2000000005064%2C2000000005065%2C2000000005066%2C2000000005067%2C2000000005068%2C2000000005069%2C2000000005070%2C2000000005071%2C2000000005072%2C2000000005073%2C2000000005074%2C2000000005075%2C2000000005076%2C2000000005077%2C2000000005078%2C2000000005079%2C2000000005080%2C2000000005081%2C2000000005082%2C2000000005083%2C2000000005084%2C2000000005085%2C2000000005086%2C2000000005087%2C2000000005088%2C2000000005089%2C2000000005090%2C2000000005091%2C2000000005092%2C2000000005093%2C2000000005094%2C2000000005095%2C2000000005096%2C2000000005097%2C2000000005098%2C2000000005099%2C2000000005100%2C2000000005101%2C2000000005102%2C2000000005566%2C2000000004016&pcContext=http%3A%2F%2F192.168.6.156%3A80&endtime=2020-07-31&territorialunitname=%E4%B8%AD%E7%9F%B3%E5%8C%96%E9%95%BF%E5%B2%AD%E5%88%86%E5%85%AC%E5%8F%B8&starttime=2020-06-01&uuid=1639ecb2851e41a68cd5fe2ad8e530c6ljrERRefcojAGrDCmkSuGLqbgUblIL'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit81.append(caseinfo.copy())

caseinfo['id'] = 3
caseinfo['name'] = '作业统计-办票耗时统计'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'gho'
caseinfo['exresult'] = {"条件":[{"模式":"长岭石化管理员", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORK_TICKET_TIME_CONSUM/workTimeConsum?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TICKET_TIME_CONSUM&orgid=&starttime=&endtime=&displayorder=0&0.8587592777046524&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_TICKET_TIME_CONSUM/workTimeConsum?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TICKET_TIME_CONSUM&orgid=&starttime=&endtime=&displayorder=0&0.8587592777046524&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit81.append(caseinfo.copy())

caseinfo['id'] = 4
caseinfo['name'] = '作业统计-年度票证类型数量统计'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'gh'
caseinfo['exresult'] = {"条件":[{"模式":"用火作业", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORKTICKET_ANNUAL_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_ANNUAL_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522year%2522%253A%25222020%2522%257D&0.57361167452527
url = 'http://192.168.6.156/hse/HSE_WORKTICKET_ANNUAL_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_ANNUAL_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522year%2522%253A%25222020%2522%257D&0.57361167452527'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit81.append(caseinfo.copy())

caseinfo['id'] = 5
caseinfo['name'] = '作业统计-任务/票证分布情况统计'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'gh'
caseinfo['exresult'] = {"条件":[{"模式":"票证明细", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORKTICKET_DISTRIBUTION_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_DISTRIBUTION_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522year%2522%253A%25222020%2522%257D&0.9875320375286794
url = 'http://192.168.6.156/hse/HSE_WORKTICKET_DISTRIBUTION_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_DISTRIBUTION_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522year%2522%253A%25222020%2522%257D&0.9875320375286794'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit81.append(caseinfo.copy())

caseinfo['id'] = 6
caseinfo['name'] = '作业统计-票证问题统计'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'gh'
caseinfo['exresult'] =  {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORKTICKET_PROBLEMS_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_PROBLEMS_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522year%2522%253A%25222020%2522%257D&0.7745833126418957
url = 'http://192.168.6.156/hse/HSE_WORKTICKET_PROBLEMS_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_PROBLEMS_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E4%25B8%25AD%25E7%259F%25B3%25E5%258C%2596%25E9%2595%25BF%25E5%25B2%25AD%25E5%2588%2586%25E5%2585%25AC%25E5%258F%25B8%2522%252C%2522orgid%2522%253A2000000004016%252C%2522year%2522%253A%25222020%2522%257D&0.7745833126418957'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit81.append(caseinfo.copy())
