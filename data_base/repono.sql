-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: repono
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `tb_clientes`
--

DROP TABLE IF EXISTS `tb_clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefone` varchar(50) NOT NULL,
  `dt_nascimento` varchar(10) NOT NULL,
  `cpf` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_clientes`
--

LOCK TABLES `tb_clientes` WRITE;
/*!40000 ALTER TABLE `tb_clientes` DISABLE KEYS */;
INSERT INTO `tb_clientes` VALUES (4,'Fernada ','00000000000','(00)00000-0000','00/00/0000','000.000.000-00');
/*!40000 ALTER TABLE `tb_clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_fornecedores`
--

DROP TABLE IF EXISTS `tb_fornecedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_fornecedores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `cnpj` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_fornecedores`
--

LOCK TABLES `tb_fornecedores` WRITE;
/*!40000 ALTER TABLE `tb_fornecedores` DISABLE KEYS */;
INSERT INTO `tb_fornecedores` VALUES (2,'TEST','TEST','(31)58227-5727','00.000.000/0000-00');
/*!40000 ALTER TABLE `tb_fornecedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_funcionario`
--

DROP TABLE IF EXISTS `tb_funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_funcionario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `cargo` varchar(50) NOT NULL,
  `dt_nascimento` varchar(10) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `telefone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `endereco` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_funcionario`
--

