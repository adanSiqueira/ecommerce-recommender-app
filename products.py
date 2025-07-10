import pandas as pd

products = [
    {
        'id': 1,
        'name': 'Camiseta de Futebol Brasil Masculino',
        'type': 'Roupa',
        'category': 'Esportes',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': 'Padrão',
        'season': 'Geral',
        'price': 89.90,
        'image': 'https://dummyimage.com/150x150/007bff/ffffff&text=Brasil+M'
    },
    {
        'id': 2,
        'name': 'Camiseta de Futebol Brasil Feminino',
        'type': 'Roupa',
        'category': 'Esportes',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': 'Padrão',
        'season': 'Geral',
        'price': 89.90,
        'image': 'https://dummyimage.com/150x150/f54291/ffffff&text=Brasil+F'
    },
    {
        'id': 3,
        'name': 'Chuteira Futebol',
        'type': 'Calçado',
        'category': 'Esportes',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'sizes': [37, 38, 39, 40, 41, 42, 43, 44],
        'color': 'Preto',
        'price': 219.90,
        'image': 'https://dummyimage.com/150x150/222222/ffffff&text=Chuteira'
    },
    {
        'id': 4,
        'name': 'Teclado Gamer',
        'type': 'Acessório',
        'category': 'Gamer',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 149.90,
        'image': 'https://dummyimage.com/150x150/000000/ffffff&text=Teclado'
    },
    {
        'id': 5,
        'name': 'Camiseta Dragon Ball',
        'type': 'Roupa',
        'category': 'Nerd',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': 'Padrão',
        'season': 'Geral',
        'price': 79.90,
        'image': 'https://dummyimage.com/150x150/ffcc00/000000&text=DBZ'
    },
    {
        'id': 6,
        'name': 'Camiseta de Basquete Masculino',
        'type': 'Roupa',
        'category': 'Esportes',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': 'Padrão',
        'season': 'Geral',
        'price': 89.90,
        'image': 'https://dummyimage.com/150x150/0000ff/ffffff&text=Basquete+M'
    },
    {
        'id': 7,
        'name': 'Camiseta de Basquete Feminino',
        'type': 'Roupa',
        'category': 'Esportes',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': 'Padrão',
        'season': 'Geral',
        'price': 89.90,
        'image': 'https://dummyimage.com/150x150/ff69b4/ffffff&text=Basquete+F'
    },
    {
        'id': 8,
        'name': 'Bermuda de Basquete Masculino',
        'type': 'Roupa',
        'category': 'Esportes',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': 'Padrão',
        'season': 'Geral',
        'price': 59.90,
        'image': 'https://dummyimage.com/150x150/1e90ff/ffffff&text=Bermuda+M'
    },
    {
        'id': 9,
        'name': 'Bermuda de Basquete Feminino',
        'type': 'Roupa',
        'category': 'Esportes',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': 'Padrão',
        'season': 'Geral',
        'price': 59.90,
        'image': 'https://dummyimage.com/150x150/ff69b4/ffffff&text=Bermuda+F'
    },
    {
        'id': 10,
        'name': 'Tênis de Corrida Masculino',
        'type': 'Calçado',
        'category': 'Esportes',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': [38, 39, 40, 41, 42, 43, 44],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'price': 259.90,
        'image': 'https://dummyimage.com/150x150/000000/ffffff&text=Tenis+M'
    },
    {
        'id': 11,
        'name': 'Tênis de Corrida Feminino',
        'type': 'Calçado',
        'category': 'Esportes',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': [34, 35, 36, 37, 38],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'price': 259.90,
        'image': 'https://dummyimage.com/150x150/ff69b4/ffffff&text=Tenis+F'
    },
    {
        'id': 12,
        'name': 'Luva de Boxe Adulto',
        'type': 'Acessório',
        'category': 'Esportes',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 129.90,
        'image': 'https://dummyimage.com/150x150/800000/ffffff&text=Luva+Adulto'
    },
    {
        'id': 13,
        'name': 'Luva de Boxe Infantil',
        'type': 'Acessório',
        'category': 'Esportes',
        'gender': 'Unissex',
        'age_group': 'Infantil',
        'color': 'Padrão',
        'price': 99.90,
        'image': 'https://dummyimage.com/150x150/ff9999/000000&text=Luva+Infantil'
    },
    {
        'id': 14,
        'name': 'Bola de Basquete',
        'type': 'Acessório',
        'category': 'Esportes',
        'gender': 'Unissex',
        'age_group': 'Todas',
        'color': 'Padrão',
        'price': 89.90,
        'image': 'https://dummyimage.com/150x150/a0522d/ffffff&text=Basquete'
    },
    {
        'id': 15,
        'name': 'Bola de Futebol',
        'type': 'Acessório',
        'category': 'Esportes',
        'gender': 'Unissex',
        'age_group': 'Todas',
        'color': 'Padrão',
        'price': 89.90,
        'image': 'https://dummyimage.com/150x150/006400/ffffff&text=Futebol'
    },
    {
        'id': 16,
        'name': 'Kimono Adulto',
        'type': 'Acessório',
        'category': 'Esportes',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 159.90,
        'image': 'https://dummyimage.com/150x150/00008b/ffffff&text=Kimono+A'
    },
    {
        'id': 17,
        'name': 'Kimono Infantil',
        'type': 'Acessório',
        'category': 'Esportes',
        'gender': 'Unissex',
        'age_group': 'Infantil',
        'color': 'Padrão',
        'price': 129.90,
        'image': 'https://dummyimage.com/150x150/1e90ff/ffffff&text=Kimono+I'
    },
    {
        'id': 18,
        'name': 'Óculos de Natação',
        'type': 'Acessório',
        'category': 'Esportes',
        'gender': 'Unissex',
        'age_group': 'Todas',
        'color': 'Padrão',
        'price': 49.90,
        'image': 'https://dummyimage.com/150x150/4682b4/ffffff&text=Óculos'
    },
    {
        'id': 19,
        'name': 'Bicicleta Adulto',
        'type': 'Acessório',
        'category': 'Esportes',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'price': 799.90,
        'image': 'https://dummyimage.com/150x150/ff8c00/ffffff&text=Bicicleta'
    },
    {
        'id': 20,
        'name': 'Cadeira Escritório',
        'type': 'Acessório',
        'category': 'Casa e Decoração',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'price': 449.90,
        'image': 'https://dummyimage.com/150x150/808080/ffffff&text=Cadeira'
    },
    {
        'id': 21,
        'name': 'Quadro Futebol',
        'type': 'Acessório',
        'category': 'Casa e Decoração',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 79.90,
        'image': 'https://dummyimage.com/150x150/2f4f4f/ffffff&text=Futebol'
    },
    {
        'id': 22,
        'name': 'Quadro Paisagem',
        'type': 'Acessório',
        'category': 'Casa e Decoração',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 79.90,
        'image': 'https://dummyimage.com/150x150/3cb371/ffffff&text=Paisagem'
    },
    {
        'id': 23,
        'name': 'Quadro Desenho',
        'type': 'Acessório',
        'category': 'Casa e Decoração',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 79.90,
        'image': 'https://dummyimage.com/150x150/dda0dd/000000&text=Desenho'
    },
    {
        'id': 24,
        'name': 'Jogo de Cama',
        'type': 'Acessório',
        'category': 'Casa e Decoração',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'price': 199.90,
        'image': 'https://dummyimage.com/150x150/f5f5f5/000000&text=Cama'
    },
    {
        'id': 25,
        'name': 'Headset Gamer',
        'type': 'Acessório',
        'category': 'Gamer',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 179.90,
        'image': 'https://dummyimage.com/150x150/800080/ffffff&text=Headset'
    },
    {
        'id': 26,
        'name': 'Mousepad Gamer',
        'type': 'Acessório',
        'category': 'Gamer',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 49.90,
        'image': 'https://dummyimage.com/150x150/4b0082/ffffff&text=Mousepad'
    },
    {
        'id': 27,
        'name': 'Joystick',
        'type': 'Acessório',
        'category': 'Gamer',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 139.90,
        'image': 'https://dummyimage.com/150x150/000000/ffffff&text=Joystick'
    },
    {
        'id': 28,
        'name': 'Cadeira Gamer',
        'type': 'Acessório',
        'category': 'Gamer',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'price': 599.90,
        'image': 'https://dummyimage.com/150x150/ff0000/ffffff&text=Cadeira+Gamer'
    },
    {
        'id': 29,
        'name': 'Pista Carrinho Hotweels',
        'type': 'Acessório',
        'category': 'Brinquedos',
        'gender': 'Unissex',
        'age_group': 'Infantil',
        'color': 'Padrão',
        'price': 119.90,
        'image': 'https://dummyimage.com/150x150/f4a460/000000&text=Pista'
    },
    {
        'id': 30,
        'name': 'Carrinho Hotweels Miniatura',
        'type': 'Acessório',
        'category': 'Brinquedos',
        'gender': 'Masculino',
        'age_group': 'Infantil',
        'color': 'Padrão',
        'price': 29.90,
        'image': 'https://dummyimage.com/150x150/b22222/ffffff&text=Carrinho'
    },
    {
        'id': 31,
        'name': 'Boneca Barbie',
        'type': 'Acessório',
        'category': 'Brinquedos',
        'gender': 'Feminino',
        'age_group': 'Infantil',
        'color': 'Padrão',
        'price': 59.90,
        'image': 'https://dummyimage.com/150x150/ffc0cb/000000&text=Barbie'
    },
    {
        'id': 32,
        'name': 'Caderno Heróis',
        'type': 'Acessório',
        'category': 'Brinquedos',
        'gender': 'Masculino',
        'age_group': 'Infantil',
        'color': 'Padrão',
        'price': 19.90,
        'image': 'https://dummyimage.com/150x150/0000cd/ffffff&text=Heróis'
    },
    {
        'id': 33,
        'name': 'Caderno Princesas',
        'type': 'Acessório',
        'category': 'Brinquedos',
        'gender': 'Feminino',
        'age_group': 'Infantil',
        'color': 'Padrão',
        'price': 19.90,
        'image': 'https://dummyimage.com/150x150/ff69b4/ffffff&text=Princesas'
    },
    {
        'id': 34,
        'name': 'Hortelã',
        'type': 'Acessório',
        'category': 'Plantas',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 12.90,
        'image': 'https://dummyimage.com/150x150/228b22/ffffff&text=Hortelã'
    },
    {
        'id': 35,
        'name': 'Samambaia',
        'type': 'Acessório',
        'category': 'Plantas',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 29.90,
        'image': 'https://dummyimage.com/150x150/006400/ffffff&text=Samambaia'
    },
    {
        'id': 36,
        'name': 'Terra',
        'type': 'Acessório',
        'category': 'Plantas',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 9.90,
        'image': 'https://dummyimage.com/150x150/8b4513/ffffff&text=Terra'
    },
    {
        'id': 37,
        'name': 'Semente de Girassol',
        'type': 'Acessório',
        'category': 'Plantas',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 4.90,
        'image': 'https://dummyimage.com/150x150/ffff00/000000&text=Girassol'
    },
    {
        'id': 38,
        'name': 'Adubos',
        'type': 'Acessório',
        'category': 'Plantas',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 14.90,
        'image': 'https://dummyimage.com/150x150/556b2f/ffffff&text=Adubo'
    },
    {
        'id': 39,
        'name': 'Orquídeas',
        'type': 'Acessório',
        'category': 'Plantas',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 49.90,
        'image': 'https://dummyimage.com/150x150/dda0dd/000000&text=Orquídea'
    },
    {
        'id': 40,
        'name': 'Vaso de Cerâmica',
        'type': 'Acessório',
        'category': 'Plantas',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 24.90,
        'image': 'https://dummyimage.com/150x150/b22222/ffffff&text=Vaso'
    },
    {
        'id': 41,
        'name': 'Suporte de parede para plantas',
        'type': 'Acessório',
        'category': 'Plantas',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 39.90,
        'image': 'https://dummyimage.com/150x150/8b0000/ffffff&text=Suporte'
    },
    {
        'id': 42,
        'name': 'Fertilizante',
        'type': 'Acessório',
        'category': 'Plantas',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'color': 'Padrão',
        'price': 19.90,
        'image': 'https://dummyimage.com/150x150/9acd32/000000&text=Fertilizante'
    },
    {
        'id': 43,
        'name': 'Camiseta Marvel',
        'type': 'Roupa',
        'category': 'Nerd',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': 'Padrão',
        'season': 'Geral',
        'price': 79.90,
        'image': 'https://dummyimage.com/150x150/ff0000/ffffff&text=Marvel'
    },
    {
        'id': 44,
        'name': 'Camiseta Batman',
        'type': 'Roupa',
        'category': 'Nerd',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': 'Padrão',
        'season': 'Geral',
        'price': 79.90,
        'image': 'https://dummyimage.com/150x150/000000/ffffff&text=Batman'
    },
    {
        'id': 45,
        'name': 'Jogo de Cartas Pokémon',
        'type': 'Acessório',
        'category': 'Nerd',
        'gender': 'Unissex',
        'age_group': 'Todas',
        'color': 'Padrão',
        'price': 59.90,
        'image': 'https://dummyimage.com/150x150/ffd700/000000&text=Pokemon'
    },
    {
        'id': 46,
        'name': 'Almofada Desenho',
        'type': 'Acessório',
        'category': 'Nerd',
        'gender': 'Unissex',
        'age_group': 'Todas',
        'color': 'Padrão',
        'price': 39.90,
        'image': 'https://dummyimage.com/150x150/8a2be2/ffffff&text=Almofada'
    },
    {
        'id': 47,
        'name': 'Camisa Básica Masculino',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 49.90,
        'image': 'https://dummyimage.com/150x150/0000ff/ffffff&text=Básica+M'
    },
    {
        'id': 48,
        'name': 'Camisa Básica Feminino',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 49.90,
        'image': 'https://dummyimage.com/150x150/ff69b4/000000&text=Básica+F'
    },
    {
        'id': 49,
        'name': 'Camisa Social Masculino',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 99.90,
        'image': 'https://dummyimage.com/150x150/191970/ffffff&text=Social+M'
    },
    {
        'id': 50,
        'name': 'Camisa Social Feminino',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 99.90,
        'image': 'https://dummyimage.com/150x150/ffb6c1/000000&text=Social+F'
    },
    {
        'id': 51,
        'name': 'Bermuda',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Verão',
        'price': 59.90,
        'image': 'https://dummyimage.com/150x150/2e8b57/ffffff&text=Bermuda'
    },
    {
        'id': 52,
        'name': 'Calça Masculino',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 89.90,
        'image': 'https://dummyimage.com/150x150/696969/ffffff&text=Calça+M'
    },
    {
        'id': 53,
        'name': 'Calça Feminino',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 89.90,
        'image': 'https://dummyimage.com/150x150/d87093/000000&text=Calça+F'
    },
    {
        'id': 54,
        'name': 'Vestido',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Verão',
        'price': 119.90,
        'image': 'https://dummyimage.com/150x150/f08080/000000&text=Vestido'
    },
    {
        'id': 55,
        'name': 'Saia',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Verão',
        'price': 69.90,
        'image': 'https://dummyimage.com/150x150/ff69b4/ffffff&text=Saia'
    },
    {
        'id': 56,
        'name': 'Cueca',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 19.90,
        'image': 'https://dummyimage.com/150x150/000000/ffffff&text=Cueca'
    },
    {
        'id': 57,
        'name': 'Calcinha',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 19.90,
        'image': 'https://dummyimage.com/150x150/f4a460/000000&text=Calcinha'
    },
    {
        'id': 58,
        'name': 'Meias',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 14.90,
        'image': 'https://dummyimage.com/150x150/808080/ffffff&text=Meias'
    },
    {
        'id': 59,
        'name': 'Bota',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Feminino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Inverno',
        'price': 199.90,
        'image': 'https://dummyimage.com/150x150/8b4513/ffffff&text=Bota'
    },
    {
        'id': 60,
        'name': 'Cachecol',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Inverno',
        'price': 39.90,
        'image': 'https://dummyimage.com/150x150/2f4f4f/ffffff&text=Cachecol'
    },
    {
        'id': 61,
        'name': 'Luvas Adulto',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Unissex',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Inverno',
        'price': 24.90,
        'image': 'https://dummyimage.com/150x150/708090/ffffff&text=Luvas+Adulto'
    },
    {
        'id': 62,
        'name': 'Luvas Infantil',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Unissex',
        'age_group': 'Infantil',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Inverno',
        'price': 19.90,
        'image': 'https://dummyimage.com/150x150/87cefa/000000&text=Luvas+Infantil'
    },
    {
        'id': 63,
        'name': 'Camisa Pólo Masculina',
        'type': 'Roupa',
        'category': 'Moda',
        'gender': 'Masculino',
        'age_group': 'Adulto',
        'sizes': ['P', 'M', 'G'],
        'color': ['Preto', 'Branco', 'Azul', 'Rosa', 'Verde'],
        'season': 'Geral',
        'price': 79.90,
        'image': 'https://dummyimage.com/150x150/4682b4/ffffff&text=Polo+M'
    },
    {
    "id": 64,
    "name": "Calça de Moletom",
    "type": "Roupa",
    "category": "Esportes",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 54.54,
    "image": "https://dummyimage.com/150x150/472000/ffffff&text=P64"
  },
  {
    "id": 65,
    "name": "Suéter",
    "type": "Roupa",
    "category": "Moda",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 58.93,
    "image": "https://dummyimage.com/150x150/109000/ffffff&text=P65"
  },
  {
    "id": 66,
    "name": "  Blusa de Moletom",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 136.86,
    "image": "https://dummyimage.com/150x150/264000/ffffff&text=P66"
  },
  {
    "id": 67,
    "name": "Calça de Moletom",
    "type": "Roupa",
    "category": "Esportes",
    "gender": "Masculino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 97.57,
    "image": "https://dummyimage.com/150x150/162000/ffffff&text=P67"
  },
  {
    "id": 68,
    "name": "Touca",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Unissex",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 80.23,
    "image": "https://dummyimage.com/150x150/429000/ffffff&text=P68"
  },
  {
    "id": 69,
    "name": "Calça de Moletom",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 184.12,
    "image": "https://dummyimage.com/150x150/761000/ffffff&text=P69"
  },
  {
    "id": 70,
    "name": "Touca",
    "type": "Roupa",
    "category": "Moda",
    "gender": "Masculino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 159.58,
    "image": "https://dummyimage.com/150x150/368000/ffffff&text=P70"
  },
  {
    "id": 71,
    "name": "  Blusa de Moletom",
    "type": "Roupa",
    "category": "Moda",
    "gender": "Feminino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 85.28,
    "image": "https://dummyimage.com/150x150/735000/ffffff&text=P71"
  },
  {
    "id": 72,
    "name": "Touca",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 131.55,
    "image": "https://dummyimage.com/150x150/187000/ffffff&text=P72"
  },
  {
    "id": 73,
    "name": "Suéter",
    "type": "Roupa",
    "category": "Moda",
    "gender": "Masculino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 124.89,
    "image": "https://dummyimage.com/150x150/380000/ffffff&text=P73"
  },
  {
    "id": 74,
    "name": "  Blusa de Moletom",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Masculino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 151.25,
    "image": "https://dummyimage.com/150x150/748000/ffffff&text=P74"
  },
  {
    "id": 75,
    "name": "Touca",
    "type": "Roupa",
    "category": "Moda",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 180.97,
    "image": "https://dummyimage.com/150x150/812000/ffffff&text=P75"
  },
  {
    "id": 76,
    "name": "  Blusa de Moletom",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 110.32,
    "image": "https://dummyimage.com/150x150/503000/ffffff&text=P76"
  },
  {
    "id": 77,
    "name": "Sobretudo",
    "type": "Roupa",
    "category": "Moda",
    "gender": "Feminino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 66.27,
    "image": "https://dummyimage.com/150x150/424000/ffffff&text=P77"
  },
  {
    "id": 78,
    "name": "Suéter",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Feminino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 133.36,
    "image": "https://dummyimage.com/150x150/427000/ffffff&text=P78"
  },
  {
    "id": 79,
    "name": "Sobretudo",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 74.72,
    "image": "https://dummyimage.com/150x150/679000/ffffff&text=P79"
  },
  {
    "id": 80,
    "name": "Touca",
    "type": "Roupa",
    "category": "Esportes",
    "gender": "Masculino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 151.89,
    "image": "https://dummyimage.com/150x150/768000/ffffff&text=P80"
  },
  {
    "id": 81,
    "name": "Suéter",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Feminino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 124.5,
    "image": "https://dummyimage.com/150x150/540000/ffffff&text=P81"
  },
  {
    "id": 82,
    "name": "Suéter",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Feminino",
    "age_group": "Infantil",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 89.28,
    "image": "https://dummyimage.com/150x150/403000/ffffff&text=P82"
  },
  {
    "id": 83,
    "name": "Touca",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Feminino",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 120.91,
    "image": "https://dummyimage.com/150x150/738000/ffffff&text=P83"
  },
  {
    "id": 84,
    "name": "Macacão do Ursinho Pooh",
    "type": "Roupa",
    "category": "Nerd",
    "gender": "Feminino",
    "age_group": "Adulto",
    "sizes": [
      "P",
      "M",
      "G"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Inverno",
    "price": 142.91,
    "image": "https://dummyimage.com/150x150/738000/ffffff&text=P83"
  },
  {
    "id": 85,
    "name": "Tenis Mizuno One",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 70.78,
    "image": "https://dummyimage.com/150x150/906000/ffffff&text=P85"
  },
  {
    "id": 86,
    "name": "Tenis Olympicus Top",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 160.8,
    "image": "https://dummyimage.com/150x150/625000/ffffff&text=P86"
  },
  {
    "id": 87,
    "name": "Tenis UnderArmour Casual",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 114.94,
    "image": "https://dummyimage.com/150x150/859000/ffffff&text=P87"
  },
  {
    "id": 88,
    "name": "Tenis Mizuno Strong",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "37",
      "38",
      "39",
      "40",
      "41",
      "42",
      "43",
      "44"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 90.2,
    "image": "https://dummyimage.com/150x150/347000/ffffff&text=P88"
  },
  {
    "id": 89,
    "name": "Tenis Adidas One",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 189.74,
    "image": "https://dummyimage.com/150x150/457000/ffffff&text=P89"
  },
  {
    "id": 90,
    "name": "Tenis Adidas One",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Feminino",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 74.31,
    "image": "https://dummyimage.com/150x150/567000/ffffff&text=P90"
  },
  {
    "id": 91,
    "name": "Tenis Olympicus Strong",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Feminino",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 172.41,
    "image": "https://dummyimage.com/150x150/621000/ffffff&text=P91"
  },
  {
    "id": 92,
    "name": "Tenis Rebook AirFlow",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "37",
      "38",
      "39",
      "40",
      "41",
      "42",
      "43",
      "44"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 52.06,
    "image": "https://dummyimage.com/150x150/289000/ffffff&text=P92"
  },
  {
    "id": 93,
    "name": "Tenis Olympicus Performance",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Feminino",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 165.39,
    "image": "https://dummyimage.com/150x150/734000/ffffff&text=P93"
  },
  {
    "id": 94,
    "name": "Tenis Adidas AirFlow",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 104.12,
    "image": "https://dummyimage.com/150x150/860000/ffffff&text=P94"
  },
  {
    "id": 95,
    "name": "Tenis Mizuno AirFlow",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 165.97,
    "image": "https://dummyimage.com/150x150/593000/ffffff&text=P95"
  },
  {
    "id": 96,
    "name": "Tenis Mizuno TheBest",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 198.34,
    "image": "https://dummyimage.com/150x150/728000/ffffff&text=P96"
  },
  {
    "id": 97,
    "name": "Tenis Adidas Top",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Feminino",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 198.77,
    "image": "https://dummyimage.com/150x150/537000/ffffff&text=P97"
  },
  {
    "id": 98,
    "name": "Tenis Asics Top",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 175.77,
    "image": "https://dummyimage.com/150x150/730000/ffffff&text=P98"
  },
  {
    "id": 99,
    "name": "Tenis UnderArmour AirFlow",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 180.96,
    "image": "https://dummyimage.com/150x150/519000/ffffff&text=P99"
  },
  {
    "id": 100,
    "name": "Tenis Mizuno Ultra",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Feminino",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 192.91,
    "image": "https://dummyimage.com/150x150/436000/ffffff&text=P100"
  },
  {
    "id": 101,
    "name": "Tenis Jordan Top",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "37",
      "38",
      "39",
      "40",
      "41",
      "42",
      "43",
      "44"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 106.58,
    "image": "https://dummyimage.com/150x150/659000/ffffff&text=P101"
  },
  {
    "id": 102,
    "name": "Tenis Jordan TheBest",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "37",
      "38",
      "39",
      "40",
      "41",
      "42",
      "43",
      "44"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 196.61,
    "image": "https://dummyimage.com/150x150/158000/ffffff&text=P102"
  },
  {
    "id": 103,
    "name": "Tenis Rebook AirFlow",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Unissex",
    "age_group": "Adulto",
    "sizes": [
      "33",
      "34",
      "35",
      "36",
      "37"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 141.67,
    "image": "https://dummyimage.com/150x150/324000/ffffff&text=P103"
  },
  {
    "id": 104,
    "name": "Tenis Rebook Max",
    "type": "Calçado",
    "category": "Esportes",
    "gender": "Masculino",
    "age_group": "Adulto",
    "sizes": [
      "37",
      "38",
      "39",
      "40",
      "41",
      "42",
      "43",
      "44"
    ],
    "color": [
      "Preto",
      "Branco",
      "Azul",
      "Rosa",
      "Verde"
    ],
    "season": "Geral",
    "price": 55.43,
    "image": "https://dummyimage.com/150x150/587000/ffffff&text=P104"
  }
]

produtos = pd.DataFrame(products)
products = produtos.to_csv('products.csv', )