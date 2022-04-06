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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (1,'Renault','Paquito Fernandez','1997-03-05','Francia','Era un compa que agarró un HotWheels y lo hizo grandote y ya se hizo millonario'),(2,'Chevrolet','Pedrito Sanchez y Bumbblebee','2022-02-06','Paises Bajos','Se encontró un nopal e hizo esta wea'),(3,'Nissan','Juan Nissan','1986-11-25','Lesotho','Un pibe que vendía elote en vaso, descubrio que con las ruedas de su bici podia hacer un coche\n'),(5,'Toyota','Kiichiro Toyoda','1937-08-28','Japon','Toyota Motor Corporation es una empresa japonesa de fabricación de automóviles. Fundada en 1933 por Kiichiro Toyoda, su sede principal está ubicada en Toyota (Aichi) y Bunkyo (Tokio) aunque, por su carácter multinacional, cuenta con fábricas y sedes en varios países.'),(6,'Tesla','Elon Musk','2003-07-01','EEUU','Tesla (anteriormente, Tesla Motors, Inc.)​ es una empresa estadounidense con sede en Austin, Texas, y liderada por Elon Musk, que diseña, fabrica y vende automóviles eléctricos, componentes para la propulsión de vehículos eléctricos, techos solares, instalaciones solares fotovoltaicas y baterías domésticas'),(7,'Audi','August Horch','1909-07-16','Alemania','Audi es una empresa multinacional alemana fabricante de automóviles de alta gama y deportivos. Su sede central se encuentra en Ingolstadt, Baviera y forma parte desde 1965 del Grupo Volkswagen.\nAugust Horch (1868-1951), uno de los pioneros de la industria automovilística alemana, fundó en Colonia (Alemania) la empresa de autos Horch en 1899, cuyo primer automóvil comenzó a circular por vías públicas en 1901. Después de algunas dificultades financieras y desavenencias internas, decidió abandonar la compañía para crear una nueva fábrica de automóviles. Así nació la empresa automovilística llamada «August Horch & Cie. Motorwagenwerke AG» en Zwickau, el 16 de julio de 1909.2'),(8,'Volvo','	SKF, Assar Gabrielsson y Gustav Larson','1927-04-14','Suecia','Volvo Cars (en sueco: Volvo personvagnar) es una marca de automóviles sueca con sede en Gotemburgo, Suecia subsidiaria de la compañía automotriz china Geely.​ Fue originalmente fundada en 1927 por el ingeniero Gustav Larson y el economista Assar Gabrielsson, como una empresa subsidiaria de la fabricante de rodamientos SKF. A pesar de que se suele confundir con el conglomerado de propiedad sueca AB Volvo (fabricante de vehículos industriales, camiones, autobuses y equipamiento de construcción) las dos firmas han sido independientes desde que AB Volvo vendió Volvo Cars en 1999 a Ford Motor Company para ser parte del grupo llamado Premier Automotive Group.'),(9,'Cadillac','	Henry M. Leland\nHenry Ford','1902-01-20','EEUU','Cadillac es una marca de automóviles de lujo, fabricados y vendidos por la empresa estadounidense General Motors creada por William Murphy en 1902. El nombre fue tomado del fundador de la ciudad de Detroit, Míchigan, en 1701, el oficial del ejército francés, Antoine de la Mothe Cadillac. '),(10,'Fiat','	Gianni Agnelli','1899-07-11','Italia','Fiat Automobiles -siglas de Fabbrica Italiana Automobili Torino (en español: Fábrica Italiana de Automóviles de Turín) es una histórica marca italiana de automóviles, bajo la que se comercializan vehículos desde 1899, origen del mayor grupo industrial italiano, Fiat S.p.A., propiedad de Stellantis.'),(11,'Isuzu','Yoshisuke Aikawa','1916-06-16','Japon','Tal como lo hemos dicho, Isuzu nace en 1916, cuando la Tokyo Gas Co. decide crear una filial llamada Tokio Ishikawajima Engineering Co. Ltd para construir una planta e iniciar la producción de vehículos y 2 años más tarde, en 1918, se comienza la fabricación de vehículos bajo un acuerdo con la marca Wolseley Motors, que eran destinados para el mercado japonés. el primer modelo fue el automóvil Wolseley Motors A9 a partir del año 1922. en 1924, inicia la producción y el ensamblaje de camiones.');
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
  CONSTRAINT `car_ibfk_1` FOREIGN KEY (`Brand_id`) REFERENCES `brand` (`Id_brand`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `car_ibfk_2` FOREIGN KEY (`User_id`) REFERENCES `user` (`Id_User`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'UMX-585-X','Rojo','Ta medio feito',150000,1,1),(2,'9226 TKU','Azul','Raspon en la facia',50000,6,5),(3,'1173 OPL','Cafe','Lo estrelle',70000,5,1),(4,'7343 BTU','Rojo','Me abrieron el coche para robarme mi mandado y rompieron un espejo',120000,1,3),(5,'0230 NHH','Negro','No tiene luces frontales',12000,1,10),(6,'6062 IUV','Rojo','Me estampe en un poste',78000,8,11),(7,'3042 QLB','Blanco','Faltan los asientos traseros',80000,5,9),(8,'9283 PFQ','Verde','Totalmente bien',95000,9,8),(9,'7070 GXC','Blanco','Me robaron las placas',60000,10,2),(10,'6374 ZFN','Rojo','En excelentes condiciones',25000,7,3);
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
  CONSTRAINT `model_ibfk_1` FOREIGN KEY (`Brand_id`) REFERENCES `brand` (`Id_brand`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model`
--

LOCK TABLES `model` WRITE;
/*!40000 ALTER TABLE `model` DISABLE KEYS */;
INSERT INTO `model` VALUES (1,'Duster','Camioneta',4,5,50,'De la roja',2013,223000,100000,'Partes que no me sé',1),(2,'Dacia Duster','Todo terreno',4,5,50,'de la roja',2013,230000,100000,'El motor sigue siendo un F4R de 2.0 litros con 16 válvulas, 133 caballos de potencia y un torque 192. En versiones manual y automática. Sus rines son de 16 pulgadas en acero y aluminio, dependiendo de la versión',1),(3,'Chevy','De turismo',2,4,40,'de la verde',2008,12000,40000,' se introdujo un nuevo frente más ancho, y se destaca el ya ofrecer transmisión automática y motor 1.6 TBI.',2),(4,'Patrol','Todo terreno',4,5,50,'de la roja',2020,230000,100000,'motor re chido de 120 caballos de fuerza',3),(5,'Versa','De turismo',4,4,45,'Magna',2022,230000,100000,'combustible de 5 L / 100 km (56 mpg -imp ; 47 mpg -US ), y tiene un manual de cinco velocidades o una variable continua transmisión (CVT).',3),(6,'Ducato','Comecial ligero',4,5,40,'Premium',2020,200000,123000,'Los motores son de gasolina del Peugeot 504, mientras que el diésel es del Citroën CX diésel. Ambas unidades están acoplados a una caja de cambios Citroën. El J5 remplazó a la furgoneta Peugeot J7 de 1400 kg de carga útil. El Talbot Express era la versión del Peugeot vendido por Talbot para el mercado británico. ',10),(7,'A3','De turismo',4,4,50,'Magna',2021,230000,100000,'1.8T quattro usaba el motor de 150 CV (110 kW) y 180 CV y el mismo sistema basado en el embrague Haldex como el de la primera generación del Audi TT. ',7),(8,'XT4','SUV',4,5,55,'Premium',2018,230000,100000,'El motor de XT4 es de la misma cilindrada que la mayoría de sus —2.0 litros— rivales asistido con turbo, sin embargo, es más lento para acelerar de 0 a 100 km/h.',9),(9,'XC40','Todo terreno',4,5,50,'premium',2013,230000,100000,' batería de 78 kWh le proporciona una autonomía de unos 400 km según WLTP o 335 km según la homologación EPA.1​La batería pesa unos 500 kg. La garantía de Volvo para la batería es de 8 años o 160.000 km, lo que ocurra primero.2​',8);
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,'2022-03-26',5,'Estuvo bien chido el motor de esta wea',1),(2,'2022-04-06',5,'Texto de ejemplo',1),(3,'2022-04-06',4,'Publicacion generica',2),(4,'2022-04-06',2,'Texto de ejemplo',2),(5,'2022-04-06',6,'Publicacion generica',5),(6,'2022-04-06',8,'Texto de ejemplo',6),(7,'2022-04-06',9,'Texto de ejemplo',9),(8,'2022-04-06',1,'Publicacion generica',10),(9,'2022-04-06',7,'Texto de ejemplo',11),(10,'2022-04-06',3,'Publicacion generica',9),(11,'2022-04-06',2,'Texto de ejemplo',6);
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `section`
--

LOCK TABLES `section` WRITE;
/*!40000 ALTER TABLE `section` DISABLE KEYS */;
INSERT INTO `section` VALUES (1,'2022-03-25','Motor',1),(2,'2022-04-06','Motor',2),(3,'2022-04-06','Estetica',1),(4,'2022-04-06','General',1),(5,'2022-04-06','Motor',1),(6,'2022-04-06','Frenos',5),(7,'2022-04-06','Suspension',6),(8,'2022-04-06','General',9),(9,'2022-04-06','Aceleracion',8),(10,'2022-04-06','Performance',8),(11,'2022-04-06','Frenos',6);
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Uriel','Duana Chavez','abc12345','uriel@gmail.com','M'),(2,'Gustavo Angel','Montoya Martinez','sdas1855!d','gusm@gmail.com','M'),(3,'Ulises','Florean Guzman','sger748427','ulisesF@gmail.com','M'),(5,'Carlos','Hernandez','abc123','carlosh@gmail.com','M'),(6,'Ernesto','Perez Martinez','asxc25440','ernestin@gmail.com','M'),(7,'Estela','Gutierrez Pereida','dasvc4155','estelin@gmail.com','F'),(8,'Marcela','Chavez Ramirez','jhbnn8825cr','marcela@gmail.com','F'),(9,'Juan Carlos','Ramirez Gutierrez','jankarra0525','jankarlos@gmail.com','M'),(10,'Perengano','Lopez Gonzalez','pereng8985','pereng@gmail.com','M');
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

-- Dump completed on 2022-04-06 11:11:37
