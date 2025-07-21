CREATE DATABASE Assignment_7;


CREATE TABLE CUST_MSTR (
    CustID INT,
    Name VARCHAR(50),
    Date DATE
);

CREATE TABLE master_child (
    OrderID INT,
    Product VARCHAR(50),
    Date DATE,
    DateKey INT
);

CREATE TABLE H_ECOM_Orders (
    OrderID INT,
    Price FLOAT
);
SELECT  * FROM CUST_MSTR;
SELECT * FROM master_child;
SELECT  * FROM H_ECOM_Orders;
