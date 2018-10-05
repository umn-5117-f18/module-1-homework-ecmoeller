drop table survey;

create table survey(
  person_id SERIAL PRIMARY KEY,
  q1 varchar(255),
  q2 varchar(255),
  q3 varchar(255),
  q4 varchar(255),
  q5 varchar(255)
);

insert into survey (q1, q2, q3, q4, q5) values ('a', 'b', 'c', 'd', 'e');
