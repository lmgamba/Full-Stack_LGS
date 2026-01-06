-- ###############################33--------------
INSERT INTO
    `202509_shop`.`users` (
        name,
        surname,
        age,
        mail,
        register_date,
        status,
        password,
        rol
    )
VALUES (
        'Juan',
        'Pérez García',
        28,
        'juan.perez@gmail.com',
        '2024-01-10 09:15:00',
        1,
        '$2y$10$A1b2C3d4E5f6G7h8I9j0K',
        'user'
    ),
    (
        'María',
        'López Sánchez',
        34,
        'maria.lopez@gmail.com',
        '2024-01-12 11:20:00',
        1,
        '$2y$10$B2c3D4e5F6g7H8i9J0k1L',
        'admin'
    ),
    (
        'Carlos',
        'Ruiz Martín',
        41,
        'carlos.ruiz@gmail.com',
        '2024-01-15 14:45:00',
        1,
        '$2y$10$C3d4E5f6G7h8I9j0K1L2M',
        'user'
    ),
    (
        'Laura',
        'Gómez Navarro',
        25,
        'laura.gomez@gmail.com',
        '2024-01-18 08:30:00',
        1,
        '$2y$10$D4E5f6G7h8I9j0K1L2M3N',
        'user'
    ),
    (
        'Pedro',
        'Fernández Díaz',
        37,
        'pedro.fernandez@gmail.com',
        '2024-01-20 16:10:00',
        0,
        '$2y$10$E5f6G7h8I9j0K1L2M3N4O',
        'user'
    ),
    (
        'Ana',
        'Moreno Castillo',
        29,
        'ana.moreno@gmail.com',
        '2024-01-22 10:05:00',
        1,
        '$2y$10$F6G7h8I9j0K1L2M3N4O5P',
        'admin'
    ),
    (
        'David',
        'Torres Vega',
        45,
        'david.torres@gmail.com',
        '2024-01-25 13:40:00',
        1,
        '$2y$10$G7h8I9j0K1L2M3N4O5P6Q',
        'user'
    ),
    (
        'Lucía',
        'Ramírez Flores',
        31,
        'lucia.ramirez@gmail.com',
        '2024-01-27 17:55:00',
        1,
        '$2y$10$H8I9j0K1L2M3N4O5P6Q7R',
        'user'
    ),
    (
        'Jorge',
        'Vidal Romero',
        39,
        'jorge.vidal@gmail.com',
        '2024-02-01 09:00:00',
        1,
        '$2y$10$I9j0K1L2M3N4O5P6Q7R8S',
        'user'
    ),
    (
        'Elena',
        'Cruz Ortega',
        27,
        'elena.cruz@gmail.com',
        '2024-02-03 12:25:00',
        1,
        '$2y$10$j0K1L2M3N4O5P6Q7R8S9T',
        'user'
    ),
    (
        'Sergio',
        'Molina Reyes',
        33,
        'sergio.molina@gmail.com',
        '2024-02-05 15:10:00',
        1,
        '$2y$10$K1L2M3N4O5P6Q7R8S9T0U',
        'admin'
    ),
    (
        'Patricia',
        'Herrera Campos',
        36,
        'patricia.herrera@gmail.com',
        '2024-02-08 10:50:00',
        1,
        '$2y$10$L2M3N4O5P6Q7R8S9T0U1V',
        'user'
    ),
    (
        'Alberto',
        'Santos Núñez',
        42,
        'alberto.santos@gmail.com',
        '2024-02-10 18:35:00',
        0,
        '$2y$10$M3N4O5P6Q7R8S9T0U1V2W',
        'user'
    ),
    (
        'Isabel',
        'Prieto León',
        26,
        'isabel.prieto@gmail.com',
        '2024-02-12 09:40:00',
        1,
        '$2y$10$N4O5P6Q7R8S9T0U1V2W3X',
        'user'
    ),
    (
        'Miguel',
        'Cano Rojas',
        48,
        'miguel.cano@gmail.com',
        '2024-02-15 16:20:00',
        1,
        '$2y$10$O5P6Q7R8S9T0U1V2W3X4Y',
        'admin'
    ),
    (
        'Raquel',
        'Blanco Gil',
        32,
        'raquel.blanco@gmail.com',
        '2024-02-18 11:15:00',
        1,
        '$2y$10$P6Q7R8S9T0U1V2W3X4Y5Z',
        'user'
    ),
    (
        'Iván',
        'Suárez Pardo',
        35,
        'ivan.suarez@gmail.com',
        '2024-02-20 14:55:00',
        1,
        '$2y$10$Q7R8S9T0U1V2W3X4Y5Z6A',
        'user'
    ),
    (
        'Natalia',
        'Aguilar Soto',
        24,
        'natalia.aguilar@gmail.com',
        '2024-02-22 08:10:00',
        1,
        '$2y$10$R8S9T0U1V2W3X4Y5Z6A7B',
        'user'
    ),
    (
        'Fernando',
        'Iglesias Méndez',
        44,
        'fernando.iglesias@gmail.com',
        '2024-02-25 19:30:00',
        1,
        '$2y$10$S9T0U1V2W3X4Y5Z6A7B8C',
        'user'
    ),
    (
        'Beatriz',
        'Domínguez Lara',
        30,
        'beatriz.dominguez@gmail.com',
        '2024-02-28 10:00:00',
        1,
        '$2y$10$T0U1V2W3X4Y5Z6A7B8C9D',
        'user'
    );

