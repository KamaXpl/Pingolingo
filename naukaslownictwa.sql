-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 06 Lis 2023, 08:36
-- Wersja serwera: 10.4.22-MariaDB
-- Wersja PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `naukaslownictwa`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `easy`
--

CREATE TABLE `easy` (
  `question` text NOT NULL,
  `A` text NOT NULL,
  `B` text NOT NULL,
  `C` text NOT NULL,
  `D` text NOT NULL,
  `E` text NOT NULL,
  `F` text NOT NULL,
  `Pop_odp` text NOT NULL,
  `photos_folder` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `easy`
--

INSERT INTO `easy` (`question`, `A`, `B`, `C`, `D`, `E`, `F`, `Pop_odp`, `photos_folder`) VALUES
('jablko.jpg', 'raspberry', 'pear', 'strawberry', 'blueberry', 'apple', 'banana', 'apple', '../../../Nauka-Slownictwa/img/jablko.jpg'),
('banan.jpg', 'apple', 'strawberry', 'raspberry', 'banana', 'tomato', 'carrot', 'banana', '../../../Nauka-Slownictwa/img/banan.jpg'),
('borowka.jpg', 'blueberry', 'banana', 'pear', 'cabbage', 'onion', 'apple', 'blueberry', '../../../Nauka-Slownictwa/img/borowka.jpg'),
('pomarancza.jpg', 'pear', 'strawberry', 'rasberry', 'onion', 'apple', 'orange', 'orange', '../../../Nauka-Slownictwa/img/pomarancza.jpg'),
('gruszka.jpg', 'apple', 'banana', 'pear', 'carrot', 'cabbage', 'orange', 'pear', '../../../Nauka-Slownictwa/img/gruszka.jpg'),
('truskawka.jpg', 'strawberry', 'blueberry', 'rasberry', 'banana', 'apple', 'orange', 'strawberry', '../../../Nauka-Slownictwa/img/truskawka.jpg'),
('kot.jpg', 'dog', 'snake', 'cat', 'lion', 'tiger', 'bird', 'cat', '../../../Nauka-Slownictwa/img/kot.jpg'),
('pies.jpg', 'cat', 'cow', 'dog', 'lion', 'snake', 'mouse', 'dog', '../../../Nauka-Slownictwa/img/pies.jpg'),
('lew.jpg', 'tiger', 'cheetah', 'dog', 'cat', 'lion', 'mouse', 'lion', '../../../Nauka-Slownictwa/img/lew.jpg'),
('roza.jpg', 'tulip', 'tree', 'rosa', 'orchid', 'blueberry', 'birch', 'rosa', '../../../Nauka-Slownictwa/img/roza.jpg'),
('drzwi.jpg', 'roof', 'floor', 'house', 'door', 'hall', 'living room', 'door', '../../../Nauka-Slownictwa/img/drzwi.jpg'),
('linijka.jpg', 'rubber', 'ruler', 'pencil sharper', 'notebook', 'book', 'marker', 'ruler', '../../../Nauka-Slownictwa/img/linijka.jpg'),
('zeszyt.jpg', 'ruler', 'rubber', 'notebook', 'pen', 'pencil box', 'pencil sharper', 'notebook', '../../../Nauka-Slownictwa/img/zeszyt.jpg'),
('auto.jpg', 'lorry', 'car', 'bus', 'train', 'airplane', 'ship', 'car', '../../../Nauka-Slownictwa/img/auto.jpg'),
('swinia.jpg', 'penguin', 'turtle', 'pig', 'goldfish', 'mouse', 'cat', 'pig', '../../../Nauka-Slownictwa/img/swinia.jpg'),
('szachy.jpg', 'chess', 'game', 'globe', 'scooter', 'roller skates', 'catch', 'chess', '../../../Nauka-Slownictwa/img/szachy.jpg'),
('krowa.jpg', 'cow', 'sheep', 'chicken', 'turtle', 'cat', 'dog', 'cow', '../../../Nauka-Slownictwa/img/krowa.jpg'),
('okulary.jpg', 'glasses', 'socks', 'skirt', 'pants', 'boots', 'hat', 'glasses', '../../../Nauka-Slownictwa/img/okulary.jpg'),
('lampa.jpg', 'lamp', 'bookshelf', 'carpet', 'ceiling', 'chimney', 'door', 'lamp', '../../../Nauka-Slownictwa/img/lampa.jpg'),
('lozko.jpg', 'lamp', 'desk', 'bed', 'bookshelf', 'bin', 'carpet', 'bed', '../../../Nauka-Slownictwa/img/lozko.jpg'),
('klawiatura.jpg', 'laptop', 'tablet', 'keyboard', 'microphone', 'speakers', 'charger', 'keyboard', '../../../Nauka-Slownictwa/img/klawiatura.jpg'),
('zielony.jpg', 'blue', 'yellow', 'green', 'red', 'black', 'purple', 'green', '../../../Nauka-Slownictwa/img/zielony.jpg'),
('zyrafa.jpg', 'dog', 'turtle', 'horse', 'panda', 'giraffe', 'koala', 'giraffe', '../../../Nauka-Slownictwa/img/zyrafa.jpg'),
('grzyb.jpg', 'mushroom', 'onions', 'cabbage', 'carrot', 'pumpkin', 'avocado', 'mushroom', '../../../Nauka-Slownictwa/img/grzyb.jpg'),
('marchewka.jpg', 'carrot', 'potato', 'tomato', 'cucumber', 'onion', 'cabbage', 'carrot', '../../../Nauka-Slownictwa/img/marchewka.jpg');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `medhar`
--

CREATE TABLE `medhar` (
  `question` text NOT NULL,
  `word` text NOT NULL,
  `word_without_letter` text NOT NULL,
  `right_letter` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `medhar`
--

INSERT INTO `medhar` (`question`, `word`, `word_without_letter`, `right_letter`) VALUES
('kot', 'cat', 'c_t', 'a'),
('litera', 'letter', 'l_tt_r', 'e'),
('słowo', 'word', 'w_rd', 'o'),
('mysz', 'mouse', 'm_use', 'o'),
('dotyk', 'touch', 't_uch', 'o'),
('drzewo', 'tree', 'tr__', 'e'),
('ziemniak', 'potato', 'p_tat_', 'o'),
('śmierć', 'death', 'de_th', 'a'),
('nowy', 'new', 'n_w', 'e'),
('zielony', 'green', 'gr__n', 'e'),
('basen', 'pool', 'p__l', 'o'),
('jacht', 'yacht', '_acht', 'y'),
('tak', 'yes', '_es', 'y'),
('wczoraj', 'yesterday', '_esterda_', 'y'),
('lód', 'ice', '_ce', 'i'),
('zapalić', 'ignite', '_gn_te', 'i'),
('niemożliwy', 'impossible', '_mposs_ble', 'i'),
('brzydki', 'ugly', '_gly', 'u'),
('jednogłośny', 'unanimous', '_nanimo_s', 'u'),
('wspólny', 'common', 'c_mm_n', 'o');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `medium1`
--

CREATE TABLE `medium1` (
  `question` text NOT NULL,
  `A` text NOT NULL,
  `B` text NOT NULL,
  `C` text NOT NULL,
  `D` text NOT NULL,
  `E` text NOT NULL,
  `F` text NOT NULL,
  `G` text NOT NULL,
  `H` text NOT NULL,
  `Pop_odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `medium1`
--

INSERT INTO `medium1` (`question`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, `Pop_odp`) VALUES
('Gepard', 'Duck', 'Monkey', 'Bird', 'Buffalo', 'Koala', 'Bear', 'Cheetah', 'Sheep', 'Cheetah'),
('Fretka', 'Ferret', 'Giraffe', 'Donkey', 'Axolotl', 'Hamster', 'Hyenas', 'Cougar', 'Hedgehog', 'Ferret'),
('Ciemny dąb', 'Oak', 'Blue spruce', 'Birch', 'Curry tree', 'Cacao tree', 'Dark oak', 'Burflower-tree', 'White Oak', 'Dark oak'),
('Szmaragd', 'Diamond', 'Gold', 'Emerald', 'Iron', 'Bronze', 'Copper', 'Coal', 'Ruby', 'Emerald'),
('Tulipan', 'Sunflower', 'Tulip', 'Rose', 'Orchid', 'Lily', 'Daisy', 'Iris', 'Peony', 'Tulip'),
('Grzmot', 'Thunder', 'Cloud', 'Rain', 'Wind', 'Storm', 'Rainbow', 'Sun', 'Fog', 'Thunder'),
('Dach', 'Floor', 'Wall', 'Door', 'Roof', 'Window', 'Lamp', 'Desk', 'Pillar', 'Roof'),
('Wiatrak', 'Rug', 'Bin', 'Lamp', 'Desk', 'Windmill', 'Chair', 'Bed', 'Keyboard', 'Windmill'),
('Córka', 'Sister', 'Brother', 'Mother', 'Father', 'Grandad', 'Grandma', 'Son', 'Daughter', 'Daughter'),
('Piasek', 'Sand', 'Gravel', 'Red sand', 'Sandstone', 'Andesite', 'Stone', 'Bazalt', 'Granite', 'Sand'),
('Podkładka', 'Mouse', 'Keyboard', 'Monitor', 'Mousepad', 'Lightbar', 'Processor', 'Handcam', 'Microfon', 'Mousepad'),
('Skarpetki', 'Dress', 'Skirt', 'Socks', 'Hat', 'Sweatshirt', 'Pants', 'Gloves', 'Boots', 'Socks'),
('Leniwiec', 'Sloth', 'Wolf ', 'Quokka', 'Deer', 'Turtles', 'Lynxes', 'Cattle', 'Gorillas', 'Sloth'),
('Kapusta', 'Onions', 'Turnip', 'Lettuce', 'Cabbage', 'Cauliflower', 'Beet', 'Celery', 'Radish', 'Cabbage'),
('Gruszka', 'Apple', 'Blueberries', 'Cherry', 'Avocado', 'Watermelon', 'Pear', 'Raspberry', 'Plum', 'Pear'),
('Pociąg', 'Car', 'Train', 'Airplane', 'Underground', 'Bus', 'Truck', 'Tractor', 'Combine', 'Train'),
('Pochmurny', 'Foggy', 'Sunny', 'Wet', 'Shower', 'Cloudy', 'Freezing', 'Mild', 'Shining', 'Cloudy'),
('Bliźniak', 'Son', 'Brother', 'Twin', 'Sister', 'Niece', 'Uncle', 'Mother', 'Daughter', 'Twin'),
('Ćwiczyć', 'Match', 'Trophy', 'Tournament', 'Racket', 'Draw', 'Train', 'Medal', 'Shoot', 'Train'),
('Wiadro', 'Bucket', 'Rug', 'Electricity', 'Basic', 'Mop', 'Water', 'Broom', 'Duster', 'Bucket'),
('Bramka', 'Prom', 'Gate', 'Ferry', 'Port', 'Camper', 'Boot', 'Tunnel', 'Platform', 'Gate'),
('Ciężarówka', 'Car', 'Lorry', 'Motorbike', 'Bike', 'Minibus', 'Bus', 'Ship', 'Yacht', 'Lorry'),
('Ciasto', 'Carrot', 'Cookie', 'Cake', 'Mushroom', 'Potato', 'Peal', 'Bean', 'Peach', 'Cake'),
('Kawiarnia', 'Calorie', 'Chop', 'Afternoon tea', 'Cafe', 'Drive-through', 'Food truck', 'Grape', 'Tea', 'Cafe');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `test`
--

CREATE TABLE `test` (
  `question` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `A` text NOT NULL,
  `B` text NOT NULL,
  `C` text NOT NULL,
  `D` text NOT NULL,
  `E` text NOT NULL,
  `F` text NOT NULL,
  `Pop_odp` text NOT NULL,
  `photos_folder` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `test`
--

INSERT INTO `test` (`question`, `A`, `B`, `C`, `D`, `E`, `F`, `Pop_odp`, `photos_folder`) VALUES
('kot', 'cat', 'dog', 'strawberry', 'pear', 'cabbage', 'onion', 'cat', '\"C:\\Users\\games\\Documents\\GitHub\\Nauka-Slownictwa\\images\\kot.jpg\"'),
('pies', 'snake', 'penguin', 'frog', 'turtle', 'cat', 'dog', 'dog', '\"C:\\Users\\games\\Documents\\GitHub\\Nauka-Slownictwa\\images\\pies.jpg\"');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `words`
--

CREATE TABLE `words` (
  `polish` text NOT NULL,
  `english` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `words`
--

INSERT INTO `words` (`polish`, `english`) VALUES
('jabłko', 'apple'),
('pomarańcza', 'orange'),
('truskawka', 'strawberry'),
('borówka', 'blueberry'),
('gospoda', 'inn'),
('powtórka', 'revision'),
('dzika fauna i flora', 'wildlife'),
('pałac', 'mansion'),
('ogrzewanie', 'heating'),
('nieszczęśliwy', 'miserable'),
('wykład', 'lecture'),
('podziwiać', 'admire'),
('słuchowy', 'aural'),
('gruszka', 'pear'),
('chór', 'choir'),
('spostrzec', 'notice'),
('rozsądny', 'sensible'),
('internat', 'dormitory'),
('pokój nauczycielski', 'staffroom'),
('zamek(budowla)', 'castle'),
('lider', 'leader'),
('scena', 'stage'),
('muzyka', 'music'),
('kot', 'cat'),
('pies', 'dog'),
('ręka', 'hand'),
('noga', 'leg'),
('mysz', 'mouse'),
('pająk', 'spider'),
('koń', 'horse');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
