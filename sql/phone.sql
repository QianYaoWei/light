create table contact (
    id integer primary key default 1,
    name text,
    phone_num text
);

create table call_recored (
    id integer primary key default 1,
    name text,
    phone_num text,
    type integer,
    time integer
);
