-- MySQL dump 10.13  Distrib 5.6.24, for osx10.8 (x86_64)
--
-- Host: 127.0.0.1    Database: db_liguang_se
-- ------------------------------------------------------
-- Server version	5.6.17

--
-- Table structure for table `image_info`
--

DROP TABLE IF EXISTS `image_info`;

CREATE TABLE `image_info` (
  `image_id` varchar(40) NOT NULL,
  `image_title` varchar(40) NOT NULL,
  `image_type` varchar(40) NOT NULL,
  `image_link_head` varchar(150) NOT NULL,
  `image_link_tail` varchar(20000) NOT NULL,
  `image_date` datetime NOT NULL,
  `image_create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `image_count` int(11) NOT NULL,
  PRIMARY KEY (`image_title`,`image_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Dump completed on 2016-07-08 19:01:23
