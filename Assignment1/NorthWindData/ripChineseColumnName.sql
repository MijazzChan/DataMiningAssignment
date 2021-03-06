USE northwind;

# Fxxk Chinese Column Name for Better Dev Experience
# FxxK CHINESE CHAR
RENAME TABLE 产品 TO tProduct;

ALTER TABLE tProduct
    CHANGE 产品ID productID INT NOT NULL;
ALTER TABLE tProduct
    CHANGE 产品名称 pName VARCHAR(80) NULL;
ALTER TABLE tProduct
    CHANGE 供应商ID supplierID INT NULL;
ALTER TABLE tProduct
    CHANGE 类别ID categoryID INT NULL;
ALTER TABLE tProduct
    CHANGE 单位数量 pDetail VARCHAR(40) NULL;
ALTER TABLE tProduct
    CHANGE 单价 pPrice DECIMAL(19, 4) NULL;
ALTER TABLE tProduct
    CHANGE 库存量 pStorage INT NULL;
ALTER TABLE tProduct
    CHANGE 订购量 pPurchaseCount INT NULL;
ALTER TABLE tProduct
    CHANGE 再订购量 pRePurchaseCount INT NULL;
ALTER TABLE tProduct
    CHANGE 中止 pAbortFlag TINYINT(1) NULL;

ALTER TABLE 供应商
    CHANGE 供应商ID supplierID INT NOT NULL;
ALTER TABLE 供应商
    CHANGE 公司名称 supplierName VARCHAR(80) NULL;
ALTER TABLE 供应商
    CHANGE 联系人姓名 sContactName VARCHAR(60) NULL;
ALTER TABLE 供应商
    CHANGE 联系人头衔 sContactJobRank VARCHAR(60) NULL;
ALTER TABLE 供应商
    CHANGE 地址 sAddress VARCHAR(120) NULL;
ALTER TABLE 供应商
    CHANGE 城市 sCity VARCHAR(30) NULL;
ALTER TABLE 供应商
    CHANGE 地区 sRegion VARCHAR(30) NULL;
ALTER TABLE 供应商
    CHANGE 邮政编码 sPostalCode VARCHAR(20) NULL;
ALTER TABLE 供应商
    CHANGE 国家 sState VARCHAR(30) NULL;
ALTER TABLE 供应商
    CHANGE 电话 sTel VARCHAR(48) NULL;
ALTER TABLE 供应商
    CHANGE 传真 sFaxTel VARCHAR(48) NULL;
ALTER TABLE 供应商
    CHANGE 主页 sHomePage LONGTEXT NULL;
RENAME TABLE 供应商 TO tSupplier;


ALTER TABLE 客户
    CHANGE 客户ID customerID VARCHAR(10) NOT NULL;

ALTER TABLE 客户
    CHANGE 公司名称 cCompanyName VARCHAR(80) NULL;

ALTER TABLE 客户
    CHANGE 联系人姓名 cContactName VARCHAR(60) NULL;

ALTER TABLE 客户
    CHANGE 联系人头衔 cContactJobRank VARCHAR(60) NULL;

ALTER TABLE 客户
    CHANGE 地址 cAddress VARCHAR(120) NULL;

ALTER TABLE 客户
    CHANGE 城市 cCity VARCHAR(30) NULL;

ALTER TABLE 客户
    CHANGE 地区 cRegion VARCHAR(30) NULL;

ALTER TABLE 客户
    CHANGE 邮政编码 cPostalCode VARCHAR(20) NULL;

ALTER TABLE 客户
    CHANGE 国家 cState VARCHAR(30) NULL;

ALTER TABLE 客户
    CHANGE 电话 cTel VARCHAR(48) NULL;

ALTER TABLE 客户
    CHANGE 传真 cFaxTel VARCHAR(48) NULL;

RENAME TABLE 客户 TO tCustomer;

ALTER TABLE 类别
    CHANGE 类别ID categoryID INT NOT NULL;

ALTER TABLE 类别
    CHANGE 类别名称 categoryName VARCHAR(30) NULL;

ALTER TABLE 类别
    CHANGE 说明 cDetail LONGTEXT NULL;

ALTER TABLE 类别
    CHANGE 图片 cImage LONGBLOB NULL;

RENAME TABLE 类别 TO tCategory;

