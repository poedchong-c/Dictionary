/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.7.2-MariaDB, for Win64 (AMD64)
--
-- Host: 192.168.100.10    Database: dictionary
-- ------------------------------------------------------
-- Server version	11.8.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `word`
--

DROP TABLE IF EXISTS `word`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `word` (
  `Column1` varchar(50) DEFAULT NULL,
  `Column2` varchar(50) DEFAULT NULL,
  `Column3` varchar(50) DEFAULT NULL,
  `Column4` varchar(50) DEFAULT NULL,
  `Column5` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `word`
--

LOCK TABLES `word` WRITE;
/*!40000 ALTER TABLE `word` DISABLE KEYS */;
INSERT INTO `word` VALUES
('id','vocab','meaning','category_id','gif_url'),
('1','สวัสดี','Hello','1','https://www.th-sl.com//wp-content/uploads/2020/09/1.1.1.gif'),
('2','ขอบคุณ','Thank you','1','https://www.th-sl.com//wp-content/uploads/2020/09/1.2.1.gif'),
('3','สบายดี','I am fine','1','https://www.th-sl.com//wp-content/uploads/2021/10/4.098.gif'),
('4','ยินดีด้วย','Welcome','1','https://www.th-sl.com//wp-content/uploads/2023/12/2566-0945.gif'),
('5','ทำไม','Why?','2','https://www.th-sl.com//wp-content/uploads/2020/09/1.56.1.gif'),
('6','กี่โมง','What time?','2','https://www.th-sl.com//wp-content/uploads/2021/10/6.041-02.gif'),
('7','อะไร','What?','2','https://www.th-sl.com//wp-content/uploads/2020/09/1.55.1.gif'),
('8','หนึ่ง','One','3','https://www.th-sl.com//wp-content/uploads/2021/05/2.100.1.gif'),
('9','สอง','Two','3','https://www.th-sl.com//wp-content/uploads/2021/05/2.100.2.gif'),
('10','สาม','Three','3','https://www.th-sl.com//wp-content/uploads/2021/05/2.100.3.gif'),
('11','สี่','Four','3','https://www.th-sl.com//wp-content/uploads/2021/05/2.100.4.gif'),
('12','ห้า','Five','3','https://www.th-sl.com//wp-content/uploads/2021/05/2.100.5.gif'),
('13','ตอนเช้า','Morning','4','https://www.th-sl.com//wp-content/uploads/2020/09/1.35.2.gif'),
('14','ตอนเย็น','Evening','4','https://www.th-sl.com//wp-content/uploads/2020/09/1.37.1.gif'),
('15','เที่ยงวัน','Noon','4','https://www.th-sl.com//wp-content/uploads/2021/06/2.100.47.gif'),
('16','เที่ยงคืน','Midnight','4','https://www.th-sl.com//wp-content/uploads/2025/06/1.38.2-2.gif'),
('17','หมั่นไส้','dislike','5','https://www.th-sl.com//wp-content/uploads/2025/11/2568-0383.gif'),
('18','เบื่อ','bored','5','https://www.th-sl.com//wp-content/uploads/2020/09/5.87.1.gif'),
('19','โกรธ','angry','5','https://www.th-sl.com//wp-content/uploads/2020/09/5.72.1.gif'),
('20','เสียใจ','sad','5','https://www.th-sl.com//wp-content/uploads/2020/09/5.83.2.gif'),
('21','ดีใจ','happy','5','https://www.th-sl.com//wp-content/uploads/2020/09/5.83.1.gif'),
('22','ข้าวไก่ทอด','fried chicken rice','6','https://www.th-sl.com//wp-content/uploads/2025/08/2568-0295.gif'),
('23','กะเพรา','kaphrao','6','https://www.th-sl.com//wp-content/uploads/2020/09/3.13.2.gif'),
('24','ไข่เจียว','omelette','6','https://www.th-sl.com//wp-content/uploads/2023/11/5-4-1.gif'),
('25','ผัดไทย','padthai','6','https://www.th-sl.com//wp-content/uploads/2020/09/5.15.2.gif');
/*!40000 ALTER TABLE `word` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2026-03-30 19:57:36
