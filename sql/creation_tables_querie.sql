CREATE TABLE campos (
    campo_id SERIAL PRIMARY KEY NOT NULL,
    nombre_campo VARCHAR(50),
    fecha_creacion TIMESTAMP,
    actualizado TIMESTAMP
);

CREATE TABLE pozos (
    pozo_id SERIAL PRIMARY KEY NOT NULL,
    nombre_pozo VARCHAR(50) NOT NULL,
    campo_id INTEGER,
    fecha_creacion TIMESTAMP,
    actualizado TIMESTAMP,
    CONSTRAINT fk_pozos_campos FOREIGN KEY (campo_id) REFERENCES campos(campo_id) ON DELETE CASCADE
);

CREATE TABLE cimas (
    cima_id SERIAL PRIMARY KEY NOT NULL,
    nombre_cima VARCHAR(50) NOT NULL,
    pozo_id INTEGER,
    cima_md FLOAT NOT NULL,
    base_md FLOAT NOT NULL,
    fecha_creacion TIMESTAMP,
    actualizado TIMESTAMP,
    CONSTRAINT fk_cimas_pozos FOREIGN KEY (pozo_id) REFERENCES pozos(pozo_id) ON DELETE CASCADE
);

CREATE TABLE registros (
    registro_id SERIAL PRIMARY KEY NOT NULL,
    pozo_id INTEGER,
    tipo_registro INTEGER NOT NULL,
    medido BOOLEAN NOT NULL,
    fecha_creacion TIMESTAMP,
    actualizado TIMESTAMP,
    CONSTRAINT fk_registros_pozos FOREIGN KEY (pozo_id) REFERENCES pozos(pozo_id) ON DELETE CASCADE
);

CREATE TABLE registros_medidos (
    registro_medido_id SERIAL PRIMARY KEY NOT NULL,
    registro_id INTEGER,
    md FLOAT NOT NULL,
    valor FLOAT NOT NULL,
    fecha_creacion TIMESTAMP,
    actualizado TIMESTAMP,
    CONSTRAINT fk_registrosmedidos_registros FOREIGN KEY (registro_id) REFERENCES registros(registro_id) ON DELETE CASCADE
);

CREATE TABLE registros_sinteticos (
    registro_sintetico_id SERIAL PRIMARY KEY NOT NULL,
    registro_id INTEGER,
    md FLOAT NOT NULL,
    valor FLOAT NOT NULL,
    fecha_creacion TIMESTAMP,
    actualizado TIMESTAMP,
    CONSTRAINT fk_registrossinteticos_registros FOREIGN KEY (registro_id) REFERENCES registros(registro_id) ON DELETE CASCADE
);