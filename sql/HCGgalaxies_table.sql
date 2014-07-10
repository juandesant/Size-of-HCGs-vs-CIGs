-- phpMyAdmin SQL Dump
-- version 4.1.12deb0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 10, 2014 at 05:19 AM
-- Server version: 5.5.29-0ubuntu0.12.04.2
-- PHP Version: 5.3.10-1ubuntu3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `UNPUBLISHED_SIZES_HCG_VS_CIG`
--

-- --------------------------------------------------------

--
-- Initial table structure for table `HCGgalaxies`
--

CREATE TABLE IF NOT EXISTS `HCGgalaxies` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key',
  `ObjectName` varchar(16) NOT NULL COMMENT 'Object Name',
  `RA` varchar(16) NOT NULL COMMENT 'Right Ascension (hms)',
  `Dec` varchar(16) NOT NULL COMMENT 'Declination (dms)',
  `RA_deg` float NOT NULL COMMENT 'Right Ascension (degrees)',
  `Dec_deg` float NOT NULL COMMENT 'Declination (degrees)',
  `l_cz` varchar(3) DEFAULT NULL COMMENT 'lowerlimit on cz',
  `cz` int(11) DEFAULT NULL COMMENT 'Radial Velocity (km/s)',
  `z` float DEFAULT NULL COMMENT 'Redshift',
  `z_uncertainty` float DEFAULT NULL COMMENT 'Redshift uncertainty',
  `z_Qual` varchar(3) DEFAULT NULL,
  `ANG_SIZE_MAJ` float DEFAULT NULL COMMENT 'Major Diam (arcmin)',
  `ANG_SIZE_MIN` float DEFAULT NULL COMMENT 'Minor Diam (arcmin)',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ObjectName` (`ObjectName`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='Galaxies in HCGs where N > 3' AUTO_INCREMENT=339 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


-- Add column to include HCG group

ALTER TABLE `HCGgalaxies` ADD `groupNumber` INT NULL COMMENT 'Group number' AFTER `ObjectName`;


-- provide values for HCG group column

UPDATE HCGgalaxies SET groupNumber = replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(ObjectName, "HCG", ""), "a", ""), "b", ""), "c", ""), "d", ""), "e", ""), "f", ""), "g", ""), "h", ""), "q", ""), "LEDA", "") ;


-- test to see if all the groups have more than 3 galaxies.

SELECT groupNumber, count(*) as N,  FROM `HCGgalaxies` group by groupNumber



-- calculate baricenter and group velocity and velocity dispersion

SELECT
  groupNumber, count(*) as N, avg(RA_deg) as RA_deg, avg(Dec_deg) as Dec_deg, avg(cz) as cz
FROM
  `HCGgalaxies` group by groupNumber


-- calculate baricenter and group velocity and velocity dispersion

SELECT
  hcg.groupNumber, count(*) as N, avg(hcg.RA_deg) as RA_deg, avg(hcg.Dec_deg) as Dec_deg, avg(hcg.cz) as cz, stddev(hcg.cz)
FROM
  `HCGgalaxies` hcg group by hcg.groupNumber

