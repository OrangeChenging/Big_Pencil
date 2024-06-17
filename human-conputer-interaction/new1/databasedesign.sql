

ALTER SESSION SET CONSTRAINTS = DEFERRED;

-- ----------------------------
-- Table structure for achievements
-- ----------------------------
DROP TABLE achievements;
CREATE TABLE achievements (
  achievements_code         varchar(20) NOT NULL,
  achievements_name         varchar(20) NOT NULL,
  achievements_sort         varchar(20) DEFAULT NULL,
  achievements_level        varchar(20) DEFAULT NULL,
  achievements_rank         varchar(20) DEFAULT NULL ,
  achievements_licence_time varchar(20) DEFAULT NULL ,
  PRIMARY KEY (achievements_code)
);

-- ----------------------------
-- Records of achievements
-- ----------------------------

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE admin;
CREATE TABLE admin (
  userName varchar2(20) NOT NULL,
  password varchar2(20) NOT NULL,
  PRIMARY KEY (userName,password)
) ;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO admin VALUES ('00000', '00000');

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE department;
CREATE TABLE department (
  dept_code varchar2(20) NOT NULL ,
  dept_name varchar2(20) NOT NULL ,
  dept_manager varchar2(20) DEFAULT NULL ,
  dept_address varchar2(50) DEFAULT NULL ,
  dept_postcode varchar2(10) DEFAULT NULL ,
  dept_tel varchar2(15) DEFAULT NULL,
  dept_introduce varchar2(255) DEFAULT NULL,
  dept_establish_time varchar2(20) DEFAULT NULL,
  PRIMARY KEY (dept_code)
);

--CONSTRAINT dept_manager FOREIGN KEY (dept_manager) REFERENCES researcher (researcher_code)
--CREATE INDEX dept_manager_index ON department (dept_manager);

ALTER TABLE score ADD CONSTRAINT FK_T_SCORE_REFE FOREIGN KEY (STU_ID)
REFERENCES T_STU (STU_ID);

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO department VALUES ('1111111111', '11111111111', '7676', '11111111111', '1111111111', '111111111', '111111111111111', '2017-03-23');

-- ----------------------------
-- Table structure for project
-- ----------------------------
DROP TABLE project;
CREATE TABLE project (
  proj_code varchar(20) NOT NULL  ,
  proj_name varchar(20) NOT NULL  ,
  proj_source varchar(20) DEFAULT NULL  ,
  proj_funds varchar(255) DEFAULT NULL ,
  proj_duration varchar(255) DEFAULT NULL ,
  PRIMARY KEY (proj_code)
);

-- ----------------------------
-- Records of project
-- ----------------------------
INSERT INTO project VALUES ('123', 'Android项目', '部立项', '20W', '1年');

-- ----------------------------
-- Table structure for relation_achieve_project
-- ----------------------------
DROP TABLE relation_achieve_project;
CREATE TABLE relation_achieve_project (
  proj_code VARCHAR2(20) NOT NULL,
  achievements_code VARCHAR2(20),
  PRIMARY KEY (proj_code),
  CONSTRAINT achieve FOREIGN KEY (achievements_code) REFERENCES achievements (achievements_code) ON DELETE CASCADE,
  CONSTRAINT project_code FOREIGN KEY (proj_code) REFERENCES project (proj_code) ON DELETE CASCADE
);

-- CREATE INDEX achieve ON relation_achieve_project (achievements_code);

-- ----------------------------
-- Records of relation_achieve_project
-- ----------------------------

-- ----------------------------
-- Table structure for relation_reseacher_declare_project
-- ----------------------------

DROP TABLE relation_researcher_project;
CREATE TABLE relation_researcher_project (
  researcher_code VARCHAR2(20) NOT NULL,
  proj_code VARCHAR2(20) NOT NULL,
  role VARCHAR2(20) NOT NULL,
  PRIMARY KEY (proj_code,researcher_code),
  CONSTRAINT fk_project_code FOREIGN KEY (proj_code) REFERENCES project (proj_code) ON DELETE CASCADE,
  CONSTRAINT fk_reasercher_code FOREIGN KEY (researcher_code) REFERENCES researcher (researcher_code) ON DELETE CASCADE
);

-- CREATE INDEX "fk_reasercher_code_index" ON "relation_reseacher_declare_project" ("researcher_code");

-- ----------------------------
-- Records of relation_reseacher_declare_project
-- ----------------------------
INSERT INTO relation_researcher_project VALUES ('123456', '101010', '负责主持');
INSERT INTO relation_researcher_project VALUES ('234567', '202020', '一般参加');

-- ----------------------------
-- Table structure for researcher
-- ----------------------------
DROP TABLE  researcher;
CREATE TABLE researcher (
  researcher_code varchar(20) NOT NULL,
  researcher_name varchar(20) NOT NULL ,
  researcher_sex varchar(4) NOT NULL ,
  researcher_born varchar(20) DEFAULT NULL,
  researcher_edulevel varchar(10) DEFAULT NULL ,
  researcher_locate varchar(20) NOT NULL ,
  researcher_work_date varchar(20) DEFAULT NULL ,
  researcher_job_title varchar(20) DEFAULT NULL ,
  researcher_base_wage number(20,0) DEFAULT NULL,
  researcher_post_wage number(20,0) DEFAULT NULL ,
  researcher_bonus_wage number(20,0) DEFAULT NULL ,
  PRIMARY KEY (researcher_code)
);

--KEY researcher_locate (researcher_locate),
--CONSTRAINT researcher_locate FOREIGN KEY (researcher_locate) REFERENCES department (dept_code)
-- ----------------------------
-- Records of researcher
-- ----------------------------

INSERT INTO 'researcher' VALUES ('00000', '00000', '0000', '2017-03-25', '0000', '1111111111', '2017-03-15', '职称A', '0', '0', '0');
INSERT INTO 'researcher' VALUES ('121', '121', '2', '2017-03-29', '21', '1111111111', '2017-03-29', '职称A', '12', '12', '12');
INSERT INTO 'researcher' VALUES ('7676', '7676', '7676', '2017-03-29', '76', '1111111111', '2017-03-29', '职称B', '76', '76', '76');
INSERT INTO 'researcher' VALUES ('8888', '8888', '888', '2017-03-29', '888', '1111111111', '2017-03-29', '职称A', '8888', '88', '888');