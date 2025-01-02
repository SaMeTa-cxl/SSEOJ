use sseoj;
-- 需要添加的数据表，有3个tab缩进的表为已完成的表

-- judge_server
			-- tag
			-- following
			-- post
-- post_comment
-- post_comment_like_users
-- post_like_users
-- post_tags
			-- problem
			-- problem_list
			-- problem_list_problems
-- problem_list_star_users
-- problem_pass_users
-- problem_star_users
-- problem_tags
			-- solution
			-- solution_comment
-- solution_comment_like_users
-- solution_like_users
-- solution_tags
-- study_plan
-- submission
			-- tag



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
 'test_case_5'),

 ('Greatest Common Divisor',
 'Calculate the greatest common divisor (GCD) of two integers.',
 'Two integers separated by a space.',
 'An integer representing the GCD.',
 '1 <= a, b <= 1000',
 '{"inputs": ["12 18", "100 45"], "outputs": ["6", "5"]}',
 2,
 1500,
 128,
 0,
 0,
 'Number theory problem',
 0,
 NOW(),
 TRUE,
 'test_case_6'),

('Least Common Multiple',
 'Calculate the least common multiple (LCM) of two integers.',
 'Two integers separated by a space.',
 'An integer representing the LCM.',
 '1 <= a, b <= 1000',
 '{"inputs": ["4 6", "10 15"], "outputs": ["12", "30"]}',
 2,
 1500,
 128,
 0,
 0,
 'Number theory problem',
 0,
 NOW(),
 TRUE,
 'test_case_7'),

('Factorial',
 'Calculate the factorial of a given integer.',
 'A single integer.',
 'An integer representing the factorial.',
 '1 <= n <= 20',
 '{"inputs": ["5", "10"], "outputs": ["120", "3628800"]}',
 3,
 2000,
 256,
 0,
 0,
 'Basic recursion problem',
 0,
 NOW(),
 TRUE,
 'test_case_8'),

('Fibonacci Sequence',
 'Calculate the Nth term of the Fibonacci sequence.',
 'A single integer N.',
 'An integer representing the Nth term.',
 '1 <= N <= 50',
 '{"inputs": ["5", "10"], "outputs": ["5", "55"]}',
 3,
 1500,
 128,
 0,
 0,
 'Dynamic programming problem',
 0,
 NOW(),
 TRUE,
 'test_case_9'),

('Palindrome Check',
 'Check if a given string is a palindrome.',
 'A single string.',
 'YES if it is a palindrome, NO otherwise.',
 '1 <= length of string <= 100',
 '{"inputs": ["racecar", "hello"], "outputs": ["YES", "NO"]}',
 1,
 1000,
 128,
 0,
 0,
 'String processing problem',
 0,
 NOW(),
 TRUE,
 'test_case_10'),

('Anagram Check',
 'Check if two strings are anagrams of each other.',
 'Two strings separated by a space.',
 'YES if they are anagrams, NO otherwise.',
 '1 <= length of each string <= 100',
 '{"inputs": ["listen silent", "hello world"], "outputs": ["YES", "NO"]}',
 2,
 1500,
 128,
 0,
 0,
 'String processing problem',
 0,
 NOW(),
 TRUE,
 'test_case_11'),

('Matrix Multiplication',
 'Multiply two matrices of given dimensions.',
 'Two matrices represented as space-separated rows and columns.',
 'A matrix representing the product.',
 '1 <= rows, cols <= 10',
 '{"inputs": ["1 2 3 4|5 6 7 8", "1 0 0 1|0 1 1 0"], "outputs": ["19 22|43 50", "1 1|0 1"]}',
 4,
 2000,
 512,
 0,
 0,
 'Matrix manipulation problem',
 0,
 NOW(),
 TRUE,
 'test_case_12'),

('Longest Common Subsequence',
 'Find the length of the longest common subsequence of two strings.',
 'Two strings separated by a space.',
 'An integer representing the LCS length.',
 '1 <= length of each string <= 1000',
 '{"inputs": ["abcde ace", "abc xyz"], "outputs": ["3", "0"]}',
 4,
 3000,
 256,
 0,
 0,
 'Dynamic programming problem',
 0,
 NOW(),
 TRUE,
 'test_case_13'),

