-- MySQL dump 10.13  Distrib 8.0.25, for macos11 (x86_64)
--
-- Host: localhost    Database: college
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Class`
--

DROP TABLE IF EXISTS `Class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Class` (
  `CName` varchar(10) NOT NULL,
  `Time` char(4) NOT NULL,
  `Room` varchar(20) NOT NULL,
  PRIMARY KEY (`CName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Class`
--

LOCK TABLES `Class` WRITE;
/*!40000 ALTER TABLE `Class` DISABLE KEYS */;
INSERT INTO `Class` VALUES ('Chem 422','MW2','Busch'),('CS 210','MW4','Remote'),('CS 213','Any','Remote'),('CS 323','TTh8','Busch'),('Econ 586','TTh6','CAC'),('Econ 607','MTh4','CAC'),('Eng 256','TTh5','CAC'),('Eng 316','MTH3','CAC'),('Hist 102','Any','CAC'),('Hist 401','Any','CAC'),('Math 311','MW5','Liv'),('Phy 421','TTh4','Busch'),('Phy 605','TTh6','Busch');
/*!40000 ALTER TABLE `Class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Enrollment`
--

DROP TABLE IF EXISTS `Enrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Enrollment` (
  `SId` int NOT NULL,
  `CName` varchar(10) NOT NULL,
  `Pos` smallint NOT NULL,
  KEY `SId` (`SId`),
  KEY `CName` (`CName`),
  CONSTRAINT `enrollment_ibfk_1` FOREIGN KEY (`SId`) REFERENCES `Student` (`Id`),
  CONSTRAINT `enrollment_ibfk_2` FOREIGN KEY (`CName`) REFERENCES `Class` (`CName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Enrollment`
--

LOCK TABLES `Enrollment` WRITE;
/*!40000 ALTER TABLE `Enrollment` DISABLE KEYS */;
INSERT INTO `Enrollment` VALUES (100,'Math 311',1),(100,'CS 210',3),(150,'CS 210',2),(150,'CS 213',5),(150,'CS 323',1),(150,'Math 311',10),(200,'Phy 605',3),(200,'CS 323',2),(250,'Eng 256',8),(250,'Eng 316',7),(250,'CS 213',26),(300,'Hist 102',24),(300,'CS 210',6),(350,'Chem 422',14),(350,'Hist 401',2),(400,'Econ 586',1),(400,'Econ 607',4);
/*!40000 ALTER TABLE `Enrollment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HonorStudent`
--

DROP TABLE IF EXISTS `HonorStudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `HonorStudent` (
  `SId` int NOT NULL,
  KEY `SId` (`SId`),
  CONSTRAINT `honorstudent_ibfk_1` FOREIGN KEY (`SId`) REFERENCES `Student` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HonorStudent`
--

LOCK TABLES `HonorStudent` WRITE;
/*!40000 ALTER TABLE `HonorStudent` DISABLE KEYS */;
INSERT INTO `HonorStudent` VALUES (100),(150),(250);
/*!40000 ALTER TABLE `HonorStudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Student` (
  `Id` int NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Major` varchar(20) NOT NULL,
  `Year` enum('FR','SO','JR','SR','GR') NOT NULL DEFAULT 'FR',
  `Age` tinyint NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student`
--

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` VALUES (100,'Perez','Math','JR',21),(150,'Patel','CS','SO',19),(200,'Eastwood','Physics','GR',26),(250,'Chen','English','SR',22),(300,'Madsen','History','FR',18),(350,'Harris','Chemistry','SR',21),(400,'Bakalova','Economics','GR',24);
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-02 18:30:42
