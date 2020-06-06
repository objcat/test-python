-- auto-generated definition
create table key
(
    en_name     text not null,
    rp          text not null,
    name        text default '',
    img         text default '',
    point       text default '',
    distance    text default '',
    cut_ratio   text default '',
    create_time text default '',
    update_time text default '',
    constraint key_pk
        unique (en_name, rp)
);

-- 720x1280
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('challenge_boss', '720x1280', '挑战首领', '', '356,1088', '', '', '2020-6-5 22:28:03', '2020-6-5 22:28:07');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('second_challenge_boss', '720x1280', '弹窗上的挑战首领', '', '356,980', '', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('battle', '720x1280', '战斗', '', '356,1223', '', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('retry', '720x1280', '再次挑战', './img/retry.png', '356,1140', '31.575305938720703', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('next', '720x1280', '下一关', './img/next.png', '356,1140', '48.0312385559082', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('white_place', '720x1280', '点击空白', '', '356,1140', '', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('king_challenge', '720x1280', '王座之塔挑战', '', '349,890', '', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('king_tower_continue', '720x1280', '王座之塔继续', './img/touch_screen_continue.png', '356,1140', '31.575305938720703', '0.7', '2020-6-5 22:30:26', '2020-6-5 22:30:26');

-- 1080x2340
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('challenge_boss', '1080x2340', '挑战首领', '', '552,2091', '', '', '2020-6-5 22:30:26', '2020-6-5 22:30:30');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('second_challenge_boss', '1080x2340', '弹窗上的挑战首领', '', '539,1673', '', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('battle', '1080x2340', '战斗', '', '526,2255', '', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('retry', '1080x2340', '再次挑战', './img/retry.png', '526,1926', '19.899747848510742', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('next', '1080x2340', '下一关', './img/next.png', '535,1872', '36.0', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('white_place', '1080x2340', '点击空白', '', '356,1140', '', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('king_challenge', '1080x2340', '王座之塔挑战', '', '533,1420', '', '', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
INSERT OR REPLACE INTO key (en_name, rp, name, img, point, distance, cut_ratio, create_time, update_time) VALUES ('king_tower_continue', '1080x2340', '王座之塔继续', './img/touch_screen_continue.png', '535,1872', '20.784608840942383', '0.7', '2020-6-5 22:30:26', '2020-6-5 22:30:26');
