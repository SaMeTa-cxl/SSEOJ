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
