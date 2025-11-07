-- Creating the ids table.
CREATE TABLE `ids` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pi_id` varchar(6) DEFAULT NULL,
  `name` varchar(25) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `pi_id` (`pi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Creating the temperatures table.
CREATE TABLE `temperatures` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `celsius` float NOT NULL,
  `fahrenheit` float NOT NULL,
  `kelvin` float NOT NULL,
  `pi_id` varchar(6) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_pi_id` (`pi_id`),
  CONSTRAINT `fk_pi_id` FOREIGN KEY (`pi_id`) REFERENCES `ids` (`pi_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

