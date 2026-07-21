-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema db_gestao_residuos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_gestao_residuos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_gestao_residuos` ;
USE `db_gestao_residuos` ;

-- -----------------------------------------------------
-- Table `db_gestao_residuos`.`tb_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_gestao_residuos`.`tb_cliente` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `nome_empresa` VARCHAR(100) NOT NULL,
  `endereco` VARCHAR(150) NULL,
  `email` VARCHAR(100) NULL,
  `telefone` VARCHAR(20) NULL,
  `cnpj` CHAR(14) NOT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_gestao_residuos`.`tb_tipo_residuo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_gestao_residuos`.`tb_tipo_residuo` (
  `id_tipo_residuo` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(50) NOT NULL,
  `descricao` VARCHAR(150) NULL,
  PRIMARY KEY (`id_tipo_residuo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_gestao_residuos`.`tb_solicitacao_coleta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_gestao_residuos`.`tb_solicitacao_coleta` (
  `id_solicitacao` INT NOT NULL AUTO_INCREMENT,
  `data_solicitacao` DATE NOT NULL,
  `peso_estimado` DECIMAL(10,2) NOT NULL,
  `status` VARCHAR(20) NULL,
  `observacao` VARCHAR(150) NULL,
  `data_importacao` DATETIME NULL,
  `tb_cliente_id_cliente` INT NOT NULL,
  `tb_tipo_residuo_id_tipo_residuo` INT NOT NULL,
  PRIMARY KEY (`id_solicitacao`),
  INDEX `fk_tb_solicitacao_coleta_tb_cliente_idx` (`tb_cliente_id_cliente` ASC) VISIBLE,
  INDEX `fk_tb_solicitacao_coleta_tb_tipo_residuo1_idx` (`tb_tipo_residuo_id_tipo_residuo` ASC) VISIBLE,
  CONSTRAINT `fk_tb_solicitacao_coleta_tb_cliente`
    FOREIGN KEY (`tb_cliente_id_cliente`)
    REFERENCES `db_gestao_residuos`.`tb_cliente` (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tb_solicitacao_coleta_tb_tipo_residuo1`
    FOREIGN KEY (`tb_tipo_residuo_id_tipo_residuo`)
    REFERENCES `db_gestao_residuos`.`tb_tipo_residuo` (`id_tipo_residuo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_gestao_residuos`.`tb_log_processamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_gestao_residuos`.`tb_log_processamento` (
  `id_log` INT NOT NULL AUTO_INCREMENT,
  `nome_arquivo` VARCHAR(100) NULL,
  `data_hora_inicio` DATETIME NULL,
  `data_hora_fim` DATETIME NULL,
  `registros_lidos` INT NULL,
  `registros_importados` INT NULL,
  `registros_invalidos` INT NULL,
  `status_execucao` VARCHAR(20) NULL,
  PRIMARY KEY (`id_log`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
