import csv

from pyecharts import options as opts
from pyecharts.charts import Geo, Timeline, Bar, Pie
from pyecharts.globals import ChartType

citiesList = []
citiesSellCount = []
citiesMoney = []

monthList = []
monthMoney = []
with open('queryResult/csv/按城市统计的金额.csv', 'r', encoding='utf-8') as f:
    f.readline()  # 跳表头
    for row in csv.reader(f):
        citiesList.append(row[0])
        citiesMoney.append(int(float(row[1])))  # 硬转一层跳float, 带小数点直接转报错
with open('queryResult/csv/按城市统计的数量.csv', 'r', encoding='utf-8') as f:
    f.readline()
    for row in csv.reader(f):
        citiesSellCount.append(int(float(row[1])))

with open('queryResult/csv/按月份统计的.csv', 'r', encoding='utf-8') as f:
    f.readline()
    for row in csv.reader(f):
        monthList.append('20年-{}月'.format(row[0]))
        monthMoney.append(int(float(row[1])))

graph1 = (
    Geo()
        .add_schema(maptype="china")
        .add(
        "geo",
        [list(z) for z in zip(citiesList, citiesMoney)],
        type_=ChartType.HEATMAP,
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="销售金额热力图"),
    )
).render('销售金额热力图.html')

graph2 = (
    Geo()
        .add_schema(maptype="china")
        .add(
        "geo",
        [list(z) for z in zip(citiesList, citiesSellCount)],
        type_=ChartType.HEATMAP,
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="销售数量热力图"),
    )
).render('销售数量热力图.html')

# 语句用途
# SELECT t_product.product_screen_size, SUM(t_sale.sale_product_count)
# FROM t_sale, t_product
# WHERE t_sale.sale_product_id = t_product.product_id
# AND MONTH(t_sale.sale_check_time) = %MONTH%     !!!!!-CHANGE HERE-!!!!!
# GROUP BY product_screen_size;
#
# sql内做函数不方便, 用SQL取到每个月的分尺寸销量做可视化

name_list = ['27', '32', '38', '42', '46', '48', '55', '60', '65', '70', '88']
total_data = {}
classified_data = {}
for month in range(3, 11):
    tmpY = []
    tmpClassifiedSmall = 0
    tmpClassifiedMedium = 0
    tmpClassifiedLarge = 0
    with open('queryResult/' + str(month) + '.csv', 'r', encoding='utf-8') as f:
        f.readline()  # 跳表头
        for row in csv.reader(f):
            tmpScreenSize = int(row[0])
            tmpSell = int(float(row[1]))
            tmpY.append(tmpSell)
            if tmpScreenSize < 40:
                tmpClassifiedSmall += tmpSell
            elif tmpScreenSize > 60:
                tmpClassifiedLarge += tmpSell
            else:
                tmpClassifiedMedium += tmpSell
    total_data[month] = tmpY
    classified_data[month] = [tmpClassifiedSmall, tmpClassifiedMedium, tmpClassifiedLarge]


def get_month_overlap_chart(month: int) -> Bar:
    bar = (
        Bar().add_xaxis(xaxis_data=name_list)
            .add_yaxis(
            series_name="销量",
            y_axis=total_data[month],
            label_opts=opts.LabelOpts(is_show=True),
        ).set_global_opts(
            title_opts=opts.TitleOpts(
                title="2020年{}月各尺寸销量".format(month)
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="shadow"
            ),
            xaxis_opts=opts.AxisOpts(name='单位: 英寸'),
            yaxis_opts=opts.AxisOpts(name='销量: 台')
        ).set_series_opts(
            label_opts=opts.LabelOpts(is_show=True),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="average", name="平均值"),
                ]
            ),
        )
    )
    pie = (
        Pie()
            .add(
            series_name="销售占比",
            data_pair=[
                ["小屏(<=38寸)", classified_data[month][0]],
                ["中等大小屏幕", classified_data[month][1]],
                ["大屏(>=65寸)", classified_data[month][2]]
            ],
            center=["25%", "35%"],
            radius="28%",
        )
            .set_series_opts(tooltip_opts=opts.TooltipOpts(is_show=True, trigger="item"))
    )
    return bar.overlap(pie)


# 生成时间轴的图
timeline = Timeline(init_opts=opts.InitOpts(width="1400px", height="700px"))

for m in range(3, 11):
    timeline.add(get_month_overlap_chart(month=m), time_point=str(m))

timeline.add_schema(is_auto_play=True, play_interval=1000)
timeline.render("sellStats.html")
