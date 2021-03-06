from datetime import datetime

# 数据库配置
USERNAME = 'dataminingassignment1'
PASSWORD = 'dataminingassignment1'
HOSTNAME = '192.168.123.4'
PORT = '10000'
DATABASE = 'DataMiningAssignment1'
DB_URL = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8mb4' \
    .format(username=USERNAME, pwd=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)

# 数据来自于 www.liemingwang.com/gsmz/maoyi/1056.html
TRADE_COMPANY = '亿博源贸易有限公司 天扬贸易有限公司 雷驰尊上贸易公司 捷龙贸易有限公司 金利贸易公司 齐齐贸易有限公司 新丰商贸有限公司 龙博贸易公司 嘉利华商贸有限公司 佰仕贸易有限公司 名都商贸有限公司 富蒙商贸有限公司 新诚贸易公司 鸿泰商贸有限公司 舜杰商贸有限公司 尊海贸易有限公司 金涛贸易公司 炜烨贸易有限公司 圣尔贸易公司 迪派贸易有限公司 联翼贸易有限公司 欣景博贸易有限公司 五湖贸易有限公司 国晶贸易有限公司 欣源宏商贸有限公司 新都贸易公司 光明贸易公司 凯瑞特商贸有限公司 锦程正阳商贸公司 贵发贸易公司 唯品商贸有限公司 乐一商贸有限公司 汇川商贸有限公司 大帆商贸公司 福泰商贸有限公司 润森工贸有限公司 天大物贸有限公司 合盛贸易有限公司 汇达贸易有限公司 鑫仟顺贸易有限公司 利晟商贸有限公司 多优多商贸有限公司 浩友贸易有限公司 永逸贸易公司 佳丽商贸有限公司 伊厦贸易有限公司 九紫星贸易有限公司 赢时贸易有限公司 生德贸易有限责任公司 赛岐贸易有限公司 三鑫贸易有限公司 蚂蚁商贸有限公司 爱威尔商贸公司 辰南商贸公司 兴燕贸易有限公司 韵仪商贸公司 景悦商贸有限公司 信杰诚贸易有限公司 富林贸易有限公司 九桥商贸公司 吕红发商贸公司 翔鹏商贸有限公司 易露发贸易公司 森鑫源贸易有限公司 铭航商贸有限责任公司 俊雅商贸有限公司 白帆贸易有限公司 恒顺祥商贸有限公司 苏川联志贸易公司 金伙伴商贸有限公司 荣祥商贸有限公司 勤裕鼎商贸公司 荣福实业贸易公司 鲜派贸易有限公司 鹏昊贸易有限公司 骏兴贸易有限责任公司 五丰商贸有限公司 兴荣强商贸有限公司 蓉蓉商贸有限公司 宇德贸易有限公司 森道尔贸易有限公司 圣金龙商贸有限公司 天友商贸有限责任公司 万晟贸易有限公司 东威宏贸易有限公司 益民工贸有限公司 波菲特商贸有限公司 恒远商贸公司 嘉实伟业商贸有限公司 沐和贸易有限公司 桓瑞贸易有限公司 天娇贸易有限公司' \
    .split(' ')
SUPPLIER_COMPANY = '广盈宝 聚昌泰 亚富通 万宏谦 仁裕如 富佳裕 协汇复 耀吉辉 鼎永捷 新益伟 复发春 圣祥利 裕义康 厚圣康 嘉合兴 裕亚鑫 义贵华 久万浩 巨润恒 益宏元 众义达 恒永谦 寿台圣 茂正金 豪嘉利 发瑞圣 恒美合 洪鼎瑞 昌益广 全伟光 优聚全 光多宏 聚昌进 新凯本 正广圣 新成鼎 合干长 鸿升行 升佳福 厚盈寿 祥康宏 亨裕圣 正复长 鑫泰贵 鑫丰禄 顺润泰 隆长禄 大聚凯 光鑫茂 禄大永 贵发优 福顺德'.split(
    ' ')
# 名, 城市配置
FIRST_NAME = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄"
FEMALE_NAME = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
MALE_NAME = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
CITIES = '上海、北京、深圳、广州、天津、重庆、苏州、成都、武汉、杭州、南京、青岛、无锡、长沙、宁波、郑州、佛山、济南、南通、东莞'.split('、')
DELIVERY_COMPANY = '顺丰速递 德邦物流 百世汇通 EMS 中通快递 申通快递 圆通快递 韵达快递 天天快递'.split(' ')
DELIVERY_COMPANY_WEIGHT = [83, 79, 75, 74, 70, 68, 70, 60]

# 静态Specs
EMPLOYEE_COUNT = 300
CUSTOMER_COUNT = len(TRADE_COMPANY)
SUPPLIER_COMPANY_COUNT = len(SUPPLIER_COMPANY)
PRODUCT_COUNT = 80
DELIVERY_COMPANY_COUNT = len(DELIVERY_COMPANY)
TIME_START = datetime.strptime('2020/03/01-08:01:01', '%Y/%m/%d-%H:%M:%S')
TIME_END = datetime.strptime('2020/10/01-23:59:59', '%Y/%m/%d-%H:%M:%S')
# 相隔214天

# 1,000,000条销量数据
SALES_COUNT = 1000000