('Binary Search',
 'Perform a binary search on a sorted array to find a target value.',
 'An array followed by an integer, separated by a space.',
 'The index of the target value, or -1 if not found.',
 '1 <= length of array <= 1000, -10^6 <= elements, target <= 10^6',
 '{"inputs": ["1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 101 103 105 107 109 111 113 115 117 119 121 123 125 127 129 131 133 135 137 139 141 143 145 147 149 151 153 155 157 159 161 163 165 167 169 171 173 175 177 179 181 183 185 187 189 191 193 195 197 199", "125"], "outputs": ["62"]}',
 2,
 2000,
 128,
 0,
 0,
 'Search algorithm problem',
 0,
 NOW(),
 TRUE,
 'test_case_14'),

('Knapsack Problem',
 'Solve the 0/1 knapsack problem to maximize value.',
 'Number of items, capacity, and weights and values of items.',
 'An integer representing the maximum value.',
 '1 <= number of items <= 100, 1 <= capacity <= 1000',
 '{"inputs": ["4 7|1 3 4 5|1 4 5 7"], "outputs": ["9"]}',
 5,
 3000,
 256,
 0,
 0,
 'Optimization problem',
 0,
 NOW(),
 TRUE,
 'test_case_15');


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
 (20, '区间规划', 2),
 (21, '语言', null),
 (22, 'C', 21),
 (23, 'C++', 21),
 (24, 'Java', 21),
 (25, 'Python3', 21),
 (26, 'JavaScript', 21),
 (27, 'Golang', 21);


