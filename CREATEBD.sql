CREATE SCHEMA IF NOT EXISTS `ahorcado` DEFAULT CHARACTER SET utf8 ;
USE `ahorcado` ;
-- -----------------------------------------------------
-- Table `Ahorcado`.`Word`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Word` (
  `idWord` INT NOT NULL,
  `textWord` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idWord`)
)
ENGINE = InnoDB;