-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Czas generowania: 08 Cze 2020, 21:14
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `io_sem4_211a_uzaleznienia`
--
CREATE DATABASE IF NOT EXISTS `io_sem4_211a_uzaleznienia` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `io_sem4_211a_uzaleznienia`;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `adres`
--

DROP TABLE IF EXISTS `adres`;
CREATE TABLE `adres` (
  `id` int(11) NOT NULL,
  `miasto` text NOT NULL,
  `ulica` text NOT NULL,
  `numer_domu` text NOT NULL,
  `numer_lokalu` text DEFAULT NULL,
  `kod_pocztowy` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `adres`
--

INSERT INTO `adres` (`id`, `miasto`, `ulica`, `numer_domu`, `numer_lokalu`, `kod_pocztowy`) VALUES
(1, 'Świętoszówka', 'ul. Bielska', '135', NULL, '43-386'),
(2, 'Radom', 'Al. Wojska Polskiego', '66', '2', '26-604'),
(3, 'Tarnowskie Góry', 'ul. Piaseczna', '8', '5', '42-680'),
(4, 'Katowice', 'ul. Rymarska', '56', NULL, '40-425'),
(5, 'Rzeszów', 'ul. Bohaterów Westerplatte', '24', '1', '35-040'),
(6, 'Rzeszów', 'ul. Bohaterów Westerplatte', '45', '4', '35-040'),
(7, 'Katowice', '9 Maja', '11', '5', '40-303');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `obywatel`
--

DROP TABLE IF EXISTS `obywatel`;
CREATE TABLE `obywatel` (
  `pesel` varchar(11) NOT NULL,
  `imie` text NOT NULL,
  `nazwisko` text NOT NULL,
  `dataUrodzenia` date NOT NULL,
  `adres` int(11) NOT NULL,
  `stan` text NOT NULL,
  `nr_telefonu` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `obywatel`
--

INSERT INTO `obywatel` (`pesel`, `imie`, `nazwisko`, `dataUrodzenia`, `adres`, `stan`, `nr_telefonu`) VALUES
('03260921119', 'Beata', 'Nowak', '2003-06-09', 2, 'Nie podjęto akcji', NULL),
('75092338256', 'Ignacy', 'Kowalski', '1975-09-23', 6, 'Nie podjęto działania', '535553989'),
('81043075006', 'Katarzyna', 'Walczak', '1981-04-30', 3, 'W trakcie', '723582548'),
('89011089442', 'Edyta', 'Ostrowska', '1989-01-10', 7, 'Nie podjęto działania', '798600231'),
('94061897868', 'Mirosława', 'Kucharska', '1994-06-18', 1, 'Nie podjęto działania', '516842608');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `rachunek`
--

DROP TABLE IF EXISTS `rachunek`;
CREATE TABLE `rachunek` (
  `id` int(11) NOT NULL,
  `idSklepu` int(11) NOT NULL,
  `peselKlienta` varchar(11) NOT NULL,
  `data` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `rachunek`
--

INSERT INTO `rachunek` (`id`, `idSklepu`, `peselKlienta`, `data`) VALUES
(1, 1, '94061897868', '2020-03-18'),
(2, 1, '94061897868', '2020-03-19'),
(3, 1, '94061897868', '2020-03-20'),
(4, 2, '81043075006', '2020-04-07'),
(5, 2, '81043075006', '2020-04-10'),
(6, 2, '81043075006', '2020-04-12');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `sklep`
--

DROP TABLE IF EXISTS `sklep`;
CREATE TABLE `sklep` (
  `id` int(11) NOT NULL,
  `nazwa` text NOT NULL,
  `adres` int(11) NOT NULL,
  `peselWlasciciela` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `sklep`
--

INSERT INTO `sklep` (`id`, `nazwa`, `adres`, `peselWlasciciela`) VALUES
(1, 'ABC', 4, '89011089442'),
(2, 'XYZ', 5, '75092338256');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zakup`
--

DROP TABLE IF EXISTS `zakup`;
CREATE TABLE `zakup` (
  `id` int(11) NOT NULL,
  `idRachunku` int(11) NOT NULL,
  `substancja` text NOT NULL,
  `ilosc` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `zakup`
--

INSERT INTO `zakup` (`id`, `idRachunku`, `substancja`, `ilosc`) VALUES
(1, 1, 'Puszka 500ml', 3),
(2, 2, 'Butelka 1l', 2),
(3, 3, 'Lek przeciwbólowy', 1),
(4, 4, 'Lek przeciwbólowy', 1),
(5, 5, 'Antybiotyk', 1),
(6, 6, 'Puszka 500ml', 2),
(7, 1, 'Butelka 1l', 1);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `adres`
--
ALTER TABLE `adres`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `obywatel`
--
ALTER TABLE `obywatel`
  ADD PRIMARY KEY (`pesel`);

--
-- Indeksy dla tabeli `rachunek`
--
ALTER TABLE `rachunek`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `sklep`
--
ALTER TABLE `sklep`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `zakup`
--
ALTER TABLE `zakup`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `adres`
--
ALTER TABLE `adres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT dla tabeli `rachunek`
--
ALTER TABLE `rachunek`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT dla tabeli `sklep`
--
ALTER TABLE `sklep`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT dla tabeli `zakup`
--
ALTER TABLE `zakup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