LOCK TABLES `tb_funcionario` WRITE;
/*!40000 ALTER TABLE `tb_funcionario` DISABLE KEYS */;
INSERT INTO `tb_funcionario` VALUES (1,'Ítalo Guilherme Alves Xavier','Diretor','15/09/2003','157.489.316-56','(31)97133-2110','italogax13@gmail.com','R. Mariza Rezende Vieria 552, Bela Vista III'),(2,'1','1','15/09/2003','1','1','1','1'),(4,'000000000000','000000000','00/00/0000','000.000.000-00','(00)00000-0000','000000000000','trwesddgtytrr3');
/*!40000 ALTER TABLE `tb_funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_produtos`
--

DROP TABLE IF EXISTS `tb_produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_produtos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(50) NOT NULL,
  `fornecedor` varchar(45) NOT NULL,
  `vl_compra` float NOT NULL,
  `vl_venda` float NOT NULL,
  `estoque` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_produtos`
--

LOCK TABLES `tb_produtos` WRITE;
/*!40000 ALTER TABLE `tb_produtos` DISABLE KEYS */;
INSERT INTO `tb_produtos` VALUES (1,'Calça Fem.','Fem.','TEST',9,120,887),(2,'Calça Masc.','Jeans ','TEST',80,160,988),(3,'Blusa Fem.','Fem.','TEST',40,80,795),(4,'Calça Jeans','Masc.','TEST',70,140,1000),(5,'Bermuda Jeans','Masc.','TEST',50,100,1000),(6,'Blusa algodão','Masc.','TEST',30,60,1000),(7,'Camisa social','Masc.','TEST',80,160,1000),(8,'Conjunto moleton','Masc.','TEST',120,240,800),(9,'Calça moleton','Masc.','TEST',60,120,1000);
/*!40000 ALTER TABLE `tb_produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_vendarotativa`
--

DROP TABLE IF EXISTS `tb_vendarotativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_vendarotativa` (
  `id` int NOT NULL,
  `produto` varchar(45) NOT NULL,
  `quantidade` int NOT NULL,
  `vl_unidade` varchar(45) NOT NULL,
  `vl_total` double NOT NULL,
  `id_pk` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_pk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_vendarotativa`
--

LOCK TABLES `tb_vendarotativa` WRITE;
/*!40000 ALTER TABLE `tb_vendarotativa` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_vendarotativa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_vendas`
--

DROP TABLE IF EXISTS `tb_vendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_vendas` (
  `codigo` int NOT NULL AUTO_INCREMENT,
  `pedido` varchar(5) DEFAULT NULL,
  `id` int DEFAULT NULL,
  `produto` varchar(50) DEFAULT NULL,
  `vl_unidade` varchar(50) DEFAULT NULL,
  `quantidade` varchar(50) DEFAULT NULL,
  `funcionario` varchar(50) DEFAULT NULL,
  `vl_total` float DEFAULT NULL,
  `forma_pagamento` varchar(50) DEFAULT NULL,
  `desconto` varchar(50) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=178 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_vendas`
--

LOCK TABLES `tb_vendas` WRITE;
/*!40000 ALTER TABLE `tb_vendas` DISABLE KEYS */;
INSERT INTO `tb_vendas` VALUES (1,NULL,1,'Calça Fem.','120.0','2',NULL,240,NULL,NULL,'2023-03-02','13:58:25'),(2,NULL,5,'Calça Fem.','120.0','4',NULL,480,NULL,NULL,'2023-03-02','13:58:25'),(4,'2vK7v',1,'Calça Fem.','120.0','3',NULL,360,NULL,NULL,'2023-03-02','14:30:07'),(5,'JKRsx',2,'Calça Masc.','160.0','4',NULL,640,NULL,NULL,'2023-03-02','14:31:03'),(6,'JKRsx',3,'Blusa Fem.','80.0','6',NULL,480,NULL,NULL,'2023-03-02','14:31:03'),(8,'Pp561',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','16:36:30'),(9,'I0zqS',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','16:39:13'),(10,'bajep',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','16:45:47'),(11,'4gyEa',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','16:51:40'),(12,'Ws4hM',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','16:55:33'),(13,'SoMuP',1,'Calça Fem.','120.0','10',NULL,1200,NULL,NULL,'2023-03-06','16:58:01'),(14,'JkrzS',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','17:01:02'),(15,'VMzRq',1,'Calça Fem.','120.0','10',NULL,1200,NULL,NULL,'2023-03-06','17:08:42'),(16,'VMzRq',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-06','17:08:42'),(17,'VMzRq',7,'Camisa social','160.0','2',NULL,320,NULL,NULL,'2023-03-06','17:08:42'),(18,'7dzCU',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','17:40:39'),(19,'7dzCU',2,'Calça Masc.','160.0','10',NULL,1600,NULL,NULL,'2023-03-06','17:40:39'),(20,'7dzCU',3,'Blusa Fem.','80.0','10',NULL,800,NULL,NULL,'2023-03-06','17:40:39'),(21,'WudPO',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','17:42:48'),(22,'WudPO',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-06','17:42:48'),(23,'WudPO',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-06','17:42:48'),(24,'p1GVz',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-06','17:46:20'),(25,'p1GVz',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-06','17:46:20'),(27,'AZl5S',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','17:50:32'),(28,'AZl5S',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-06','17:50:32'),(29,'AZl5S',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-06','17:50:32'),(30,'lbJYx',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','17:56:07'),(31,'lbJYx',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-06','17:56:07'),(32,'lbJYx',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-06','17:56:07'),(33,'8e02l',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-06','23:37:10'),(34,'8e02l',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-06','23:37:10'),(35,'8e02l',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-06','23:37:10'),(36,'qyPNu',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-07','16:25:55'),(37,'qyPNu',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-07','16:25:55'),(38,'qyPNu',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-07','16:25:55'),(39,'aeHdU',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-07','16:31:02'),(40,'aeHdU',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-07','16:31:02'),(42,'9Cc6b',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-07','16:34:53'),(43,'9Cc6b',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-07','16:34:53'),(44,'9Cc6b',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-07','16:34:53'),(45,'XRt7M',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-07','16:39:45'),(46,'XRt7M',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-07','16:39:45'),(47,'XRt7M',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-07','16:39:45'),(48,'GKWkC',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-07','17:03:49'),(49,'GKWkC',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-07','17:03:49'),(50,'GKWkC',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-07','17:03:49'),(51,'l0c1r',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-07','17:05:36'),(52,'l0c1r',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-07','17:05:36'),(53,'l0c1r',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-07','17:05:36'),(54,'iueKg',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-07','17:07:37'),(55,'iueKg',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-07','17:07:37'),(56,'iueKg',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-07','17:07:37'),(57,'AkbI0',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','14:51:42'),(58,'AkbI0',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','14:51:42'),(59,'AkbI0',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','14:51:42'),(60,'J7w7o',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:01:16'),(61,'J7w7o',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','15:01:16'),(62,'J7w7o',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','15:01:16'),(63,'HzSAu',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:04:36'),(64,'HzSAu',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','15:04:36'),(65,'HzSAu',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','15:04:36'),(66,'YP0pR',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:06:56'),(67,'YP0pR',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','15:06:56'),(68,'YP0pR',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','15:06:56'),(69,'lwCYr',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:14:40'),(70,'lwCYr',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','15:14:40'),(72,'PRjEk',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:17:06'),(73,'PRjEk',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','15:17:06'),(75,'pUt33',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:18:25'),(76,'pUt33',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','15:18:25'),(78,'MNWkI',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:39:16'),(79,'MNWkI',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','15:39:16'),(81,'RH13A',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:40:19'),(82,'RH13A',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','15:40:19'),(84,'1hQ33',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:41:36'),(85,'1hQ33',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','15:41:36'),(87,'tHokY',1,'Calça Fem.','120.0','2',NULL,240,NULL,NULL,'2023-03-08','15:42:30'),(88,'tHokY',2,'Calça Masc.','160.0','2',NULL,320,NULL,NULL,'2023-03-08','15:42:30'),(90,'vsWfU',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:52:06'),(91,'vsWfU',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:52:06'),(92,'vsWfU',5,'Bermuda Jeans','100.0','5',NULL,500,NULL,NULL,'2023-03-08','15:52:06'),(93,'ebRdc',1,'Calça Fem.','120.0','1',NULL,120,NULL,NULL,'2023-03-08','15:52:52'),(94,'ebRdc',2,'Calça Masc.','160.0','2',NULL,320,NULL,NULL,'2023-03-08','15:52:52'),(95,'ebRdc',3,'Blusa Fem.','80.0','1',NULL,80,NULL,NULL,'2023-03-08','15:52:52'),(96,'ZqEkP',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:57:32'),(97,'ZqEkP',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:57:32'),(98,'ZqEkP',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','15:57:32'),(99,'kLIIo',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:04:17'),(100,'kLIIo',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:04:17'),(101,'kLIIo',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','17:04:17'),(102,'fgn0x',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:05:39'),(103,'fgn0x',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:05:39'),(105,'Z3F9L',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:07:35'),(106,'Z3F9L',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:07:35'),(107,'Z3F9L',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','17:07:35'),(108,'SHk6m',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:07:35'),(109,'SHk6m',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:07:35'),(110,'SHk6m',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','17:07:35'),(111,'vhb1L',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:07:35'),(112,'vhb1L',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:07:35'),(113,'vhb1L',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','17:07:35'),(114,'DhaGT',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:07:35'),(115,'DhaGT',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:07:35'),(116,'DhaGT',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','17:07:35'),(117,'L8kOG',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:17:32'),(118,'L8kOG',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:17:32'),(120,'9hXlM',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:17:32'),(121,'tmdUO',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:18:16'),(122,'tmdUO',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:18:16'),(123,'tmdUO',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','17:18:16'),(124,'5Pc53',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:18:16'),(125,'5Pc53',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','17:18:16'),(127,'dUGnw',3,'Blusa Fem.','80.0','5',NULL,400,NULL,NULL,'2023-03-08','17:18:16'),(128,'JSZqb',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:20:35'),(129,'JSZqb',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:20:35'),(131,'QZfNo',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:20:35'),(132,'QZfNo',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:20:35'),(134,'uqTZD',1,'Calça Fem.','120.0','5',NULL,600,NULL,NULL,'2023-03-08','17:20:35'),(135,'uqTZD',2,'Calça Masc.','160.0','5',NULL,800,NULL,NULL,'2023-03-08','17:20:35'),(137,'QyU9U',1,'Calça Fem.','120.0','1',NULL,120,NULL,NULL,'2023-03-09','13:48:15'),(138,'QyU9U',1,'Calça Fem.','120.0','1',NULL,120,NULL,NULL,'2023-03-09','13:48:15'),(139,'QyU9U',8,'Conjunto moleton','240.0','10',NULL,2400,NULL,NULL,'2023-03-09','13:48:15'),(140,'G2e6e',1,'Calça Fem.','120.0','1',NULL,120,NULL,NULL,'2023-03-09','13:48:15'),(141,'G2e6e',1,'Calça Fem.','120.0','1',NULL,120,NULL,NULL,'2023-03-09','13:48:15'),(142,'G2e6e',8,'Conjunto moleton','240.0','10',NULL,2400,NULL,NULL,'2023-03-09','13:48:15'),(143,'1PqT5',1,'Calça Fem.','120.0','1',NULL,120,NULL,NULL,'2023-03-09','13:48:15'),(144,'1PqT5',1,'Calça Fem.','120.0','1',NULL,120,NULL,NULL,'2023-03-09','13:48:15'),(145,'1PqT5',8,'Conjunto moleton','240.0','10',NULL,2400,NULL,NULL,'2023-03-09','13:48:15'),(146,'1cOLu',1,'Calça Fem.','120.0','1',NULL,120,NULL,NULL,'2023-03-09','13:48:15'),(147,'1cOLu',1,'Calça Fem.','120.0','1',NULL,120,NULL,NULL,'2023-03-09','13:48:15'),(148,'1cOLu',8,'Conjunto moleton','240.0','10',NULL,2400,NULL,NULL,'2023-03-09','13:48:15'),(149,'CXfjL',1,'Calça Fem.','120.0','10',NULL,1200,NULL,NULL,'2023-03-09','13:48:59'),(150,'2jehP',1,'Calça Fem.','120.0','10',NULL,1200,NULL,NULL,'2023-03-09','13:48:59'),(151,'hP6OS',8,'Conjunto moleton','240.0','100',NULL,24000,NULL,NULL,'2023-03-09','13:49:16'),(152,'bity3',8,'Conjunto moleton','240.0','100',NULL,24000,NULL,NULL,'2023-03-09','13:49:16'),(153,'XtE3o',1,'Calça Fem.','120.0','5',NULL,600,'Debito',NULL,'2023-03-09','15:06:45'),(154,'7rHP8',1,'Calça Fem.','120.0','5',NULL,600,'Debito',NULL,'2023-03-09','15:06:45'),(155,'1NWon',1,'Calça Fem.','120.0','5',NULL,600,'Forma de Pagamento',NULL,'2023-03-09','15:10:12'),(156,'1NWon',2,'Calça Masc.','160.0','5',NULL,800,'Forma de Pagamento',NULL,'2023-03-09','15:10:12'),(158,'7hi1f',1,'Calça Fem.','120.0','5',NULL,600,'Forma de Pagamento',NULL,'2023-03-09','15:17:47'),(159,'Bjz3Z',1,'Calça Fem.','120.0','5',NULL,600,'Forma de Pagamento',NULL,'2023-03-09','15:17:47'),(160,'4piuJ',1,'Calça Fem.','120.0','1',NULL,120,'Debito',NULL,'2023-03-09','15:18:15'),(161,'SUhuP',1,'Calça Fem.','120.0','1',NULL,120,'Debito',NULL,'2023-03-09','15:18:15'),(162,'wAHDv',3,'Blusa Fem.','80.0','100',NULL,8000,'Forma de Pagamento',NULL,'2023-03-10','19:32:43'),(163,'jXK8o',3,'Blusa Fem.','80.0','100',NULL,8000,'Forma de Pagamento',NULL,'2023-03-10','19:32:43'),(164,'Y3BF1',1,'Calça Fem.','120.0','1',NULL,120,'Forma de Pagamento',NULL,'2023-03-19','23:38:13'),(165,'Y3BF1',2,'Calça Masc.','160.0','1',NULL,160,'Forma de Pagamento',NULL,'2023-03-19','23:38:13'),(167,'6d7uA',1,'Calça Fem.','120.0','1',NULL,120,'Forma de Pagamento',NULL,'2023-03-19','23:38:13'),(168,'6d7uA',2,'Calça Masc.','160.0','1',NULL,160,'Forma de Pagamento',NULL,'2023-03-19','23:38:13'),(170,'sn8ju',1,'Calça Fem.','120.0','1',NULL,120,'Forma de Pagamento',NULL,'2023-03-19','23:38:13'),(171,'sn8ju',2,'Calça Masc.','160.0','1',NULL,160,'Forma de Pagamento',NULL,'2023-03-19','23:38:13'),(172,'EWoAH',2,'Calça Masc.','160.0','1',NULL,160,'Forma de Pagamento',NULL,'2023-03-20','15:26:23'),(173,'2BDa5',2,'Calça Masc.','160.0','1',NULL,160,'Forma de Pagamento',NULL,'2023-03-20','15:26:23'),(174,'6aQzd',1,'Calça Fem.','120.0','1',NULL,120,'Forma de Pagamento',NULL,'2023-03-20','15:27:08'),(175,'xqdMp',1,'Calça Fem.','120.0','1',NULL,120,'Forma de Pagamento',NULL,'2023-03-20','15:27:08'),(176,'omeDy',1,'Calça Fem.','120.0','1',NULL,120,'Forma de Pagamento',NULL,'2023-03-22','16:10:07'),(177,'OyDjP',1,'Calça Fem.','120.0','1',NULL,120,'Forma de Pagamento',NULL,'2023-03-22','16:10:07');
/*!40000 ALTER TABLE `tb_vendas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'repono'
--

--
-- Dumping routines for database 'repono'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-29 15:21:33
