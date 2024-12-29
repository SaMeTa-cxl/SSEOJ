use sseoj;

-- 禁用外键约束
set foreign_key_checks = 0;

-- 删除所有表中的数据并重置 auto_increment
delete from judge_server;
alter table judge_server auto_increment = 1;

delete from tag;
alter table tag auto_increment = 1;

delete from following;
alter table following auto_increment = 1;

delete from post;
alter table post auto_increment = 1;

delete from post_comment;
alter table post_comment auto_increment = 1;

delete from post_comment_like_users;
alter table post_comment_like_users auto_increment = 1;

delete from post_like_users;
alter table post_like_users auto_increment = 1;

delete from post_tags;
alter table post_tags auto_increment = 1;

delete from problem;
alter table problem auto_increment = 1;

delete from problem_list;
alter table problem_list auto_increment = 1;

delete from problem_list_problems;
alter table problem_list_problems auto_increment = 1;

delete from problem_list_star_users;
alter table problem_list_star_users auto_increment = 1;

delete from problem_pass_users;
alter table problem_pass_users auto_increment = 1;

delete from problem_star_users;
alter table problem_star_users auto_increment = 1;

delete from problem_tags;
alter table problem_tags auto_increment = 1;

delete from solution;
alter table solution auto_increment = 1;

delete from solution_comment;
alter table solution_comment auto_increment = 1;

delete from solution_comment_like_users;
alter table solution_comment_like_users auto_increment = 1;

delete from solution_like_users;
alter table solution_like_users auto_increment = 1;

delete from solution_tags;
alter table solution_tags auto_increment = 1;

delete from study_plan;
alter table study_plan auto_increment = 1;

delete from submission;
alter table submission auto_increment = 1;

delete from tag;
alter table tag auto_increment = 1;

-- 恢复外键约束
set foreign_key_checks = 1;


-- user
-- user_groups
-- user_user_permissions
-- user部分不做处理

-- 插入题目数据
insert into problem (
    name,
    description,
    input_style,
    output_style,
    data_range,
    sample,
    difficulty,
    time_limit,
    memory_limit,
    pass_cnt,
    attempt_cnt,
    source,
    star_cnt,
    create_time,
    check_status,
    test_case_id
) values
('Addition',
 'Calculate the sum of two integers provided as input.',
 'Two integers separated by a space.',
 'An integer representing the sum.',
 '1 <= a, b <= 1000',
 '{"inputs": ["1 2", "5 6"], "outputs": ["3", "11"]}',
 1,
 1000,
 128,
 0,
 0,
 'Basic arithmetic problem',
 0,
 NOW(),
 TRUE,
 'test_case_1'),

('Subtraction',
 'Calculate the difference between two integers provided as input.',
 'Two integers separated by a space.',
 'An integer representing the difference.',
 '1 <= a, b <= 1000',
 '{"inputs": ["3 2", "9 5"], "outputs": ["1", "4"]}',
 1,
 1000,
 128,
 0,
 0,
 'Basic arithmetic problem',
 0,
 NOW(),
 TRUE,
 'test_case_2'),

('Multiplication',
 'Calculate the product of two integers provided as input.',
 'Two integers separated by a space.',
 'An integer representing the product.',
 '1 <= a, b <= 100',
 '{"inputs": ["3 4", "7 8"], "outputs": ["12", "56"]}',
 2,
 1500,
 256,
 0,
 0,
 'Basic arithmetic problem',
 0,
 NOW(),
 TRUE,
 'test_case_3'),

('Division',
 'Calculate the quotient of two integers provided as input.',
 'Two integers separated by a space.',
 'An integer representing the quotient.',
 '1 <= a, b <= 1000 and b != 0',
 '{"inputs": ["10 2", "15 3"], "outputs": ["5", "5"]}',
 2,
 2000,
 256,
 0,
 0,
 'Basic arithmetic problem',
 0,
 NOW(),
 TRUE,
 'test_case_4'),

('Prime Check',
 'Check if a given number is prime.',
 'A single integer.',
 'YES if prime, NO otherwise.',
 '1 <= n <= 10000',
 '{"inputs": ["2", "4"], "outputs": ["YES", "NO"]}',
 3,
 1000,
 128,
 0,
 0,
 'Number theory problem',
 0,
 NOW(),
 TRUE,
 'test_case_5');


--  插入tag数据
 insert into tag (
 id, name, parent_id
 ) values
 (1, '分治', null),
 (2, '动态规划', null),
 (3, '贪心算法', null),
 (4, '回溯', null),
 (5, '图', null),
 (6, '字符串', null),
 (7, '最短路算法', null),
 (8, '搜索', null),
 (9, '树', null),
 (10, '并查集', null),
 (11, '归并排序', 1),
 (12, '快速排序', 1),
 (13, '二分查找', 1),
 (14, 'Strassen矩阵乘法', 1),
 (15, 'Karatsuba乘法', 1),
 (16, '背包问题', 2),
 (17, '最长递增子序列', 2),
 (18, '最长公共子序列', 2),
 (19, '动态规划树', 2),
 (20, '区间规划', 2);

