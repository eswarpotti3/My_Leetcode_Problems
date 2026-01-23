
delete from person where id not in (select mini_id from(
select min(id) as mini_id, email from person group by email)test)