-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema QueenFlossy
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `QueenFlossy` ;

-- -----------------------------------------------------
-- Schema QueenFlossy
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `QueenFlossy` DEFAULT CHARACTER SET utf8 ;
USE `QueenFlossy` ;

-- -----------------------------------------------------
-- Table `QueenFlossy`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `QueenFlossy`.`users` ;

CREATE TABLE IF NOT EXISTS `QueenFlossy`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(256) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `QueenFlossy`.`posts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `QueenFlossy`.`posts` ;

CREATE TABLE IF NOT EXISTS `QueenFlossy`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL,
  `posting` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `title` VARCHAR(255) NULL,
  `photo` LONGBLOB NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_post_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_post_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `QueenFlossy`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
