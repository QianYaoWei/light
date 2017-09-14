-- CREATE TABLE book_mark (
--     id BIGINT PRIMARY KEY, 
--     bookpath TEXT, 
--     mark_pos INTEGER DEFAULT 0, -- 书签跳转位置
--     descri CHARACTER(20), -- 书签描述信息
--     create_time TIMESTAMP -- 创建时间
-- );

create table glob_id (
    id INTEGER PRIMARY KEY DEFAULT 1,
    cur_id BIGINT DEFAULT 1
);

create table book (
    id integer primary key default 1,
    path text,
    cur_page INTEGER DEFAULT 0
);

create table reader (
    id integer primary key default 1,
    cur_book_id integer default 1
);
