tabelausu = """create table if not exists Usuario(
USU_id int auto_increment,
USU_login varchar(40) not null,
USU_senha varchar(40) not null,
primary key (USU_id)
)"""
pegar = 'insert into ' \
'Usuario(USU_login, USU_senha) ' \
'values (%s, %s)'
ver = 'select USU_login, USU_senha from Usuario ' \
'order by USU_id desc limit 1'
ver_adm = 'select USU_login, USU_senha from Usuario ' \
'order by USU_id desc'
verificar = 'select USU_login from Usuario ' \
'where USU_login = (%s)'