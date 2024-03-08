CREATE TABLE campos (
	campo_id serial NOT NULL,
	nombre_campo varchar(50) NOT NULL,
	fecha_creacion timestamp NOT NULL,
	actualizado timestamp NOT NULL,
	CONSTRAINT campos_pk PRIMARY KEY (campo_id)
);

CREATE TABLE pozos (
	pozo_id serial NOT NULL,
	nombre_pozo varchar(50) NOT NULL,
	campo_id serial NOT NULL,
	fecha_creacion timestamp NOT NULL,
	actualizado timestamp NOT NULL,
	CONSTRAINT newtable_pk PRIMARY KEY (pozo_id),
	CONSTRAINT pozos_campos_fk FOREIGN KEY (campo_id) REFERENCES campos(campo_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE cimas (
	cima_id serial NOT NULL,
	nombre_cima varchar(50) NOT NULL,
	pozo_id serial NOT NULL,
	cima_md float4 NULL,
	fecha_creacion timestamp NOT NULL,
	actualizado timestamp NOT NULL,
	CONSTRAINT cimas_pk PRIMARY KEY (cima_id),
	CONSTRAINT cimas_pozos_fk FOREIGN KEY (pozo_id) REFERENCES pozos(pozo_id) ON DELETE CASCADE ON UPDATE CASCADE
);