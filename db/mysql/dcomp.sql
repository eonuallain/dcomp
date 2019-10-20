SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `dcomp`;

USE dcomp;

CREATE TABLE IF NOT EXISTS `task_encryption` (
  `id` int(11) NOT NULL,
  `text_unencrytped` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `text_encrytped` text CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `processed` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `task_encryption`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_process` (`processed`);

ALTER TABLE `task_encryption`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
