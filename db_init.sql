-- DB 기본 설정
CREATE DATABASE IF NOT EXISTS jt
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_0900_ai_ci;
USE translate_app;

-- 사용자
CREATE TABLE users (
  id             BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  email          VARCHAR(255) NOT NULL,
  password_hash  VARCHAR(255) NOT NULL, 
  created_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 단문 번역 로그 (convert 버튼 한 번 = 한 행)
CREATE TABLE translations (
  id                BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  user_id           BIGINT UNSIGNED NOT NULL,           -- 누가 요청했는지
  source_text       MEDIUMTEXT NOT NULL,
  translated_text   MEDIUMTEXT NULL,                    -- 실패 시 NULL 가능
  tokens_prompt     INT UNSIGNED NULL,
  created_at        DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_translations_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE,

  INDEX ix_trans_user_created (user_id, created_at),
  FULLTEXT KEY ft_source_text (source_text)             -- 원문 검색 필요하면 유용
) ENGINE=InnoDB;
