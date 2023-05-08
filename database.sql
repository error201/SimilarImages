DROP database if exists images_db;

CREATE TABLE IF NOT EXISTS `images_db`.`images` (
  `filepath` VARCHAR(255) NOT NULL,
  `filename` VARCHAR(45) NOT NULL,
  `format` VARCHAR(20) NOT NULL,
  `mode` VARCHAR(5) NOT NULL,
  `width` INT NOT NULL,
  `height` INT NOT NULL,
  `size` INT NOT NULL,
  `hash_000` VARCHAR(16) NOT NULL,
  `hash_090` VARCHAR(16) NOT NULL,
  `hash_180` VARCHAR(16) NOT NULL,
  `hash_270` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`filepath`),
  UNIQUE INDEX `filepath_UNIQUE` (`filepath` ASC) VISIBLE);