ALTER TABLE 订单
    CHANGE 订单ID orderID INT NOT NULL;

ALTER TABLE 订单
    CHANGE 客户ID customerID VARCHAR(10) NULL;

ALTER TABLE 订单
    CHANGE 雇员ID employeeID INT NULL;

ALTER TABLE 订单
    CHANGE 订购日期 orderDate DATETIME NULL;

ALTER TABLE 订单
    CHANGE 到货日期 signedDate DATETIME NULL;

ALTER TABLE 订单
    CHANGE 发货日期 sentDate DATETIME NULL;

ALTER TABLE 订单
    CHANGE 运货商 deliveryCompany INT NULL;

ALTER TABLE 订单
    CHANGE 运货费 deliveryFee DECIMAL(19, 4) NULL;

ALTER TABLE 订单
    CHANGE 货主名称 ownerName VARCHAR(80) NULL;

ALTER TABLE 订单
    CHANGE 货主地址 ownerAddress VARCHAR(120) NULL;

ALTER TABLE 订单
    CHANGE 货主城市 ownerCity VARCHAR(30) NULL;

ALTER TABLE 订单
    CHANGE 货主地区 ownerRegion VARCHAR(30) NULL;

ALTER TABLE 订单
    CHANGE 货主邮政编码 ownerPostalCode VARCHAR(20) NULL;

ALTER TABLE 订单
    CHANGE 货主国家 ownerState VARCHAR(30) NULL;

RENAME TABLE 订单 TO tOrder;

ALTER TABLE 订单明细
    CHANGE 订单ID orderID INT NOT NULL;

ALTER TABLE 订单明细
    CHANGE 产品ID productID INT NOT NULL;

ALTER TABLE 订单明细
    CHANGE 单价 productPrice DECIMAL(19, 4) NULL;

ALTER TABLE 订单明细
    CHANGE 数量 productCount INT NULL;

ALTER TABLE 订单明细
    CHANGE 折扣 productDiscount FLOAT NULL;

RENAME TABLE 订单明细 TO tOrderDetail;

ALTER TABLE 运货商
    CHANGE 运货商ID DeliveryCompanyID INT NOT NULL;

ALTER TABLE 运货商
    CHANGE 公司名称 dCompanyName VARCHAR(80) NULL;

ALTER TABLE 运货商
    CHANGE 电话 dCompanyTel VARCHAR(48) NULL;

RENAME TABLE 运货商 TO tDeliveryCompany;

ALTER TABLE 雇员
    CHANGE 雇员ID employeeID INT NOT NULL;

ALTER TABLE 雇员
    CHANGE 姓氏 eSurname VARCHAR(40) NULL;

ALTER TABLE 雇员
    CHANGE 名字 eName VARCHAR(20) NULL;

ALTER TABLE 雇员
    CHANGE 头衔 eJobRank VARCHAR(60) NULL;

ALTER TABLE 雇员
    CHANGE 尊称 eTitle VARCHAR(50) NULL;

ALTER TABLE 雇员
    CHANGE 出生日期 eBirthDate DATETIME NULL;

ALTER TABLE 雇员
    CHANGE 雇用日期 eHireDate DATETIME NULL;

ALTER TABLE 雇员
    CHANGE 地址 eAddress VARCHAR(120) NULL;

ALTER TABLE 雇员
    CHANGE 城市 eCity VARCHAR(30) NULL;

ALTER TABLE 雇员
    CHANGE 地区 eRegion VARCHAR(30) NULL;

ALTER TABLE 雇员
    CHANGE 邮政编码 ePostalCode VARCHAR(20) NULL;

ALTER TABLE 雇员
    CHANGE 国家 eState VARCHAR(30) NULL;

ALTER TABLE 雇员
    CHANGE 家庭电话 eHomeTel VARCHAR(48) NULL;

ALTER TABLE 雇员
    CHANGE 分机 eTelExtension VARCHAR(8) NULL;

ALTER TABLE 雇员
    CHANGE 照片 eImage LONGBLOB NULL;

ALTER TABLE 雇员
    CHANGE 备注 eRemark LONGTEXT NULL;

ALTER TABLE 雇员
    CHANGE 上级 eSuperior INT NULL;

RENAME TABLE 雇员 TO tEmployee;


