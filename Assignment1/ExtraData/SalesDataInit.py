import uuid
from datetime import timedelta
from random import choice, randint, randrange

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ExtraData.CONSTANTS import *

# INSTALL pymysql AT FIRST
# sqlalchemy有pymysql依赖

# 工具函数类  Utils-Functions Here
def genRandomDate(start, end):
    """
    用于生成两日之间的随机datetime, CONSTANTS处可改变起始与结束
    :param start: 开始日期
    :param end: 结束日期
    :return: 随机datetime
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def genEmployee(num):
    """
    生成员工对象赋随机参数
    :param num: 数量
    :return: List(员工)
    """
    employeeList = []
    for i in range(num):
        if choice(['male', 'female']) == 'male':
            employeeList.append(Employee(employee_name=genName(True),
                                         employee_tel=str(randint(13000000000, 14000000000)), employee_sex=True))
        else:
            employeeList.append(Employee(employee_name=genName(False),
                                         employee_tel=str(randint(13000000000, 14000000000)),
                                         employee_sex=False))
    return employeeList


def genCustomer():
    """
    生成随机顾客对象
    :return: List(顾客)
    """
    tradeCompanyList = []
    for i in range(len(TRADE_COMPANY)):
        tradeCompanyList.append(Customer(customer_name=TRADE_COMPANY[i],
                                         customer_tel=str(randint(13000000000, 14000000000)),
                                         customer_city=choice(CITIES)))
    return tradeCompanyList


def genName(sex):
    """
    依据CONSTANTS中的姓名列随机生成姓名
    :param sex: 性别
    :return: 单个姓名
    """
    name = choice(FIRST_NAME[choice(range(len(FIRST_NAME)))])
    if sex:
        name += choice(MALE_NAME[choice(range(len(MALE_NAME)))])
        name += choice(MALE_NAME[choice(range(len(MALE_NAME)))])
    else:
        name += choice(FEMALE_NAME[choice(range(len(FEMALE_NAME)))])
        name += choice(FEMALE_NAME[choice(range(len(FEMALE_NAME)))])
    return name


def genSupplier():
    """
    生成供货商对象, 单次生成数量在CONSTANTS处可调
    :return: List(供货商)
    """
    supplierList = []
    for i in range(len(SUPPLIER_COMPANY)):
        supplierList.append(Supplier(supplier_name=SUPPLIER_COMPANY[i],
                                     supplier_tel=str(randint(13000000000, 14000000000))))
    return supplierList


def genProduct(count):
    """
    生成产品对象, 有权重
    :param count: 数量
    :return: List(产品)
    """
    productList = []
    size = [27, 32, 38, 42, 46, 48, 55, 60, 65, 70, 88]
    # 尺寸权重
    preps = [1, 2, 3, 4, 3, 5, 8, 4, 7, 3, 1]
    n = []
    for i in range(len(size)):
        for j in range(preps[i]):
            n.append(size[i])
    for i in range(count):
        sizeTmp = choice(n)
        productList.append(
            Product(product_name=(uuid.uuid4().hex[0:6] + str(sizeTmp) + 'TV'), product_screen_size=sizeTmp,
                    product_price=randint(50 * sizeTmp, 150 * sizeTmp),
                    product_storage=randint(100, 100000)))
    return productList


def genDeliveryCompany():
    """
    生成送货公司对象
    :return: List(送货公司)
    """
    deliveryCompany = []
    for i in range(len(DELIVERY_COMPANY)):
        deliveryCompany.append(DeliveryCorp(delivery_name=DELIVERY_COMPANY[i]))
    return deliveryCompany


def genSalesChecks(salesCount):
    """
    生成销售记录对象, 满足CONSTANTS处的数量约束以及外键约束
    :param salesCount: 条目数量
    :return: List(销售记录)
    """
    salesList = []
    for _ in range(salesCount):
        tmp = Sale(sale_product_id=randint(1, PRODUCT_COUNT), sale_customer_id=randint(1, CUSTOMER_COUNT),
                   sale_employee_id=randint(1, EMPLOYEE_COUNT), sale_supplier_id=randint(1, SUPPLIER_COMPANY_COUNT),
                   sale_check_time=genRandomDate(TIME_START, TIME_END),
                   sale_delivery_id=randint(1, DELIVERY_COMPANY_COUNT),
                   sale_product_count=randint(1, 200))
        salesList.append(tmp)
    return salesList


engine = create_engine(DB_URL, echo=True)
Base = declarative_base(engine)


# 实体类(表类) Entity Class
# 类Spring Data JPA(JAVA)写法
class Customer(Base):
    __tablename__ = 't_customer'
    customer_id = Column(BIGINT, primary_key=True, autoincrement=True)
    customer_name = Column(VARCHAR(100), nullable=False)
    customer_city = Column(VARCHAR(40), nullable=False)
    customer_tel = Column(VARCHAR(40), nullable=True)


class Employee(Base):
    __tablename__ = 't_employee'
    employee_id = Column(BIGINT, primary_key=True, autoincrement=True)
    employee_name = Column(VARCHAR(40), nullable=False)
    employee_tel = Column(VARCHAR(40), nullable=True)
    employee_sex = Column(Boolean, nullable=True)


class Supplier(Base):
    __tablename__ = 't_supplier'
    supplier_id = Column(BIGINT, primary_key=True, autoincrement=True)
    supplier_name = Column(VARCHAR(100), nullable=False)
    supplier_tel = Column(VARCHAR(40), nullable=True)


class Product(Base):
    __tablename__ = 't_product'
    product_id = Column(BIGINT, primary_key=True, autoincrement=True)
    product_name = Column(VARCHAR(100), nullable=False, index=True)
    product_screen_size = Column(INTEGER, nullable=False)
    product_price = Column(DECIMAL(8, 2), nullable=False)
    product_storage = Column(INTEGER, nullable=False)
    CheckConstraint(product_storage >= 0, 'storage_negetive_check')


class DeliveryCorp(Base):
    __tablename__ = 't_delivery'
    delivery_id = Column(INTEGER, primary_key=True, autoincrement=True)
    delivery_name = Column(VARCHAR(40), nullable=False)


class Sale(Base):
    __tablename__ = 't_sale'
    sale_check_id = Column(BIGINT, primary_key=True, autoincrement=True)
    sale_product_id = Column(BIGINT, index=True, nullable=False)
    sale_customer_id = Column(BIGINT, index=True, nullable=False)
    sale_employee_id = Column(BIGINT, index=True, nullable=False)
    sale_supplier_id = Column(BIGINT, index=True, nullable=False)
    sale_check_time = Column(DateTime, nullable=False)
    sale_delivery_id = Column(INTEGER, nullable=False)
    sale_product_count = Column(BIGINT, nullable=False)
    ForeignKeyConstraint([sale_product_id], [Product.product_id], name='fk_product_id')
    ForeignKeyConstraint([sale_customer_id], [Customer.customer_id], name='fk_customer_id')
    ForeignKeyConstraint([sale_employee_id], [Employee.employee_id], name='fk_employee_id')
    ForeignKeyConstraint([sale_supplier_id], [Supplier.supplier_id], name='fk_supplier_id')
    ForeignKeyConstraint([sale_delivery_id], [DeliveryCorp.delivery_id], name='fk.delivery_id')
    CheckConstraint(sale_product_count >= 0, 'product_count_check')

# 表类重建
Base.metadata.drop_all()
Base.metadata.create_all()

session = sessionmaker(engine)()

# 载入对象并通过session将对象写入持久化
# JAVA-SPRING DATA JPA - Repository.save() but need manual flush the buffer
session.add_all(genEmployee(EMPLOYEE_COUNT))
session.add_all(genCustomer())
session.add_all(genSupplier())
session.add_all(genProduct(PRODUCT_COUNT))
session.add_all(genDeliveryCompany())
session.commit()
session.add_all(genSalesChecks(SALES_COUNT))

# TODO: YOU MAY NEED TO DO THIS IN BATCH, SINCE IT SUCKS ME 2.8GiB/16GiB MEMORY USAGE HERE!
# TODO: 如果内存不够建议分批处理
# SPLIT_TIME = 20
# for _ in range(SPLIT_TIME):
#     session.add_all(genSalesChecks(int(SALES_COUNT/SPLIT_TIME)))
#     time.sleep(1)

session.commit()
