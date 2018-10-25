drop table if exists entries;
create table Comic (
  id integer primary key autoincrement,
  title text not null,
  'language_id' integer foreign key [Language].id 
);

create table [Page](
    id integer primary key autoincrement,
    
);

create table Tag();

create table Author(
    id
);

create table [Language](
    id integer primary key autoincrement,
    'name' text not null
);