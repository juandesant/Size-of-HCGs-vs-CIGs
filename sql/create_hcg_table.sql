CREATE DATABASE `SIZES_HCG_VS_CIG` DEFAULT CHARACTER SET `utf8`;
USE SIZES_HCG_VS_CIG;
CREATE TABLE `HCG_LVM_2001` (
  `hcg_id` int(11) unsigned NOT NULL,
  `ra2000` float DEFAULT NULL COMMENT 'right ascension of the HCG centre in degrees',
  `dec2000` float DEFAULT NULL COMMENT 'declination of the HCG centre in degrees',
  `size` float DEFAULT NULL COMMENT 'group size in arcseconds',
  PRIMARY KEY (`hcg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
