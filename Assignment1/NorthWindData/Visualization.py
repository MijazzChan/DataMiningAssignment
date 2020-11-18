import csv

from pyecharts.charts import Line, Geo, Bar, Page
from pyecharts import options as opts
from pyecharts.globals import ChartType

xDate = []
ySellAmount = []
ySellAmountSum = []
xCity = []
yCityCount = []
with open('queryResult/SELECT_year_tOrder_orderDate_.csv', 'r', encoding='utf-8') as f:
    f.readline() # 跳表头
    for row in csv.reader(f):
        xDate.append('{}-{}'.format(row[0], row[1]))
        ySellAmount.append(round(float(row[2]), 0))

ySellAmountSum.append(ySellAmount[0])
for index in range(1, len(ySellAmount)):
    ySellAmountSum.append(ySellAmountSum[len(ySellAmountSum)-1]+ySellAmount[index])

with open('queryResult/SELECT_tOrder_ownerCity_AS_count_t.csv', 'r', encoding='utf-8') as f:
    f.readline()
    for row in csv.reader(f):
        xCity.append(row[0])
        yCityCount.append(int(row[1]))


graph1 = (
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xDate)
    .add_yaxis("总销量", ySellAmountSum, is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="销量总金额"))
)

graph2 = (
    Bar(
        init_opts=opts.InitOpts(
            animation_opts=opts.AnimationOpts(
                animation_delay=1000, animation_easing="elasticOut"
            ), width="1600px", height="800px"
        )
    )
    .add_xaxis(xDate)
    .add_yaxis("每月销售量", ySellAmount)
    .set_global_opts(title_opts=opts.TitleOpts(title="每月销售金额"))
)

graph3 = (
    Geo(init_opts=opts.InitOpts(width="1600px", height="800px"))
        .add_schema(maptype="china")
        .add(
        "geo",
        [list(z) for z in zip(xCity, yCityCount)],
        type_=ChartType.HEATMAP,
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="货主位置热力图"),
    )
)

p = Page().add(graph1).add(graph2).add(graph3).render('可视化.html')