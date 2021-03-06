
drop table u_pass;
create table u_pass (
  user_id character varying(10) not null  primary key
  , password character varying(10) not null
);

drop table u_data;
create table u_data (
  user_id character varying(10) not null primary key
  , name_m  character varying(10) not null
  , name_s  character varying(10) not null
  , name_mk  character varying(10) 
  , name_sk  character varying(10) 
  , seinen_dt  date
  , jusho1  character varying(10) 
  , jusho2  character varying(10) 
  , jusho3  character varying(30) 
  , jusho4  character varying(30) 
  , yubin  character varying(7) 
  , email  character varying(30) 
  , tel  character varying(11)  
  , tel_mob  character varying(11)  
  , memo  character varying(100)  
);

drop table k_data;
create table k_data (
  kokyaku_id serial not null default nextval('kokyaku_seq')
  , name_m character varying(10) not null
  , name_s character varying(10) not null
  , name_mk character varying(10)
  , name_sk character varying(10)
  , age integer
  , seinen_dt date
  , seibetsu character varying(3)
  , yubin character varying(7)
  , jusho1 character varying(10)
  , jusho2 character varying(10)
  , jusho3 character varying(30)
  , jusho4 character varying(30)
  , email character varying(30)
  , tel character varying(11)
  , tel_mob character varying(11)
  , memo character varying(100)
  , primary key (kokyaku_id)
);

drop table p_menu;
create table p_menu (
  menu_id integer not null primary key
  , menu_nm  character varying(15) not null
  , menu_kg  bigint default 0
  , memo  character varying(100)  
);

drop table k_rireki;
create table k_rireki (
  kokyaku_id integer not null
  , start_dt date not null
  , end_dt date not null 
  , menu_id integer not null
  , ninzu  integer 
  , memo  character varying(100) 
  , primary key (kokyaku_id, start_dt)
);