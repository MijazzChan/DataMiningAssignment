-- CREATE DATABASE IF NOT EXISTS DataMiningAssignment1;
--
-- GRANT ALL PRIVILEGES ON DataMiningAssignment1.* TO 'dataminingassignment1'@'192.168.123.2' IDENTIFIED BY 'dataminingassignment1';
--
-- FLUSH PRIVILEGES;

# 客户总流水(十大客户)
SELECT t_customer.customer_id                                   AS '客户id',
       t_customer.customer_name                                 AS '客户名',
       sum(t_sale.sale_product_count * t_product.product_price) AS '总流水'
FROM t_customer,
     t_product,
     t_sale
WHERE t_customer.customer_id = t_sale.sale_customer_id
  AND t_product.product_id = t_sale.sale_product_id
GROUP BY t_customer.customer_id
ORDER BY 总流水 DESC
LIMIT 10;


# 客户平均订单金额排名
SELECT t_customer.customer_id                                                                    AS '客户id',
       t_customer.customer_name                                                                  AS '客户名',
       count(t_sale.sale_customer_id)                                                            AS '总单量',
       sum(t_sale.sale_product_count * t_product.product_price)                                  AS '总价',
       sum(t_sale.sale_product_count * t_product.product_price) / count(t_sale.sale_customer_id) AS '平均每单价格'
FROM t_customer,
     t_sale,
     t_product
WHERE t_customer.customer_id = t_sale.sale_customer_id
  AND t_product.product_id = t_sale.sale_product_id
GROUP BY t_customer.customer_id
ORDER BY 平均每单价格 DESC
LIMIT 10;


# 员工开单金额流水排名
SELECT t_employee.employee_id                                   AS '雇员id',
       t_employee.employee_name                                 AS '雇员姓名',
       sum(t_sale.sale_product_count * t_product.product_price) AS '雇员总流水'
FROM t_employee,
     t_product,
     t_sale
WHERE t_employee.employee_id = t_sale.sale_employee_id
  AND t_product.product_id = t_sale.sale_product_id
GROUP BY t_employee.employee_id
ORDER BY 雇员总流水 DESC
LIMIT 10;


# 热销产品排名
SELECT t_product.product_id           AS '产品编号',
       t_product.product_name         AS '产品型名',
       t_product.product_screen_size  AS '屏幕大小',
       t_product.product_price        AS '单价',
       sum(t_sale.sale_product_count) AS '总销量'
FROM t_product,
     t_sale
WHERE t_product.product_id = t_sale.sale_product_id
GROUP BY t_product.product_id
ORDER BY 总销量 DESC
LIMIT 10;


# 按屏幕尺寸的销量排名(合并多产品的, 取尺寸为GROUP BY的)
SELECT t_product.product_screen_size  AS '屏幕尺寸',
       sum(t_sale.sale_product_count) AS '销量'
FROM t_product,
     t_sale
WHERE t_product.product_id = t_sale.sale_product_id
GROUP BY 屏幕尺寸
ORDER BY 销量 DESC
LIMIT 20;

# 3日内可能出现库存告警的, 数据共214天, 取平均日销量的
SELECT t_product.product_id                                                   AS '产品编号',
       t_product.product_name                                                 AS '产品型名',
       sum(t_sale.sale_product_count) / 214                                   AS '平均日销量',
       t_product.product_storage                                              AS '存量',
       (t_product.product_storage < sum(t_sale.sale_product_count) / 214 * 3) AS '库存告警',
       t_product.product_storage / (sum(t_sale.sale_product_count) / 214)     AS '预计剩余天数'
FROM t_product,
     t_sale
WHERE t_product.product_id = t_sale.sale_product_id
GROUP BY t_product.product_id
ORDER BY 预计剩余天数 ASC
LIMIT 100;

# 按城市统计销售量的
SELECT t_customer.customer_city         AS '客户城市',
	     sum( t_sale.sale_product_count ) AS '销售产品数量'
FROM
	t_sale,
	t_product,
	t_customer
WHERE
	  t_sale.sale_product_id = t_product.product_id
AND t_sale.sale_customer_id = t_customer.customer_id
GROUP BY t_customer.customer_city
ORDER BY 销售产品数量 DESC
LIMIT 20;

# 按城市统计销售金额的
SELECT t_customer.customer_city         AS '客户城市',
	     sum( t_sale.sale_product_count * t_product.product_price ) AS '销售金额'
FROM
	t_sale,
	t_product,
	t_customer
WHERE
	  t_sale.sale_product_id = t_product.product_id
AND t_sale.sale_customer_id = t_customer.customer_id
GROUP BY t_customer.customer_city
ORDER BY 销售金额 DESC
LIMIT 20;

# 按月份统计销售额
SELECT MONTH(t_sale.sale_check_time)                            AS '月份',
       sum(t_sale.sale_product_count * t_product.product_price) AS '单月销售额'
FROM t_sale, t_product
WHERE t_sale.sale_product_id = t_product.product_id
GROUP BY 月份
ORDER BY 单月销售额
LIMIT 10;