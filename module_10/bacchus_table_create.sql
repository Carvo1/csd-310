/*
    Title: bacchus_table_create.sql
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 11 July 2020
    Description: Bacchus Winery database initialization script.
*/


/*
-- drop contstraints if they exist
ALTER TABLE product_orders DROP FOREIGN KEY fk_product;
ALTER TABLE product_orders DROP FOREIGN KEY fk_distributors;
ALTER TABLE supply_orders DROP FOREIGN KEY fk_supplies;
ALTER TABLE supply_orders DROP FOREIGN KEY fk_suppliers;
ALTER TABLE hours_worked DROP FOREIGN KEY fk_employees;
*/

-- drop tables if they exist
DROP TABLE IF EXISTS distributors;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS product_orders;
DROP TABLE IF EXISTS supplies;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS supply_orders;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS hours_worked;

/*
    Create table(s)
*/

CREATE TABLE distributors (
    distributors_id    INT             NOT NULL    AUTO_INCREMENT,
    distributors_name  VARCHAR(30)     NOT NULL,
    PRIMARY KEY(distributors_id)
);

CREATE TABLE product (
    product_id         INT             NOT NULL    AUTO_INCREMENT,
    product_name       VARCHAR(30)     NOT NULL,
    quantity           INT             NOT NULL,
    PRIMARY KEY(product_id) 
);

CREATE TABLE product_orders (
    product_order_id   INT             NOT NULL    AUTO_INCREMENT,
    date_of_order      DATE            NOT NULL,
    product_id         INT             NOT NULL,
    quantity           INT             NOT NULL,
    cost_per_unit      FLOAT           NOT NULL,
    distributors_id    INT             NOT NULL,
    PRIMARY KEY(product_order_id),
    CONSTRAINT fk_product
    FOREIGN KEY (product_id)
        REFERENCES product(product_id),
    CONSTRAINT fk_distributors
    FOREIGN KEY (distributors_id)
        REFERENCES distributors(distributors_id)
);




CREATE TABLE supplies (
    supplies_id         INT             NOT NULL    AUTO_INCREMENT,
    supply_name         VARCHAR(30)     NOT NULL,
    quantity            INT             NOT NULL,
    PRIMARY KEY(supplies_id) 
);

CREATE TABLE suppliers (
    suppliers_id        INT             NOT NULL    AUTO_INCREMENT,
    suppliers_name      VARCHAR(30)     NOT NULL,
    PRIMARY KEY(suppliers_id) 
);

CREATE TABLE supply_orders (
    supply_order_id     INT             NOT NULL    AUTO_INCREMENT,
    order_date          DATE            NOT NULL,
    supplies_id         INT             NOT NULL,
    quantity            INT             NOT NULL,
    estimated_delivery  DATE            NOT NULL,
    actual_delivery     DATE            NOT NULL,
    suppliers_id        INT             NOT NULL,
    PRIMARY KEY(supply_order_id),
    CONSTRAINT fk_supplies
    FOREIGN KEY (supplies_id)
        REFERENCES supplies(supplies_id),
    CONSTRAINT fk_suppliers
    FOREIGN KEY (suppliers_id)
        REFERENCES suppliers(suppliers_id)
);




CREATE TABLE employees (
    employee_id         INT             NOT NULL    AUTO_INCREMENT,
    first_name          VARCHAR(30)     NOT NULL,
    last_name           VARCHAR(30)     NOT NULL,
    department          VARCHAR(30)     NOT NULL,
    PRIMARY KEY(employee_id) 
);

CREATE TABLE hours_worked (
    entry_id            INT             NOT NULL    AUTO_INCREMENT,
    date_range          VARCHAR(30)     NOT NULL,
    hours_worked        INT             NOT NULL,
    employee_id         INT             NOT NULL,
    PRIMARY KEY(entry_id),
    CONSTRAINT fk_employees
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
);

