-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema spaceweb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema spaceweb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `spaceweb` DEFAULT CHARACTER SET utf8 ;
USE `spaceweb` ;

-- -----------------------------------------------------
-- Table `spaceweb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spaceweb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `kind_of_user` VARCHAR(45) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(255) NULL,
  `life` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spaceweb`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spaceweb`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `spaceweb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spaceweb`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spaceweb`.`likes` (
  `liker_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`liker_id`, `post_id`),
  INDEX `fk_users_has_posts_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_users_has_posts_users1_idx` (`liker_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_posts_users1`
    FOREIGN KEY (`liker_id`)
    REFERENCES `spaceweb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_posts_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `spaceweb`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spaceweb`.`favarites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spaceweb`.`favarites` (
  `user_favorite_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_favorite_id`, `post_id`),
  INDEX `fk_users_has_posts_posts2_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_users_has_posts_users2_idx` (`user_favorite_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_posts_users2`
    FOREIGN KEY (`user_favorite_id`)
    REFERENCES `spaceweb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_posts_posts2`
    FOREIGN KEY (`post_id`)
    REFERENCES `spaceweb`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spaceweb`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spaceweb`.`comments` (
  `user_id_comment` INT NOT NULL,
  `post_id_comment` INT NOT NULL,
  `content` TEXT NULL,
  `ceated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id_comment`, `post_id_comment`),
  INDEX `fk_users_has_posts1_posts1_idx` (`post_id_comment` ASC) VISIBLE,
  INDEX `fk_users_has_posts1_users1_idx` (`user_id_comment` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_posts1_users1`
    FOREIGN KEY (`user_id_comment`)
    REFERENCES `spaceweb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_posts1_posts1`
    FOREIGN KEY (`post_id_comment`)
    REFERENCES `spaceweb`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