-- 插入关注数据
insert into following (
follow_time, follower_id, following_id) values
('2024-12-29', 23, 28),
('2024-12-29', 17, 34),
('2024-12-29', 7, 24),
('2024-12-29', 33, 22),
('2024-12-29', 12, 26),
('2024-12-29', 16, 22),
('2024-12-29', 28, 30),
('2024-12-29', 14, 9),
('2024-12-29', 24, 16),
('2024-12-29', 17, 24),
('2024-12-29', 14, 7),
('2024-12-29', 12, 34),
('2024-12-29', 35, 7),
('2024-12-29', 26, 30),
('2024-12-29', 21, 17),
('2024-12-29', 8, 17),
('2024-12-29', 7, 19),
('2024-12-29', 32, 34),
('2024-12-29', 15, 26),
('2024-12-29', 34, 24),
('2024-12-29', 32, 7),
('2024-12-29', 23, 15),
('2024-12-29', 33, 28),
('2024-12-29', 7, 28),
('2024-12-29', 14, 20),
('2024-12-29', 17, 13),
('2024-12-29', 35, 33),
('2024-12-29', 21, 28),
('2024-12-29', 30, 17),
('2024-12-29', 28, 27),
('2024-12-29', 12, 25),
('2024-12-29', 21, 8),
('2024-12-29', 26, 31),
('2024-12-29', 32, 11),
('2024-12-29', 22, 7),
('2024-12-29', 16, 21),
('2024-12-29', 16, 9),
('2024-12-29', 19, 27),
('2024-12-29', 23, 25),
('2024-12-29', 27, 29),
('2024-12-29', 24, 20),
('2024-12-29', 16, 30),
('2024-12-29', 24, 36),
('2024-12-29', 18, 12),
('2024-12-29', 19, 20),
('2024-12-29', 11, 32),
('2024-12-29', 26, 24),
('2024-12-29', 17, 18),
('2024-12-29', 11, 30),
('2024-12-29', 9, 21),
('2024-12-29', 11, 23),
('2024-12-29', 32, 29),
('2024-12-29', 25, 10),
('2024-12-29', 32, 10),
('2024-12-29', 10, 29),
('2024-12-29', 31, 20),
('2024-12-29', 14, 13),
('2024-12-29', 8, 33),
('2024-12-29', 17, 17),
('2024-12-29', 21, 32),
('2024-12-29', 18, 30),
('2024-12-29', 20, 16),
('2024-12-29', 15, 21),
('2024-12-29', 12, 11),
('2024-12-29', 16, 20),
('2024-12-29', 28, 23),
('2024-12-29', 13, 33),
('2024-12-29', 20, 28),
('2024-12-29', 30, 24),
('2024-12-29', 10, 12),
('2024-12-29', 22, 29),
('2024-12-29', 23, 22),
('2024-12-29', 19, 32),
('2024-12-29', 19, 17),
('2024-12-29', 9, 29),
('2024-12-29', 11, 13),
('2024-12-29', 35, 20),
('2024-12-29', 12, 13),
('2024-12-29', 19, 18),
('2024-12-29', 20, 11),
('2024-12-29', 7, 29),
('2024-12-29', 23, 24),
('2024-12-29', 28, 32),
('2024-12-29', 21, 30),
('2024-12-29', 20, 36),
('2024-12-29', 27, 34),
('2024-12-29', 7, 34),
('2024-12-29', 19, 33),
('2024-12-29', 13, 30),
('2024-12-29', 33, 17),
('2024-12-29', 12, 9),
('2024-12-29', 13, 31),
('2024-12-29', 7, 27),
('2024-12-29', 20, 27),
('2024-12-29', 13, 27),
('2024-12-29', 31, 16),
('2024-12-29', 26, 23),
('2024-12-29', 34, 16),
('2024-12-29', 31, 30),
('2024-12-29', 9, 31),
('2024-12-29', 8, 23),
('2024-12-29', 18, 9),
('2024-12-29', 25, 13),
('2024-12-29', 19, 16),
('2024-12-29', 20, 15),
('2024-12-29', 33, 14),
('2024-12-29', 20, 17),
('2024-12-29', 15, 17),
('2024-12-29', 12, 24),
('2024-12-29', 25, 32),
('2024-12-29', 25, 30),
('2024-12-29', 21, 13),
('2024-12-29', 8, 36),
('2024-12-29', 23, 17),
('2024-12-29', 18, 13),
('2024-12-29', 16, 28),
('2024-12-29', 26, 20),
('2024-12-29', 29, 18),
('2024-12-29', 9, 7),
('2024-12-29', 23, 10),
('2024-12-29', 28, 13),
('2024-12-29', 29, 32),
('2024-12-29', 31, 36),
('2024-12-29', 29, 27),
('2024-12-29', 22, 12),
('2024-12-29', 23, 14),
('2024-12-29', 32, 18),
('2024-12-29', 8, 28),
('2024-12-29', 18, 29),
('2024-12-29', 22, 26),
('2024-12-29', 8, 29),
('2024-12-29', 9, 17),
('2024-12-29', 19, 36),
('2024-12-29', 10, 33),
('2024-12-29', 25, 23),
('2024-12-29', 33, 8),
('2024-12-29', 30, 26),
('2024-12-29', 7, 16),
('2024-12-29', 29, 29),
('2024-12-29', 16, 11),
('2024-12-29', 10, 36),
('2024-12-29', 12, 21),
('2024-12-29', 14, 35),
('2024-12-29', 18, 8),
('2024-12-29', 20, 10),
('2024-12-29', 29, 31),
('2024-12-29', 26, 21),
('2024-12-29', 26, 17),
('2024-12-29', 31, 23),
('2024-12-29', 7, 12),
('2024-12-29', 12, 30),
('2024-12-29', 35, 17),
('2024-12-29', 14, 26),
('2024-12-29', 26, 13),
('2024-12-29', 24, 19),
('2024-12-29', 30, 11),
('2024-12-29', 17, 8),
('2024-12-29', 7, 25),
('2024-12-29', 28, 26),
('2024-12-29', 35, 24),
('2024-12-29', 17, 22),
('2024-12-29', 16, 18),
('2024-12-29', 24, 33),
('2024-12-29', 11, 10),
('2024-12-29', 32, 30),
('2024-12-29', 35, 15),
('2024-12-29', 32, 20),
('2024-12-29', 16, 16),
('2024-12-29', 30, 9),
('2024-12-29', 29, 16),
('2024-12-29', 7, 21),
('2024-12-29', 13, 19),
('2024-12-29', 9, 23),
('2024-12-29', 17, 15),
('2024-12-29', 22, 31),
('2024-12-29', 7, 31),
('2024-12-29', 15, 36),
('2024-12-29', 17, 16),
('2024-12-29', 12, 27),
('2024-12-29', 10, 34),
('2024-12-29', 28, 8),
('2024-12-29', 32, 35),
('2024-12-29', 22, 23),
('2024-12-29', 13, 29),
('2024-12-29', 31, 8),
('2024-12-29', 22, 35),
('2024-12-29', 29, 34),
('2024-12-29', 33, 19),
('2024-12-29', 9, 35),
('2024-12-29', 12, 17),
('2024-12-29', 31, 35),
('2024-12-29', 26, 35),
('2024-12-29', 24, 17),
('2024-12-29', 33, 20),
('2024-12-29', 19, 11),
('2024-12-29', 24, 22),
('2024-12-29', 34, 27),
('2024-12-29', 34, 21),
('2024-12-29', 30, 27);


