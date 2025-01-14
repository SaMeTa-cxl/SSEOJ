-- drop database sseoj;
-- create database sseoj;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: sseoj
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user`
--
use sseoj;
DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  `user_type` varchar(20) NOT NULL,
  `avatar` varchar(50) NOT NULL,
  `profile` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_email_54dc62b2_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'pbkdf2_sha256$870000$1omVedVPHpVqGnwKqoGOw5$mn2nXAu3cjeLch1Qa7O49Y2grvuMFioq6qLkrJmm0Kk=',NULL,1,'','',1,1,'2024-12-29 09:17:06.461173','admin','admin@qq.com','2024-12-29 09:17:07.126171','Admin','static/avatar.png',NULL),(2,'pbkdf2_sha256$870000$epb3BQjMoOliDUXnANEQHq$80D3+9yMHeMqcIRe0qf/fpBzW3biOrTvSoL3ETaLVaU=',NULL,1,'','',1,1,'2024-12-29 09:17:07.129171','headinclouds','ty2434519917@foxmail.com','2024-12-29 09:17:07.785716','Admin','static/user_2.png',NULL),(3,'pbkdf2_sha256$870000$0ivxGr4qomfdarxqjDhe2N$NZU6kpZz5KKnOG3sF27WRGIooPyVCtzS5CufW8IeNIk=',NULL,1,'','',1,1,'2024-12-29 09:17:07.788717','SaMeTa-cxl','cxl@qq.com','2024-12-29 09:17:08.456288','Admin','static/user_3.png',NULL),(4,'pbkdf2_sha256$870000$tqipSSan71QMIWrjBzc8fV$aB/jWYTbcE+55qf/5q4SpvePm4pBcJtw27h1Lr6KfZc=','2024-12-29 10:18:16.440778',1,'','',1,1,'2024-12-29 09:17:08.457290','inu277','ljj@qq.com','2024-12-29 09:17:09.106311','Admin','static/user_4.png',NULL),(5,'pbkdf2_sha256$870000$eVEUvF8LGQky6g9vPh80JG$KfbhLu7xiFKaWSaGKXSKf/+MXi9ESL/o2oMFs+PQTd0=','2024-12-29 10:18:04.999686',1,'','',1,1,'2024-12-29 09:17:09.108304','KLmon','ldy@126.com','2024-12-29 09:17:09.782631','Admin','static/user_5.png',NULL),(6,'pbkdf2_sha256$870000$kZ4phEhNtMqJK8GThGJkIu$VVu//xN+e1RQ/xedOfNQgHtJuq62XEbHRosTsv/bFys=',NULL,1,'','',1,1,'2024-12-29 09:17:09.784631','Makima0608','lbf@qq.com','2024-12-29 09:17:10.445761','Admin','static/user_6.png',NULL),(7,'pbkdf2_sha256$870000$p7NgrdzYTcAfYCmBHdgl0R$seJiJs8/rGXW42qNclGZAYX6KWEjOhf969WZs5q/GsQ=','2024-12-29 10:17:31.443021',0,'','',0,1,'2024-12-29 09:17:10.447762','Chitanda','1@qq.com','2024-12-29 09:17:11.098980','Normal','static/avatar.png',NULL),(8,'pbkdf2_sha256$870000$Y2sJlusYlos65zNY5zS8gK$ZfioBA49lLllZhcsUj8tAnrZix5+o91Vbitpz6ebVYE=',NULL,0,'','',0,1,'2024-12-29 09:17:11.100995','Taylor Swift','2@qq.com','2024-12-29 09:17:11.768579','Normal','static/avatar.png',NULL),(9,'pbkdf2_sha256$870000$BWZuGb7RjdtTug6EAvCWbX$cxr0wL4jQXjg5spJRf5S6n/BAC0jPh7ryKPKYFIS3Po=',NULL,0,'','',0,1,'2024-12-29 09:17:11.770579','Billie Eilish','3@qq.com','2024-12-29 09:17:12.424176','Normal','static/avatar.png',NULL),(10,'pbkdf2_sha256$870000$Ua6v7anMcZHfLiAJ53VBn7$/pGJZEietHitKDb4ceYAW3MQK8SMNaa0WC3lXIMZFiI=',NULL,0,'','',0,1,'2024-12-29 09:17:12.426176','王心怡','4@qq.com','2024-12-29 09:17:13.086193','Normal','static/avatar.png',NULL),(11,'pbkdf2_sha256$870000$n2coFc5ngJTdLVG7IrkDbv$4cVQEEypzTfNMNRVlgTeOM5EVMljzLoswVEZ37L+hKk=',NULL,0,'','',0,1,'2024-12-29 09:17:13.088192','我是奶龙','5@qq.com','2024-12-29 09:17:13.743734','Normal','static/avatar.png',NULL),(12,'pbkdf2_sha256$870000$RUamzpMF6M77eFAuhYwfmV$0Aa2acYjfU4Z/pQ+XeTHtYBlyFM7AwALHOaGi7wOD4Q=',NULL,0,'','',0,1,'2024-12-29 09:17:13.746733','刘亦菲','6@qq.com','2024-12-29 09:17:14.397372','Normal','static/avatar.png',NULL),(13,'pbkdf2_sha256$870000$D1bkuxILaTrOZ2fZ3dfeb5$19ovtlCQ+ml9ImkdEvikaI7yv3Psh/QPw/JEn6q8Og4=',NULL,0,'','',0,1,'2024-12-29 09:17:14.399371','吴彦组','7@qq.com','2024-12-29 09:17:15.045371','Normal','static/avatar.png',NULL),(14,'pbkdf2_sha256$870000$rugSbY2Q82WmMQW9Gfvc5Y$wHJ76tSTpQyCH/zR+1zVUQi/GXmpQTf93EVRnYqAiNQ=',NULL,0,'','',0,1,'2024-12-29 09:17:15.047371','蔡徐坤','8@qq.com','2024-12-29 09:17:15.712945','Normal','static/avatar.png',NULL),(15,'pbkdf2_sha256$870000$GgKLGJphnj10OljzD5PAWx$jtPRHLpLSWICIqzXzesloxRUm/erE3o5lWYAVqEdHHQ=',NULL,0,'','',0,1,'2024-12-29 09:17:15.714957','芙蓉王源','9@qq.com','2024-12-29 09:17:16.373520','Normal','static/avatar.png',NULL),(16,'pbkdf2_sha256$870000$ljVFclKrDwbBqfVfGcKUUW$nDW3k7zgGKINWPAjzMMrr7BHtSplQj77mE67SQcf3DI=',NULL,0,'','',0,1,'2024-12-29 09:17:16.375519','尼古丁真','10@qq.com','2024-12-29 09:17:17.025518','Normal','static/avatar.png',NULL),(17,'pbkdf2_sha256$870000$uQcatTeS4zx5pDBAuAp7dF$M1ybavw7HPtrF5iaex5r4x1OW+HyPXehsUMNp0pSnzg=',NULL,0,'','',0,1,'2024-12-29 09:17:17.027519','Donald Trump','11@qq.com','2024-12-29 09:17:17.696092','Normal','static/avatar.png',NULL),(18,'pbkdf2_sha256$870000$8fWiHxrQyvdMRTtRsMMQMx$7wXjAtJhJT3O/tKiCEe7z6adoHkkTs3hYIkoErj7h/c=',NULL,0,'','',0,1,'2024-12-29 09:17:17.698091','Elon Musk','12@qq.com','2024-12-29 09:17:18.353088','Normal','static/avatar.png',NULL),(19,'pbkdf2_sha256$870000$ZjOiMKKDo1cLlHrj5vGLPk$JdOWY9qf2qZF5TbCX+Cey3viuYmnjMbZ4QejudTXJ64=',NULL,0,'','',0,1,'2024-12-29 09:17:18.355090','软件工程第一突破手','13@qq.com','2024-12-29 09:17:19.031089','Normal','static/avatar.png',NULL),(20,'pbkdf2_sha256$870000$k4DHjQhQqW5o7QyaIUUD8D$urp08RJuqtuGhISXiVLu1vog8U5VOxkaJj5A1Cy347g=',NULL,0,'','',0,1,'2024-12-29 09:17:19.033089','翻斗花园牛爷爷','14@qq.com','2024-12-29 09:17:19.683636','Normal','static/avatar.png',NULL),(21,'pbkdf2_sha256$870000$5wcSKXGWEcH84cCLeuPD8W$zxPAyWxDYGa/G/F4bmNekNsCpmAma6UGl9gqRs+Fs0M=',NULL,0,'','',0,1,'2024-12-29 09:17:19.685635','jioo','15@qq.com','2024-12-29 09:17:20.354281','Normal','static/avatar.png',NULL),(22,'pbkdf2_sha256$870000$h4LDCrqVjrzA0S13GiJsMC$Y3NWPAjD2s6RPf8aL1Wdd9zsCd4JeBAztC2y8rlbrQE=',NULL,0,'','',0,1,'2024-12-29 09:17:20.356278','秦始皇派蒙','16@qq.com','2024-12-29 09:17:21.022279','Normal','static/avatar.png',NULL),(23,'pbkdf2_sha256$870000$xlhxmnJPyTVKE5KOXQcbyC$FM8lm9Yx7ELe6/qrcecaWr5TMJ3XYP7nW6v3kDZ4n3k=',NULL,0,'','',0,1,'2024-12-29 09:17:21.024281','知更鸟','17@qq.com','2024-12-29 09:17:21.693868','Normal','static/avatar.png',NULL),(24,'pbkdf2_sha256$870000$NYOfGj5X56Hp8DyhsW6e6V$a1iEYdGE6388g+hZ8vfikXHNqMkCp89iz1pVfyLoSZo=',NULL,0,'','',0,1,'2024-12-29 09:17:21.695868','Kobe Bryant','18@qq.com','2024-12-29 09:17:22.361723','Normal','static/avatar.png',NULL),(25,'pbkdf2_sha256$870000$v1M4S58Ym189iH8OH52RNv$QgUBM54Bk1hW7opzL/L7Oh7epaj6RNEtkBmj4hfROFI=',NULL,0,'','',0,1,'2024-12-29 09:17:22.363723','astrobot','19@qq.com','2024-12-29 09:17:23.015723','Normal','static/avatar.png',NULL),(26,'pbkdf2_sha256$870000$s6kuiVC42hCAtSETjeWNW9$rCdhixqZoFa7jypPvIdYjwyDD8F0i8dk7HoHQjX3Yis=',NULL,0,'','',0,1,'2024-12-29 09:17:23.017722','软件工程第一狙击手','20@qq.com','2024-12-29 09:17:23.675377','Normal','static/avatar.png',NULL),(27,'pbkdf2_sha256$870000$cJijbGGWsGoeYYjCv3K1e0$R0+hJC/IcbWMt44O7VGZ5cn2TyzqyFx5YZ9aOfqVar8=',NULL,0,'','',0,1,'2024-12-29 09:17:23.677379','不是哥们','21@qq.com','2024-12-29 09:17:24.347971','Normal','static/avatar.png',NULL),(28,'pbkdf2_sha256$870000$RA68QJgPOVa7btN5zGxwAs$w0cbfX3u2s5AjB1k5MR8PzfVBxLj25LDfqdiVJAoaGg=',NULL,0,'','',0,1,'2024-12-29 09:17:24.350972','广智救你','22@qq.com','2024-12-29 09:17:25.006975','Normal','static/avatar.png',NULL),(29,'pbkdf2_sha256$870000$BpTNMTqPpgmWvWtyiMGEyy$VVu+VXWaSDmHRWj0CNdKtwbvh7+LhWVQh292aTEJRe0=',NULL,0,'','',0,1,'2024-12-29 09:17:25.008973','306第一麦当劳','23@qq.com','2024-12-29 09:17:25.656574','Normal','static/avatar.png',NULL),(30,'pbkdf2_sha256$870000$zYZqXptOZkx4jEc8LckMHy$fJwVsvE2u3ttn5KeTOkpAuHtA5rRn5lAg/jEghrkwsk=',NULL,0,'','',0,1,'2024-12-29 09:17:25.658574','我才是奶龙','24@qq.com','2024-12-29 09:17:26.322124','Normal','static/avatar.png',NULL),(31,'pbkdf2_sha256$870000$oSaygaVDpM4I7BLnoTiByV$oV2nLYjo0ocnOa3kNZHUn0L6uU7XrJvVm4XSjVpS2AM=',NULL,0,'','',0,1,'2024-12-29 09:17:26.324125','我不是奶龙','25@qq.com','2024-12-29 09:17:26.981127','Normal','static/avatar.png',NULL),(32,'pbkdf2_sha256$870000$3Y8Q2ihcdivB4iYoJwJ42c$TDGM1+uh0YLFKy/AALZDDUsE3QicmedG6AaZvFd2Z/k=',NULL,0,'','',0,1,'2024-12-29 09:17:26.983125','香蕉道的神','26@qq.com','2024-12-29 09:17:27.647125','Normal','static/avatar.png',NULL),(33,'pbkdf2_sha256$870000$tTrkZafR2LnX4kdGT3KJgr$szGlnGmWtjIrm7uAD6F4bwb+tZpV4qB6hC1JaMA3tms=',NULL,0,'','',0,1,'2024-12-29 09:17:27.649157','黄毛牛头人','27@qq.com','2024-12-29 09:17:28.329112','Normal','static/avatar.png',NULL),(34,'pbkdf2_sha256$870000$PgFXQI5r027T8SoO355upN$pBLZVGZyutuylf0aoRoYT4TCdMcOYGKN44ZlHbadUSs=',NULL,0,'','',0,1,'2024-12-29 09:17:28.331148','雨夜带刀不带伞','28@qq.com','2024-12-29 09:17:29.004824','Normal','static/avatar.png',NULL),(35,'pbkdf2_sha256$870000$Xw7ILdqEhN7ZE6CeLid27N$rywbtpDjvfk7GA9Lvaiwh3lX1/aRRhQLl7bobgm0FTA=',NULL,0,'','',0,1,'2024-12-29 09:17:29.007162','美式学弟爱上广岛学姐','29@qq.com','2024-12-29 09:17:29.652590','Normal','static/avatar.png',NULL),(36,'pbkdf2_sha256$870000$OcRvZNf6ubibr12OcY7YCl$vXjvaxl5HjTwctmKyW9QZpyUmoO3Iu3hi2waWURUe7o=',NULL,0,'','',0,1,'2024-12-29 09:17:29.654599','A大推土机刘培茄少校','30@qq.com','2024-12-29 09:17:30.316159','Normal','static/avatar.png',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-29 19:43:30

use sseoj;
-- tag
-- following
-- post
-- post_comment
-- post_comment_like_users
-- post_like_users
-- post_tags
-- problem
-- problem_list
-- problem_list_problems
-- problem_list_star_users
-- problem_pass_users
-- problem_star_users
-- problem_tags
-- solution
-- solution_comment
-- solution_comment_like_users
-- solution_like_users
-- solution_tags
-- study_plan
-- submission
-- tag



-- 禁用外键约束
set foreign_key_checks = 0;

-- 删除所有表中的数据并重置 auto_increment
delete from judge_server;
alter table judge_server auto_increment = 1;

delete from tag;
alter table tag auto_increment = 1;

delete from following;
alter table following auto_increment = 1;

delete from post;
alter table post auto_increment = 1;

delete from post_comment;
alter table post_comment auto_increment = 1;

delete from post_comment_like_users;
alter table post_comment_like_users auto_increment = 1;

delete from post_like_users;
alter table post_like_users auto_increment = 1;

delete from post_tags;
alter table post_tags auto_increment = 1;

delete from problem;
alter table problem auto_increment = 1;

delete from problem_list;
alter table problem_list auto_increment = 1;

delete from problem_list_problems;
alter table problem_list_problems auto_increment = 1;

delete from problem_list_star_users;
alter table problem_list_star_users auto_increment = 1;

delete from problem_pass_users;
alter table problem_pass_users auto_increment = 1;

delete from problem_star_users;
alter table problem_star_users auto_increment = 1;

delete from problem_tags;
alter table problem_tags auto_increment = 1;

delete from solution;
alter table solution auto_increment = 1;

delete from solution_comment;
alter table solution_comment auto_increment = 1;

delete from solution_comment_like_users;
alter table solution_comment_like_users auto_increment = 1;

delete from solution_like_users;
alter table solution_like_users auto_increment = 1;

delete from solution_tags;
alter table solution_tags auto_increment = 1;

delete from study_plan;
alter table study_plan auto_increment = 1;

delete from submission;
alter table submission auto_increment = 1;

delete from tag;
alter table tag auto_increment = 1;

-- 恢复外键约束
set foreign_key_checks = 1;

-- 插入题目数据
insert into problem (
    name,
    description,
    input_style,
    output_style,
    data_range,
    sample,
    difficulty,
    time_limit,
    memory_limit,
    pass_count,
    attempt_count,
    source,
    star_cnt,
    create_time,
    check_status,
    test_case_id
) values
('Addition',
 'Calculate the sum of two integers provided as input.',
 'Two integers separated by a space.',
 'An integer representing the sum.',
 '1 <= a, b <= 1000',
 '{"inputs": ["1 2", "5 6"], "outputs": ["3", "11"]}',
 1,
 1000,
 65536,
 0,
 0,
 'Basic arithmetic problem',
 0,
 NOW(),
 TRUE,
 'test_case_1'),

('Subtraction',
 'Calculate the difference between two integers provided as input.',
 'Two integers separated by a space.',
 'An integer representing the difference.',
 '1 <= a, b <= 1000',
 '{"inputs": ["3 2", "9 5"], "outputs": ["1", "4"]}',
 1,
 1000,
 65536,
 0,
 0,
 'Basic arithmetic problem',
 0,
 NOW(),
 TRUE,
 'test_case_2'),

('Multiplication',
 'Calculate the product of two integers provided as input.',
 'Two integers separated by a space.',
 'An integer representing the product.',
 '1 <= a, b <= 100',
 '{"inputs": ["3 4", "7 8"], "outputs": ["12", "56"]}',
 2,
 1500,
 65536,
 0,
 0,
 'Basic arithmetic problem',
 0,
 NOW(),
 TRUE,
 'test_case_3'),

('Division',
 'Calculate the quotient of two integers provided as input.',
 'Two integers separated by a space.',
 'An integer representing the quotient.',
 '1 <= a, b <= 1000 and b != 0',
 '{"inputs": ["10 2", "15 3"], "outputs": ["5", "5"]}',
 2,
 2000,
 65536,
 0,
 0,
 'Basic arithmetic problem',
 0,
 NOW(),
 TRUE,
 'test_case_4'),

('寻找两个正序数组的中位数',
'给定两个大小分别为m和n的正序（从小到大）数组nums1和nums2。<br>请你找出并返回这两个正序数组的中位数。<br>算法的时间复杂度应该为 O(log (m+n))。',
'三行数据，第一行为m n，第二三行为数组',
'输出中位数',
'1 <= m + n <= 2000<br>-106 <= nums1[i], nums2[i] <= 106',
'{"inputs": ["2 1\\n1 3\\n2"], "outputs": ["2"]}',
3,
1000,
65536,
0,
0,
'力扣',
0,
NOW(),
TRUE,
'test_case_5'),

('交易逆序对的总数',
'在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。请设计一个程序，输入一段时间内的股票交易记录record，返回其中存在的「交易逆序对」总数。',
'两行数据，第一行为record.length，第二行为record.length',
'输出总数',
'0 <= record.length <= 50000<br>0 <= record <= 10000',
'{"inputs": ["5\\n9 7 5 4 6"], "outputs": ["8"]}',
4,
1000,
65536,
0,
0,
'力扣',
0,
NOW(),
TRUE,
'test_case_6'),

('不同的子序列',
'给你两个字符串s和t，统计并返回在s的子序列中t出现的个数，结果需要对109+7取模。',
'两行数据均为字符串',
'输出个数',
'1 <= s.length, t.length <= 1000<br>s和t由英文字母组成',
'{"inputs": ["rabbbit\\nrabbit"], "outputs": ["3"]}',
4,
2000,
65536,
0,
0,
'力扣',
0,
NOW(),
TRUE,
'test_case_7'),

('数字1的个数',
'给定一个整数n，计算所有小于等于n的非负整数中数字1出现的个数。',
'输入一个整数',
'输出1的个数',
'0 <= n <= 109',
'{"inputs": ["13"], "outputs": ["6"]}',
4,
2000,
65536,
0,
0,
'力扣',
0,
NOW(),
TRUE,
'test_case_8'),

('分发糖果',
'n个孩子站成一排。给你一个整数数组ratings表示每个孩子的评分。<br>你需要按照以下要求，给这些孩子分发糖果：<br>每个孩子至少分配到1个糖果。<br>相邻两个孩子评分更高的孩子会获得更多的糖果。<br>请你给每个孩子分发糖果，计算并返回需要准备的最少糖果数目。',
'输入两行，第一行为数组个数，第二行为数组',
'输出最少数目',
'n == ratings.length<br>1 <= n <= 2 * 104<br>0 <= ratings[i] <= 2 * 104',
'{"inputs": ["3\\n1 0 2"], "outputs": ["5"]}',
4,
2000,
65536,
0,
0,
'力扣',
0,
NOW(),
TRUE,
'test_case_9'),

('买卖股票的最佳时期',
'给你一个整数数组prices，其中prices[i]表示某支股票第i天的价格。<br>在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有一股股票。你也可以先购买，然后在同一天出售。<br>返回你能获得的最大利润。',
'输入两行，第一行为数组个数，第二行为数组',
'输出最大利润',
'1 <= prices.length <= 3 * 104<br>0 <= prices[i] <= 104',
'{"inputs": ["6\\n7 1 5 3 6 4"], "outputs": ["7"]}',
2,
1000,
65536,
0,
0,
'力扣',
0,
NOW(),
TRUE,
'test_case_10'),

('括号生成',
'数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。',
'输入一个整数',
'输出所有组合',
'1 <= n <= 8',
'{"inputs": ["3"], "outputs": ["((()))\\n(()())\\n(())()\\n()(())\\n()()()"]}',
1,
1000,
65536,
0,
0,
'力扣',
0,
NOW(),
TRUE,
'test_case_11'),

('下一个更大的数值平衡数',
'如果整数x满足：对于每个数位d，这个数位恰好在x中出现d次。那么整数x就是一个数值平衡数。<br>给你一个整数n，请你返回严格大于n的最小数值平衡数。',
'输入一个整数',
'输出一个整数',
'0 <= n <= 106',
'{"inputs": ["1000"], "outputs": ["1333"]}',
2,
2000,
65536,
0,
0,
'力扣',
0,
NOW(),
TRUE,
'test_case_12');

update problem set attempt_count = 1;


 -- 插入problem_pass_users
insert into problem_pass_users(id, problem_id, user_id)
 values
(1, 1, 2),
(2, 2, 8),
(3, 3, 9),
(4, 4, 6),
(5, 5, 15),
(6, 5, 3),
(7, 5, 4),
(8, 5, 7),
(9, 1, 10),
(10, 1, 11),
(11, 1, 12),
(12, 1, 5),
(13, 1, 14),
(14, 1, 1),
(15, 1, 13);


 -- 插入problem_star_users
insert into problem_star_users(id, problem_id, user_id)
values
(1, 1, 3),
(2, 1, 5),
(3, 2, 7),
(4, 2, 9),
(5, 3, 2),
(6, 3, 6),
(7, 4, 8),
(8, 4, 10),
(9, 5, 4),
(10, 5, 11),
(11, 5, 2);


--  插入tag数据
 insert into tag (
 id, name, parent_id
 ) values
 (1, '分治', null),
 (2, '动态规划', null),
 (3, '贪心算法', null),
 (4, '回溯', null),
 (5, '图', null),
 (6, '字符串', null),
 (7, '最短路算法', null),
 (8, '搜索', null),
 (9, '树', null),
 (10, '并查集', null),
 (11, '归并排序', 1),
 (12, '快速排序', 1),
 (13, '二分查找', 1),
 (14, 'Strassen矩阵乘法', 1),
 (15, 'Karatsuba乘法', 1),
 (16, '背包问题', 2),
 (17, '最长递增子序列', 2),
 (18, '最长公共子序列', 2),
 (19, '动态规划树', 2),
 (20, '区间规划', 2),
 (21, '语言', null),
 (22, 'C', 21),
 (23, 'C++', 21),
 (24, 'Java', 21),
 (25, 'Python3', 21),
 (26, 'JavaScript', 21),
 (27, 'Golang', 21);

 -- 插入problem_tags
insert into problem_tags
(id, problem_id, tag_id)
values
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 4),
(5, 2, 5),
(6, 2, 6),
(7, 3, 7),
(8, 3, 8),
(9, 3, 9),
(10, 4, 10),
(11, 4, 11),
(12, 4, 12);


-- 插入关注数据
insert into following (
follow_time, follower_id, following_id) values
('2024-12-29', 23, 28),
('2024-12-29', 17, 34),
('2024-12-29', 7, 24),
('2024-12-29', 33, 22),
('2024-12-29', 12, 26),
('2024-12-29', 16, 22),
('2024-12-29', 28, 30),
('2024-12-29', 14, 9),
('2024-12-29', 24, 16),
('2024-12-29', 17, 24),
('2024-12-29', 14, 7),
('2024-12-29', 12, 34),
('2024-12-29', 35, 7),
('2024-12-29', 26, 30),
('2024-12-29', 21, 17),
('2024-12-29', 8, 17),
('2024-12-29', 7, 19),
('2024-12-29', 32, 34),
('2024-12-29', 15, 26),
('2024-12-29', 34, 24),
('2024-12-29', 32, 7),
('2024-12-29', 23, 15),
('2024-12-29', 33, 28),
('2024-12-29', 7, 28),
('2024-12-29', 14, 20),
('2024-12-29', 17, 13),
('2024-12-29', 35, 33),
('2024-12-29', 21, 28),
('2024-12-29', 30, 17),
('2024-12-29', 28, 27),
('2024-12-29', 12, 25),
('2024-12-29', 21, 8),
('2024-12-29', 26, 31),
('2024-12-29', 32, 11),
('2024-12-29', 22, 7),
('2024-12-29', 16, 21),
('2024-12-29', 16, 9),
('2024-12-29', 19, 27),
('2024-12-29', 23, 25),
('2024-12-29', 27, 29),
('2024-12-29', 24, 20),
('2024-12-29', 16, 30),
('2024-12-29', 24, 36),
('2024-12-29', 18, 12),
('2024-12-29', 19, 20),
('2024-12-29', 11, 32),
('2024-12-29', 26, 24),
('2024-12-29', 17, 18),
('2024-12-29', 11, 30),
('2024-12-29', 9, 21),
('2024-12-29', 11, 23),
('2024-12-29', 32, 29),
('2024-12-29', 25, 10),
('2024-12-29', 32, 10),
('2024-12-29', 10, 29),
('2024-12-29', 31, 20),
('2024-12-29', 14, 13),
('2024-12-29', 8, 33),
('2024-12-29', 17, 17),
('2024-12-29', 21, 32),
('2024-12-29', 18, 30),
('2024-12-29', 20, 16),
('2024-12-29', 15, 21),
('2024-12-29', 12, 11),
('2024-12-29', 16, 20),
('2024-12-29', 28, 23),
('2024-12-29', 13, 33),
('2024-12-29', 20, 28),
('2024-12-29', 30, 24),
('2024-12-29', 10, 12),
('2024-12-29', 22, 29),
('2024-12-29', 23, 22),
('2024-12-29', 19, 32),
('2024-12-29', 19, 17),
('2024-12-29', 9, 29),
('2024-12-29', 11, 13),
('2024-12-29', 35, 20),
('2024-12-29', 12, 13),
('2024-12-29', 19, 18),
('2024-12-29', 20, 11),
('2024-12-29', 7, 29),
('2024-12-29', 23, 24),
('2024-12-29', 28, 32),
('2024-12-29', 21, 30),
('2024-12-29', 20, 36),
('2024-12-29', 27, 34),
('2024-12-29', 7, 34),
('2024-12-29', 19, 33),
('2024-12-29', 13, 30),
('2024-12-29', 33, 17),
('2024-12-29', 12, 9),
('2024-12-29', 13, 31),
('2024-12-29', 7, 27),
('2024-12-29', 20, 27),
('2024-12-29', 13, 27),
('2024-12-29', 31, 16),
('2024-12-29', 26, 23),
('2024-12-29', 34, 16),
('2024-12-29', 31, 30),
('2024-12-29', 9, 31),
('2024-12-29', 8, 23),
('2024-12-29', 18, 9),
('2024-12-29', 25, 13),
('2024-12-29', 19, 16),
('2024-12-29', 20, 15),
('2024-12-29', 33, 14),
('2024-12-29', 20, 17),
('2024-12-29', 15, 17),
('2024-12-29', 12, 24),
('2024-12-29', 25, 32),
('2024-12-29', 25, 30),
('2024-12-29', 21, 13),
('2024-12-29', 8, 36),
('2024-12-29', 23, 17),
('2024-12-29', 18, 13),
('2024-12-29', 16, 28),
('2024-12-29', 26, 20),
('2024-12-29', 29, 18),
('2024-12-29', 9, 7),
('2024-12-29', 23, 10),
('2024-12-29', 28, 13),
('2024-12-29', 29, 32),
('2024-12-29', 31, 36),
('2024-12-29', 29, 27),
('2024-12-29', 22, 12),
('2024-12-29', 23, 14),
('2024-12-29', 32, 18),
('2024-12-29', 8, 28),
('2024-12-29', 18, 29),
('2024-12-29', 22, 26),
('2024-12-29', 8, 29),
('2024-12-29', 9, 17),
('2024-12-29', 19, 36),
('2024-12-29', 10, 33),
('2024-12-29', 25, 23),
('2024-12-29', 33, 8),
('2024-12-29', 30, 26),
('2024-12-29', 7, 16),
('2024-12-29', 29, 29),
('2024-12-29', 16, 11),
('2024-12-29', 10, 36),
('2024-12-29', 12, 21),
('2024-12-29', 14, 35),
('2024-12-29', 18, 8),
('2024-12-29', 20, 10),
('2024-12-29', 29, 31),
('2024-12-29', 26, 21),
('2024-12-29', 26, 17),
('2024-12-29', 31, 23),
('2024-12-29', 7, 12),
('2024-12-29', 12, 30),
('2024-12-29', 35, 17),
('2024-12-29', 14, 26),
('2024-12-29', 26, 13),
('2024-12-29', 24, 19),
('2024-12-29', 30, 11),
('2024-12-29', 17, 8),
('2024-12-29', 7, 25),
('2024-12-29', 28, 26),
('2024-12-29', 35, 24),
('2024-12-29', 17, 22),
('2024-12-29', 16, 18),
('2024-12-29', 24, 33),
('2024-12-29', 11, 10),
('2024-12-29', 32, 30),
('2024-12-29', 35, 15),
('2024-12-29', 32, 20),
('2024-12-29', 16, 16),
('2024-12-29', 30, 9),
('2024-12-29', 29, 16),
('2024-12-29', 7, 21),
('2024-12-29', 13, 19),
('2024-12-29', 9, 23),
('2024-12-29', 17, 15),
('2024-12-29', 22, 31),
('2024-12-29', 7, 31),
('2024-12-29', 15, 36),
('2024-12-29', 17, 16),
('2024-12-29', 12, 27),
('2024-12-29', 10, 34),
('2024-12-29', 28, 8),
('2024-12-29', 32, 35),
('2024-12-29', 22, 23),
('2024-12-29', 13, 29),
('2024-12-29', 31, 8),
('2024-12-29', 22, 35),
('2024-12-29', 29, 34),
('2024-12-29', 33, 19),
('2024-12-29', 9, 35),
('2024-12-29', 12, 17),
('2024-12-29', 31, 35),
('2024-12-29', 26, 35),
('2024-12-29', 24, 17),
('2024-12-29', 33, 20),
('2024-12-29', 19, 11),
('2024-12-29', 24, 22),
('2024-12-29', 34, 27),
('2024-12-29', 34, 21),
('2024-12-29', 30, 27);


-- 插入帖子数据
insert into post (
title, content, like_count, comment_count, create_time, last_update_time, is_announcement, check_status, create_user_id) values
('解题求助',
'各位大大，第一道题到底怎么写？',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 7),
('第一段java实习',
'去500～999规模的饮料公司搞后台管理系统，要不要去呀，目前研一0实，请大佬给点建议',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 8),
('小米校招&实习内推',
'请使用内推码：SK9VQSH'
'前进一小米！！！
小米集团25校园招聘已经启动啦！！！
感兴趣的同学可以去 https://hr.xiaomi.com/ 官网投递简历！！！
早投递早拿offer！！
欢迎大家加入小米！！',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 9),
('学得想哭',
'学得想哭。你鸭期末周设计强度太高了',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 10),
('中珠→金湾机场',
'中珠→金湾机场。1月1日早上6:30到金湾机场，有没有一起拼车？（时间可以提前）',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 11),
('喜欢学妹应该吃哪种中药？',
'感觉和学妹相处起来会更自然一些，所以想和学妹交往啦。本人175/65，东校大四，轻度健身痕迹，普通外貌（大概40%的同性比我帅这样吧），朋友圈子很简单。业余时间主要是逛吃，游戏或者麻将，天气不冷的时候游泳比较频繁。
理想对象：03，04或05年生，爱干净，身心健康，现在或未来在大学城（有外校的朋友也可以介绍一下）
补充：已留QQ，有意向就加微信，社恐的话可以不马上见面',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 12),
('捞人',
'中珠捞今晚跑步菠萝头男生。   今晚大概6:30，momo从榕园食堂吃完绝望地骑车前往教学楼，在第一个丁字路口一个头顶菠萝头的同学哒哒跑步从我身边经过，像一道光点亮了我的夜晚，当时我的车速和他跑步的速度比较接近，于是我们保持约2米距离同路了十秒左右，期间观察到他的菠萝头戴了发带，身上衣服的颜色颇具热带感，我对这位充满青春活力感的运动少年很感兴趣，想进一步了解一下，如果这位同学看到了帖子不介意我占用一格好友列表的话可以加加我，
自我介绍：理科大三女爱运动（跑步羽毛球篮球）爱电影（星际穿越哈利波特飘）爱美食爱探店（朋友圈会分享探店经验美食攻略）',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 13),
('我觉得女朋友很扫兴',
'我觉得女朋友很扫兴。好不容易都有空，想约着女朋友一起去看电影然后一起吃个饭。在去看电影的路上，我们打车都坐的后排，女朋友凑过来跟我说话，我闻到了她有一点口臭。于是有以下对话（正常谈话声音）
我：你嘴好臭，你真应该买漱口水用用，
她：臭的是你，要买你买（挪开位置到另一边车窗）
我：你自己闻不到吗？
她：闻不到
我：你肯定感染了幽门螺旋杆菌
她：我买过试纸测了，没有
我：你回去给你舍友哈一口气，问问她们
她：保持沉默不说话
我：是不是因为你有蛀牙啊，给我看看你的蛀牙
她：继续沉默
我这时意识到她生气了，于是凑过去哄她。她还是不理我，真服了，出来看个电影有必要这样吗？我只是说了事实而已，情绪太不稳定了吧。真扫兴，电影我不看了让她自己去看吧，饭我也不想吃了，她自己去吃吧。
我错了嘛？',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 14),
('家里没经同意突然给我全款买了套房',
'家里没经同意突然给我全款买了套房。家里没经同意突然给我全款买了套房……
今天爸妈突然打电话告诉我家里给我买了套房，在越秀那边，144平，附近设施好像挺不错的。就是买菜贵一些，好像饮茶也不是很方便，估计毕业了还是要回天河那套住捏。爸妈说后续装修要我拿主意，这咋搞啊？有没有人办过相应手续啊？
但其实有人不建议我要，因为我可能还要承担另外的费用。房屋过户有三种形式：继承、赠与和买卖。如果采用继承方式，则需要在公证处做继承公证，公证处的收费是房屋价值的1%。
而选取赠与方式，则需要缴纳契税。《中华人民共和国契税法》第四条明确，契税的计税依据包括土地使用权赠与、房屋赠与以及其他没有价格的转移土地、房屋权属行为，为税务机关参照土地使用权出售、房屋买卖的市场价格依法核定的价格。同时该法也规定了契税税率为3%-5%。
最后一种就是买卖的方式。根据《中华人民共和国个人所得税法》第三条，个人出售自有住房取得的所得应按照“财产转让所得”项目征收个人所得税，税率为20%。但是如果该房屋同时满足家庭唯一住宅、购买时间超过五年的条件，则个人所得税免交。',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 15),
('中珠北门外卖被偷',
'天杀的谁偷的外卖，晚了几分钟就不见了，这么饿是吧，偷外卖的人期末全挂。期末人怨气极重',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 16),
('中珠榕11的电梯能用了吗',
'中珠榕11的电梯能用了吗。看到有同学乘坐',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 17),
('好无聊想当军师了',
'好无聊想当军师了。好无聊哈哈哈想当军师了 嘿嘿有需要的uus可以留联系方式 我来！不过技巧只占三分 剩下还得看缘分啊',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 18),
('呜呜中珠明天求搭子',
'呜呜中珠明天求搭子。历史原创话剧专场《霞隐紫泉》即将上演
紫泉宫殿锁烟霞，夜月风回狸弄沙。却道人间无鬼魅，破乱归正展宫华。
演出时间：2024年12月29日（周日）19:00—21:30（18:30开始入场）
演出地点：海琴三号C507
该活动由历史学系（珠海）主办，中珠话剧社、大气科学学院、微电子科学与技术学院以及山海学社联合举办',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 19),
('外卖贼',
'谁把本王的喜茶偷了，如实招来',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 20),
('步道乐跑截止了吗',
'步道乐跑截止了吗。rt，步道乐跑截止了吗，今天去跑乐跑，两个打卡点都打上了说打卡点异常无效成绩。（这种可以和老师说算有效吗？里程和配速都正常）',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 21),
('我也是完蛋了',
'我也是完蛋了。crush哥笑起来好可爱啊啊啊',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 22),
('校内推销',
'老校区这边突然多了那种说是啥英语俱乐部的，给你介绍一大堆，问要钱不就支支吾吾，恶心死了，路上逮着个人就开始推销，这种人真的是校内的吗，咋进来的啊',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 23),
('大家平时都玩啥app',
'大家平时都玩啥app。单纯打发时间的话，个人感觉抖音停不下来，贴吧排外性太强，知乎更是懂哥遍地，大家都怎么看呢',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 24),
('好期待见面呐',
'好期待见面呐。还有二十天多天就能回家见面啦',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 25),
('很适合小情侣周末忙里偷闲',
'很适合小情侣周末忙里偷闲。那么问题来了，我女朋友呢',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 26),
('报告用ai可以不',
'报告用ai可以不。水课事多，报告一堆，lz实在不想自己写了，连裁缝都不想当了，直接用ai生成一整篇文章，虽说稍微去了去ai味，但心里还是没底所以可以吗',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 27),
('图书馆一个人占两座',
'图书馆一个人占两座。吃完饭下午来图书馆自习，发现有一个同学旁边的座位放了书包，桌子上没有什么东西，旁边有一个插座，于是询问这位同学旁边有没有其他人书包是否是她的，这位同学说是她的，我说能麻烦移一下吗我想坐那里，她说她东西太多了不好移要我看看其他地方，我说现在图书馆座位没有多少了，那个座位还带插头，她说要我去问问对面坐着的同学能不能移她的东西然后坐她旁边，然后我就转身走了……不是很能理解为什么东西多就可以一个人占两个人的位置。lz有点生气遂发帖',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 28),
('想问问寒假有什么中大认可的竞赛吗',
'想问问寒假有什么中大认可的竞赛吗。好像大英赛中大不认可，报了计算机二级，还有其他的吗',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 29),
('自动化模电',
'自动化模电。求自动化模电真题，有偿',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 30),
('100块钱的快乐',
'100块钱的快乐。100多一点的钱如何让全班享受
买点小东西？…那买什么呢？',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 31),
('神人舍友我真受不了你了',
'真的有很多想说的：
1、长期不洗澡不洗头，甚至最近很多天都没刷牙洗脸，晚上脱了鞋就上床了，床单不知道睡了多久也没说洗一下换一下，身上真的很臭，垃圾也是好多天不丢，满出来也不丢，床位就更不用说了，乱的要死
2、随手关灯这么基本的事做不到，无论是厕所灯还是大灯甚至自己的台灯都不记得，提醒过很多次很多次，有一天晚课两个半小时更是忘了关空调和三个灯，我最后提醒了一次直接开呛了，完全不认为自己有错
3、关于空调开关，在我和另一个舍友已经提出对于他太早开空调不太好的建议时仍然执意开空调，甚至于大中午就要开空调，搞得寝室又臭又闷，你的床位真的很臭，而且你开了倒是记得关呗
4、我之前已经发过一次贴，他看到了，给我道歉了并承诺会注意卫生的，但是并没有，而且语气阴阳怪气说寝室氛围冷清，但是大哥你那么臭我真的不想和你有任何来往
5、我想我之前的交流已经很明确了，但是他的态度一直都是在给自己找补，本质上还是不认为自己有错，我不想再白费口舌和这大哥说了，搞得像是我咄咄逼人还要和我吵架，我已经和辅导员反映过，但无奈不满足换寝室的条件，他肯定也能刷到这条帖子，我就这么给你说了，你也不用来找我，自己改，改好了我自然会删帖，改不好我就再发帖把你床位的照片和名字学号还有大头照都发出来，既然交流对你没有用那我只能采取这种极端方法来施压了，你也可以闹，闹到辅导员换寝室，那更好不过',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 32),
('求游戏推荐',
'笔记本买了好久还没怎么玩过游戏，不玩总感觉浪费了这配置(i7＋4060)',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 33),
('救命，北方人该如何在南方活过冬天',
'开空调就特别干，第二天起来嗓子冒烟，半夜喝好多水，要起夜上厕所，睡不好；不开空调就冻死个人…….怎么办。想知道南方人怎么活的',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 34),
('感觉很久没有干净的笑过了',
'就是那种纯粹 温暖 一看见也想跟着笑而且内心很透净明亮的笑',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 35),
('年度语录汇总',
'1.布什戈门
2.人生易如反掌啊
3.广智救我
4.时间差不多咯
5.city不city
6.谁说这豆角老了，这豆角可太棒了
7.主播主播，……（太长了，集友自行补充）
8.将大局逆转吧，开!（咆哮版）
9.这或许和我的家教有关吧
10.我不明白，……（奉化口音）
11.你真是饿了，什么都吃得下
12.因为他善
13.你偏要去北京是什么意思，北京到底有谁在
14.马超~马超～（超的音前短后长）
15.三折叠，怎么折都有面
16.我是奶龙，我才是奶龙
17.passion（激情）
18.我blue了
19.自→己↓吓↓自→己↑
（年底了，突发奇想想要搞一个年度语录总结，也顺便帮那些没跟上网速的集友补一补知识，大家有补充的也欢迎在评论区留言，我暂时就只能想这么多了）',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 36);

--  插入题解
insert into solution (content, title, like_count, comment_count, create_time, check_status, create_user_id, problem_id)
values
-- 第 1 题
('You can solve this problem by reading the input numbers, splitting them, and adding them directly.',
 'Simple Addition',
 0,
 0,
 now(),
 false,
 1,
 1),
('Make sure to validate that the inputs are integers before performing the addition.',
 'Addition with Type Checking',
 0,
 0,
 now(),
 false,
 2,
 1),

-- 第 2 题
('Subtract the second number from the first after splitting the input.',
 'Basic Subtraction',
 0,
 0,
 now(),
 false,
 1,
 2),
('Ensure that the result is not negative if your system does not support negative numbers.',
 'Edge Case Handling in Subtraction',
 0,
 0,
 now(),
 false,
 2,
 2),

-- 第 3 题
('Multiply the two integers after parsing the input.',
 'Simple Multiplication',
 0,
 0,
 now(),
 false,
 1,
 3),
('Use Karatsuba algorithm for faster multiplication when numbers are large.',
 'Efficient Multiplication',
 0,
 0,
 now(),
 false,
 2,
 3),

-- 第 4 题
('Divide the first number by the second and ensure you handle division by zero.',
 'Basic Division',
 0,
 0,
 now(),
 false,
 1,
 4),
('Use floating-point division to ensure accurate results for non-integer quotients.',
 'Precision in Division',
 0,
 0,
 now(),
 false,
 2,
 4),

-- 第 5 题
('Iterate through numbers up to the square root of the input to check divisibility.',
 'Prime Check Using Trial Division',
 0,
 0,
 now(),
 false,
 1,
 5),
('Use the Sieve of Eratosthenes for precomputing prime numbers.',
 'Efficient Prime Check',
 0,
 0,
 now(),
 false,
 2,
 5);


-- 插入标签关联关系nothing
insert into solution_tags (solution_id, tag_id)
values
(1, 1), (1, 13),
(2, 1), (2, 13),
(3, 1), (3, 13),
(4, 1), (4, 13),
(5, 15);


-- 插入题解评论
insert into solution_comment
(content, create_user_id, solution_id, like_count, create_time, check_status, reply_to_user_id, under_comment_id)
values
('This solution is very helpful, thank you!', 1, 1, 0, now(), false, null, null),
('I have a question about this part of your solution.', 2, 1, 0, now(), false, 1, 1),

('Great explanation, but I think there is an edge case missing.', 3, 2, 0, now(), false, null, null),
('Could you clarify how this handles large inputs?', 4, 2, 0, now(), false, 3, 3),

('This is an efficient implementation, well done!', 1, 3, 0, now(), false, null, null),
('I recommend adding more comments to improve readability.', 2, 3, 0, now(), false, 1, 5),

('I found this solution helpful for my project.', 3, 4, 0, now(), false, null, null),
('What inspired this approach? It seems unique.', 4, 4, 0, now(), false, 3, 7),

('This comment provides a good alternate perspective.', 1, 5, 0, now(), false, null, null),
('Have you considered optimizing this further?', 2, 5, 0, now(), false, 1, 9);

-- 插入题解评论点赞表
insert into solution_comment_like_users (solutioncomment_id, user_id)
values
(1, 4),
(2, 7),
(3, 1),
(4, 6),
(5, 3),
(6, 8),
(7, 2),
(8, 10),
(9, 5),
(10, 9);

-- 插入题解点赞表
insert into solution_like_users (solution_id, user_id)
values
(1, 5),
(2, 3),
(3, 9),
(4, 1),
(5, 7),
(6, 2),
(7, 8),
(8, 6),
(9, 10),
(10, 4);

-- 插入题单
insert into problem_list
(title, create_user_id, star_count, problem_count, summary, is_deleted, is_public)
values
('基础算法题单', 1, 0, 0, '包含常见的基础算法题目，如排序、查找等，用于巩固基础知识。', false, true),
('数据结构题单', 2, 0, 0, '专注于数据结构相关问题，包括链表、树、图等内容，适合中级学习者。', false, true),
('动态规划题单', 3, 0, 0, '集合了一些经典动态规划问题，帮助理解状态转移与问题分解。', false, true),
('数学题单', 4, 0, 0, '包含数论与离散数学的练习题目，适合提高数学建模能力。', false, true),
('高级算法题单', 5, 0, 0, '收录了高级算法问题，包括分治、回溯、贪心算法等，适合挑战。', false, true),
('编程比赛题单', 6, 0, 0, '精选自往届编程比赛的高质量题目，适合训练比赛能力。', false, true),
('机器学习题单', 7, 0, 0, '涉及机器学习基础算法实现与优化问题，适合初学者。', false, true),
('数据库练习题单', 8, 0, 0, '包含SQL查询与数据库设计相关问题，适合数据库入门和提高。', false, true),
('操作系统题单', 9, 0, 0, '整理了操作系统经典问题，如进程调度、内存管理等，理论与实践兼备。', false, true),
('网络题单', 10, 0, 0, '涵盖计算机网络问题，从协议到应用层，适合系统学习网络知识。', false, true);

-- 向题单中插入题目数据
insert into problem_list_problems (id, problemlist_id, problem_id)
values
(1, 1, 3),
(2, 1, 7),
(3, 2, 1),
(4, 2, 8),
(5, 3, 2),
(6, 3, 9),
(7, 4, 4),
(8, 4, 5),
(9, 5, 6),
(10, 6, 10),
(11, 7, 11),
(12, 8, 11),
(13, 9, 11),
(14, 10, 11),
(15, 10, 12);

-- 插入problem_list_star_user
insert into problem_list_star_users
(id, problemlist_id, user_id)
values
(1, 1, 3),
(2, 1, 5),
(3, 1, 7),
(4, 2, 8),
(5, 2, 10),
(6, 2, 12),
(7, 3, 2),
(8, 3, 6),
(9, 3, 9),
(10, 4, 11),
(11, 4, 13),
(12, 4, 15),
(13, 5, 16),
(14, 5, 18),
(15, 5, 20),
(16, 6, 17),
(17, 6, 19),
(18, 6, 21),
(19, 7, 22),
(20, 7, 23),
(21, 7, 25),
(22, 8, 1),
(23, 8, 14),
(24, 8, 26),
(25, 9, 4),
(26, 9, 5),
(27, 9, 28),
(28, 10, 6),
(29, 10, 8),
(30, 10, 30);

-- 插入学习计划
insert into study_plan
(user_id, problem_id, added_time, problem_status)
values
(7, 1, now(), false),
(7, 2, now(), true),
(8, 3, now(), false),
(8, 4, now(), true),
(9, 5, now(), false),
(9, 6, now(), false),
(10, 7, now(), true),
(10, 8, now(), false),
(11, 9, now(), true),
(11, 10, now(), false);


-- 插入帖子评论
insert into post_comment
(post_id, create_user_id, content, check_status, like_count, reply_to_user_id, under_comment_id_id, create_time)
values
(1, 2, 'This is a comment for post 1.', true, 5, null, null, now()),
(1, 3, 'Another comment on post 1.', true, 3, null, null, now()),
(1, 4, 'Reply to the first comment.', true, 2, null, 1, now()), -- 回复用户2的评论，under_comment_id 指向 1
(2, 5, 'This is a comment for post 2.', true, 8, null, null, now()),
(2, 6, 'Another comment on post 2.', true, 0, null, null, now()),
(3, 7, 'Comment on post 3.', true, 4, null, null, now()),
(3, 8, 'Reply to the comment on post 3.', true, 7, null, 6, now()), -- 回复用户7的评论，under_comment_id 指向 6
(4, 9, 'First comment on post 4.', true, 1, null, null, now()),
(4, 10, 'Another comment on post 4.', true, 3, null, null, now()),
(5, 11, 'Comment on post 5.', true, 2, null, null, now()),
(5, 12, 'Reply to post 5 comment.', true, 5, null, 10, now()), -- 回复用户11的评论，under_comment_id 指向 10
(6, 13, 'First comment on post 6.', true, 6, null, null, now()),
(6, 14, 'Another comment for post 6.', true, 0, null, null, now()),
(7, 15, 'Comment on post 7.', true, 2, null, null, now()),
(7, 16, 'Reply to post 7 comment.', true, 4, null, 13, now()), -- 回复用户15的评论，under_comment_id 指向 13
(8, 17, 'First comment on post 8.', true, 5, null, null, now()),
(8, 18, 'Another comment for post 8.', true, 1, null, null, now()),
(9, 19, 'Comment on post 9.', true, 7, null, null, now()),
(9, 20, 'Reply to post 9 comment.', true, 2, null, 15, now()), -- 回复用户19的评论，under_comment_id 指向 15
(10, 21, 'First comment on post 10.', true, 0, null, null, now()),
(10, 22, 'Another comment for post 10.', true, 3, null, null, now()),
(11, 23, 'First comment on post 11.', true, 9, null, null, now()),
(11, 24, 'Reply to post 11 comment.', true, 0, null, null, now()),
(12, 25, 'Comment on post 12.', true, 4, null, null, now()),
(12, 26, 'Reply to post 12 comment.', true, 1, null, 20, now()), -- 回复用户25的评论，under_comment_id 指向 20
(13, 27, 'First comment on post 13.', true, 5, null, null, now()),
(13, 28, 'Another comment for post 13.', true, 6, null, null, now()),
(14, 29, 'Comment on post 14.', true, 2, null, null, now()),
(14, 30, 'Reply to post 14 comment.', true, 3, null, 26, now()), -- 回复用户29的评论，under_comment_id 指向 26
(15, 1, 'First comment on post 15.', true, 8, null, null, now()),
(15, 2, 'Another comment for post 15.', true, 0, null, null, now()),
(16, 3, 'Comment on post 16.', true, 4, null, null, now()),
(16, 4, 'Reply to post 16 comment.', true, 1, null, null, now()),
(17, 5, 'First comment on post 17.', true, 6, null, null, now()),
(17, 6, 'Another comment for post 17.', true, 0, null, 31, now()), -- 回复用户5的评论，under_comment_id 指向 31
(18, 7, 'Comment on post 18.', true, 2, null, null, now()),
(18, 8, 'Reply to post 18 comment.', true, 4, null, 33, now()), -- 回复用户7的评论，under_comment_id 指向 33
(19, 9, 'First comment on post 19.', true, 5, null, null, now()),
(19, 10, 'Another comment for post 19.', true, 1, null, null, now()),
(20, 11, 'Comment on post 20.', true, 7, null, null, now()),
(20, 12, 'Reply to post 20 comment.', true, 2, null, null, now()),
(21, 13, 'First comment on post 21.', true, 6, null, null, now()),
(21, 14, 'Another comment for post 21.', true, 1, null, 37, now()), -- 回复用户13的评论，under_comment_id 指向 37
(22, 15, 'Comment on post 22.', true, 4, null, null, now()),
(22, 16, 'Reply to post 22 comment.', true, 1, null, null, now()),
(23, 17, 'First comment on post 23.', true, 5, null, null, now()),
(23, 18, 'Another comment for post 23.', true, 0, null, null, now()),
(24, 19, 'Comment on post 24.', true, 2, null, null, now()),
(24, 20, 'Reply to post 24 comment.', true, 3, null, 40, now()), -- 回复用户19的评论，under_comment_id 指向 40
(25, 21, 'First comment on post 25.', true, 8, null, null, now()),
(25, 22, 'Another comment for post 25.', true, 0, null, null, now()),
(26, 23, 'Comment on post 26.', true, 4, null, null, now()),
(26, 24, 'Reply to post 26 comment.', true, 1, null, null, now()),
(27, 25, 'First comment on post 27.', true, 6, null, null, now()),
(27, 26, 'Another comment for post 27.', true, 0, null, 43, now()), -- 回复用户25的评论，under_comment_id 指向 43
(28, 27, 'Comment on post 28.', true, 2, null, null, now()),
(28, 28, 'Reply to post 28 comment.', true, 4, null, null, now()),
(29, 29, 'First comment on post 29.', true, 5, null, null, now()),
(29, 30, 'Another comment for post 29.', true, 1, null, null, now()),
(30, 1, 'First comment on post 30.', true, 7, null, null, now()),
(30, 2, 'Another comment for post 30.', true, 2, null, null, now());



-- 向 post_comment_like_users 表插入数据
insert into post_comment_like_users
(postcomment_id, user_id)
values
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(3, 6),
(4, 7),
(5, 8),
(6, 9),
(7, 10),
(8, 11),
(9, 12),
(10, 13);

-- 向 post_like_users 表插入数据
insert into post_like_users
(post_id, user_id)
values
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(3, 6),
(3, 7),
(4, 8),
(4, 9),
(5, 10),
(6, 11),
(7, 12),
(8, 13),
(9, 14),
(10, 15);

-- 向 post_tags 表插入数据
insert into post_tags
(post_id, tag_id)
values
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 7),
(5, 8),
(6, 9),
(7, 10),
(8, 11),
(9, 12),
(10, 13),
(10, 14),
(11, 15),
(12, 16),
(13, 17),
(14, 18),
(15, 19),
(16, 20),
(17, 21),
(18, 22),
(19, 23),
(20, 24),
(21, 25),
(22, 26),
(23, 27);

-- 插入 submission 表数据
insert into submission
(id, problem_id, create_time, user_id, code, result, time_spent, memory_spent, error_info, language)
values
(uuid(), 1, now(), 2, 'print("Hello, world!")', 1, 20, 512, null, 'Python'),
(uuid(), 2, now(), 2, '#include<stdio.h>\nint main(){return 0;}', 2, 15, 256, null, 'C'),
(uuid(), 3, now(), 2, 'public class Main { public static void main(String[] args) { System.out.println("Hello"); } }', 3, 25, 1024, null, 'Java'),
(uuid(), 4, now(), 2, 'def add(a, b): return a + b', 1, 10, 128, null, 'Python'),
(uuid(), 5, now(), 2, 'int add(int a, int b) { return a + b; }', 1, 30, 256, null, 'C'),
(uuid(), 6, now(), 2, 'print("Judge System Test")', 4, 18, 320, '{"error": "Runtime error"}', 'Python'),
(uuid(), 7, now(), 2, 'using System; class Program { static void Main() { Console.WriteLine("Hi"); } }', 1, 12, 512, null, 'C#'),
(uuid(), 8, now(), 2, '<html><body><h1>Hello!</h1></body></html>', 5, 5, 64, null, 'HTML'),
(uuid(), 9, now(), 2, 'print("Test")', 3, 28, 800, '{"error": "Memory Limit Exceeded"}', 'Python'),
(uuid(), 10, now(), 2, 'function hello() { console.log("Hi"); }', 1, 20, 200, null, 'JavaScript'),
(uuid(), 11, now(), 2, 'console.log("Debugging");', 4, 22, 300, '{"error": "Syntax error"}', 'JavaScript'),
(uuid(), 12, now(), 2, 'print("Another Test")', 1, 25, 400, null, 'Python'),

(uuid(), 1, now(), 3, 'print("Hello, world!")', 1, 20, 512, null, 'Python'),
(uuid(), 2, now(), 3, '#include<stdio.h>\nint main(){return 0;}', 2, 15, 256, null, 'C'),
(uuid(), 3, now(), 3, 'public class Main { public static void main(String[] args) { System.out.println("Hello"); } }', 3, 25, 1024, null, 'Java'),
(uuid(), 4, now(), 3, 'def add(a, b): return a + b', 1, 10, 128, null, 'Python'),
(uuid(), 5, now(), 3, 'int add(int a, int b) { return a + b; }', 1, 30, 256, null, 'C'),
(uuid(), 6, now(), 3, 'print("Judge System Test")', 4, 18, 320, '{"error": "Runtime error"}', 'Python'),
(uuid(), 7, now(), 3, 'using System; class Program { static void Main() { Console.WriteLine("Hi"); } }', 1, 12, 512, null, 'C#'),
(uuid(), 8, now(), 3, '<html><body><h1>Hello!</h1></body></html>', 5, 5, 64, null, 'HTML'),
(uuid(), 9, now(), 3, 'print("Test")', 3, 28, 800, '{"error": "Memory Limit Exceeded"}', 'Python'),
(uuid(), 10, now(), 3, 'function hello() { console.log("Hi"); }', 1, 20, 200, null, 'JavaScript'),
(uuid(), 11, now(), 3, 'console.log("Debugging");', 4, 22, 300, '{"error": "Syntax error"}', 'JavaScript'),
(uuid(), 12, now(), 3, 'print("Another Test")', 1, 25, 400, null, 'Python'),

(uuid(), 1, now(), 4, 'print("Hello, world!")', 1, 20, 512, null, 'Python'),
(uuid(), 2, now(), 4, '#include<stdio.h>\nint main(){return 0;}', 2, 15, 256, null, 'C'),
(uuid(), 3, now(), 4, 'public class Main { public static void main(String[] args) { System.out.println("Hello"); } }', 3, 25, 1024, null, 'Java'),
(uuid(), 4, now(), 4, 'def add(a, b): return a + b', 1, 10, 128, null, 'Python'),
(uuid(), 5, now(), 4, 'int add(int a, int b) { return a + b; }', 1, 30, 256, null, 'C'),
(uuid(), 6, now(), 4, 'print("Judge System Test")', 4, 18, 320, '{"error": "Runtime error"}', 'Python'),
(uuid(), 7, now(), 4, 'using System; class Program { static void Main() { Console.WriteLine("Hi"); } }', 1, 12, 512, null, 'C#'),
(uuid(), 8, now(), 4, '<html><body><h1>Hello!</h1></body></html>', 5, 5, 64, null, 'HTML'),
(uuid(), 9, now(), 4, 'print("Test")', 3, 28, 800, '{"error": "Memory Limit Exceeded"}', 'Python'),
(uuid(), 10, now(), 4, 'function hello() { console.log("Hi"); }', 1, 20, 200, null, 'JavaScript'),
(uuid(), 11, now(), 4, 'console.log("Debugging");', 4, 22, 300, '{"error": "Syntax error"}', 'JavaScript'),
(uuid(), 12, now(), 4, 'print("Another Test")', 1, 25, 400, null, 'Python'),

(uuid(), 1, now(), 5, 'print("Hello, world!")', 1, 20, 512, null, 'Python'),
(uuid(), 2, now(), 5, '#include<stdio.h>\nint main(){return 0;}', 2, 15, 256, null, 'C'),
(uuid(), 3, now(), 5, 'public class Main { public static void main(String[] args) { System.out.println("Hello"); } }', 3, 25, 1024, null, 'Java'),
(uuid(), 4, now(), 5, 'def add(a, b): return a + b', 1, 10, 128, null, 'Python'),
(uuid(), 5, now(), 5, 'int add(int a, int b) { return a + b; }', 1, 30, 256, null, 'C'),
(uuid(), 6, now(), 5, 'print("Judge System Test")', 4, 18, 320, '{"error": "Runtime error"}', 'Python'),
(uuid(), 7, now(), 5, 'using System; class Program { static void Main() { Console.WriteLine("Hi"); } }', 1, 12, 512, null, 'C#'),
(uuid(), 8, now(), 5, '<html><body><h1>Hello!</h1></body></html>', 5, 5, 64, null, 'HTML'),
(uuid(), 9, now(), 5, 'print("Test")', 3, 28, 800, '{"error": "Memory Limit Exceeded"}', 'Python'),
(uuid(), 10, now(), 5, 'function hello() { console.log("Hi"); }', 1, 20, 200, null, 'JavaScript'),
(uuid(), 11, now(), 5, 'console.log("Debugging");', 4, 22, 300, '{"error": "Syntax error"}', 'JavaScript'),
(uuid(), 12, now(), 5, 'print("Another Test")', 1, 25, 400, null, 'Python'),

(uuid(), 1, now(), 6, 'print("Hello, world!")', 1, 20, 512, null, 'Python'),
(uuid(), 2, now(), 6, '#include<stdio.h>\nint main(){return 0;}', 2, 15, 256, null, 'C'),
(uuid(), 3, now(), 6, 'public class Main { public static void main(String[] args) { System.out.println("Hello"); } }', 3, 25, 1024, null, 'Java'),
(uuid(), 4, now(), 6, 'def add(a, b): return a + b', 1, 10, 128, null, 'Python'),
(uuid(), 5, now(), 6, 'int add(int a, int b) { return a + b; }', 1, 30, 256, null, 'C'),
(uuid(), 6, now(), 6, 'print("Judge System Test")', 4, 18, 320, '{"error": "Runtime error"}', 'Python'),
(uuid(), 7, now(), 6, 'using System; class Program { static void Main() { Console.WriteLine("Hi"); } }', 1, 12, 512, null, 'C#'),
(uuid(), 8, now(), 6, '<html><body><h1>Hello!</h1></body></html>', 5, 5, 64, null, 'HTML'),
(uuid(), 9, now(), 6, 'print("Test")', 3, 28, 800, '{"error": "Memory Limit Exceeded"}', 'Python'),
(uuid(), 10, now(), 6, 'function hello() { console.log("Hi"); }', 1, 20, 200, null, 'JavaScript'),
(uuid(), 11, now(), 6, 'console.log("Debugging");', 4, 22, 300, '{"error": "Syntax error"}', 'JavaScript'),
(uuid(), 12, now(), 6, 'print("Another Test")', 1, 25, 400, null, 'Python'),

(uuid(), 1, now(), 7, 'print("Hello, world!")', 1, 20, 512, null, 'Python'),
(uuid(), 2, now(), 7, '#include<stdio.h>\nint main(){return 0;}', 2, 15, 256, null, 'C'),
(uuid(), 3, now(), 7, 'public class Main { public static void main(String[] args) { System.out.println("Hello"); } }', 3, 25, 1024, null, 'Java'),
(uuid(), 4, now(), 7, 'def add(a, b): return a + b', 1, 10, 128, null, 'Python'),
(uuid(), 5, now(), 7, 'int add(int a, int b) { return a + b; }', 1, 30, 256, null, 'C'),
(uuid(), 6, now(), 7, 'print("Judge System Test")', 4, 18, 320, '{"error": "Runtime error"}', 'Python'),
(uuid(), 7, now(), 7, 'using System; class Program { static void Main() { Console.WriteLine("Hi"); } }', 1, 12, 512, null, 'C#'),
(uuid(), 8, now(), 7, '<html><body><h1>Hello!</h1></body></html>', 5, 5, 64, null, 'HTML'),
(uuid(), 9, now(), 7, 'print("Test")', 3, 28, 800, '{"error": "Memory Limit Exceeded"}', 'Python'),
(uuid(), 10, now(), 7, 'function hello() { console.log("Hi"); }', 1, 20, 200, null, 'JavaScript'),
(uuid(), 11, now(), 7, 'console.log("Debugging");', 4, 22, 300, '{"error": "Syntax error"}', 'JavaScript'),
(uuid(), 12, now(), 7, 'print("Another Test")', 1, 25, 400, null, 'Python');




update post set like_count = (select count(*) from post_like_users where post_id = post.id);
update post set comment_count = (select count(*) from post_comment where post_id = post.id);
update post_comment set like_count = (select count(*) from post_comment_like_users where postcomment_id = post_comment.id);