-- ######################
INSERT INTO
    `202509_SHOP`.`products` (
        `title`,
        `price`,
        `quantity`,
        `status`
    )
VALUES
    -- Electrónicos
    (
        'iPhone 15 Pro 256GB',
        1199.99,
        45,
        1
    ),
    (
        'Samsung Galaxy S24 Ultra',
        1299.99,
        32,
        1
    ),
    (
        'MacBook Air M3 13"',
        1099.99,
        28,
        1
    ),
    (
        'Sony WH-1000XM5 Auriculares',
        349.99,
        67,
        1
    ),
    (
        'Apple Watch Series 9',
        399.99,
        53,
        1
    ),
    (
        'iPad Air 11" 128GB',
        749.99,
        41,
        1
    ),
    (
        'Bose QuietComfort 45',
        329.99,
        38,
        0
    ),
    (
        'Logitech MX Master 3S Ratón',
        99.99,
        89,
        1
    ),

-- Ropa y Moda
(
    'Chaqueta Denim Levi\'s 511',
    79.99,
    120,
    1
),
(
    'Zapatillas Nike Air Max 270',
    129.99,
    75,
    1
),
(
    'Camiseta Básica Algodón Pack x3',
    29.99,
    250,
    1
),
(
    'Reloj Casio G-Shock GA-2100',
    99.99,
    60,
    1
),
(
    'Bolso Bandolera Cuero Sintético',
    49.99,
    85,
    1
),
(
    'Gafas de Sol Ray-Ban Aviator',
    159.99,
    42,
    1
),
(
    'Chándal Adidas Tiro 23',
    89.99,
    55,
    0
),

-- Hogar y Cocina
(
    'Robot Aspirador Xiaomi Mi Robot',
    299.99,
    30,
    1
),
(
    'Freidora de Aire Philips XXL',
    149.99,
    62,
    1
),
(
    'Juego de Sartenes Antiadherentes',
    79.99,
    95,
    1
),
(
    'Máquina de Café Nespresso Vertuo',
    199.99,
    40,
    1
),
(
    'Altavoz Inteligente Amazon Echo',
    99.99,
    110,
    1
),

-- Deportes y Aire Libre
(
    'Bicicleta Montaña Trek Marlin 5',
    649.99,
    18,
    1
),
(
    'Zapatillas Running Asics Gel-Nimbus',
    139.99,
    47,
    1
),
(
    'Tienda de Campaña 4 Personas',
    199.99,
    25,
    1
),
(
    'Mochila Trekking 40L Impermeable',
    79.99,
    70,
    1
),

-- Libros y Oficina
(
    'Tableta Gráfica Wacom Intuos',
    89.99,
    65,
    1
),
(
    'Kindle Paperwhite 11ª Gen',
    139.99,
    88,
    1
),
(
    'Monitor Dell 27" 4K U2723QE',
    699.99,
    22,
    1
),

-- Belleza y Cuidado
(
    'Secador Dyson Supersonic',
    429.99,
    33,
    1
),
(
    'Cepillo Dental Eléctrico Oral-B',
    89.99,
    140,
    1
),
(
    'Set Maquillaje Profesional 24 colores',
    59.99,
    105,
    0
),

-- Videojuegos
(
    'PlayStation 5 Edición Digital',
    399.99,
    15,
    1
),
(
    'Nintendo Switch OLED',
    349.99,
    27,
    1
),
(
    'Xbox Series X 1TB',
    499.99,
    19,
    1
);