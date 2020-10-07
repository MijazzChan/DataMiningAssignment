USE northwind;
# TODO: 订单量为主键, 订单数为列不合理, ditched corresponding column

# 输出一张大表，所含信息有订单ID，产品ID，客户ID，雇员ID，供应商ID，时间ID，运货商，货主城市，单价高低（50一个等级），订单数，订单金额，商品数
DROP VIEW IF EXISTS vOrderGlance;
CREATE VIEW vOrderGlance AS
SELECT tOrder.orderID                                               AS '订单ID',
       group_concat(tProduct.productID)                             AS '涉及产品ID',
       group_concat(tProduct.pName)                                 AS '涉及产品名',
       tOrder.customerID                                            AS '顾客ID',
       group_concat(tProduct.supplierID)                            AS '涉及供货商ID',
       date_format(tOrder.orderDate, '%Y-%m-%d')                    AS '订单日期',
       tDeliveryCompany.dCompanyName                                AS '送货公司',
       tOrder.ownerCity                                             AS '货主城市',
       cast(sum(tOrderDetail.productPrice * tOrderDetail.productCount
           * (1 - tOrderDetail.productDiscount)) AS DECIMAL(10, 2)) AS '订单总价',
       count(tOrderDetail.productID)                                AS '涉及商品数'
FROM tOrder,
     tOrderDetail,
     tProduct,
     tDeliveryCompany
WHERE tProduct.productID = tOrderDetail.productID
  AND tOrderDetail.orderID = tOrder.orderID
  AND tOrder.deliveryCompany = tDeliveryCompany.DeliveryCompanyID
GROUP BY tOrder.orderID;


# 输出销售额前十大客户的基本信息；
SELECT tCustomer.customerID                                         AS '顾客ID',
       tCustomer.cCompanyName                                       AS '顾客名',
       cast(sum(tOrderDetail.productCount * tOrderDetail.productPrice
           * (1 - tOrderDetail.productDiscount)) AS DECIMAL(14, 2)) AS '总流水'
FROM tCustomer,
     tOrder,
     tOrderDetail
WHERE tCustomer.customerID = tOrder.customerID
  AND tOrder.orderID = tOrderDetail.orderID
GROUP BY tCustomer.customerID
ORDER BY 总流水 DESC
LIMIT 10;


# 输出平均订单单价最高（总额/订单数）客户的基本信息；
SELECT tCustomer.customerID                                                                            AS '顾客ID',
       tCustomer.cCompanyName                                                                          AS '顾客名',
       sum(tOrderDetail.productCount * tOrderDetail.productPrice * (1 - tOrderDetail.productDiscount)) AS '总流水',
       count(tOrder.customerID)                                                                        AS '单量',
       sum(tOrderDetail.productCount * tOrderDetail.productPrice * (1 - tOrderDetail.productDiscount)) /
       count(tOrder.customerID)                                                                        AS '平均价'
FROM tCustomer,
     tOrder,
     tOrderDetail
WHERE tCustomer.customerID = tOrder.customerID
  AND tOrder.orderID = tOrderDetail.orderID
GROUP BY tCustomer.customerID
ORDER BY 平均价 DESC
LIMIT 10;

# 输出库存不足三天销售的预警商品；
# DAYSDIFF 销售数据开始到结束的天数
# @-> Session-Wide Variable
SET @DAYSDIFF = 0;
SELECT to_days(max(tOrder.orderDate)) - to_days(min(tOrder.orderDate))
FROM tOrder
INTO @DAYSDIFF;
SELECT tProduct.productID,
       tProduct.pName                                                     AS '商品名',
       tProduct.pStorage                                                  AS '库存量',
       sum(tOrderDetail.productCount) / @DAYSDIFF                         AS '日销量',
       sum(tOrderDetail.productCount) / @DAYSDIFF * 3 > tProduct.pStorage AS '库存告急'
FROM tProduct,
     tOrderDetail
WHERE tOrderDetail.productID = tProduct.productID
GROUP BY tProduct.productID
ORDER BY 库存告急 DESC
LIMIT 100;

# 输出订单最多的优秀雇员信息；
SELECT tEmployee.employeeID                        AS '员工号',
       concat(tEmployee.eSurname, tEmployee.eName) AS '员工姓名',
       count(tOrder.orderID)                       AS '总单量'
FROM tEmployee,
     tOrder
WHERE tOrder.employeeID = tEmployee.employeeID
GROUP BY tOrder.employeeID
ORDER BY 总单量 DESC;


# 输出订单总金额的随时间变化图；
SELECT year(tOrder.orderDate)                                                                          AS '年份',
       month(tOrder.orderDate)                                                                         AS '月份',
       sum(tOrderDetail.productCount * tOrderDetail.productPrice * (1 - tOrderDetail.productDiscount)) AS '销量'
FROM tOrder,
     tOrderDetail
WHERE tOrderDetail.orderID = tOrder.orderID
GROUP BY 年份, 月份
ORDER BY 年份 ASC;

# 输出商品销量的特征；即什么商品畅销，什么商品滞销;
SELECT tProduct.productID,
       tProduct.pName                             AS '商品名',
       sum(tOrderDetail.productCount) / @DAYSDIFF AS '日销量'
FROM tProduct,
     tOrderDetail
WHERE tOrderDetail.productID = tProduct.productID
GROUP BY tProduct.productID
ORDER BY 日销量 DESC
LIMIT 30;

# 输出商品销量的特征
SELECT tCategory.categoryName AS '类目', count(tOrderDetail.productID) AS '销量'
FROM tCategory,
     tOrderDetail,
     tProduct
WHERE tOrderDetail.productID = tProduct.productID
  AND tProduct.categoryID = tCategory.categoryID
GROUP BY categoryName
ORDER BY 销量 DESC ;

# 货主地区分析特征;
SELECT tOrder.ownerRegion AS '地区', count(tOrder.ownerName) AS '频数'
FROM tOrder
GROUP BY ownerRegion
ORDER BY 频数 DESC ;

# 货主城市分析特征;
SELECT tOrder.ownerCity AS '城市', count(tOrder.ownerCity) AS '频数'
FROM tOrder
GROUP BY ownerCity
ORDER BY 频数 DESC ;




