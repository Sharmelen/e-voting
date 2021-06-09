-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.25-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win32
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for e_vote
CREATE DATABASE IF NOT EXISTS `e_vote` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `e_vote`;

-- Dumping structure for table e_vote.admin_cred
CREATE TABLE IF NOT EXISTS `admin_cred` (
  `pub_key` varchar(100) DEFAULT NULL,
  `priv_hash_key` varchar(100) DEFAULT NULL,
  `priv_key` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table e_vote.admin_cred: ~1 rows (approximately)
/*!40000 ALTER TABLE `admin_cred` DISABLE KEYS */;
INSERT INTO `admin_cred` (`pub_key`, `priv_hash_key`, `priv_key`) VALUES
	('fa56e8d029fafe8a2d94195ecef9a89fa6757e83bb5b315fab89cbee524b5ace', '847396db3805269a2257bafadee39d1b5167794b0c9d1e542d1d1a924589a7b0', 'fa56e8d029fafe8a2d94195ecef9a89fa6757e83bb5b315fab89cbee524b5ace');
/*!40000 ALTER TABLE `admin_cred` ENABLE KEYS */;

-- Dumping structure for table e_vote.faculty_seat
CREATE TABLE IF NOT EXISTS `faculty_seat` (
  `name` varchar(50) DEFAULT NULL,
  `mt_no` varchar(50) DEFAULT NULL,
  `faculty` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table e_vote.faculty_seat: ~40 rows (approximately)
/*!40000 ALTER TABLE `faculty_seat` DISABLE KEYS */;
INSERT INTO `faculty_seat` (`name`, `mt_no`, `faculty`) VALUES
	('STUDENT_0', '10000', 'FSTP'),
	('STUDENT_1', '10001', 'FSTP'),
	('STUDENT_2', '10002', 'FSTP'),
	('STUDENT_3', '10003', 'FSTP'),
	('STUDENT_4', '10004', 'FSTP'),
	('STUDENT_5', '10005', 'FSTP'),
	('STUDENT_6', '10006', 'FSTP'),
	('STUDENT_7', '10007', 'FSTP'),
	('STUDENT_8', '10008', 'FKJ'),
	('STUDENT_9', '10009', 'FKJ'),
	('STUDENT_10', '10010', 'FKJ'),
	('STUDENT_11', '10011', 'FKJ'),
	('STUDENT_12', '10012', 'FKJ'),
	('STUDENT_13', '10013', 'FKJ'),
	('STUDENT_14', '10014', 'FKJ'),
	('STUDENT_15', '10015', 'FKJ'),
	('STUDENT_16', '10016', 'FPPP'),
	('STUDENT_17', '10017', 'FPPP'),
	('STUDENT_18', '10018', 'FPPP'),
	('STUDENT_19', '10019', 'FPPP'),
	('STUDENT_20', '10020', 'FPPP'),
	('STUDENT_21', '10021', 'FPPP'),
	('STUDENT_22', '10022', 'FPPP'),
	('STUDENT_23', '10023', 'FPPP'),
	('STUDENT_24', '10024', 'FPKP'),
	('STUDENT_25', '10025', 'FPKP'),
	('STUDENT_26', '10026', 'FPKP'),
	('STUDENT_27', '10027', 'FPKP'),
	('STUDENT_28', '10028', 'FPKP'),
	('STUDENT_29', '10029', 'FPKP'),
	('STUDENT_30', '10030', 'FPKP'),
	('STUDENT_31', '10031', 'FPKP'),
	('STUDENT_32', '10032', 'PB'),
	('STUDENT_33', '10033', 'PB'),
	('STUDENT_34', '10034', 'PB'),
	('STUDENT_35', '10035', 'PB'),
	('STUDENT_36', '10036', 'PB'),
	('STUDENT_37', '10037', 'PB'),
	('STUDENT_38', '10038', 'PB'),
	('STUDENT_39', '10039', 'PB');
/*!40000 ALTER TABLE `faculty_seat` ENABLE KEYS */;

-- Dumping structure for table e_vote.key_table
CREATE TABLE IF NOT EXISTS `key_table` (
  `pub_key` varchar(100) DEFAULT NULL,
  `priv_key_hash` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `priv_key` varchar(100) DEFAULT NULL,
  `faculty` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table e_vote.key_table: ~45 rows (approximately)
/*!40000 ALTER TABLE `key_table` DISABLE KEYS */;
INSERT INTO `key_table` (`pub_key`, `priv_key_hash`, `status`, `priv_key`, `faculty`) VALUES
	('91074cbb6a7f814cf6a05ba2bc17399b09f5f3243b1c2dd02f9b7096e6abcbfc', 'c2faa4fe17d76b0de5a6f35a1b0c17e53b93de1aebcb629da12966f18db00716', 'voted', '91074cbb6a7f814cf6a05ba2bc17399b09f5f3243b1c2dd02f9b7096e6abcbfc', 'FSTP'),
	('457bbe33f967f582cf544254a3db300aa1535b43218c4bb8a5e5048aaf39c116', 'bd58e8e613780857d9106e9d7fea94f3f3f3d74ae89009c4886945b34c156120', 'not voted', '457bbe33f967f582cf544254a3db300aa1535b43218c4bb8a5e5048aaf39c116', 'FSTP'),
	('4d1df986f9902df32c41413ac33ad76243481866573d4e103659484dcc6963b0', '634c268206e30c0d80892cdbfb5c5fdef8b601ada641f7a8a90ea6ae623441b8', 'not voted', '4d1df986f9902df32c41413ac33ad76243481866573d4e103659484dcc6963b0', 'FSTP'),
	('04231efc6ba3ed8f9eef85bd389033fe885553f461696baf0fd2812e92e6f2af', '65147ccd62e355041878a74847b26ec6e86df201c3f81f3f3df488ea3252cf6f', 'not voted', '04231efc6ba3ed8f9eef85bd389033fe885553f461696baf0fd2812e92e6f2af', 'FSTP'),
	('f03b51a751d5a4b5b6e2cce5735db52fa02259bb7fe696e51afe36dd67530ec0', '9ef601874cd34a5224def32ac456d9cc094c12c2adbb9f89e83d1edb88ae2fc1', 'not voted', 'f03b51a751d5a4b5b6e2cce5735db52fa02259bb7fe696e51afe36dd67530ec0', 'FSTP'),
	('99314e5aa44b6e1adaf1f33ab5a180526b522e3d60f99b6c8950d71e51c903ec', '69aa4ba016aba1bd110d0a783539af4676794a5040a9a246cf5c2cd28cc85a9f', 'not voted', '99314e5aa44b6e1adaf1f33ab5a180526b522e3d60f99b6c8950d71e51c903ec', 'FSTP'),
	('0c90a2cb7edb2fa6384784a96208c8826f58e3ac13f0c5eb64e59d2746e81f6d', '3c8cbcf9209f76e88cd83213cd4ec659a173b9b8669af0d8e90056254e182e7c', 'not voted', '0c90a2cb7edb2fa6384784a96208c8826f58e3ac13f0c5eb64e59d2746e81f6d', 'FSTP'),
	('bc89d1730ca0bd15f76bffacafc5adab0fce55e35d71ede8a3100560fde146f0', 'bb0550914f831da6fa1833bd1cd21d5ce9b2ab90d0a48a4a07439eab043d09b9', 'not voted', 'bc89d1730ca0bd15f76bffacafc5adab0fce55e35d71ede8a3100560fde146f0', 'FSTP'),
	('5290bba4a113dd0117252e3a59c7eb95dcc42a1d35b7e63a0a67c5d6b9578303', 'e63b6367a00f68065c5f6721580a2fa9875d013530c37475a6b46561641270ec', 'not voted', '5290bba4a113dd0117252e3a59c7eb95dcc42a1d35b7e63a0a67c5d6b9578303', 'FSTP'),
	('6d3bdcbac5d726b3b992d5e4be06c362e826e37e46ff62b351af897469156689', '35ec2f576b529aadecd9319010460f43fa11d746f4d2d32ce1ae8b62ac462d98', 'not voted', '6d3bdcbac5d726b3b992d5e4be06c362e826e37e46ff62b351af897469156689', 'FPPP'),
	('6dcdf63b2bf90458656faee31bb364ed02c10c73ed1ac2bb99c39e95d82aea31', 'dc272ac25176ee80923966101083f6a8b18e53ebb2990ed466822e77592918c2', 'not voted', '6dcdf63b2bf90458656faee31bb364ed02c10c73ed1ac2bb99c39e95d82aea31', 'FPPP'),
	('b6c73b7a997ab7b075fe47f2267eb75b94fec8d71aeed179bf6df843915fffd6', '608d0476a9c247bb52fcd85ac5acce5bbd30648769d30f653a00fa9e33d596fb', 'not voted', 'b6c73b7a997ab7b075fe47f2267eb75b94fec8d71aeed179bf6df843915fffd6', 'FPPP'),
	('f7d497638086a7daca8dbc4b047f050ff2dc6f7c70cbda12fe15997122f52bfa', '8fe8e4a5738d03181d0b059f88b15b0945db2d387a73f683696d532b2ac2e427', 'not voted', 'f7d497638086a7daca8dbc4b047f050ff2dc6f7c70cbda12fe15997122f52bfa', 'FPPP'),
	('1e50b6d3820de6c154b5d8d46fd566487bceb5cac71404312a19907fe6bade83', 'eed24050868ba988289c4fc95c7de92adf9a2141c872b802a37db036f0ffd80b', 'not voted', '1e50b6d3820de6c154b5d8d46fd566487bceb5cac71404312a19907fe6bade83', 'FPPP'),
	('7a3ee8f2e55a0ab0860653a3259a6d7ac0ada519ba5eb67c8a797881699dbb3f', '1325929cfd4df91480dba6b3259a399c3013e5e6df1b3a8af4e50fbad236c031', 'not voted', '7a3ee8f2e55a0ab0860653a3259a6d7ac0ada519ba5eb67c8a797881699dbb3f', 'FPPP'),
	('72f6d6a016f817b1c2ba1fd2e3a5f431a53a66b02dcaa7b1ec41aa117acd6dea', 'd428511aeeb5063fe8a28c7318be5744ed136531b73499a3c1c6db27ff05c324', 'not voted', '72f6d6a016f817b1c2ba1fd2e3a5f431a53a66b02dcaa7b1ec41aa117acd6dea', 'FPPP'),
	('7415f2b06e4e01f08deaf1fdc6e51e5bcfa01e3d1c32b915e726482fb91239d2', '31a7bb88579bdf496853c2b41ba0a62fc6e5106fed0d45fc2e8b261574ddd680', 'not voted', '7415f2b06e4e01f08deaf1fdc6e51e5bcfa01e3d1c32b915e726482fb91239d2', 'FPPP'),
	('619d0078d872557cdd9f2f417fe97bae2709402bae6bf685749f7a4cf70afc8d', '8063d758cc43abeea9afe10cdecd0b9765c27c838d73c24a573ffd42d55c6e71', 'not voted', '619d0078d872557cdd9f2f417fe97bae2709402bae6bf685749f7a4cf70afc8d', 'FPPP'),
	('52ee65e64b9785de2255741e5550d96a652f7671e569d2f91b67d946ac2d1193', '488eee655d5b6a9b19cfa49717e85aedd1f416b5af978aacdafb46d104e41a3f', 'not voted', '52ee65e64b9785de2255741e5550d96a652f7671e569d2f91b67d946ac2d1193', 'PB'),
	('3fca2947d95927edb08ab581456d71f984fd9c4a937bdd5ca6ec8bf9a4febf83', '29a2a84edd4ec3d43c7d6603b9338bc8eb4cd143d3bc3793715d6bafb379d0ce', 'not voted', '3fca2947d95927edb08ab581456d71f984fd9c4a937bdd5ca6ec8bf9a4febf83', 'PB'),
	('99bb641e0a3cdda37d41a25539ac914004640a74c4802b2c6195f2a13e4039fe', '7c5cc151ff231dbad8ff84b55d6e9926abf9cc543580f85f66407766f5d14edc', 'not voted', '99bb641e0a3cdda37d41a25539ac914004640a74c4802b2c6195f2a13e4039fe', 'PB'),
	('68b981d8a07a892faef258a61458726e64d97085be2809eba6128551afdfae1e', 'ae5381792d66e7495b355d0569d3fc450f9b428eaae954e842000f6a63c48c53', 'not voted', '68b981d8a07a892faef258a61458726e64d97085be2809eba6128551afdfae1e', 'PB'),
	('4013af6e4c1fb5dab016d231b8e5ab96a9aba69c4d10885c204cb308f51fa98b', '03526517334070ff48474b5439d79776f44ffc88bf5a3b147148dd36b43c7dc2', 'not voted', '4013af6e4c1fb5dab016d231b8e5ab96a9aba69c4d10885c204cb308f51fa98b', 'PB'),
	('5970f298259844e4330338822f1bd64ece295897198721497dcec3dc9f3deaef', '92a69fbe468917ba34a17c5a5c4958b436680ec5a457cf30a6ac9a8c8361f7c5', 'not voted', '5970f298259844e4330338822f1bd64ece295897198721497dcec3dc9f3deaef', 'PB'),
	('85e7720035c817f1a449b3febd9d8745992a21ae14ff2d48dc16168d348f0666', 'ef2c0f03ca67ee09ad50074fc4320ebe9ecd8558d40dd8dc1290055ac443228b', 'not voted', '85e7720035c817f1a449b3febd9d8745992a21ae14ff2d48dc16168d348f0666', 'PB'),
	('ed97260c34863dac1ea9c5fcb896e2277391ec2605bb978aceda3dbdd71bf496', '88d66a82c85139477ea02f5ccf9586fac425f0e461e7ec9485fc98495617229d', 'not voted', 'ed97260c34863dac1ea9c5fcb896e2277391ec2605bb978aceda3dbdd71bf496', 'PB'),
	('9eba2cec6fd0acc8504388bd9eb9c8679707ca8291326ab036dcdddf0ffb4507', 'dd2df1eb3dfc3ed42fddb72a399862a3f1beb9b5608bab30093e9f54f2c52687', 'not voted', '9eba2cec6fd0acc8504388bd9eb9c8679707ca8291326ab036dcdddf0ffb4507', 'PB'),
	('ef88d0e326af976d966988d2c6e3029c252e694ab353440bcc699f97f8bb333a', '0d4376fc3271540343bc4187e396eca5d61c93a107f7bc199d6959afbafdc04f', 'not voted', 'ef88d0e326af976d966988d2c6e3029c252e694ab353440bcc699f97f8bb333a', 'FKJ'),
	('bb8f0a6ad9f228ce7ad17665e16e252ba17d7da9e43356952737d83856a142b5', 'c85588c41992aad48211fd8f457258461707e4dcdd7c994d795f99a85d2d3ed3', 'not voted', 'bb8f0a6ad9f228ce7ad17665e16e252ba17d7da9e43356952737d83856a142b5', 'FKJ'),
	('a1a11e24171dbe6daca9aec1bd66850daf36f52c654da04e504e920be15242e3', 'd1229b7b82337e1aeaac630d99ee1eb46ef5f292ccc9a3fb8fa4cb23c44dce01', 'not voted', 'a1a11e24171dbe6daca9aec1bd66850daf36f52c654da04e504e920be15242e3', 'FKJ'),
	('20471d1d117fc74648fb6197411c2d143d4013f0b2cf65da950e897f3f6984df', '3251c60756c217715a5df5208594ac640b5d53692d66fcb8999a1d96752dfad8', 'not voted', '20471d1d117fc74648fb6197411c2d143d4013f0b2cf65da950e897f3f6984df', 'FKJ'),
	('8dddcd184b711b3e8c15ccecf6f48d1203309e20f38965fb0dc1c4059794b7cf', 'd97b678e8bd13950e961f84a3513c6ceee45119d3abeb086c404fb4e45cc2cbe', 'not voted', '8dddcd184b711b3e8c15ccecf6f48d1203309e20f38965fb0dc1c4059794b7cf', 'FKJ'),
	('62d16b3a268ddcb5eaf0a4023492c1bbf549c86314657a877678d4f2e1b01f5d', '58316d58b1e42146c52ba77f24f23d41c4191d42d33261f91c4953287a2f5974', 'not voted', '62d16b3a268ddcb5eaf0a4023492c1bbf549c86314657a877678d4f2e1b01f5d', 'FKJ'),
	('c6c58b8a744f15fdb0edf6196f06e6050f15eb8433c7c70de42e541c42369c22', 'ea7254a6eb612df7da0139f2da18f9b44b59180587e95b70555dddd5a8945060', 'not voted', 'c6c58b8a744f15fdb0edf6196f06e6050f15eb8433c7c70de42e541c42369c22', 'FKJ'),
	('bc4b11cdad6f5eceb3b9a7a8ef9269d19835f938a645fadeefcd7b4d86931f96', '69d38120a21434688d2c5687e6b691ca30d96144d9179b2904f9952e6672b913', 'not voted', 'bc4b11cdad6f5eceb3b9a7a8ef9269d19835f938a645fadeefcd7b4d86931f96', 'FKJ'),
	('9aedb41a09285cbddc3b7baa79a91864fc691b9edb0009f71e59487c09ef7851', 'bbc19bcccb4c73661006ef012067b696cb52e5abf7bcdd8460f1721f9ad4f7da', 'not voted', '9aedb41a09285cbddc3b7baa79a91864fc691b9edb0009f71e59487c09ef7851', 'FKJ'),
	('c1f46ff38b6ba599a628649677c63b2d62b770b268683bbc59756522095543ca', 'b2e6c78a60b03a85671f15c0b5eee20f0ab06057c9e65b7fe39b50b62c7e1ab2', 'not voted', 'c1f46ff38b6ba599a628649677c63b2d62b770b268683bbc59756522095543ca', 'FPKP'),
	('435c44922a6864e6eb8afc0ecd382447371953ef28ef0fda756d9a332a1ec210', '0f06821872222ef32aa43a92573d1e70757247793f8c8e9cb11482b8cdf4cd36', 'not voted', '435c44922a6864e6eb8afc0ecd382447371953ef28ef0fda756d9a332a1ec210', 'FPKP'),
	('063adec57b9bffda9ba531da3f505679711b3d9d4d3d4a9f835c5a7769146bb0', 'e080d5664b5127b6475ba4b69236a4c1c7306fd6e1cac237924b1a5eb96d6979', 'not voted', '063adec57b9bffda9ba531da3f505679711b3d9d4d3d4a9f835c5a7769146bb0', 'FPKP'),
	('e5097266d446fdc49540a6c0153e040ac6663ca114ebab444c9f3a52a744d9b7', 'eff38a81e8292f03c2da1b9f1f88220b3f00f5caf2b57aae37a38a64071b01ff', 'not voted', 'e5097266d446fdc49540a6c0153e040ac6663ca114ebab444c9f3a52a744d9b7', 'FPKP'),
	('581601cd4b159044c017a88284963bf0782330e02f2181ae9daac1e8b757d873', 'c3d14f429b4a5c6b16db09899d24883d1d49f8c1cee02a1216b324d150143ab0', 'not voted', '581601cd4b159044c017a88284963bf0782330e02f2181ae9daac1e8b757d873', 'FPKP'),
	('20d4a9d80a91024945df72fe9e2b41cf3fa91e967774c37623dceb1cd59819a2', '043ed3111a2edd1fd08c2fffea2e69629c44e0140a3dea4c48dd7c39d025a77a', 'not voted', '20d4a9d80a91024945df72fe9e2b41cf3fa91e967774c37623dceb1cd59819a2', 'FPKP'),
	('1c0648e993a79475db7ebbe2b83c01c82f63d8e31a2677c625a8e3b7cbdf6d96', 'd4180073acb30759700a4a62a0d32db23abdea7169c67df200165eee71f7cbb3', 'not voted', '1c0648e993a79475db7ebbe2b83c01c82f63d8e31a2677c625a8e3b7cbdf6d96', 'FPKP'),
	('d8c155c481a336b4e09fb808ccb046b9acb25606bc55b19fa74c751fef92b23e', '370d29f189532fb1584b3d72117422c59cd6b3ddf1e64706fc9d0367b280f18c', 'not voted', 'd8c155c481a336b4e09fb808ccb046b9acb25606bc55b19fa74c751fef92b23e', 'FPKP'),
	('a9f6ef3d7607bcbe945f1254d6b40d6d07b13930512b38c2207cce5e3eff0739', '38afbb41dadb9fd59cd96a8f49b6d328b3148d1fd32eb73d44a0be701fff6f01', 'not voted', 'a9f6ef3d7607bcbe945f1254d6b40d6d07b13930512b38c2207cce5e3eff0739', 'FPKP');
/*!40000 ALTER TABLE `key_table` ENABLE KEYS */;

-- Dumping structure for table e_vote.public_seat
CREATE TABLE IF NOT EXISTS `public_seat` (
  `name` varchar(50) DEFAULT NULL,
  `mt_no` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table e_vote.public_seat: ~12 rows (approximately)
/*!40000 ALTER TABLE `public_seat` DISABLE KEYS */;
INSERT INTO `public_seat` (`name`, `mt_no`) VALUES
	('MOHD SYAZAWAN', '2160678'),
	('MOHD ALI', '2160679'),
	('SHARMELEN', '2160680'),
	('ANISA', '2160681'),
	('AIN', '2160682'),
	('ONG CHIN SEN', '2160682'),
	('WALIUIDIN', '2160683'),
	('RASHVEENA KAUR ', '2160684'),
	('ANITA', '2160685'),
	('MOHD BAKAR', '2160686'),
	('PALVINJIT DALIWAL', '2160687'),
	('ALIA', '2160688');
/*!40000 ALTER TABLE `public_seat` ENABLE KEYS */;

-- Dumping structure for table e_vote.public_seat_vote
CREATE TABLE IF NOT EXISTS `public_seat_vote` (
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table e_vote.public_seat_vote: ~56 rows (approximately)
/*!40000 ALTER TABLE `public_seat_vote` DISABLE KEYS */;
INSERT INTO `public_seat_vote` (`name`) VALUES
	('MOHD ALI'),
	('ANISA'),
	('ONG CHIN SEN'),
	('MOHD ALI'),
	('MOHD ALI'),
	('ANISA'),
	('ONG CHIN SEN'),
	('RASHVEENA KAUR '),
	('MOHD BAKAR'),
	('ALIA'),
	('MOHD ALI'),
	('ANISA'),
	('ONG CHIN SEN'),
	('RASHVEENA KAUR '),
	('MOHD ALI'),
	('ANISA'),
	('ONG CHIN SEN'),
	('RASHVEENA KAUR '),
	('MOHD BAKAR'),
	('ALIA'),
	('MOHD ALI'),
	('ANISA'),
	('ONG CHIN SEN'),
	('RASHVEENA KAUR '),
	('MOHD BAKAR'),
	('ALIA'),
	('MOHD ALI'),
	('ANISA'),
	('ONG CHIN SEN'),
	('RASHVEENA KAUR '),
	('MOHD BAKAR'),
	('ALIA'),
	('MOHD ALI'),
	('ANISA'),
	('ONG CHIN SEN'),
	('RASHVEENA KAUR '),
	('MOHD BAKAR'),
	('ALIA'),
	('MOHD ALI'),
	('ANISA'),
	('ONG CHIN SEN'),
	('RASHVEENA KAUR '),
	('MOHD BAKAR'),
	('ALIA'),
	('MOHD ALI'),
	('ANISA'),
	('ONG CHIN SEN'),
	('RASHVEENA KAUR '),
	('MOHD BAKAR'),
	('ALIA'),
	('STUDENT_1'),
	('STUDENT_3'),
	('STUDENT_5'),
	('STUDENT_7'),
	('STUDENT_6'),
	('STUDENT_4');
/*!40000 ALTER TABLE `public_seat_vote` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
