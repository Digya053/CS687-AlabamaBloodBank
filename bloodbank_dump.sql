-- MySQL dump 10.13  Distrib 8.0.23, for osx10.16 (x86_64)
--
-- Host: localhost    Database: bloodbank
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `ALABAMA_BLOOD_STORAGE`
--

DROP TABLE IF EXISTS `ALABAMA_BLOOD_STORAGE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ALABAMA_BLOOD_STORAGE` (
  `storage_id` varchar(4) NOT NULL,
  `blood_type` varchar(3) NOT NULL,
  `quantity_in_ml` int NOT NULL,
  PRIMARY KEY (`storage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ALABAMA_BLOOD_STORAGE`
--

LOCK TABLES `ALABAMA_BLOOD_STORAGE` WRITE;
/*!40000 ALTER TABLE `ALABAMA_BLOOD_STORAGE` DISABLE KEYS */;
INSERT INTO `ALABAMA_BLOOD_STORAGE` VALUES ('AS6','A+',470),('CS4','A+',500),('HMS5','A+',500),('HS1','A+',470),('HS2','O+',500),('HS9','A+',10000),('MS11','A+',500),('MS12','B+',700),('MS3','O+',600),('MS7','B+',700),('MS8','O+',700);
/*!40000 ALTER TABLE `ALABAMA_BLOOD_STORAGE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLOOD`
--

DROP TABLE IF EXISTS `BLOOD`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BLOOD` (
  `blood_id` varchar(4) NOT NULL,
  `available_from` date DEFAULT NULL,
  `d_gender` char(1) NOT NULL,
  `d_weight` int NOT NULL,
  `d_height` int NOT NULL,
  `d_age` int NOT NULL,
  `ssn` char(9) NOT NULL,
  `organizer_id` varchar(4) NOT NULL,
  `storage_id` varchar(4) NOT NULL,
  PRIMARY KEY (`blood_id`),
  KEY `organizer_id` (`organizer_id`),
  KEY `storage_id` (`storage_id`),
  KEY `ssn` (`ssn`),
  CONSTRAINT `users_blood_ibfk_1` FOREIGN KEY (`organizer_id`) REFERENCES `ORGANIZERS` (`organizer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users_blood_ibfk_2` FOREIGN KEY (`storage_id`) REFERENCES `ALABAMA_BLOOD_STORAGE` (`storage_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users_blood_ibfk_3` FOREIGN KEY (`ssn`) REFERENCES `REGISTERED_USERS` (`ssn`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLOOD`
--

LOCK TABLES `BLOOD` WRITE;
/*!40000 ALTER TABLE `BLOOD` DISABLE KEYS */;
INSERT INTO `BLOOD` VALUES ('b1','2021-01-01','M',165,80,40,'453282599','OI2','HS1'),('b10','2021-03-03','F',145,62,28,'333445555','OI4','MS8'),('b11','2021-03-03','F',165,63,32,'986016576','OI3','MS12'),('b2','2021-02-01','M',160,76,38,'453282599','OI1','HS2'),('b3','2021-02-05','M',155,60,35,'453282599','OI5','MS3'),('b4','2021-03-20','F',145,68,40,'444556666','OI6','CS4'),('b5','2021-03-19','F',155,67,32,'333445555','OI7','HMS5'),('b6','2021-03-01','M',180,67,31,'453867543','OI8','MS7'),('b9','2021-03-01','F',155,65,27,'778899999','OI7','MS8');
/*!40000 ALTER TABLE `BLOOD` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BLOOD_DONATION_EVENT`
--

DROP TABLE IF EXISTS `BLOOD_DONATION_EVENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BLOOD_DONATION_EVENT` (
  `event_id` varchar(5) NOT NULL,
  `event_name` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `street` varchar(200) NOT NULL,
  `city` varchar(20) NOT NULL,
  `organizer_id` varchar(4) NOT NULL,
  PRIMARY KEY (`event_id`),
  KEY `organizer_id` (`organizer_id`),
  CONSTRAINT `users_blooddonationevent_ibfk_1` FOREIGN KEY (`organizer_id`) REFERENCES `ORGANIZERS` (`organizer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BLOOD_DONATION_EVENT`
--

LOCK TABLES `BLOOD_DONATION_EVENT` WRITE;
/*!40000 ALTER TABLE `BLOOD_DONATION_EVENT` DISABLE KEYS */;
INSERT INTO `BLOOD_DONATION_EVENT` VALUES ('EI11','UAH Blood Donation Event','2020-03-24','1010 Henderson Road','Huntsville','OI1'),('EI21','Lions Club Blood Donation Event','2020-01-20','2030 Oak Park','Huntsville','OI2'),('EI22','March Blood Donation Event','2021-03-01','2031 Fourth Avenue','Birmingham','OI6'),('EI23','April blood Donation Event','2021-04-01','2031 Fourth Avenue','Birmingham','OI4'),('EI28','Blood Donation for Cancer Patients','2021-05-01','2061 Pine Park','Madison','OI7'),('EI30','May Blood Donation Event','2021-05-01','1010 Henderson Road','Huntsville','OI2'),('EI31','RED Cross Blood Donation','2021-04-10','1010 Henderson Road','Huntsville','OI3'),('EI32','Lions club Blood Donation Event','2021-05-10','6372 Sherwood Apartments','Huntsville','OI2'),('EI34','Blood Donation for Life','2021-05-06','2122 Second apartments','Madison','OI2'),('EI42','Womens Day Blood Donation','2021-03-08','1781 Jackson Road','Madison','OI9'),('EI43','Christmas Blood Donation Event','2020-12-26','2031 Fourth Avenue','Birmingham','OI5'),('EI44','Blood Donation for heart patients','2021-05-04','2061 Pine Park','Madison','OI8'),('EI46','February Blood Donation Event','2021-02-02','2031 Fourth Avenue','Birmingham','OI5');
/*!40000 ALTER TABLE `BLOOD_DONATION_EVENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HOSPITALS`
--

DROP TABLE IF EXISTS `HOSPITALS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `HOSPITALS` (
  `hname` varchar(100) NOT NULL,
  `hmembership_no` varchar(4) NOT NULL,
  `city` varchar(20) NOT NULL,
  PRIMARY KEY (`hmembership_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HOSPITALS`
--

LOCK TABLES `HOSPITALS` WRITE;
/*!40000 ALTER TABLE `HOSPITALS` DISABLE KEYS */;
INSERT INTO `HOSPITALS` VALUES ('Huntsville Hospital','H1','Huntsville'),('Madison Hospital','H2','Madison'),('Crestwood Medical Center','H3','Huntsville'),('Highlands Medical Center','H4','Scottsboro'),('Athens Limestone Hospital','H5','Athens');
/*!40000 ALTER TABLE `HOSPITALS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ORGANIZERS`
--

DROP TABLE IF EXISTS `ORGANIZERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ORGANIZERS` (
  `organizer_id` varchar(4) NOT NULL,
  `organizer_name` varchar(50) NOT NULL,
  `contact_no` int NOT NULL,
  `email` varchar(320) NOT NULL,
  PRIMARY KEY (`organizer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ORGANIZERS`
--

LOCK TABLES `ORGANIZERS` WRITE;
/*!40000 ALTER TABLE `ORGANIZERS` DISABLE KEYS */;
INSERT INTO `ORGANIZERS` VALUES ('OI1','The University of Alabama in Huntsville',256824100,'contacts@uah.edu'),('OI2','Lions club',276824111,'lionsclub@gmail.com'),('OI3','Red Cross Society',800733276,'support@redcross.org'),('OI4','Florence club',21287890,'florenceclub@gmail.com'),('OI5','Birmingham Club',376824222,'brimclub@gmail.com'),('OI6','Athens Club',72127781,'athensclub@gmail.com'),('OI7','Madison Club',333212777,'madisonclub@gmail.com'),('OI8','Geo club',22189744,'geoclub@gmail.com'),('OI9','Womens club',77722233,'womensclub@gmail.com');
/*!40000 ALTER TABLE `ORGANIZERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PARTICIPATES_IN`
--

DROP TABLE IF EXISTS `PARTICIPATES_IN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PARTICIPATES_IN` (
  `pssn` char(9) NOT NULL,
  `event_id` varchar(5) NOT NULL,
  PRIMARY KEY (`pssn`,`event_id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `users_participatesin_ibfk_1` FOREIGN KEY (`pssn`) REFERENCES `REGISTERED_USERS` (`ssn`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users_participatesin_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `BLOOD_DONATION_EVENT` (`event_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PARTICIPATES_IN`
--

LOCK TABLES `PARTICIPATES_IN` WRITE;
/*!40000 ALTER TABLE `PARTICIPATES_IN` DISABLE KEYS */;
INSERT INTO `PARTICIPATES_IN` VALUES ('444556666','EI11'),('453282599','EI11'),('888665555','EI21'),('723578654','EI22'),('123456789','EI28'),('453282599','EI28'),('888665555','EI31'),('987654321','EI31'),('333445555','EI32'),('987654321','EI42'),('723578654','EI43'),('888665555','EI46'),('986016576','EI46'),('898413713','EI30');
/*!40000 ALTER TABLE `PARTICIPATES_IN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `REGISTERED_USERS`
--

DROP TABLE IF EXISTS `REGISTERED_USERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `REGISTERED_USERS` (
  `fname` varchar(20) NOT NULL,
  `mnit` varchar(1) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `ssn` char(9) NOT NULL,
  `dob` date NOT NULL,
  `city` varchar(15) NOT NULL,
  `blood_type` varchar(3) NOT NULL,
  `gender` char(1) NOT NULL,
  `email` varchar(320) NOT NULL,
  `password` varchar(300) NOT NULL,
  `weight_in_lbs` int NOT NULL,
  `height_in_lbs` int NOT NULL,
  `hmembership_no` varchar(3) NOT NULL,
  PRIMARY KEY (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `REGISTERED_USERS`
--

LOCK TABLES `REGISTERED_USERS` WRITE;
/*!40000 ALTER TABLE `REGISTERED_USERS` DISABLE KEYS */;
INSERT INTO `REGISTERED_USERS` VALUES ('Ismita','M','Tasnim','123456789','1990-03-15','Huntsville','A+','F','ismita.tasnim@gmail.com','i',60,150,'H1'),('Ethan','K','Cash','333445555','1967-11-12','Montgomery','O+','M','ethan432@gmail.com','a',186,65,'H5'),('Daniel','A','Dickinson','444556666','1989-12-01','Athens','O-','M','daniel321@gmail.com','a',160,60,'H5'),('Katrina','E','Wong','453282599','1991-12-01','Huntsville','B-','F','katrina777@gmail.com','a',125,63,'H1'),('Michael','J','Potter','453867543','1985-05-10','Madison','A-','M','michael453@gmail.com','a',197,75,'H2'),('Jacob','T','Bond','543886644','1975-02-05','Birmingham','B+','M','jacob807@gmail.com','a',200,76,'H4'),('Noah','S','Bush','723578654','1962-10-10','Auburn','B-','M','noah578@gmail.com','a',182,70,'H3'),('Derek','V','Wallace','778899999','1990-11-02','Florence','B+','M','derek702@gmail.com','a',158,63,'H3'),('William','B','Smith','888665555','1965-01-10','Huntsville','A+','M','william935@gmail.com','a',140,76,'H1'),('Angel','P','Borg','898413713','2010-03-10','Birmingham','AB+','F','angel@gmail.com','j',150,60,'H2'),('Elizabeth','J','English','986016576','1994-10-10','Birmingham','A+','F','elizabeth@gmail.com','a',145,63,'H2'),('Steffaine','D','Zelaya','987654321','1993-11-02','Huntsville','A+','F','steffaine@gmail.com','a',128,58,'H1'),('Ram','K','Shrestha','345678912','1971-03-18','Huntsville','A+','M','ram.shrestha@gmail.com','r',150,62,'H1');
/*!40000 ALTER TABLE `REGISTERED_USERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SPONSORED_BY`
--

DROP TABLE IF EXISTS `SPONSORED_BY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SPONSORED_BY` (
  `event_id` varchar(5) NOT NULL,
  `hmembership_no` varchar(4) NOT NULL,
  `amount_in_dollars` int NOT NULL,
  PRIMARY KEY (`event_id`,`hmembership_no`),
  KEY `hmembership_no` (`hmembership_no`),
  CONSTRAINT `users_sponsoredby_ibfk_1` FOREIGN KEY (`hmembership_no`) REFERENCES `HOSPITALS` (`hmembership_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users_sponsoredby_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `BLOOD_DONATION_EVENT` (`event_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SPONSORED_BY`
--

LOCK TABLES `SPONSORED_BY` WRITE;
/*!40000 ALTER TABLE `SPONSORED_BY` DISABLE KEYS */;
INSERT INTO `SPONSORED_BY` VALUES ('EI11','H1',500),('EI21','H1',500),('EI21','H3',520),('EI22','H4',450),('EI23','H5',500),('EI28','H2',450),('EI30','H1',500),('EI31','H5',520),('EI32','H3',500),('EI34','H2',450),('EI42','H2',500),('EI43','H4',450),('EI46','H4',450);
/*!40000 ALTER TABLE `SPONSORED_BY` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-22 12:38:51
