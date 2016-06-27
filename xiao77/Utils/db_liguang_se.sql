/*
 Navicat MySQL Data Transfer

 Source Server         : db_liguang
 Source Server Version : 50617
 Source Host           : localhost
 Source Database       : db_liguang_se

 Target Server Version : 50617
 File Encoding         : utf-8

 Date: 06/27/2016 14:23:03 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `image_info`
-- ----------------------------
DROP TABLE IF EXISTS `image_info`;
CREATE TABLE `image_info` (
  `image_id` varchar(40) NOT NULL,
  `image_title` varchar(40) NOT NULL,
  `image_type` varchar(40) NOT NULL,
  `image_link_head` varchar(150) NOT NULL,
  `image_link_tail` varchar(20000) NOT NULL,
  `image_date` varchar(20) NOT NULL,
  `image_create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `image_count` int(11) NOT NULL,
  PRIMARY KEY (`image_title`,`image_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
