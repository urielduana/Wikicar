-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: wikicar
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `brand` (
  `Id_brand` int(15) NOT NULL AUTO_INCREMENT,
  `Brand_name` varchar(25) NOT NULL,
  `Founders` varchar(100) NOT NULL,
  `Foundation_date` date NOT NULL,
  `Country` varchar(20) NOT NULL,
  `Brand_history` text NOT NULL,
  PRIMARY KEY (`Id_brand`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (1,'Renault','Paquito Fernandez','1997-03-05','Francia','Era un compa que agarró un HotWheels y lo hizo grandote y ya se hizo millonario'),(2,'Chevrolet','Pedrito Sanchez y Bumbblebee','2022-02-06','Paises Bajos','Se encontró un nopal e hizo esta wea');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `car` (
  `Id_car` int(15) NOT NULL AUTO_INCREMENT,
  `Registration_plate` varchar(10) NOT NULL,
  `Color` varchar(20) NOT NULL,
  `Deficiency` text DEFAULT NULL,
  `Mileage` int(10) NOT NULL,
  `User_id` int(15) NOT NULL,
  `Brand_id` int(15) NOT NULL,
  PRIMARY KEY (`Id_car`),
  KEY `Brand_id` (`Brand_id`),
  KEY `User_id` (`User_id`),
  CONSTRAINT `car_ibfk_1` FOREIGN KEY (`Brand_id`) REFERENCES `brand` (`Id_Brand`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `car_ibfk_2` FOREIGN KEY (`User_id`) REFERENCES `user` (`Id_User`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'UMX-585-X','Rojo','Ta medio feito',150000,1,1);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model`
--

DROP TABLE IF EXISTS `model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model` (
  `Id_model` int(15) NOT NULL AUTO_INCREMENT,
  `Model_name` varchar(15) NOT NULL,
  `Model_type` varchar(15) NOT NULL,
  `Doors` int(2) DEFAULT NULL,
  `Seats` int(2) DEFAULT NULL,
  `GasTank_capacity` int(5) DEFAULT NULL,
  `Gas_type` varchar(30) DEFAULT NULL,
  `Model_year` int(4) DEFAULT NULL,
  `Starting_price` float DEFAULT NULL,
  `Actual_price` float DEFAULT NULL,
  `Configuration` text NOT NULL,
  `Brand_id` int(15) NOT NULL,
  PRIMARY KEY (`Id_model`),
  KEY `Brand_id` (`Brand_id`),
  CONSTRAINT `model_ibfk_1` FOREIGN KEY (`Brand_id`) REFERENCES `brand` (`Id_Brand`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model`
--

LOCK TABLES `model` WRITE;
/*!40000 ALTER TABLE `model` DISABLE KEYS */;
INSERT INTO `model` VALUES (1,'Duster','Camioneta',4,5,50,'De la roja',2013,223000,100000,'Partes que no me sé',1);
/*!40000 ALTER TABLE `model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news` (
  `Id_news` int(15) NOT NULL AUTO_INCREMENT,
  `News_date` date NOT NULL,
  `News_score` float NOT NULL,
  `News_text` text NOT NULL,
  `Section_id` int(15) NOT NULL,
  PRIMARY KEY (`Id_news`),
  KEY `Section_id` (`Section_id`),
  CONSTRAINT `news_ibfk_1` FOREIGN KEY (`Section_id`) REFERENCES `section` (`Id_section`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (2,'2022-03-26',7,'Taba chido',1);
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `Id_post` int(15) NOT NULL AUTO_INCREMENT,
  `Post_date` date NOT NULL,
  `Post_score` float NOT NULL,
  `Post_text` text NOT NULL,
  `Section_id` int(15) NOT NULL,
  PRIMARY KEY (`Id_post`),
  KEY `Section_id` (`Section_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`Section_id`) REFERENCES `section` (`Id_section`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,'2022-03-26',5,'Estuvo bien chido el motor de esta wea',1);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `section`
--

DROP TABLE IF EXISTS `section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `section` (
  `Id_section` int(15) NOT NULL AUTO_INCREMENT,
  `Creation_date` date NOT NULL,
  `Section_type` varchar(20) NOT NULL,
  `Model_id` int(15) NOT NULL,
  PRIMARY KEY (`Id_section`),
  KEY `Model_id` (`Model_id`),
  CONSTRAINT `section_ibfk_1` FOREIGN KEY (`Model_id`) REFERENCES `model` (`Id_model`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `section`
--

LOCK TABLES `section` WRITE;
/*!40000 ALTER TABLE `section` DISABLE KEYS */;
INSERT INTO `section` VALUES (1,'2022-03-25','Motor',1);
/*!40000 ALTER TABLE `section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `Id_User` int(15) NOT NULL AUTO_INCREMENT,
  `User_name` varchar(35) NOT NULL,
  `User_lastname` varchar(35) NOT NULL,
  `Password` varchar(35) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Gender` char(1) NOT NULL,
  PRIMARY KEY (`Id_User`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Uriel','Duana Chavez','abc12345','uriel@gmail.com','M'),(2,'Gustavo Angel','Montoya Martinez','sdas1855!d','gusm@gmail.com','M'),(3,'Ulises','Florean Guzman','sger748427','ulisesF@gmail.com','M');
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

-- Dump completed on 2022-03-28 17:10:59
