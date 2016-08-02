CREATE DATABASE `test` DEFAULT CHARACTER SET UTF8;
USE TEST;
CREATE TABLE `info` (
  `city_code` varchar(1000) DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `address` varchar(1000) DEFAULT NULL,
  `phone` varchar(1000) DEFAULT NULL,
  `x` varchar(1000) DEFAULT NULL,
  `y` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `city` (
  `name` varchar(1000) DEFAULT NULL,
  `code` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