-- 插入帖子数据
insert into post (
title, content, like_count, comment_count, create_time, last_update_time, is_announcement, check_status, create_user_id) values
('解题求助',
'各位大大，第一道题到底怎么写？',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 7),
('第一段java实习',
'去500～999规模的饮料公司搞后台管理系统，要不要去呀，目前研一0实，请大佬给点建议',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 8),
('小米校招&实习内推',
'请使用内推码：SK9VQSH'
'前进一小米！！！
小米集团25校园招聘已经启动啦！！！
感兴趣的同学可以去 https://hr.xiaomi.com/ 官网投递简历！！！
早投递早拿offer！！
欢迎大家加入小米！！',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 9),
('学得想哭',
'学得想哭。你鸭期末周设计强度太高了',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 10),
('中珠→金湾机场',
'中珠→金湾机场。1月1日早上6:30到金湾机场，有没有一起拼车？（时间可以提前）',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 11),
('喜欢学妹应该吃哪种中药？',
'感觉和学妹相处起来会更自然一些，所以想和学妹交往啦。本人175/65，东校大四，轻度健身痕迹，普通外貌（大概40%的同性比我帅这样吧），朋友圈子很简单。业余时间主要是逛吃，游戏或者麻将，天气不冷的时候游泳比较频繁。
理想对象：03，04或05年生，爱干净，身心健康，现在或未来在大学城（有外校的朋友也可以介绍一下）
补充：已留QQ，有意向就加微信，社恐的话可以不马上见面',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 12),
('捞人',
'中珠捞今晚跑步菠萝头男生。   今晚大概6:30，momo从榕园食堂吃完绝望地骑车前往教学楼，在第一个丁字路口一个头顶菠萝头的同学哒哒跑步从我身边经过，像一道光点亮了我的夜晚，当时我的车速和他跑步的速度比较接近，于是我们保持约2米距离同路了十秒左右，期间观察到他的菠萝头戴了发带，身上衣服的颜色颇具热带感，我对这位充满青春活力感的运动少年很感兴趣，想进一步了解一下，如果这位同学看到了帖子不介意我占用一格好友列表的话可以加加我，
自我介绍：理科大三女爱运动（跑步羽毛球篮球）爱电影（星际穿越哈利波特飘）爱美食爱探店（朋友圈会分享探店经验美食攻略）',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 13),
('我觉得女朋友很扫兴',
'我觉得女朋友很扫兴。好不容易都有空，想约着女朋友一起去看电影然后一起吃个饭。在去看电影的路上，我们打车都坐的后排，女朋友凑过来跟我说话，我闻到了她有一点口臭。于是有以下对话（正常谈话声音）
我：你嘴好臭，你真应该买漱口水用用，
她：臭的是你，要买你买（挪开位置到另一边车窗）
我：你自己闻不到吗？
她：闻不到
我：你肯定感染了幽门螺旋杆菌
她：我买过试纸测了，没有
我：你回去给你舍友哈一口气，问问她们
她：保持沉默不说话
我：是不是因为你有蛀牙啊，给我看看你的蛀牙
她：继续沉默
我这时意识到她生气了，于是凑过去哄她。她还是不理我，真服了，出来看个电影有必要这样吗？我只是说了事实而已，情绪太不稳定了吧。真扫兴，电影我不看了让她自己去看吧，饭我也不想吃了，她自己去吃吧。
我错了嘛？',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 14),
('家里没经同意突然给我全款买了套房',
'家里没经同意突然给我全款买了套房。家里没经同意突然给我全款买了套房……
今天爸妈突然打电话告诉我家里给我买了套房，在越秀那边，144平，附近设施好像挺不错的。就是买菜贵一些，好像饮茶也不是很方便，估计毕业了还是要回天河那套住捏。爸妈说后续装修要我拿主意，这咋搞啊？有没有人办过相应手续啊？
但其实有人不建议我要，因为我可能还要承担另外的费用。房屋过户有三种形式：继承、赠与和买卖。如果采用继承方式，则需要在公证处做继承公证，公证处的收费是房屋价值的1%。
而选取赠与方式，则需要缴纳契税。《中华人民共和国契税法》第四条明确，契税的计税依据包括土地使用权赠与、房屋赠与以及其他没有价格的转移土地、房屋权属行为，为税务机关参照土地使用权出售、房屋买卖的市场价格依法核定的价格。同时该法也规定了契税税率为3%-5%。
最后一种就是买卖的方式。根据《中华人民共和国个人所得税法》第三条，个人出售自有住房取得的所得应按照“财产转让所得”项目征收个人所得税，税率为20%。但是如果该房屋同时满足家庭唯一住宅、购买时间超过五年的条件，则个人所得税免交。',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 15),
('中珠北门外卖被偷',
'天杀的谁偷的外卖，晚了几分钟就不见了，这么饿是吧，偷外卖的人期末全挂。期末人怨气极重',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 16),
('中珠榕11的电梯能用了吗',
'中珠榕11的电梯能用了吗。看到有同学乘坐',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 17),
('好无聊想当军师了',
'好无聊想当军师了。好无聊哈哈哈想当军师了 嘿嘿有需要的uus可以留联系方式 我来！不过技巧只占三分 剩下还得看缘分啊',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 18),
('呜呜中珠明天求搭子',
'呜呜中珠明天求搭子。历史原创话剧专场《霞隐紫泉》即将上演
紫泉宫殿锁烟霞，夜月风回狸弄沙。却道人间无鬼魅，破乱归正展宫华。
演出时间：2024年12月29日（周日）19:00—21:30（18:30开始入场）
演出地点：海琴三号C507
该活动由历史学系（珠海）主办，中珠话剧社、大气科学学院、微电子科学与技术学院以及山海学社联合举办',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 19),
('外卖贼',
'谁把本王的喜茶偷了，如实招来',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 20),
('步道乐跑截止了吗',
'步道乐跑截止了吗。rt，步道乐跑截止了吗，今天去跑乐跑，两个打卡点都打上了说打卡点异常无效成绩。（这种可以和老师说算有效吗？里程和配速都正常）',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 21),
('我也是完蛋了',
'我也是完蛋了。crush哥笑起来好可爱啊啊啊',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 22),
('校内推销',
'老校区这边突然多了那种说是啥英语俱乐部的，给你介绍一大堆，问要钱不就支支吾吾，恶心死了，路上逮着个人就开始推销，这种人真的是校内的吗，咋进来的啊',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 23),
('大家平时都玩啥app',
'大家平时都玩啥app。单纯打发时间的话，个人感觉抖音停不下来，贴吧排外性太强，知乎更是懂哥遍地，大家都怎么看呢',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 24),
('好期待见面呐',
'好期待见面呐。还有二十天多天就能回家见面啦',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 25),
('很适合小情侣周末忙里偷闲',
'很适合小情侣周末忙里偷闲。那么问题来了，我女朋友呢',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 26),
('报告用ai可以不',
'报告用ai可以不。水课事多，报告一堆，lz实在不想自己写了，连裁缝都不想当了，直接用ai生成一整篇文章，虽说稍微去了去ai味，但心里还是没底所以可以吗',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 27),
('图书馆一个人占两座',
'图书馆一个人占两座。吃完饭下午来图书馆自习，发现有一个同学旁边的座位放了书包，桌子上没有什么东西，旁边有一个插座，于是询问这位同学旁边有没有其他人书包是否是她的，这位同学说是她的，我说能麻烦移一下吗我想坐那里，她说她东西太多了不好移要我看看其他地方，我说现在图书馆座位没有多少了，那个座位还带插头，她说要我去问问对面坐着的同学能不能移她的东西然后坐她旁边，然后我就转身走了……不是很能理解为什么东西多就可以一个人占两个人的位置。lz有点生气遂发帖',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 28),
('想问问寒假有什么中大认可的竞赛吗',
'想问问寒假有什么中大认可的竞赛吗。好像大英赛中大不认可，报了计算机二级，还有其他的吗',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 29),
('自动化模电',
'自动化模电。求自动化模电真题，有偿',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 30),
('100块钱的快乐',
'100块钱的快乐。100多一点的钱如何让全班享受
买点小东西？…那买什么呢？',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 31),
('神人舍友我真受不了你了',
'真的有很多想说的：
1、长期不洗澡不洗头，甚至最近很多天都没刷牙洗脸，晚上脱了鞋就上床了，床单不知道睡了多久也没说洗一下换一下，身上真的很臭，垃圾也是好多天不丢，满出来也不丢，床位就更不用说了，乱的要死
2、随手关灯这么基本的事做不到，无论是厕所灯还是大灯甚至自己的台灯都不记得，提醒过很多次很多次，有一天晚课两个半小时更是忘了关空调和三个灯，我最后提醒了一次直接开呛了，完全不认为自己有错
3、关于空调开关，在我和另一个舍友已经提出对于他太早开空调不太好的建议时仍然执意开空调，甚至于大中午就要开空调，搞得寝室又臭又闷，你的床位真的很臭，而且你开了倒是记得关呗
4、我之前已经发过一次贴，他看到了，给我道歉了并承诺会注意卫生的，但是并没有，而且语气阴阳怪气说寝室氛围冷清，但是大哥你那么臭我真的不想和你有任何来往
5、我想我之前的交流已经很明确了，但是他的态度一直都是在给自己找补，本质上还是不认为自己有错，我不想再白费口舌和这大哥说了，搞得像是我咄咄逼人还要和我吵架，我已经和辅导员反映过，但无奈不满足换寝室的条件，他肯定也能刷到这条帖子，我就这么给你说了，你也不用来找我，自己改，改好了我自然会删帖，改不好我就再发帖把你床位的照片和名字学号还有大头照都发出来，既然交流对你没有用那我只能采取这种极端方法来施压了，你也可以闹，闹到辅导员换寝室，那更好不过',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 32),
('求游戏推荐',
'笔记本买了好久还没怎么玩过游戏，不玩总感觉浪费了这配置(i7＋4060)',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 33),
('救命，北方人该如何在南方活过冬天',
'开空调就特别干，第二天起来嗓子冒烟，半夜喝好多水，要起夜上厕所，睡不好；不开空调就冻死个人…….怎么办。想知道南方人怎么活的',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 34),
('感觉很久没有干净的笑过了',
'就是那种纯粹 温暖 一看见也想跟着笑而且内心很透净明亮的笑',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 35),
('年度语录汇总',
'1.布什戈门
2.人生易如反掌啊
3.广智救我
4.时间差不多咯
5.city不city
6.谁说这豆角老了，这豆角可太棒了
7.主播主播，……（太长了，集友自行补充）
8.将大局逆转吧，开!（咆哮版）
9.这或许和我的家教有关吧
10.我不明白，……（奉化口音）
11.你真是饿了，什么都吃得下
12.因为他善
13.你偏要去北京是什么意思，北京到底有谁在
14.马超~马超～（超的音前短后长）
15.三折叠，怎么折都有面
16.我是奶龙，我才是奶龙
17.passion（激情）
18.我blue了
19.自→己↓吓↓自→己↑
（年底了，突发奇想想要搞一个年度语录总结，也顺便帮那些没跟上网速的集友补一补知识，大家有补充的也欢迎在评论区留言，我暂时就只能想这么多了）',
 0, 0, '2024-12-28', '2024-12-29',
 False, True, 36);

--  插入题解
insert into solution (content, title, like_count, comment_count, create_time, check_status, create_user_id, problem_id) values
-- 第 1 题
('You can solve this problem by reading the input numbers, splitting them, and adding them directly.',
 'Simple Addition',
 0,
 0,
 now(),
 false,
 1,
 1),
('Make sure to validate that the inputs are integers before performing the addition.',
 'Addition with Type Checking',
 0,
 0,
 now(),
 false,
 2,
 1),

-- 第 2 题
('Subtract the second number from the first after splitting the input.',
 'Basic Subtraction',
 0,
 0,
 now(),
 false,
 1,
 2),
('Ensure that the result is not negative if your system does not support negative numbers.',
 'Edge Case Handling in Subtraction',
 0,
 0,
 now(),
 false,
 2,
 2),

-- 第 3 题
('Multiply the two integers after parsing the input.',
 'Simple Multiplication',
 0,
 0,
 now(),
 false,
 1,
 3),
('Use Karatsuba algorithm for faster multiplication when numbers are large.',
 'Efficient Multiplication',
 0,
 0,
 now(),
 false,
 2,
 3),

-- 第 4 题
('Divide the first number by the second and ensure you handle division by zero.',
 'Basic Division',
 0,
 0,
 now(),
 false,
 1,
 4),
('Use floating-point division to ensure accurate results for non-integer quotients.',
 'Precision in Division',
 0,
 0,
 now(),
 false,
 2,
 4),

-- 第 5 题
('Iterate through numbers up to the square root of the input to check divisibility.',
 'Prime Check Using Trial Division',
 0,
 0,
 now(),
 false,
 1,
 5),
('Use the Sieve of Eratosthenes for precomputing prime numbers.',
 'Efficient Prime Check',
 0,
 0,
 now(),
 false,
 2,
 5),

-- 第 6 题
('Use dynamic programming to find the optimal solution.',
 'Dynamic Programming Approach',
 0,
 0,
 now(),
 false,
 1,
 6),
('Break the problem into smaller subproblems and solve recursively.',
 'Recursive Solution',
 0,
 0,
 now(),
 false,
 2,
 6),

-- 第 7 题
('Simulate the problem step by step to understand edge cases.',
 'Simulation-Based Solution',
 0,
 0,
 now(),
 false,
 1,
 7),
('Optimize the simulation by precomputing intermediate results.',
 'Optimized Simulation',
 0,
 0,
 now(),
 false,
 2,
 7),

-- 第 8 题
('Use binary search for efficient resolution of the problem.',
 'Binary Search Approach',
 0,
 0,
 now(),
 false,
 1,
 8),
('Combine binary search with a hash table for faster lookups.',
 'Hybrid Binary Search',
 0,
 0,
 now(),
 false,
 2,
 8),

-- 第 9 题
('Apply breadth-first search to explore all possibilities.',
 'BFS Solution',
 0,
 0,
 now(),
 false,
 1,
 9),
('Depth-first search can also be used but may require backtracking.',
 'DFS Solution',
 0,
 0,
 now(),
 false,
 2,
 9),

-- 第 10 题
('Use modular arithmetic to simplify calculations.',
 'Modular Arithmetic Solution',
 0,
 0,
 now(),
 false,
 1,
 10),
('Precompute factorials to handle large inputs efficiently.',
 'Precomputation Solution',
 0,
 0,
 now(),
 false,
 2,
 10),

-- 第 11 题
('Sort the input and apply a two-pointer technique.',
 'Sorting and Two-Pointer Method',
 0,
 0,
 now(),
 false,
 1,
 11),
('Use a priority queue to handle dynamic updates.',
 'Priority Queue Solution',
 0,
 0,
 now(),
 false,
 2,
 11),

-- 第 12 题
('Implement a greedy strategy to achieve the best results.',
 'Greedy Algorithm Solution',
 0,
 0,
 now(),
 false,
 1,
 12),
('Compare the greedy approach with dynamic programming for optimality.',
 'Greedy vs DP Solution',
 0,
 0,
 now(),
 false,
 2,
 12),

-- 第 13 题
('Represent the input as a graph and apply Dijkstra’s algorithm.',
 'Graph-Based Solution',
 0,
 0,
 now(),
 false,
 1,
 13),
('Use Floyd-Warshall algorithm for all-pairs shortest paths.',
 'All-Pairs Shortest Path',
 0,
 0,
 now(),
 false,
 2,
 13),

-- 第 14 题
('Use sliding window technique for efficient computation.',
 'Sliding Window Method',
 0,
 0,
 now(),
 false,
 1,
 14),
('Enhance the sliding window with hash maps for better performance.',
 'Advanced Sliding Window',
 0,
 0,
 now(),
 false,
 2,
 14),

-- 第 15 题
('Apply a divide-and-conquer approach to break the problem into smaller parts.',
 'Divide and Conquer',
 0,
 0,
 now(),
 false,
 1,
 15),
('Compare divide-and-conquer with brute force for understanding trade-offs.',
 'Brute Force vs Divide and Conquer',
 0,
 0,
 now(),
 false,
 2,
 15);


-- 插入标签关联关系nothing
insert into solution_tags (solution_id, tag_id) values
(1, 1), (1, 13),
(2, 1), (2, 13),
(3, 1), (3, 13),
(4, 1), (4, 13),
(5, 15),
(6, 15),
(7, 1), (7, 13),
(8, 1), (8, 13),
(9, 3),
(10, 3);


-- 插入题解评论
insert into solution_comment
(content, create_user_id, solution_id, like_count, create_time, check_status, reply_to_user_id)
values
('This solution is very helpful, thank you!', 1, 1, 0, now(), false, null),
('I have a question about this part of your solution.', 2, 1, 0, now(), false, 1),

('Great explanation, but I think there is an edge case missing.', 3, 2, 0, now(), false, null),
('Could you clarify how this handles large inputs?', 4, 2, 0, now(), false, 3),

('This is an efficient implementation, well done!', 1, 3, 0, now(), false, null),
('I recommend adding more comments to improve readability.', 2, 3, 0, now(), false, 1),

('I found this solution helpful for my project.', 3, 4, 0, now(), false, null),
('What inspired this approach? It seems unique.', 4, 4, 0, now(), false, 3),

('This comment provides a good alternate perspective.', 1, 5, 0, now(), false, null),
('Have you considered optimizing this further?', 2, 5, 0, now(), false, 1);


-- 插入题单
insert into problem_list
(title, create_user_id, star_count, problem_count, summary, is_deleted, is_public)
values
('基础算法题单', 1, 0, 0, '包含常见的基础算法题目，如排序、查找等，用于巩固基础知识。', false, true),
('数据结构题单', 2, 0, 0, '专注于数据结构相关问题，包括链表、树、图等内容，适合中级学习者。', false, true),
('动态规划题单', 3, 0, 0, '集合了一些经典动态规划问题，帮助理解状态转移与问题分解。', false, true),
('数学题单', 4, 0, 0, '包含数论与离散数学的练习题目，适合提高数学建模能力。', false, true),
('高级算法题单', 5, 0, 0, '收录了高级算法问题，包括分治、回溯、贪心算法等，适合挑战。', false, true),
('编程比赛题单', 6, 0, 0, '精选自往届编程比赛的高质量题目，适合训练比赛能力。', false, true),
('机器学习题单', 7, 0, 0, '涉及机器学习基础算法实现与优化问题，适合初学者。', false, true),
('数据库练习题单', 8, 0, 0, '包含SQL查询与数据库设计相关问题，适合数据库入门和提高。', false, true),
('操作系统题单', 9, 0, 0, '整理了操作系统经典问题，如进程调度、内存管理等，理论与实践兼备。', false, true),
('网络题单', 10, 0, 0, '涵盖计算机网络问题，从协议到应用层，适合系统学习网络知识。', false, true);

-- 向题单中插入题目数据
insert into problem_list_problems (id, problemlist_id, problem_id) values
(1, 1, 3),
(2, 1, 7),
(3, 2, 1),
(4, 2, 8),
(5, 3, 2),
(6, 3, 9),
(7, 4, 4),
(8, 4, 5),
(9, 5, 6),
(10, 6, 10),
(11, 7, 11),
(12, 8, 12),
(13, 9, 13),
(14, 10, 14),
(15, 10, 15);


-- 插入学习计划

-- 插入