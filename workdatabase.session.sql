CREATE TABLE 早餐店菜單(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);
CREATE TABLE variant(
    id INT PRIMARY KEY AUTO_INCREMENT,
    menu_id INT,
    size VARCHAR(3) NOT NULL,
    price INT NOT NULL DEFAULT 30
);
DESCRIBE variant;
-- INSERT INTO  早餐店菜單 (id, name) VALUES(1,'拿鐵');
-- INSERT INTO  早餐店菜單 (id, name) VALUES(2,'美式');
-- INSERT INTO  早餐店菜單 (id, name) VALUES(3,'奶茶');
-- INSERT INTO  早餐店菜單 (id, name) VALUES(4,'紅茶');
-- INSERT INTO  早餐店菜單 (id, name) VALUES(5,'綠茶');
-- INSERT INTO  早餐店菜單 (name) VALUES('烏龍茶');
-- INSERT INTO variant (menu_id,size) VALUES(1,'中杯');
-- INSERT INTO variant (menu_id,size,price) VALUES(1,'大杯',50);
-- INSERT INTO variant (menu_id,size) VALUES(2,'中杯');
-- INSERT INTO variant (menu_id,size,price) VALUES(2,'大杯',50);
-- INSERT INTO variant (menu_id,size,price) VALUES(3,'中杯',40);
-- INSERT INTO variant (menu_id,size,price) VALUES(3,'大杯',50);
-- INSERT INTO variant (menu_id,size) VALUES(4,'中杯');
-- INSERT INTO variant (menu_id,size,price) VALUES(4,'大杯',50);
-- INSERT INTO variant (menu_id,size,price) VALUES(5,'中杯',40);
-- INSERT INTO variant (menu_id,size,price) VALUES(5,'大杯',50);
-- INSERT INTO variant (menu_id,size,price) VALUES(6,'中杯',40);
INSERT INTO variant (menu_id,size,price) VALUES(7,'中杯',40);

-- SHOW TABLES;
-- DROP TABLE 早餐店菜單;
-- SET SQL_SAFE_UPDATES=0;
-- UPDATE 早餐店菜單 set price=50 WHERE name='奶茶';
-- UPDATE 早餐店菜單 set name='高山烏龍' where id=6;
-- UPDATE 早餐店菜單 set price=35 where price<=35;
SELECT * FROM 早餐店菜單;
SELECT * FROM variant;
SELECT name,size,price FROM 早餐店菜單 RIGHT JOIN variant ON 早餐店菜單.id=variant.menu_id;

-- DELETE from 早餐店菜單 where name='紅茶'
-- SELECT name,price FROM 早餐店菜單 WHERE name='美式' or price=40 
-- TRUNCATE TABLE 早餐店菜單
-- SHOW TABLES