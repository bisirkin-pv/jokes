--create schema dbo;

/* table containing jokes */
create table dbo.jokes(
     id serial primary key
    ,txt text
);