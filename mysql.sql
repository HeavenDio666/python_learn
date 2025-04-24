SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for area 
-- ----------------------------
DROP TABLE IF EXISTS `python_learn_user`;
CREATE TABLE `python_learn_user`  (
                              `id` int(11) NOT NULL AUTO_INCREMENT,
                              `uid` varchar(50) COMMENT '编号' ,
                              `name` varchar(50) COMMENT '姓名' ,
                              `role` varchar(60) COMMENT '角色 0-管理员 1-用户 2-作者',
                              `gender` varchar(50) COMMENT '性别' ,
                              `age` INTEGER COMMENT '年龄' ,
                              `image` varchar(1024) COMMENT '头像' ,
                              `mobile` varchar(1024) COMMENT '电话' ,
                              `email` varchar(50) COMMENT '账号' ,
                              `username` varchar(50) COMMENT '账号' ,
                              `password` varchar(100) COMMENT '密码',
							  `description` varchar(100) COMMENT '简介',
                              `deleted` INTEGER COMMENT '是否删除',
                              `createDate` datetime COMMENT '创建时间',
                              `updateDate` datetime COMMENT '更新时间',
                              `operator` varchar(60) COMMENT '操作',
                              PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

insert into python_learn_user
(uid,name,role,username,password,deleted,createDate,updateDate,operator)
values
    ('989f5a38-40ed-4655-82b9-6cff82cb7830','管理员','0','manager','62cb613f61230d45d45dec87df3be745',0,now(),now(),'989f5a38-40ed-4655-82b9-6cff82cb7831');

-- 课程管理
DROP TABLE IF EXISTS `python_learn_content`;
CREATE TABLE `python_learn_content`  (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `uid` varchar(50) COMMENT '编号' ,
                                 `name` varchar(50) COMMENT '名称' ,
                                 `content` varchar(50) COMMENT '内容' ,
                                 `period` varchar(50) COMMENT '课时' ,
                                 `author` varchar(50) COMMENT '授课' ,
                                 `video` varchar(50) COMMENT '视频' ,
                                 `price` varchar(50) COMMENT '价格' ,
                                 `image` varchar(1024) COMMENT '图片',
                                 `description` varchar(1024) COMMENT '说明' ,
                                 `deleted` INTEGER COMMENT '是否删除',
                                 `createDate` datetime COMMENT '创建时间',
                                 `updateDate` datetime COMMENT '更新时间',
                                 `operator` varchar(60) COMMENT '操作',
                                 PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 资讯管理
DROP TABLE IF EXISTS `python_learn_notice`;
CREATE TABLE `python_learn_notice`  (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `uid` varchar(50) COMMENT '编号' ,
                                 `name` varchar(50) COMMENT '名称' ,
                                 `content` varchar(1024) COMMENT '内容' ,
                                 `image` varchar(1024) COMMENT '图片',
                                 `description` varchar(1024) COMMENT '说明' ,
                                 `deleted` INTEGER COMMENT '是否删除',
                                 `createDate` datetime COMMENT '创建时间',
                                 `updateDate` datetime COMMENT '更新时间',
                                 `operator` varchar(60) COMMENT '操作',
                                 PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 应用管理
DROP TABLE IF EXISTS `python_learn_exam`;
CREATE TABLE `python_learn_exam`  (
                                    `id` int(11) NOT NULL AUTO_INCREMENT,
                                    `uid` varchar(50) COMMENT '编号',
                                    `name` varchar(1024) COMMENT '名称',
                                    `content` varchar(1024)  COMMENT '课程',
                                    `description` varchar(1024)  COMMENT '描述',
                                    `image` varchar(1024)  COMMENT '描述',
                                    `status` varchar(50) COMMENT '状态 0-公共 1-个人',
                                    `user` varchar(50) COMMENT '用户',
                                    `single` INTEGER COMMENT '单选题',
                                    `multiple` INTEGER COMMENT '多选题',
                                    `judge` INTEGER COMMENT '判断题',
                                    `deleted` INTEGER COMMENT '是否删除',
                                    `createDate` datetime COMMENT '创建时间',
                                    `updateDate` datetime COMMENT '更新时间',
                                    `operator` varchar(60) COMMENT '操作',
                                    PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


-- 试题管理
DROP TABLE IF EXISTS `python_learn_test`;
CREATE TABLE `python_learn_test`  (
                                    `id` int(11) NOT NULL AUTO_INCREMENT,
                                    `uid` varchar(50) COMMENT '编号',
                                    `name` varchar(1024) COMMENT '标题',
                                    `analysis` varchar(1024) COMMENT '解析',
                                    `answer` varchar(1024) COMMENT '答案',
                                    `image` varchar(1024) COMMENT '图片' ,
                                    `type` varchar(1024)  COMMENT '类型',
                                    `deleted` INTEGER COMMENT '是否删除',
                                    `createDate` datetime COMMENT '创建时间',
                                    `updateDate` datetime COMMENT '更新时间',
                                    `operator` varchar(60) COMMENT '操作',
                                    PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


-- 选项管理
DROP TABLE IF EXISTS `python_learn_option`;
CREATE TABLE `python_learn_option`  (
                                      `id` int(11) NOT NULL AUTO_INCREMENT,
                                      `uid` varchar(50) COMMENT '编号',
                                      `test` varchar(1024) COMMENT '题目',
                                      `name` varchar(1024)  COMMENT '标题',
                                      `choice` varchar(1024) COMMENT '选项',
                                      `seq` INTEGER COMMENT '序号',
                                      `deleted` INTEGER COMMENT '是否删除',
                                      `createDate` datetime COMMENT '创建时间',
                                      `updateDate` datetime COMMENT '更新时间',
                                      `operator` varchar(60) COMMENT '操作',
                                      PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 考试试题
DROP TABLE IF EXISTS `python_learn_exam_test`;
CREATE TABLE `python_learn_exam_test`  (
                                         `id` int(11) NOT NULL AUTO_INCREMENT,
                                         `uid` varchar(50) COMMENT '编号',
                                         `exam` varchar(1024) COMMENT '标题',
                                         `test` varchar(1024)  COMMENT '试题',
                                         `seq` INTEGER COMMENT '状态',
                                         `deleted` INTEGER COMMENT '是否删除',
                                         `createDate` datetime COMMENT '创建时间',
                                         `updateDate` datetime COMMENT '更新时间',
                                         `operator` varchar(60) COMMENT '操作',
                                         PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 答案管理
DROP TABLE IF EXISTS `python_learn_answer`;
CREATE TABLE `python_learn_answer`  (
                                      `id` int(11) NOT NULL AUTO_INCREMENT,
                                      `uid` varchar(50) COMMENT '编号',
                                      `record` varchar(1024) COMMENT '记录',
                                      `exam` varchar(1024) COMMENT '试卷',
                                      `test` varchar(1024)  COMMENT '试题',
                                      `answer` varchar(1024)  COMMENT '答案',
                                      `correct` varchar(1024)  COMMENT '正确答案',
                                      `user` varchar(1024)  COMMENT '用户',
                                      `status` INTEGER COMMENT '0-错误 1-正确',
                                      `deleted` INTEGER COMMENT '是否删除',
                                      `createDate` datetime COMMENT '创建时间',
                                      `updateDate` datetime COMMENT '更新时间',
                                      `operator` varchar(60) COMMENT '操作',
                                      PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 考试记录
DROP TABLE IF EXISTS `python_learn_exam_record`;
CREATE TABLE `python_learn_exam_record`  (
                                           `id` int(11) NOT NULL AUTO_INCREMENT,
                                           `uid` varchar(50) COMMENT '编号',
                                           `exam` varchar(1024) COMMENT '标题',
                                           `user` varchar(1024)  COMMENT '用户',
                                           `score` INTEGER COMMENT '得分',
                                           `status` INTEGER COMMENT '状态',
                                           `startTime` datetime COMMENT '创建时间',
                                           `endTime` datetime COMMENT '更新时间',
                                           `deleted` INTEGER COMMENT '是否删除',
                                           `createDate` datetime COMMENT '创建时间',
                                           `updateDate` datetime COMMENT '更新时间',
                                           `operator` varchar(60) COMMENT '操作',
                                           PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 测试管理
DROP TABLE IF EXISTS `python_learn_link`;
CREATE TABLE `python_learn_link`  (
                                    `id` int(11) NOT NULL AUTO_INCREMENT,
                                    `uid` varchar(50) COMMENT '编号',
                                    `name` varchar(1024) COMMENT '题目',
                                    `image` varchar(1024) COMMENT '图片' ,
                                    `seq` INTEGER COMMENT '题号',
                                    `deleted` INTEGER COMMENT '是否删除',
                                    `createDate` datetime COMMENT '创建时间',
                                    `updateDate` datetime COMMENT '更新时间',
                                    `operator` varchar(60) COMMENT '操作',
                                    PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 测试管理
DROP TABLE IF EXISTS `python_learn_result`;
CREATE TABLE `python_learn_result`  (
                                    `id` int(11) NOT NULL AUTO_INCREMENT,
                                    `uid` varchar(50) COMMENT '编号',
                                    `user` varchar(1024) COMMENT '用户',
                                    `link` varchar(1024) COMMENT '测试' ,
                                    `choice` varchar(1024) COMMENT '选项' ,
                                    `deleted` INTEGER COMMENT '是否删除',
                                    `createDate` datetime COMMENT '创建时间',
                                    `updateDate` datetime COMMENT '更新时间',
                                    `operator` varchar(60) COMMENT '操作',
                                    PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


-- 收藏管理
DROP TABLE IF EXISTS `python_learn_collect`;
CREATE TABLE `python_learn_collect`  (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `uid` varchar(50) COMMENT '编号' ,
                                 `user` varchar(50) COMMENT '用户' ,
                                 `content` varchar(1024) COMMENT '歌曲',
                                 `deleted` INTEGER COMMENT '是否删除',
                                 `createDate` datetime COMMENT '创建时间',
                                 `updateDate` datetime COMMENT '更新时间',
                                 `operator` varchar(60) COMMENT '操作',
                                 PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 评分管理
DROP TABLE IF EXISTS `python_learn_score`;
CREATE TABLE `python_learn_score`  (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `uid` varchar(50) COMMENT '编号' ,
                                 `user` varchar(50) COMMENT '用户' ,
                                 `content` varchar(1024) COMMENT '歌曲',
                                 `score` INTEGER COMMENT '歌曲',
                                 `deleted` INTEGER COMMENT '是否删除',
                                 `createDate` datetime COMMENT '创建时间',
                                 `updateDate` datetime COMMENT '更新时间',
                                 `operator` varchar(60) COMMENT '操作',
                                 PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 评论管理
DROP TABLE IF EXISTS `python_learn_comment`;
CREATE TABLE `python_learn_comment`  (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `uid` varchar(50) COMMENT '编号' ,
                                 `user` varchar(50) COMMENT '用户' ,
                                 `content` varchar(1024) COMMENT '歌曲',
                                 `comment` varchar(1024) COMMENT '评论',
                                 `score` INTEGER COMMENT '评分',
                                 `deleted` INTEGER COMMENT '是否删除',
                                 `createDate` datetime COMMENT '创建时间',
                                 `updateDate` datetime COMMENT '更新时间',
                                 `operator` varchar(60) COMMENT '操作',
                                 PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
