-- Create a table to store the CSV data
CREATE TABLE IF NOT EXISTS padel_players (
  player_id SERIAL PRIMARY KEY, -- Using SERIAL for automatic ID generation
  Nombre VARCHAR(500),
  Ranking INT,  -- Modified to allow NULL values
  Puntuacion INT,
  Companero VARCHAR(255),
  Posicion VARCHAR(255),
  LugarNacimiento VARCHAR(255),
  FechaNacimiento DATE, 
  Altura FLOAT,
  Residencia VARCHAR(255),
  PartidosJugados INT,
  PartidosGanados INT,
  PartidosPerdidos INT,
  Rendimiento FLOAT,
  Racha INT,

  "2020_PartidosJugados" INT,
  "2020_PartidosGanados" INT,
  "2020_PartidosPerdidos" INT,
  "2020_Rendimiento" FLOAT,
  "2020_Torneos ganados" INT,
  "2020_Finales" INT,

  "2019_PartidosJugados" INT,
  "2019_PartidosGanados" INT,
  "2019_PartidosPerdidos" INT,
  "2019_Rendimiento" FLOAT,
  "2019_Torneos ganados" INT,
  "2019_Finales" INT,

  "2018_PartidosJugados" INT,
  "2018_PartidosGanados" INT,
  "2018_PartidosPerdidos" INT,
  "2018_Rendimiento" FLOAT,
  "2018_Torneos ganados" INT,
  "2018_Finales" INT,

  "2017_PartidosJugados" INT,
  "2017_PartidosGanados" INT,
  "2017_PartidosPerdidos" INT,
  "2017_Rendimiento" FLOAT,
  "2017_Torneos ganados" INT,
  "2017_Finales" INT,

  "2016_PartidosJugados" INT,
  "2016_PartidosGanados" INT,
  "2016_PartidosPerdidos" INT,
  "2016_Rendimiento" FLOAT,
  "2016_Torneos ganados" INT,
  "2016_Finales" INT,

  "2015_PartidosJugados" INT,
  "2015_PartidosGanados" INT,
  "2015_PartidosPerdidos" INT,
  "2015_Rendimiento" FLOAT,
  "2015_Torneos ganados" INT,
  "2015_Finales" INT,

  "2014_PartidosJugados" INT,
  "2014_PartidosGanados" INT,
  "2014_PartidosPerdidos" INT,
  "2014_Rendimiento" FLOAT,
  "2014_Torneos ganados" INT,
  "2014_Finales" INT,

  "2013_PartidosJugados" INT,
  "2013_PartidosGanados" INT,
  "2013_PartidosPerdidos" INT,
  "2013_Rendimiento" FLOAT,
  "2013_Torneos ganados" INT,
  "2013_Finales" INT,
  Circuito VARCHAR(255)
);

-- Set datestyle to ISO with day-month-year order
SET datestyle = 'ISO, DMY';

-- Load the CSV data into the table, allowing NULL values for "Ranking" column
COPY padel_players (Nombre, Ranking, Puntuacion, Companero, Posicion, LugarNacimiento, FechaNacimiento, Altura, Residencia, PartidosJugados, PartidosGanados, PartidosPerdidos, Rendimiento, Racha, "2020_PartidosJugados", "2020_PartidosGanados", "2020_PartidosPerdidos", "2020_Rendimiento", "2020_Torneos ganados", "2020_Finales", "2019_PartidosJugados", "2019_PartidosGanados", "2019_PartidosPerdidos", "2019_Rendimiento", "2019_Torneos ganados", "2019_Finales", "2018_PartidosJugados", "2018_PartidosGanados", "2018_PartidosPerdidos", "2018_Rendimiento", "2018_Torneos ganados", "2018_Finales", "2017_PartidosJugados", "2017_PartidosGanados", "2017_PartidosPerdidos", "2017_Rendimiento", "2017_Torneos ganados", "2017_Finales", "2016_PartidosJugados", "2016_PartidosGanados", "2016_PartidosPerdidos", "2016_Rendimiento", "2016_Torneos ganados", "2016_Finales", "2015_PartidosJugados", "2015_PartidosGanados", "2015_PartidosPerdidos", "2015_Rendimiento", "2015_Torneos ganados", "2015_Finales", "2014_PartidosJugados", "2014_PartidosGanados", "2014_PartidosPerdidos", "2014_Rendimiento", "2014_Torneos ganados", "2014_Finales", "2013_PartidosJugados", "2013_PartidosGanados", "2013_PartidosPerdidos", "2013_Rendimiento", "2013_Torneos ganados", "2013_Finales", Circuito)
FROM '/docker-entrypoint-initdb.d/world_padel_tour_dataset.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1'; -- had problems with UTF-8 encoding
