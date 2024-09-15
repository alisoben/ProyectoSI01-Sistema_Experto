# base_conocimiento.py

comidas = [
    # Desayunos
    {
        "nombre": "Avena con leche de almendra y frutas",
        "calorias": 250,
        "carbohidratos": 40,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "sin lactosa", "bajo en sodio", "orgánico"],
        "observaciones": "Alto en fibra, bajo en sodio, ideal para un desayuno ligero."
    },
    {
        "nombre": "Tostadas de aguacate con huevo",
        "calorias": 350,
        "carbohidratos": 25,
        "proteinas": 12,
        "sodio": 80,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "sin gluten"],
        "observaciones": "Ideal para personas con bajo requerimiento de carbohidratos, alto en grasas saludables."
    },
    {
        "nombre": "Smoothie verde de espinacas y proteína vegetal",
        "calorias": 180,
        "carbohidratos": 20,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "desayuno",
        "categorias": ["vegano", "bajo en carbohidratos", "sin gluten", "orgánico"],
        "observaciones": "Bajo en calorías y carbohidratos, ideal para dietas veganas y bajas en carbohidratos."
    },
    {
        "nombre": "Panqueques de avena con frutas",
        "calorias": 300,
        "carbohidratos": 50,
        "proteinas": 10,
        "sodio": 30,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "dieta andina"],
        "observaciones": "Alto en carbohidratos complejos y fibra, adecuado para un desayuno energético."
    },
    {
        "nombre": "Tortilla de espinacas con champiñones",
        "calorias": 250,
        "carbohidratos": 10,
        "proteinas": 20,
        "sodio": 60,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Ideal para una dieta baja en carbohidratos, alto en proteínas."
    },
    {
        "nombre": "Batido de avena, plátano y mantequilla de maní",
        "calorias": 350,
        "carbohidratos": 45,
        "proteinas": 12,
        "sodio": 20,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "dieta criolla"],
        "observaciones": "Alto en energía, ideal para comenzar el día y adecuado para dieta criolla."
    },
    {
        "nombre": "Tostadas integrales con queso cottage y fresas",
        "calorias": 300,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 70,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "sin lactosa"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para hipertensión y sin lactosa."
    },
    {
        "nombre": "Omelette de claras de huevo con espinacas y champiñones",
        "calorias": 200,
        "carbohidratos": 5,
        "proteinas": 18,
        "sodio": 60,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Ideal para personas con hipertensión o que siguen una dieta baja en carbohidratos."
    },
    {
        "nombre": "Pan de centeno con palta y semillas de chía",
        "calorias": 280,
        "carbohidratos": 35,
        "proteinas": 6,
        "sodio": 40,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "vegano", "dieta andina", "bajo en sodio"],
        "observaciones": "Rico en ácidos grasos saludables y bajo en sodio."
    },
    {
        "nombre": "Smoothie de piña y espinaca con proteína de guisante",
        "calorias": 220,
        "carbohidratos": 35,
        "proteinas": 15,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "orgánico"],
        "observaciones": "Ideal para un desayuno ligero, bajo en calorías y adecuado para veganos."
    },
    {
        "nombre": "Muffins de zanahoria y avena sin azúcar",
        "calorias": 250,
        "carbohidratos": 40,
        "proteinas": 8,
        "sodio": 30,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "bajo en sodio", "vegetariano"],
        "observaciones": "Perfecto para personas con enfermedad celíaca y bajo en sodio."
    },
    {
        "nombre": "Pan de plátano sin gluten con almendras",
        "calorias": 300,
        "carbohidratos": 45,
        "proteinas": 7,
        "sodio": 20,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "sin lactosa", "orgánico"],
        "observaciones": "Adecuado para personas con intolerancia al gluten y la lactosa."
    },
    {
        "nombre": "Quinoa con leche de coco y frutas",
        "calorias": 320,
        "carbohidratos": 50,
        "proteinas": 6,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin lactosa", "dieta andina", "orgánico"],
        "observaciones": "Alto en fibra y antioxidantes, ideal para un desayuno saludable."
    },
    {
        "nombre": "Crepes de avena y cacao sin azúcar",
        "calorias": 280,
        "carbohidratos": 50,
        "proteinas": 8,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "sin lactosa", "vegetariano"],
        "observaciones": "Ideal para personas con intolerancia a la lactosa y el gluten."
    },
    {
        "nombre": "Arepas de maíz con queso de cabra y aguacate",
        "calorias": 350,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 70,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "vegetariano", "dieta criolla"],
        "observaciones": "Rico en fibra y grasas saludables, sin gluten."
    },
    {
        "nombre": "Tortilla de claras de huevo con champiñones y cebolla",
        "calorias": 200,
        "carbohidratos": 5,
        "proteinas": 18,
        "sodio": 40,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Ideal para desarrollo muscular y bajo en carbohidratos, apto para hipertensión."
    },
    {
        "nombre": "Batido de espinacas, plátano y proteína de suero",
        "calorias": 250,
        "carbohidratos": 35,
        "proteinas": 20,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para una vida saludable."
    },
    {
        "nombre": "Pan integral con aguacate y tomate",
        "calorias": 280,
        "carbohidratos": 40,
        "proteinas": 6,
        "sodio": 30,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio", "orgánico"],
        "observaciones": "Ideal para una dieta vegetariana, bajo en sodio y adecuado para hipertensión."
    },
    {
        "nombre": "Arepas de maíz con huevo y palta",
        "calorias": 350,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 70,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "vegetariano", "dieta criolla"],
        "observaciones": "Rico en fibra y grasas saludables, adecuado para bajar de peso."
    },
    {
        "nombre": "Smoothie de piña, espinaca y chía",
        "calorias": 200,
        "carbohidratos": 35,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "bajo en carbohidratos", "orgánico"],
        "observaciones": "Ideal para una vida saludable y bajo en carbohidratos."
    },
    {
        "nombre": "Porridge de avena con semillas de linaza",
        "calorias": 320,
        "carbohidratos": 45,
        "proteinas": 10,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio", "orgánico"],
        "observaciones": "Alto en fibra, ideal para el control del colesterol."
    },
    {
        "nombre": "Tostadas de aguacate y huevo duro",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 12,
        "sodio": 60,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Alto en proteínas y grasas saludables, adecuado para una dieta baja en carbohidratos."
    },
    {
        "nombre": "Panqueques de quinua con arándanos",
        "calorias": 330,
        "carbohidratos": 50,
        "proteinas": 10,
        "sodio": 30,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "vegetariano", "dieta andina"],
        "observaciones": "Ideal para personas con enfermedad celíaca, rico en antioxidantes."
    },
    {
        "nombre": "Pudding de chía con leche de coco y mango",
        "calorias": 240,
        "carbohidratos": 25,
        "proteinas": 8,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin lactosa", "bajo en sodio", "orgánico"],
        "observaciones": "Adecuado para intolerancia a la lactosa, bajo en sodio."
    },
    {
        "nombre": "Tostadas de centeno con queso ricotta y espinacas",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 15,
        "sodio": 50,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Ideal para hipertensión, rico en proteínas y bajo en sodio."
    },
    {
        "nombre": "Avena con leche de avena y moras",
        "calorias": 250,
        "carbohidratos": 40,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin lactosa", "sin gluten", "orgánico"],
        "observaciones": "Rico en fibra, sin gluten ni lactosa, ideal para vida saludable."
    },
    {
        "nombre": "Pan integral con aguacate y semillas de sésamo",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 8,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "orgánico"],
        "observaciones": "Bajo en sodio, ideal para personas con hipertensión."
    },
    {
        "nombre": "Batido de fresas con avena y espinacas",
        "calorias": 220,
        "carbohidratos": 35,
        "proteinas": 10,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin lactosa", "sin gluten", "bajo en sodio"],
        "observaciones": "Ideal para una vida saludable, bajo en sodio y sin gluten."
    },
    {
        "nombre": "Arepas de maíz con queso de cabra y cilantro",
        "calorias": 350,
        "carbohidratos": 45,
        "proteinas": 12,
        "sodio": 50,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "vegetariano", "dieta criolla"],
        "observaciones": "Rico en carbohidratos complejos, ideal para una dieta criolla."
    },
    {
        "nombre": "Smoothie de mango, chía y espinaca",
        "calorias": 200,
        "carbohidratos": 40,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin lactosa", "sin gluten", "orgánico"],
        "observaciones": "Alto en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Pan de trigo integral con huevo pochado y espinacas",
        "calorias": 280,
        "carbohidratos": 35,
        "proteinas": 12,
        "sodio": 30,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Ideal para personas con hipertensión y control de colesterol."
    },
    {
        "nombre": "Crepes de harina de almendra con arándanos",
        "calorias": 270,
        "carbohidratos": 20,
        "proteinas": 10,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Adecuado para una dieta baja en carbohidratos y sin gluten."
    },
    {
        "nombre": "Tostadas de aguacate con tomates cherry y espárragos",
        "calorias": 300,
        "carbohidratos": 40,
        "proteinas": 8,
        "sodio": 20,
        "tipo": "desayuno",
        "categorias": ["vegano", "vegetariano", "sin lactosa", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Bowl de acai con frutas y granola sin gluten",
        "calorias": 280,
        "carbohidratos": 50,
        "proteinas": 5,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "vegano", "sin gluten", "orgánico"],
        "observaciones": "Rico en antioxidantes, ideal para una dieta sin gluten."
    },
    {
        "nombre": "Porridge de quinua con frutos secos",
        "calorias": 320,
        "carbohidratos": 50,
        "proteinas": 8,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "vegetariano", "dieta andina"],
        "observaciones": "Ideal para una dieta andina, alto en fibra y sin gluten."
    },
    {
        "nombre": "Batido de almendras con plátano y espirulina",
        "calorias": 200,
        "carbohidratos": 35,
        "proteinas": 8,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "orgánico"],
        "observaciones": "Rico en antioxidantes y proteínas vegetales, ideal para una vida saludable."
    },
    {
        "nombre": "Pancakes de avena y claras de huevo con fresas",
        "calorias": 300,
        "carbohidratos": 45,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Alto en proteínas y bajo en sodio, adecuado para hipertensión."
    },
    {
        "nombre": "Smoothie bowl de mango, espinacas y chía",
        "calorias": 220,
        "carbohidratos": 35,
        "proteinas": 8,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Tostadas de pan integral con palta y queso cottage",
        "calorias": 300,
        "carbohidratos": 40,
        "proteinas": 12,
        "sodio": 30,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "orgánico"],
        "observaciones": "Bajo en sodio y alto en proteínas, ideal para hipertensión."
    },
    {
        "nombre": "Yogur de coco con granola de quinoa y arándanos",
        "calorias": 280,
        "carbohidratos": 40,
        "proteinas": 10,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "dieta andina"],
        "observaciones": "Rico en antioxidantes y fibra, ideal para una dieta andina."
    },
    {
        "nombre": "Omelette de espinacas con champiñones y tomate",
        "calorias": 250,
        "carbohidratos": 8,
        "proteinas": 20,
        "sodio": 20,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Ideal para hipertensión y desarrollo muscular."
    },
    {
        "nombre": "Pan de centeno con mermelada de frutas sin azúcar",
        "calorias": 220,
        "carbohidratos": 50,
        "proteinas": 4,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Ideal para personas con enfermedad celíaca y bajo contenido de sodio."
    },
    {
        "nombre": "Crepes de harina de arroz con mantequilla de almendras",
        "calorias": 300,
        "carbohidratos": 45,
        "proteinas": 12,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Adecuado para personas con intolerancia a la lactosa y que siguen una dieta baja en carbohidratos."
    },
    {
        "nombre": "Batido de arándanos, plátano y espinacas",
        "calorias": 210,
        "carbohidratos": 35,
        "proteinas": 8,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin lactosa", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y rico en antioxidantes, ideal para hipertensión."
    },
    {
        "nombre": "Tostadas de pan integral con aguacate y huevo duro",
        "calorias": 280,
        "carbohidratos": 30,
        "proteinas": 12,
        "sodio": 30,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Alto en proteínas y bajo en sodio, adecuado para hipertensión."
    },
    {
        "nombre": "Smoothie de espinacas, manzana y semillas de chía",
        "calorias": 180,
        "carbohidratos": 30,
        "proteinas": 5,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "bajo en sodio", "orgánico"],
        "observaciones": "Alto en fibra y antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Tostadas de arroz con mantequilla de almendra y plátano",
        "calorias": 220,
        "carbohidratos": 35,
        "proteinas": 8,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "sin lactosa", "vegano"],
        "observaciones": "Adecuado para personas con intolerancia a la lactosa, bajo en sodio."
    },
    {
        "nombre": "Batido de fresa con proteína vegana y leche de almendra",
        "calorias": 210,
        "carbohidratos": 25,
        "proteinas": 20,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas vegetales y antioxidantes, ideal para el desarrollo muscular."
    },
    {
        "nombre": "Arepas de yuca con queso de cabra",
        "calorias": 250,
        "carbohidratos": 30,
        "proteinas": 12,
        "sodio": 50,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "vegetariano", "dieta criolla"],
        "observaciones": "Rico en carbohidratos complejos y sin gluten, ideal para una dieta criolla."
    },
    {
        "nombre": "Batido de piña, espinaca y jengibre",
        "calorias": 180,
        "carbohidratos": 35,
        "proteinas": 6,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en antioxidantes, ideal para hipertensión."
    },
    {
        "nombre": "Pancakes de harina de coco con frambuesas",
        "calorias": 260,
        "carbohidratos": 25,
        "proteinas": 10,
        "sodio": 20,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Adecuado para personas que siguen una dieta baja en carbohidratos."
    },
    {
        "nombre": "Tostadas de aguacate con rábanos y semillas de calabaza",
        "calorias": 230,
        "carbohidratos": 25,
        "proteinas": 8,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegano", "vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Rico en grasas saludables y fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Bowl de quinua con frutas y nueces",
        "calorias": 300,
        "carbohidratos": 50,
        "proteinas": 10,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "dieta andina"],
        "observaciones": "Rico en fibra y proteínas, adecuado para una dieta andina."
    },
    {
        "nombre": "Yogur de soja con semillas de lino y fresas",
        "calorias": 180,
        "carbohidratos": 25,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Bajo en sodio y rico en fibra, ideal para hipertensión."
    },
    {
        "nombre": "Tortilla de espárragos con claras de huevo y pimientos",
        "calorias": 220,
        "carbohidratos": 8,
        "proteinas": 18,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para desarrollo muscular."
    },
    {
        "nombre": "Tostadas integrales con queso feta y aguacate",
        "calorias": 270,
        "carbohidratos": 35,
        "proteinas": 10,
        "sodio": 40,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Bajo en sodio y alto en grasas saludables, ideal para hipertensión."
    },
    {
        "nombre": "Batido de kale, piña y proteína de guisante",
        "calorias": 200,
        "carbohidratos": 25,
        "proteinas": 15,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en antioxidantes y proteínas, ideal para el desarrollo muscular."
    },
    {
        "nombre": "Porridge de trigo sarraceno con arándanos",
        "calorias": 240,
        "carbohidratos": 45,
        "proteinas": 8,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Bajo en sodio y sin gluten, ideal para una vida saludable."
    },
    {
        "nombre": "Tortilla de papas con cebolla y espinacas",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 10,
        "sodio": 20,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y rico en carbohidratos complejos, ideal para hipertensión."
    },
    {
        "nombre": "Smoothie de mora, linaza y espinacas",
        "calorias": 200,
        "carbohidratos": 30,
        "proteinas": 8,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en antioxidantes y bajo en sodio, ideal para bajar de peso."
    },
    {
        "nombre": "Tostadas de centeno con hummus y pepino",
        "calorias": 250,
        "carbohidratos": 30,
        "proteinas": 10,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Bajo en sodio y rico en fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Pudding de chia con leche de coco y mango",
        "calorias": 200,
        "carbohidratos": 25,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Bajo en sodio y rico en fibra, ideal para bajar de peso."
    },
    {
        "nombre": "Batido de zanahoria, manzana y cúrcuma",
        "calorias": 180,
        "carbohidratos": 35,
        "proteinas": 5,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en antioxidantes y bajo en sodio, ideal para bajar de peso."
    },
    {
        "nombre": "Pan de maíz con miel de abeja y nueces",
        "calorias": 250,
        "carbohidratos": 40,
        "proteinas": 7,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten"],
        "observaciones": "Adecuado para una dieta sin gluten, alto en fibra."
    },
    {
        "nombre": "Omelette de claras de huevo con cebolla y pimientos",
        "calorias": 220,
        "carbohidratos": 10,
        "proteinas": 18,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Batido de arándanos, proteína de soja y almendra",
        "calorias": 190,
        "carbohidratos": 25,
        "proteinas": 15,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas y antioxidantes, ideal para el desarrollo muscular."
    },
    {
        "nombre": "Tostadas de aguacate con semillas de girasol",
        "calorias": 240,
        "carbohidratos": 30,
        "proteinas": 8,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "vegano", "bajo en sodio"],
        "observaciones": "Rico en grasas saludables y fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Porridge de quinoa con leche de coco y nueces",
        "calorias": 280,
        "carbohidratos": 45,
        "proteinas": 10,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "dieta andina"],
        "observaciones": "Adecuado para una dieta andina, rico en proteínas y sin gluten."
    },
    {
        "nombre": "Panqueques de harina de almendra con compota de frutas",
        "calorias": 230,
        "carbohidratos": 30,
        "proteinas": 12,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Batido de plátano, leche de soja y linaza",
        "calorias": 210,
        "carbohidratos": 40,
        "proteinas": 8,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Bajo en sodio y rico en fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Tostadas de centeno con aguacate y rábanos",
        "calorias": 220,
        "carbohidratos": 30,
        "proteinas": 7,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Bajo en sodio y rico en fibra, ideal para hipertensión."
    },
    {
        "nombre": "Porridge de avena con arándanos y semillas de chía",
        "calorias": 260,
        "carbohidratos": 45,
        "proteinas": 10,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "orgánico"],
        "observaciones": "Rico en antioxidantes y fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Batido de fresa, avena y proteína de guisante",
        "calorias": 220,
        "carbohidratos": 35,
        "proteinas": 15,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas vegetales, ideal para el desarrollo muscular."
    },
    {
        "nombre": "Tortilla de calabacín con cebolla y claras de huevo",
        "calorias": 230,
        "carbohidratos": 8,
        "proteinas": 18,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Batido de frambuesa, avena y linaza",
        "calorias": 200,
        "carbohidratos": 40,
        "proteinas": 6,
        "sodio": 10,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Bajo en sodio y rico en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Tostadas de pan de centeno con palta y huevo duro",
        "calorias": 260,
        "carbohidratos": 30,
        "proteinas": 12,
        "sodio": 20,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Bajo en sodio y alto en proteínas, ideal para hipertensión."
    },
    {
        "nombre": "Batido de espinaca, manzana y jengibre",
        "calorias": 180,
        "carbohidratos": 30,
        "proteinas": 5,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Bajo en sodio y rico en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Porridge de avena con semillas de cáñamo y coco rallado",
        "calorias": 240,
        "carbohidratos": 40,
        "proteinas": 10,
        "sodio": 15,
        "tipo": "desayuno",
        "categorias": ["vegetariano", "sin gluten", "orgánico"],
        "observaciones": "Rico en proteínas y fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Crepes de harina de arroz con mantequilla de almendra",
        "calorias": 250,
        "carbohidratos": 40,
        "proteinas": 12,
        "sodio": 5,
        "tipo": "desayuno",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },

    # Almuerzos
    {
        "nombre": "Pollo a la parrilla con ensalada de quinoa",
        "calorias": 400,
        "carbohidratos": 35,
        "proteinas": 30,
        "sodio": 80,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "dieta andina", "sin gluten"],
        "observaciones": "Alto en proteínas y fibra, bajo en carbohidratos, ideal para mantener el nivel de energía."
    },
    {
        "nombre": "Salmón con brócoli al vapor",
        "calorias": 450,
        "carbohidratos": 15,
        "proteinas": 40,
        "sodio": 60,
        "tipo": "almuerzo",
        "categorias": ["bajo en sodio", "bajo en carbohidratos", "orgánico"],
        "observaciones": "Rico en omega-3, bajo en sodio, ideal para hipertensión y colesterol alto."
    },
    {
        "nombre": "Ensalada de espinacas con tofu y aguacate",
        "calorias": 300,
        "carbohidratos": 20,
        "proteinas": 18,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["vegano", "bajo en carbohidratos", "bajo en sodio", "orgánico"],
        "observaciones": "Ideal para personas veganas, baja en carbohidratos y sodio."
    },
    {
        "nombre": "Arroz integral con lentejas y verduras",
        "calorias": 500,
        "carbohidratos": 80,
        "proteinas": 20,
        "sodio": 70,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "sin lactosa", "dieta andina", "orgánico"],
        "observaciones": "Alto en carbohidratos complejos y fibra, ideal para personas con alto requerimiento de energía."
    },
    {
        "nombre": "Pescado frito con yuca y ensalada de cebolla",
        "calorias": 550,
        "carbohidratos": 45,
        "proteinas": 35,
        "sodio": 90,
        "tipo": "almuerzo",
        "categorias": ["dieta criolla", "dieta amazónica"],
        "observaciones": "Alto en proteínas y grasas saludables, típico de la dieta criolla y amazónica."
    },
    {
        "nombre": "Pechuga de pollo a la plancha con ensalada de lentejas",
        "calorias": 400,
        "carbohidratos": 25,
        "proteinas": 35,
        "sodio": 50,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en proteínas, ideal para hipertensión y desarrollo muscular."
    },
    {
        "nombre": "Tilapia al horno con vegetales asados",
        "calorias": 350,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en sodio", "bajo en carbohidratos", "orgánico"],
        "observaciones": "Ideal para dietas bajas en carbohidratos y control de sodio."
    },
    {
        "nombre": "Quinoa con pimientos, cebolla y tofu",
        "calorias": 320,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 25,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "vegano", "sin gluten", "dieta andina"],
        "observaciones": "Bajo en sodio, rico en proteínas vegetales, ideal para dietas andinas y veganas."
    },
    {
        "nombre": "Pasta de arroz con pesto de albahaca",
        "calorias": 500,
        "carbohidratos": 70,
        "proteinas": 12,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "sin gluten", "sin lactosa"],
        "observaciones": "Apta para celíacos y personas intolerantes a la lactosa."
    },
    {
        "nombre": "Taco de quinoa y frijoles negros",
        "calorias": 450,
        "carbohidratos": 55,
        "proteinas": 18,
        "sodio": 35,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "vegano", "sin gluten", "dieta criolla"],
        "observaciones": "Alto en fibra y proteínas, ideal para personas veganas."
    },
    {
        "nombre": "Cazuela de carne de res con papas y zanahorias",
        "calorias": 550,
        "carbohidratos": 40,
        "proteinas": 35,
        "sodio": 60,
        "tipo": "almuerzo",
        "categorias": ["dieta criolla", "sin gluten"],
        "observaciones": "Ideal para quienes buscan una dieta tradicional criolla."
    },
    {
        "nombre": "Ensalada de pollo con palta y espárragos",
        "calorias": 350,
        "carbohidratos": 10,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Ideal para dietas bajas en carbohidratos y hipertensión."
    },
    {
        "nombre": "Pescado a la parrilla con papas dulces",
        "calorias": 400,
        "carbohidratos": 35,
        "proteinas": 30,
        "sodio": 45,
        "tipo": "almuerzo",
        "categorias": ["dieta amazónica", "sin lactosa"],
        "observaciones": "Rico en ácidos grasos saludables, ideal para una dieta amazónica."
    },
    {
        "nombre": "Sopa de quinoa con pollo",
        "calorias": 300,
        "carbohidratos": 30,
        "proteinas": 25,
        "sodio": 25,
        "tipo": "almuerzo",
        "categorias": ["dieta andina", "sin gluten", "bajo en sodio"],
        "observaciones": "Adecuada para personas con hipertensión y para dietas andinas."
    },
    {
        "nombre": "Ensalada de garbanzos con tomate y cilantro",
        "calorias": 350,
        "carbohidratos": 50,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Alto en fibra y bajo en sodio, ideal para personas con hipertensión."
    },
    {
        "nombre": "Pollo asado con quinoa y espárragos",
        "calorias": 400,
        "carbohidratos": 30,
        "proteinas": 35,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "dieta andina", "sin gluten"],
        "observaciones": "Alto en proteínas y fibra, bajo en sodio, ideal para desarrollo muscular."
    },
    {
        "nombre": "Pescado al horno con batata y ensalada",
        "calorias": 450,
        "carbohidratos": 50,
        "proteinas": 25,
        "sodio": 50,
        "tipo": "almuerzo",
        "categorias": ["dieta amazónica", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en antioxidantes y omega-3, bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Fajitas de pollo con pimientos y cebolla",
        "calorias": 400,
        "carbohidratos": 30,
        "proteinas": 35,
        "sodio": 60,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en carbohidratos", "sin lactosa"],
        "observaciones": "Bajo en carbohidratos, ideal para diabetes y desarrollo muscular."
    },
    {
        "nombre": "Ensalada de garbanzos con aguacate y tomate",
        "calorias": 350,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Ideal para hipertensión, alto en fibra y grasas saludables."
    },
    {
        "nombre": "Pechuga de pollo con arroz integral y brócoli",
        "calorias": 450,
        "carbohidratos": 50,
        "proteinas": 30,
        "sodio": 70,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Ideal para una dieta baja en sodio y rica en proteínas, adecuada para hipertensión."
    },
    {
        "nombre": "Salmón a la parrilla con puré de camote",
        "calorias": 400,
        "carbohidratos": 35,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "sin lactosa", "bajo en sodio"],
        "observaciones": "Rico en omega-3, bajo en sodio y carbohidratos, adecuado para colesterol alto."
    },
    {
        "nombre": "Ensalada de lentejas con rúcula y zanahoria",
        "calorias": 350,
        "carbohidratos": 45,
        "proteinas": 18,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en proteínas vegetales, ideal para una vida saludable."
    },
    {
        "nombre": "Cazuela de carne de res con yuca",
        "calorias": 500,
        "carbohidratos": 50,
        "proteinas": 35,
        "sodio": 60,
        "tipo": "almuerzo",
        "categorias": ["dieta criolla", "sin gluten"],
        "observaciones": "Alto en proteínas y carbohidratos, adecuado para personas que buscan desarrollo muscular."
    },
    {
        "nombre": "Tacos de pescado con ensalada de col",
        "calorias": 350,
        "carbohidratos": 40,
        "proteinas": 25,
        "sodio": 35,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio", "bajo en carbohidratos"],
        "observaciones": "Adecuado para personas con hipertensión, alto en proteínas."
    },
    {
        "nombre": "Lomo saltado con papas y arroz integral",
        "calorias": 550,
        "carbohidratos": 60,
        "proteinas": 30,
        "sodio": 90,
        "tipo": "almuerzo",
        "categorias": ["dieta criolla", "sin gluten"],
        "observaciones": "Ideal para una dieta criolla, rico en proteínas y carbohidratos."
    },
    {
        "nombre": "Ensalada de pollo con aguacate y quinoa",
        "calorias": 350,
        "carbohidratos": 30,
        "proteinas": 30,
        "sodio": 50,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "dieta andina"],
        "observaciones": "Ideal para una dieta alta en proteínas y sin gluten."
    },
    {
        "nombre": "Pescado a la parrilla con arroz integral y ensalada de rúcula",
        "calorias": 400,
        "carbohidratos": 40,
        "proteinas": 30,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Bajo en sodio y rico en proteínas, ideal para una dieta saludable."
    },
    {
        "nombre": "Tacos de lechuga con pollo y guacamole",
        "calorias": 300,
        "carbohidratos": 20,
        "proteinas": 25,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Ideal para una dieta baja en carbohidratos, alta en proteínas."
    },
    {
        "nombre": "Pechuga de pollo con batata y espárragos",
        "calorias": 400,
        "carbohidratos": 40,
        "proteinas": 35,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Adecuado para una dieta rica en proteínas y baja en sodio."
    },
    {
        "nombre": "Ensalada de lentejas con remolacha y espinaca",
        "calorias": 350,
        "carbohidratos": 40,
        "proteinas": 18,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Ideal para una dieta vegana, rica en proteínas vegetales."
    },
    {
        "nombre": "Tilapia al horno con brócoli y zanahorias",
        "calorias": 380,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Adecuado para una dieta baja en sodio y sin gluten."
    },
    {
        "nombre": "Quinoa con tofu y verduras al vapor",
        "calorias": 320,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegano", "vegetariano", "sin gluten", "dieta andina"],
        "observaciones": "Rico en proteínas vegetales y sin gluten, ideal para una dieta andina."
    },
    {
        "nombre": "Cazuela de carne de res con zanahorias y papas",
        "calorias": 500,
        "carbohidratos": 45,
        "proteinas": 35,
        "sodio": 70,
        "tipo": "almuerzo",
        "categorias": ["dieta criolla", "sin gluten"],
        "observaciones": "Alto en proteínas, ideal para una dieta criolla rica en nutrientes."
    },
    {
        "nombre": "Pescado frito con ensalada de col y arroz integral",
        "calorias": 450,
        "carbohidratos": 50,
        "proteinas": 30,
        "sodio": 80,
        "tipo": "almuerzo",
        "categorias": ["dieta criolla", "sin gluten"],
        "observaciones": "Ideal para una dieta criolla, alto en proteínas."
    },
    {
        "nombre": "Sopa de quinua con vegetales y pollo",
        "calorias": 300,
        "carbohidratos": 30,
        "proteinas": 25,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["dieta andina", "sin gluten", "bajo en sodio"],
        "observaciones": "Adecuado para hipertensión y personas con intolerancia al gluten."
    },
    {
        "nombre": "Pollo al horno con espárragos y arroz integral",
        "calorias": 400,
        "carbohidratos": 40,
        "proteinas": 30,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para una dieta baja en sal."
    },
    {
        "nombre": "Tilapia al horno con ensalada de aguacate y tomate",
        "calorias": 350,
        "carbohidratos": 20,
        "proteinas": 25,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Bajo en sodio y carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Pasta de garbanzos con salsa de tomate y albahaca",
        "calorias": 380,
        "carbohidratos": 45,
        "proteinas": 20,
        "sodio": 50,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "vegetariano", "bajo en carbohidratos"],
        "observaciones": "Ideal para una dieta baja en carbohidratos y sin gluten."
    },
    {
        "nombre": "Ensalada de atún con garbanzos y rúcula",
        "calorias": 320,
        "carbohidratos": 20,
        "proteinas": 28,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Pechuga de pollo a la plancha con ensalada de quinoa",
        "calorias": 380,
        "carbohidratos": 35,
        "proteinas": 30,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "dieta andina", "bajo en sodio"],
        "observaciones": "Adecuado para una dieta rica en proteínas y baja en sodio."
    },
    {
        "nombre": "Salmón a la parrilla con papas y espárragos",
        "calorias": 420,
        "carbohidratos": 35,
        "proteinas": 28,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Ideal para una dieta baja en sodio y alta en proteínas."
    },
    {
        "nombre": "Ensalada de lentejas con aguacate y cilantro",
        "calorias": 300,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 15,
        "tipo": "almuerzo",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y rico en proteínas vegetales, ideal para una vida saludable."
    },
    {
        "nombre": "Pasta de arroz integral con pesto de albahaca",
        "calorias": 400,
        "carbohidratos": 50,
        "proteinas": 12,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "sin gluten", "sin lactosa"],
        "observaciones": "Adecuado para una dieta libre de gluten y lactosa."
    },
    {
        "nombre": "Tacos de pollo con lechuga y guacamole",
        "calorias": 320,
        "carbohidratos": 25,
        "proteinas": 25,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Pollo salteado con espinacas y quinoa",
        "calorias": 370,
        "carbohidratos": 30,
        "proteinas": 35,
        "sodio": 35,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "dieta andina", "sin lactosa"],
        "observaciones": "Ideal para una dieta alta en proteínas y baja en carbohidratos."
    },
    {
        "nombre": "Pollo asado con ensalada de espinacas y quinoa",
        "calorias": 400,
        "carbohidratos": 35,
        "proteinas": 35,
        "sodio": 50,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio", "dieta andina"],
        "observaciones": "Rico en proteínas y fibra, bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Tilapia a la parrilla con puré de batata y espárragos",
        "calorias": 380,
        "carbohidratos": 40,
        "proteinas": 25,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Bajo en sodio y rico en proteínas, ideal para hipertensión."
    },
    {
        "nombre": "Pasta de garbanzos con salsa de tomate y espinacas",
        "calorias": 400,
        "carbohidratos": 50,
        "proteinas": 18,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "sin gluten", "bajo en carbohidratos"],
        "observaciones": "Ideal para una dieta sin gluten y baja en carbohidratos."
    },
    {
        "nombre": "Salmón al horno con arroz integral y ensalada de rúcula",
        "calorias": 450,
        "carbohidratos": 35,
        "proteinas": 30,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Adecuado para una dieta alta en proteínas y baja en sodio."
    },
    {
        "nombre": "Ensalada de quinoa con tofu y aguacate",
        "calorias": 350,
        "carbohidratos": 45,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegano", "sin gluten", "bajo en sodio", "dieta andina"],
        "observaciones": "Bajo en sodio y alto en proteínas vegetales, ideal para hipertensión."
    },
    {
        "nombre": "Pechuga de pollo con ensalada de garbanzos y zanahorias",
        "calorias": 400,
        "carbohidratos": 35,
        "proteinas": 35,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Adecuado para una dieta rica en proteínas y baja en sodio."
    },
    {
        "nombre": "Ensalada de espinacas con lentejas y aguacate",
        "calorias": 320,
        "carbohidratos": 35,
        "proteinas": 18,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en fibra y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Quinoa con verduras al vapor y tofu marinado",
        "calorias": 340,
        "carbohidratos": 45,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegano", "sin gluten", "bajo en sodio", "dieta andina"],
        "observaciones": "Ideal para una dieta baja en sodio y rica en proteínas vegetales."
    },
    {
        "nombre": "Cazuela de carne de res con papas y espinacas",
        "calorias": 500,
        "carbohidratos": 40,
        "proteinas": 35,
        "sodio": 60,
        "tipo": "almuerzo",
        "categorias": ["dieta criolla", "sin gluten"],
        "observaciones": "Alto en proteínas, ideal para una dieta criolla."
    },
    {
        "nombre": "Tacos de lechuga con pollo y guacamole",
        "calorias": 320,
        "carbohidratos": 25,
        "proteinas": 25,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Salmón a la parrilla con ensalada de quinoa y aguacate",
        "calorias": 450,
        "carbohidratos": 40,
        "proteinas": 30,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "dieta andina", "sin lactosa"],
        "observaciones": "Alto en proteínas y omega-3, ideal para bajar de peso."
    },
    {
        "nombre": "Sopa de vegetales con pollo y arroz integral",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 25,
        "sodio": 25,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Bajo en sodio y rico en proteínas, ideal para hipertensión."
    },
    {
        "nombre": "Lomo saltado con papas horneadas y ensalada",
        "calorias": 550,
        "carbohidratos": 45,
        "proteinas": 35,
        "sodio": 70,
        "tipo": "almuerzo",
        "categorias": ["dieta criolla", "sin gluten"],
        "observaciones": "Alto en proteínas y rico en carbohidratos complejos, ideal para hipertensión."
    },
    {
        "nombre": "Salmón con ensalada de espárragos y brócoli",
        "calorias": 400,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para colesterol alto."
    },
    {
        "nombre": "Ensalada de atún con garbanzos y pepino",
        "calorias": 350,
        "carbohidratos": 25,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en proteínas y bajo en carbohidratos, ideal para diabetes."
    },
    {
        "nombre": "Pechuga de pollo a la parrilla con puré de calabaza",
        "calorias": 400,
        "carbohidratos": 40,
        "proteinas": 35,
        "sodio": 35,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para bajar de peso."
    },
    {
        "nombre": "Pollo al curry con arroz integral y espinacas",
        "calorias": 380,
        "carbohidratos": 45,
        "proteinas": 30,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Rico en proteínas y fibra, bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Ensalada de lentejas con espinacas y aguacate",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en fibra y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Sopa de calabaza y garbanzos con tofu",
        "calorias": 320,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en fibra, ideal para hipertensión."
    },
    {
        "nombre": "Tacos de pescado con lechuga y aguacate",
        "calorias": 300,
        "carbohidratos": 25,
        "proteinas": 25,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Quinoa con pimientos asados y pollo al grill",
        "calorias": 400,
        "carbohidratos": 35,
        "proteinas": 35,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa", "dieta andina"],
        "observaciones": "Rico en proteínas y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Pasta de calabacín con salsa de tomate y pollo",
        "calorias": 350,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Bajo en carbohidratos y rico en proteínas, ideal para diabetes."
    },
    {
        "nombre": "Ensalada de rúcula con salmón y aguacate",
        "calorias": 400,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 25,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "bajo en carbohidratos", "sin lactosa"],
        "observaciones": "Alto en omega-3 y bajo en carbohidratos, ideal para colesterol alto."
    },
    {
        "nombre": "Lentejas con quinoa y vegetales asados",
        "calorias": 360,
        "carbohidratos": 50,
        "proteinas": 18,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Alto en proteínas vegetales y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Pollo al horno con ensalada de espárragos y tomate",
        "calorias": 380,
        "carbohidratos": 30,
        "proteinas": 35,
        "sodio": 35,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Rico en proteínas y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Ensalada de garbanzos con rúcula y pepino",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 12,
        "sodio": 15,
        "tipo": "almuerzo",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en fibra y bajo en sodio, ideal para una vida saludable."
    },
    {
        "nombre": "Tortilla de espárragos con pimientos y claras de huevo",
        "calorias": 250,
        "carbohidratos": 10,
        "proteinas": 20,
        "sodio": 15,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Rico en proteínas y bajo en carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Cazuela de pollo con batata y espinacas",
        "calorias": 360,
        "carbohidratos": 40,
        "proteinas": 30,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en proteínas, ideal para una vida saludable."
    },
    {
        "nombre": "Sopa de pollo con zanahoria y quinoa",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 25,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "dieta andina", "sin lactosa"],
        "observaciones": "Adecuado para una dieta baja en sodio y rica en proteínas."
    },
    {
        "nombre": "Tacos de tofu con ensalada de col y aguacate",
        "calorias": 320,
        "carbohidratos": 35,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en proteínas vegetales, ideal para hipertensión."
    },
    {
        "nombre": "Pasta de arroz integral con verduras y pesto",
        "calorias": 380,
        "carbohidratos": 50,
        "proteinas": 12,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "sin gluten", "sin lactosa"],
        "observaciones": "Adecuado para personas con intolerancia al gluten y lactosa."
    },
    {
        "nombre": "Tilapia con puré de coliflor y espárragos",
        "calorias": 350,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para bajar de peso."
    },
    {
        "nombre": "Pollo salteado con verduras y arroz integral",
        "calorias": 400,
        "carbohidratos": 45,
        "proteinas": 35,
        "sodio": 40,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Rico en proteínas y fibra, bajo en sodio, ideal para bajar de peso."
    },
    {
        "nombre": "Salmón a la plancha con quinoa y espinacas",
        "calorias": 450,
        "carbohidratos": 35,
        "proteinas": 35,
        "sodio": 35,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Rico en proteínas y omega-3, ideal para bajar de peso."
    },
    {
        "nombre": "Pollo al curry con quinoa y espinacas",
        "calorias": 400,
        "carbohidratos": 35,
        "proteinas": 35,
        "sodio": 35,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "dieta andina", "sin lactosa"],
        "observaciones": "Adecuado para una dieta rica en proteínas y baja en carbohidratos."
    },
    {
        "nombre": "Ensalada de pollo con aguacate y tomates cherry",
        "calorias": 350,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Rico en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Ensalada de quinoa con espárragos y pimientos",
        "calorias": 330,
        "carbohidratos": 45,
        "proteinas": 12,
        "sodio": 20,
        "tipo": "almuerzo",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y rico en fibra, ideal para una vida saludable."
    },

    # Cenas
    {
        "nombre": "Sopa de pollo con verduras",
        "calorias": 300,
        "carbohidratos": 25,
        "proteinas": 20,
        "sodio": 50,
        "tipo": "cena",
        "categorias": ["bajo en sodio", "sin gluten"],
        "observaciones": "Baja en calorías y sodio, ideal para una cena ligera."
    },
    {
        "nombre": "Tacos de lechuga con carne de res magra",
        "calorias": 400,
        "carbohidratos": 15,
        "proteinas": 30,
        "sodio": 60,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten"],
        "observaciones": "Ideal para una cena baja en carbohidratos, alta en proteínas."
    },
    {
        "nombre": "Sopa de mariscos con leche de coco",
        "calorias": 350,
        "carbohidratos": 20,
        "proteinas": 25,
        "sodio": 70,
        "tipo": "cena",
        "categorias": ["dieta criolla", "dieta amazónica", "sin lactosa"],
        "observaciones": "Rica en proteínas, apta para personas con intolerancia a la lactosa."
    },
    {
        "nombre": "Puré de papa con filete de pavo",
        "calorias": 450,
        "carbohidratos": 50,
        "proteinas": 25,
        "sodio": 50,
        "tipo": "cena",
        "categorias": ["sin gluten", "dieta andina"],
        "observaciones": "Adecuada para personas con enfermedad celíaca, rica en carbohidratos."
    },
    {
        "nombre": "Quinua con espárragos y tofu",
        "calorias": 350,
        "carbohidratos": 45,
        "proteinas": 20,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegetariano", "vegano", "bajo en sodio", "dieta andina"],
        "observaciones": "Ideal para personas con hipertensión, alta en fibra y proteínas vegetales."
    },
    {
        "nombre": "Atún con ensalada de pepino y palta",
        "calorias": 300,
        "carbohidratos": 10,
        "proteinas": 25,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "bajo en sodio", "sin lactosa"],
        "observaciones": "Ideal para una cena ligera, baja en sodio y carbohidratos."
    },
    {
        "nombre": "Tortilla de coliflor con espinacas y queso feta",
        "calorias": 250,
        "carbohidratos": 12,
        "proteinas": 20,
        "sodio": 60,
        "tipo": "cena",
        "categorias": ["vegetariano", "bajo en carbohidratos"],
        "observaciones": "Ideal para una cena baja en carbohidratos y rica en proteínas."
    },
    {
        "nombre": "Pollo salteado con verduras y jengibre",
        "calorias": 400,
        "carbohidratos": 25,
        "proteinas": 35,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Adecuado para personas con intolerancia al gluten y lactosa."
    },
    {
        "nombre": "Sopa de vegetales con lentejas",
        "calorias": 350,
        "carbohidratos": 50,
        "proteinas": 20,
        "sodio": 40,
        "tipo": "cena",
        "categorias": ["vegetariano", "bajo en sodio", "sin lactosa"],
        "observaciones": "Rica en fibra y proteínas vegetales, ideal para hipertensión."
    },
    {
        "nombre": "Tostadas de camote con guacamole",
        "calorias": 300,
        "carbohidratos": 40,
        "proteinas": 8,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "dieta criolla"],
        "observaciones": "Adecuado para una cena ligera y saludable, sin gluten."
    },
    {
        "nombre": "Pasta de trigo sarraceno con tomate y albahaca",
        "calorias": 400,
        "carbohidratos": 60,
        "proteinas": 10,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["vegetariano", "sin gluten"],
        "observaciones": "Alto en carbohidratos complejos, ideal para una dieta sin gluten."
    },
    {
        "nombre": "Ensalada de rúcula con tofu y almendras",
        "calorias": 250,
        "carbohidratos": 10,
        "proteinas": 18,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegetariano", "vegano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Bajo en calorías y sodio, ideal para una cena ligera."
    },
    {
        "nombre": "Sopa de espárragos con garbanzos",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegetariano", "bajo en sodio", "sin gluten"],
        "observaciones": "Ideal para personas con hipertensión y enfermedad celíaca."
    },
    {
        "nombre": "Pollo al limón con quinoa y espárragos",
        "calorias": 350,
        "carbohidratos": 30,
        "proteinas": 25,
        "sodio": 50,
        "tipo": "cena",
        "categorias": ["bajo en sodio", "sin gluten", "dieta andina"],
        "observaciones": "Adecuado para una dieta baja en sodio y rica en proteínas."
    },
    {
        "nombre": "Salmón al vapor con puré de coliflor",
        "calorias": 400,
        "carbohidratos": 20,
        "proteinas": 35,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Ideal para una cena baja en carbohidratos y rica en omega-3."
    },
    {
        "nombre": "Ensalada de pollo con pepino y aguacate",
        "calorias": 300,
        "carbohidratos": 10,
        "proteinas": 25,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "bajo en sodio", "sin lactosa"],
        "observaciones": "Ideal para una cena ligera y baja en carbohidratos, apto para hipertensión."
    },
    {
        "nombre": "Sopa de zanahoria y jengibre",
        "calorias": 200,
        "carbohidratos": 30,
        "proteinas": 5,
        "sodio": 15,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Ideal para una cena baja en calorías, adecuada para hipertensión."
    },
    {
        "nombre": "Salteado de tofu con vegetales al vapor",
        "calorias": 250,
        "carbohidratos": 20,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegetariano", "vegano", "bajo en carbohidratos"],
        "observaciones": "Bajo en carbohidratos y alto en proteínas vegetales, ideal para una vida saludable."
    },
    {
        "nombre": "Salmón al vapor con puré de coliflor",
        "calorias": 400,
        "carbohidratos": 15,
        "proteinas": 35,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin lactosa", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Alto en omega-3, ideal para colesterol alto y vida saludable."
    },
    {
        "nombre": "Pollo al limón con espárragos",
        "calorias": 320,
        "carbohidratos": 10,
        "proteinas": 30,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Adecuado para hipertensión y dietas bajas en carbohidratos."
    },
    {
        "nombre": "Sopa de calabaza y garbanzos",
        "calorias": 300,
        "carbohidratos": 40,
        "proteinas": 10,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["vegetariano", "vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Adecuada para hipertensión y una vida saludable."
    },
    {
        "nombre": "Tortilla de espárragos con espinacas",
        "calorias": 250,
        "carbohidratos": 8,
        "proteinas": 20,
        "sodio": 40,
        "tipo": "cena",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Ideal para una cena ligera y baja en carbohidratos."
    },
    {
        "nombre": "Tacos de lechuga con carne magra",
        "calorias": 350,
        "carbohidratos": 15,
        "proteinas": 30,
        "sodio": 50,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten", "bajo en sodio"],
        "observaciones": "Adecuado para desarrollo muscular, bajo en sodio."
    },
    {
        "nombre": "Pollo a la plancha con puré de calabaza",
        "calorias": 320,
        "carbohidratos": 35,
        "proteinas": 25,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["bajo en sodio", "sin lactosa", "sin gluten"],
        "observaciones": "Bajo en sodio y apto para personas con intolerancia a la lactosa."
    },
    {
        "nombre": "Sopa de quinua con pollo y verduras",
        "calorias": 280,
        "carbohidratos": 30,
        "proteinas": 20,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["dieta andina", "sin gluten", "bajo en sodio"],
        "observaciones": "Alto en proteínas y fibra, ideal para hipertensión."
    },
    {
        "nombre": "Ensalada de rúcula con pollo y tomates cherry",
        "calorias": 250,
        "carbohidratos": 10,
        "proteinas": 30,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "bajo en sodio", "sin gluten"],
        "observaciones": "Bajo en carbohidratos, ideal para personas con hipertensión."
    },
    {
        "nombre": "Sopa de vegetales con garbanzos y espinacas",
        "calorias": 280,
        "carbohidratos": 35,
        "proteinas": 12,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Ideal para una cena ligera, baja en sodio."
    },
    {
        "nombre": "Salmón al vapor con espárragos y puré de coliflor",
        "calorias": 350,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Rico en proteínas y bajo en sodio, ideal para una cena ligera."
    },
    {
        "nombre": "Tacos de lechuga con carne molida magra",
        "calorias": 300,
        "carbohidratos": 15,
        "proteinas": 28,
        "sodio": 40,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten"],
        "observaciones": "Alto en proteínas, ideal para desarrollo muscular."
    },
    {
        "nombre": "Pollo asado con batata y espárragos",
        "calorias": 350,
        "carbohidratos": 30,
        "proteinas": 30,
        "sodio": 50,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Ideal para una dieta saludable y baja en sodio."
    },
    {
        "nombre": "Sopa de brócoli y zanahoria con tofu",
        "calorias": 280,
        "carbohidratos": 30,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Ideal para una dieta vegana y baja en sodio."
    },
    {
        "nombre": "Tortilla de champiñones y espinacas",
        "calorias": 260,
        "carbohidratos": 8,
        "proteinas": 20,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Bajo en carbohidratos y alto en proteínas, ideal para una cena ligera."
    },
    {
        "nombre": "Pollo al limón con quinua y brócoli",
        "calorias": 320,
        "carbohidratos": 30,
        "proteinas": 25,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en sodio", "dieta andina"],
        "observaciones": "Adecuado para una dieta andina baja en sodio."
    },
    {
        "nombre": "Ensalada de garbanzos con rúcula y aguacate",
        "calorias": 280,
        "carbohidratos": 35,
        "proteinas": 10,
        "sodio": 10,
        "tipo": "cena",
        "categorias": ["vegetariano", "vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Alto en fibra y bajo en sodio, ideal para una dieta vegana."
    },
    {
        "nombre": "Cazuela de pollo con vegetales y batata",
        "calorias": 320,
        "carbohidratos": 40,
        "proteinas": 25,
        "sodio": 40,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Adecuado para una cena ligera y saludable."
    },
    {
        "nombre": "Pechuga de pollo a la plancha con batata asada",
        "calorias": 350,
        "carbohidratos": 35,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para una cena ligera."
    },
    {
        "nombre": "Sopa de calabaza y jengibre",
        "calorias": 200,
        "carbohidratos": 30,
        "proteinas": 5,
        "sodio": 10,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Baja en calorías y rica en antioxidantes, ideal para hipertensión."
    },
    {
        "nombre": "Salmón al vapor con espinacas salteadas",
        "calorias": 350,
        "carbohidratos": 15,
        "proteinas": 30,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en omega-3 y bajo en sodio, ideal para una cena ligera."
    },
    {
        "nombre": "Sopa de zanahoria y cúrcuma con tofu",
        "calorias": 220,
        "carbohidratos": 30,
        "proteinas": 10,
        "sodio": 15,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Adecuado para una cena ligera y rica en antioxidantes."
    },
    {
        "nombre": "Tacos de lechuga con carne molida magra",
        "calorias": 300,
        "carbohidratos": 15,
        "proteinas": 28,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para desarrollo muscular."
    },
    {
        "nombre": "Pollo al horno con puré de batata y espárragos",
        "calorias": 360,
        "carbohidratos": 40,
        "proteinas": 30,
        "sodio": 40,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Adecuado para una cena ligera y baja en sodio."
    },
    {
        "nombre": "Ensalada de garbanzos con rúcula y tomates cherry",
        "calorias": 320,
        "carbohidratos": 40,
        "proteinas": 12,
        "sodio": 15,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en fibra y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Tortilla de claras de huevo con espinacas",
        "calorias": 260,
        "carbohidratos": 5,
        "proteinas": 22,
        "sodio": 15,
        "tipo": "cena",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para una cena ligera."
    },
    {
        "nombre": "Pollo al vapor con puré de coliflor",
        "calorias": 300,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Sopa de espárragos y garbanzos",
        "calorias": 280,
        "carbohidratos": 30,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y rico en fibra, ideal para una cena ligera."
    },
    {
        "nombre": "Salmón al horno con puré de coliflor y espárragos",
        "calorias": 350,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y omega-3, bajo en sodio, ideal para bajar de peso."
    },
    {
        "nombre": "Tortilla de espinacas con queso feta y pimientos",
        "calorias": 280,
        "carbohidratos": 12,
        "proteinas": 20,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para desarrollo muscular."
    },
    {
        "nombre": "Pechuga de pollo con ensalada de aguacate y espárragos",
        "calorias": 340,
        "carbohidratos": 10,
        "proteinas": 35,
        "sodio": 40,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Adecuado para una dieta baja en carbohidratos y alta en proteínas."
    },
    {
        "nombre": "Ensalada de lentejas con espinacas y aguacate",
        "calorias": 300,
        "carbohidratos": 35,
        "proteinas": 18,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en fibra, ideal para hipertensión."
    },
    {
        "nombre": "Sopa de pollo con quinoa y zanahorias",
        "calorias": 280,
        "carbohidratos": 30,
        "proteinas": 25,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin gluten", "dieta andina", "sin lactosa"],
        "observaciones": "Adecuado para una dieta alta en proteínas y baja en carbohidratos."
    },
    {
        "nombre": "Pechuga de pavo a la parrilla con brócoli y puré de batata",
        "calorias": 370,
        "carbohidratos": 40,
        "proteinas": 35,
        "sodio": 40,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para desarrollo muscular."
    },
    {
        "nombre": "Tacos de pescado con lechuga y guacamole",
        "calorias": 300,
        "carbohidratos": 20,
        "proteinas": 25,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Sopa de calabaza con garbanzos y espinacas",
        "calorias": 320,
        "carbohidratos": 45,
        "proteinas": 12,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en fibra, ideal para hipertensión."
    },
    {
        "nombre": "Pollo al limón con espárragos y arroz integral",
        "calorias": 400,
        "carbohidratos": 35,
        "proteinas": 35,
        "sodio": 35,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Adecuado para una dieta rica en proteínas y baja en sodio."
    },
    {
        "nombre": "Ensalada de atún con pepino y tomates cherry",
        "calorias": 320,
        "carbohidratos": 15,
        "proteinas": 30,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Ensalada de rúcula con garbanzos y aguacate",
        "calorias": 300,
        "carbohidratos": 30,
        "proteinas": 12,
        "sodio": 15,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en fibra, ideal para hipertensión."
    },
    {
        "nombre": "Tacos de lechuga con carne molida magra y guacamole",
        "calorias": 320,
        "carbohidratos": 15,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para desarrollo muscular."
    },
    {
        "nombre": "Sopa de zanahoria y jengibre con tofu",
        "calorias": 280,
        "carbohidratos": 35,
        "proteinas": 12,
        "sodio": 15,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en fibra y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Pollo al vapor con espárragos y puré de coliflor",
        "calorias": 340,
        "carbohidratos": 25,
        "proteinas": 30,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para bajar de peso."
    },
    {
        "nombre": "Sopa de quinoa con espinacas y pollo",
        "calorias": 310,
        "carbohidratos": 35,
        "proteinas": 25,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["sin gluten", "dieta andina", "sin lactosa"],
        "observaciones": "Adecuado para una dieta alta en proteínas y baja en sodio."
    },
    {
        "nombre": "Salmón a la plancha con ensalada de aguacate y espinacas",
        "calorias": 380,
        "carbohidratos": 15,
        "proteinas": 30,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en carbohidratos", "sin lactosa"],
        "observaciones": "Rico en omega-3 y bajo en carbohidratos, ideal para una vida saludable."
    },
    {
        "nombre": "Ensalada de quinoa con tofu y espinacas",
        "calorias": 300,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio", "dieta andina"],
        "observaciones": "Rico en proteínas vegetales y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Pechuga de pavo al horno con puré de zanahorias",
        "calorias": 350,
        "carbohidratos": 30,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Adecuado para una dieta rica en proteínas y baja en sodio."
    },
    {
        "nombre": "Sopa de calabacín con garbanzos y pimientos",
        "calorias": 310,
        "carbohidratos": 40,
        "proteinas": 12,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en fibra y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Pollo al horno con ensalada de espárragos y tomates cherry",
        "calorias": 380,
        "carbohidratos": 25,
        "proteinas": 35,
        "sodio": 35,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Adecuado para una dieta rica en proteínas y baja en sodio."
    },
    {
        "nombre": "Tortilla de claras de huevo con espárragos y pimientos",
        "calorias": 250,
        "carbohidratos": 8,
        "proteinas": 20,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegetariano", "bajo en carbohidratos", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Sopa de zanahoria y cúrcuma con tofu",
        "calorias": 220,
        "carbohidratos": 30,
        "proteinas": 10,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Adecuado para una dieta ligera y rica en antioxidantes."
    },
    {
        "nombre": "Pechuga de pollo a la parrilla con puré de batata",
        "calorias": 370,
        "carbohidratos": 35,
        "proteinas": 35,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y bajo en sodio, ideal para bajar de peso."
    },
    {
        "nombre": "Tilapia al horno con ensalada de pepino y aguacate",
        "calorias": 320,
        "carbohidratos": 15,
        "proteinas": 30,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Ensalada de garbanzos con rúcula y tomates cherry",
        "calorias": 280,
        "carbohidratos": 35,
        "proteinas": 10,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Alto en fibra y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Ensalada de quinoa con espárragos y tofu",
        "calorias": 300,
        "carbohidratos": 40,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en proteínas vegetales y bajo en sodio, ideal para una vida saludable."
    },
    {
        "nombre": "Pollo al grill con puré de zanahorias y espárragos",
        "calorias": 340,
        "carbohidratos": 30,
        "proteinas": 35,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Adecuado para una dieta alta en proteínas y baja en sodio."
    },
    {
        "nombre": "Ensalada de atún con aguacate y espinacas",
        "calorias": 320,
        "carbohidratos": 15,
        "proteinas": 30,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Pechuga de pavo con ensalada de rúcula y nueces",
        "calorias": 350,
        "carbohidratos": 20,
        "proteinas": 35,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en carbohidratos", "sin lactosa"],
        "observaciones": "Rico en proteínas y grasas saludables, ideal para bajar de peso."
    },
    {
        "nombre": "Salmón a la plancha con puré de batata y espinacas",
        "calorias": 400,
        "carbohidratos": 35,
        "proteinas": 30,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Adecuado para una dieta alta en proteínas y baja en sodio."
    },
    {
        "nombre": "Sopa de espárragos con pollo y garbanzos",
        "calorias": 330,
        "carbohidratos": 40,
        "proteinas": 25,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Adecuado para una dieta rica en proteínas y baja en sodio."
    },
    {
        "nombre": "Pollo al vapor con puré de coliflor y zanahorias",
        "calorias": 310,
        "carbohidratos": 25,
        "proteinas": 30,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Rico en proteínas y bajo en sodio, ideal para bajar de peso."
    },
    {
        "nombre": "Pollo a la parrilla con ensalada de espinacas y tomate",
        "calorias": 340,
        "carbohidratos": 20,
        "proteinas": 35,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Adecuado para una dieta alta en proteínas y baja en carbohidratos."
    },
    {
        "nombre": "Sopa de brócoli con pollo y zanahorias",
        "calorias": 320,
        "carbohidratos": 35,
        "proteinas": 25,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en sodio", "sin lactosa"],
        "observaciones": "Adecuado para una dieta rica en proteínas y baja en sodio."
    },
    {
        "nombre": "Ensalada de garbanzos con quinoa y pimientos",
        "calorias": 340,
        "carbohidratos": 45,
        "proteinas": 15,
        "sodio": 20,
        "tipo": "cena",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en proteínas vegetales y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Pechuga de pollo con ensalada de espárragos y aguacate",
        "calorias": 330,
        "carbohidratos": 20,
        "proteinas": 35,
        "sodio": 30,
        "tipo": "cena",
        "categorias": ["sin gluten", "bajo en carbohidratos", "sin lactosa"],
        "observaciones": "Rico en proteínas y bajo en carbohidratos, ideal para desarrollo muscular."
    },
    {
        "nombre": "Tacos de lechuga con pollo y ensalada de col",
        "calorias": 310,
        "carbohidratos": 20,
        "proteinas": 30,
        "sodio": 25,
        "tipo": "cena",
        "categorias": ["bajo en carbohidratos", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en proteínas y bajo en carbohidratos, ideal para bajar de peso."
    },

    # Snacks
    {
        "nombre": "Frutas frescas (manzana, pera, plátano)",
        "calorias": 100,
        "carbohidratos": 25,
        "proteinas": 1,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "orgánico"],
        "observaciones": "Bajo en calorías, ideal para un snack rápido y saludable."
    },
    {
        "nombre": "Yogur de almendra con fresas",
        "calorias": 150,
        "carbohidratos": 15,
        "proteinas": 5,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["sin lactosa", "bajo en carbohidratos", "orgánico"],
        "observaciones": "Ideal para personas con intolerancia a la lactosa, alto en calcio."
    },
    {
        "nombre": "Palitos de zanahoria con hummus",
        "calorias": 120,
        "carbohidratos": 15,
        "proteinas": 4,
        "sodio": 30,
        "tipo": "snack",
        "categorias": ["vegetariano", "bajo en carbohidratos", "sin gluten", "orgánico"],
        "observaciones": "Alto en fibra y bajo en calorías, ideal para un snack saludable."
    },
    {
        "nombre": "Almendras y nueces mixtas",
        "calorias": 200,
        "carbohidratos": 8,
        "proteinas": 6,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Rico en grasas saludables, ideal para dietas bajas en carbohidratos."
    },
    {
        "nombre": "Batido de proteína vegana con espinacas y moras",
        "calorias": 180,
        "carbohidratos": 20,
        "proteinas": 15,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en proteínas y antioxidantes, ideal para un snack después de entrenar."
    },
    {
        "nombre": "Barritas de avena y arándanos",
        "calorias": 180,
        "carbohidratos": 30,
        "proteinas": 4,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten"],
        "observaciones": "Ideal para un snack energético, sin gluten y alto en fibra."
    },
    {
        "nombre": "Palitos de apio con mantequilla de almendra",
        "calorias": 150,
        "carbohidratos": 8,
        "proteinas": 5,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["sin gluten", "bajo en carbohidratos", "orgánico"],
        "observaciones": "Rico en fibra y grasas saludables, ideal para una dieta baja en carbohidratos."
    },
    {
        "nombre": "Chips de camote horneados",
        "calorias": 200,
        "carbohidratos": 30,
        "proteinas": 2,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y sin gluten, ideal para un snack saludable."
    },
    {
        "nombre": "Hummus con rodajas de pepino",
        "calorias": 120,
        "carbohidratos": 10,
        "proteinas": 6,
        "sodio": 15,
        "tipo": "snack",
        "categorias": ["vegetariano", "vegano", "bajo en carbohidratos"],
        "observaciones": "Rico en proteínas vegetales y bajo en carbohidratos."
    },
    {
        "nombre": "Chips de plátano sin azúcar",
        "calorias": 180,
        "carbohidratos": 40,
        "proteinas": 1,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "dieta criolla"],
        "observaciones": "Adecuado para un snack energético en una dieta criolla o vegana."
    },
    {
        "nombre": "Frutas secas con nueces",
        "calorias": 200,
        "carbohidratos": 25,
        "proteinas": 5,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegetariano", "vegano", "sin gluten"],
        "observaciones": "Alto en antioxidantes, ideal para un snack saludable."
    },
    {
        "nombre": "Yogur de coco con semillas de chía",
        "calorias": 150,
        "carbohidratos": 10,
        "proteinas": 4,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Ideal para personas con intolerancia a la lactosa y al gluten."
    },
    {
        "nombre": "Muffin de almendras y coco sin azúcar",
        "calorias": 160,
        "carbohidratos": 15,
        "proteinas": 6,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["sin gluten", "sin lactosa", "bajo en carbohidratos"],
        "observaciones": "Adecuado para dietas bajas en carbohidratos y sin gluten."
    },
    {
        "nombre": "Batido de frutos rojos con proteína de suero",
        "calorias": 180,
        "carbohidratos": 20,
        "proteinas": 15,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["sin lactosa", "bajo en sodio"],
        "observaciones": "Ideal para un snack proteico después de entrenar."
    },
    {
        "nombre": "Palomitas de maíz sin sal",
        "calorias": 100,
        "carbohidratos": 20,
        "proteinas": 2,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en calorías y sodio, ideal para un snack ligero."
    },
    {
        "nombre": "Barritas de proteína de almendra y coco",
        "calorias": 180,
        "carbohidratos": 20,
        "proteinas": 12,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "orgánico"],
        "observaciones": "Rico en proteínas vegetales, ideal para desarrollo muscular."
    },
    {
        "nombre": "Frutos secos sin sal con pasas",
        "calorias": 200,
        "carbohidratos": 30,
        "proteinas": 5,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegetariano", "vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Ideal para hipertensión, alto en fibra y antioxidantes."
    },
    {
        "nombre": "Palitos de zanahoria con hummus",
        "calorias": 120,
        "carbohidratos": 12,
        "proteinas": 4,
        "sodio": 20,
        "tipo": "snack",
        "categorias": ["vegetariano", "bajo en carbohidratos", "sin gluten"],
        "observaciones": "Adecuado para dietas bajas en carbohidratos, alto en fibra."
    },
    {
        "nombre": "Tortillas de maíz con guacamole",
        "calorias": 150,
        "carbohidratos": 18,
        "proteinas": 5,
        "sodio": 15,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio, ideal para una vida saludable."
    },
    {
        "nombre": "Batido de proteína con espinaca y arándanos",
        "calorias": 180,
        "carbohidratos": 20,
        "proteinas": 15,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en antioxidantes y proteínas, ideal para después del entrenamiento."
    },
    {
        "nombre": "Yogur de soja con almendras y chía",
        "calorias": 160,
        "carbohidratos": 15,
        "proteinas": 7,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["sin gluten", "sin lactosa", "vegano"],
        "observaciones": "Adecuado para intolerancia a la lactosa, rico en omega-3."
    },
    {
        "nombre": "Barritas de granola con semillas de lino",
        "calorias": 190,
        "carbohidratos": 25,
        "proteinas": 8,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Alto en fibra, ideal para hipertensión."
    },
    {
        "nombre": "Chips de plátano sin azúcar",
        "calorias": 200,
        "carbohidratos": 30,
        "proteinas": 2,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "dieta amazónica"],
        "observaciones": "Ideal para una dieta amazónica o vegetariana."
    },
    {
        "nombre": "Palitos de apio con salsa de yogur",
        "calorias": 120,
        "carbohidratos": 8,
        "proteinas": 6,
        "sodio": 15,
        "tipo": "snack",
        "categorias": ["vegetariano", "bajo en carbohidratos", "sin gluten"],
        "observaciones": "Bajo en carbohidratos, ideal para un snack saludable."
    },
    {
        "nombre": "Manzanas con mantequilla de almendra",
        "calorias": 200,
        "carbohidratos": 25,
        "proteinas": 5,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "sin lactosa"],
        "observaciones": "Adecuado para una vida saludable, alto en fibra."
    },
    {
        "nombre": "Chips de col rizada horneados",
        "calorias": 100,
        "carbohidratos": 10,
        "proteinas": 3,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Palitos de pepino con crema de garbanzos",
        "calorias": 150,
        "carbohidratos": 15,
        "proteinas": 6,
        "sodio": 20,
        "tipo": "snack",
        "categorias": ["vegano", "vegetariano", "sin gluten", "bajo en carbohidratos"],
        "observaciones": "Ideal para una dieta baja en carbohidratos."
    },
    {
        "nombre": "Batido de frambuesa con leche de coco",
        "calorias": 180,
        "carbohidratos": 20,
        "proteinas": 5,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Frutas deshidratadas con nueces",
        "calorias": 200,
        "carbohidratos": 30,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Tortitas de arroz integral con mantequilla de maní",
        "calorias": 180,
        "carbohidratos": 25,
        "proteinas": 8,
        "sodio": 20,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en proteínas y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Yogur de coco con granola sin gluten",
        "calorias": 160,
        "carbohidratos": 20,
        "proteinas": 6,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["sin gluten", "sin lactosa", "vegano"],
        "observaciones": "Adecuado para personas con intolerancia a la lactosa."
    },
    {
        "nombre": "Tostadas de arroz con hummus y pimientos",
        "calorias": 150,
        "carbohidratos": 18,
        "proteinas": 5,
        "sodio": 15,
        "tipo": "snack",
        "categorias": ["vegano", "vegetariano", "sin gluten", "bajo en carbohidratos"],
        "observaciones": "Bajo en sodio y carbohidratos, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de manzana deshidratada sin azúcar",
        "calorias": 120,
        "carbohidratos": 28,
        "proteinas": 1,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "orgánico"],
        "observaciones": "Rico en fibra y sin azúcares añadidos, ideal para una vida saludable."
    },
    {
        "nombre": "Batido de espinacas con piña y semillas de lino",
        "calorias": 170,
        "carbohidratos": 25,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y rico en fibra, ideal para hipertensión."
    },
    {
        "nombre": "Frutas frescas con yogur de soja",
        "calorias": 180,
        "carbohidratos": 30,
        "proteinas": 7,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en fibra y antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de manzana deshidratada sin azúcar",
        "calorias": 100,
        "carbohidratos": 25,
        "proteinas": 1,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Bajo en calorías, ideal para una dieta ligera."
    },
    {
        "nombre": "Palitos de zanahoria con hummus de remolacha",
        "calorias": 150,
        "carbohidratos": 20,
        "proteinas": 6,
        "sodio": 20,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en carbohidratos"],
        "observaciones": "Bajo en carbohidratos y alto en fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Batido de arándanos con leche de almendra",
        "calorias": 170,
        "carbohidratos": 30,
        "proteinas": 5,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Bajo en sodio y alto en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Tostadas de arroz con aguacate y semillas de chía",
        "calorias": 180,
        "carbohidratos": 25,
        "proteinas": 5,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en grasas saludables, ideal para una vida saludable."
    },
    {
        "nombre": "Palitos de apio con mantequilla de almendra",
        "calorias": 150,
        "carbohidratos": 8,
        "proteinas": 5,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["sin gluten", "bajo en carbohidratos", "orgánico"],
        "observaciones": "Alto en grasas saludables y bajo en carbohidratos, ideal para hipertensión."
    },
    {
        "nombre": "Frutas frescas con yogur griego",
        "calorias": 180,
        "carbohidratos": 25,
        "proteinas": 8,
        "sodio": 15,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en antioxidantes y bajo en sodio, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de col rizada con aceite de oliva",
        "calorias": 100,
        "carbohidratos": 10,
        "proteinas": 3,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en fibra y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Tortitas de arroz con mermelada de frutos rojos sin azúcar",
        "calorias": 120,
        "carbohidratos": 30,
        "proteinas": 2,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "sin lactosa"],
        "observaciones": "Bajo en sodio y rico en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Palomitas de maíz sin sal",
        "calorias": 100,
        "carbohidratos": 20,
        "proteinas": 2,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en calorías y sodio, ideal para un snack ligero."
    },
    {
        "nombre": "Batido de espinacas con manzana y linaza",
        "calorias": 180,
        "carbohidratos": 25,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en antioxidantes y bajo en sodio, ideal para una vida saludable."
    },
    {
        "nombre": "Barritas de avena con frutos secos y chocolate oscuro",
        "calorias": 180,
        "carbohidratos": 25,
        "proteinas": 5,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de zanahoria horneados con guacamole",
        "calorias": 150,
        "carbohidratos": 18,
        "proteinas": 4,
        "sodio": 15,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en carbohidratos"],
        "observaciones": "Bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Frutas frescas con yogur griego sin lactosa",
        "calorias": 120,
        "carbohidratos": 20,
        "proteinas": 8,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "sin lactosa"],
        "observaciones": "Adecuado para personas con intolerancia a la lactosa."
    },
    {
        "nombre": "Palomitas de maíz sin sal y aceite de coco",
        "calorias": 100,
        "carbohidratos": 20,
        "proteinas": 2,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio, ideal para hipertensión y colesterol alto."
    },
    {
        "nombre": "Batido de proteínas con espinacas y moras",
        "calorias": 180,
        "carbohidratos": 25,
        "proteinas": 15,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa", "bajo en sodio"],
        "observaciones": "Alto en antioxidantes y proteínas, ideal para desarrollo muscular."
    },
    {
        "nombre": "Galletas de avena con pasas sin gluten",
        "calorias": 150,
        "carbohidratos": 30,
        "proteinas": 4,
        "sodio": 15,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y alto en fibra, ideal para hipertensión."
    },
    {
        "nombre": "Bowl de frutas frescas con granola de quinoa",
        "calorias": 200,
        "carbohidratos": 40,
        "proteinas": 6,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "dieta andina"],
        "observaciones": "Rico en antioxidantes, ideal para una dieta andina."
    },
    {
        "nombre": "Hummus con palitos de pepino y zanahoria",
        "calorias": 140,
        "carbohidratos": 20,
        "proteinas": 5,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en carbohidratos"],
        "observaciones": "Alto en fibra, bajo en sodio, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de plátano horneado sin azúcar",
        "calorias": 130,
        "carbohidratos": 28,
        "proteinas": 2,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegano", "dieta amazónica", "sin gluten"],
        "observaciones": "Ideal para una dieta amazónica, rico en carbohidratos complejos."
    },
    {
        "nombre": "Batido de fresa, almendra y proteína de soja",
        "calorias": 170,
        "carbohidratos": 25,
        "proteinas": 15,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas y antioxidantes, ideal para desarrollo muscular."
    },
    {
        "nombre": "Frutas deshidratadas sin azúcar añadida",
        "calorias": 140,
        "carbohidratos": 30,
        "proteinas": 2,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en fibra y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Yogur de coco con semillas de lino y fresas",
        "calorias": 180,
        "carbohidratos": 20,
        "proteinas": 8,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Adecuado para personas con intolerancia a la lactosa."
    },
    {
        "nombre": "Tortitas de arroz integral con guacamole",
        "calorias": 160,
        "carbohidratos": 25,
        "proteinas": 4,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y grasas saludables, ideal para una vida saludable."
    },
    {
        "nombre": "Barritas de avena con almendra y coco",
        "calorias": 190,
        "carbohidratos": 25,
        "proteinas": 6,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en fibra, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de kale horneados con sal marina",
        "calorias": 120,
        "carbohidratos": 15,
        "proteinas": 3,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Alto en antioxidantes y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Palitos de apio con crema de almendras",
        "calorias": 150,
        "carbohidratos": 10,
        "proteinas": 5,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Adecuado para personas con alergia a los frutos secos."
    },
    {
        "nombre": "Yogur de soja con frutas frescas y chia",
        "calorias": 160,
        "carbohidratos": 30,
        "proteinas": 7,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en fibra y proteínas vegetales, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de manzana deshidratada sin azúcar",
        "calorias": 100,
        "carbohidratos": 25,
        "proteinas": 1,
        "sodio": 0,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "orgánico"],
        "observaciones": "Bajo en calorías, ideal para una dieta saludable."
    },
    {
        "nombre": "Batido de mango con leche de almendra y linaza",
        "calorias": 180,
        "carbohidratos": 30,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Tortitas de maíz con salsa de tomate casera",
        "calorias": 150,
        "carbohidratos": 25,
        "proteinas": 4,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y rico en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Smoothie de plátano, fresa y avena",
        "calorias": 200,
        "carbohidratos": 40,
        "proteinas": 8,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en antioxidantes y fibra, ideal para bajar de peso."
    },
    {
        "nombre": "Barritas de granola de quinoa y chía",
        "calorias": 190,
        "carbohidratos": 25,
        "proteinas": 6,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "dieta andina"],
        "observaciones": "Rico en fibra y proteínas, ideal para una dieta andina."
    },
    {
        "nombre": "Tacos de lechuga con tofu y guacamole",
        "calorias": 170,
        "carbohidratos": 20,
        "proteinas": 10,
        "sodio": 15,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en proteínas vegetales, ideal para una vida saludable."
    },
    {
        "nombre": "Batido de proteína de guisante con espinacas y plátano",
        "calorias": 200,
        "carbohidratos": 25,
        "proteinas": 15,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Alto en proteínas vegetales, ideal para desarrollo muscular."
    },
    {
        "nombre": "Tortitas de arroz con hummus de remolacha",
        "calorias": 150,
        "carbohidratos": 25,
        "proteinas": 5,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y rico en antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de batata con guacamole",
        "calorias": 140,
        "carbohidratos": 30,
        "proteinas": 4,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en carbohidratos"],
        "observaciones": "Bajo en carbohidratos, ideal para bajar de peso."
    },
    {
        "nombre": "Yogur de soja con nueces y arándanos",
        "calorias": 170,
        "carbohidratos": 20,
        "proteinas": 7,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Adecuado para personas con intolerancia a la lactosa."
    },
    {
        "nombre": "Palitos de zanahoria con crema de almendras",
        "calorias": 140,
        "carbohidratos": 12,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en carbohidratos"],
        "observaciones": "Adecuado para personas con alergia a los frutos secos."
    },
    {
        "nombre": "Tostadas de maíz con salsa de aguacate y tomate",
        "calorias": 160,
        "carbohidratos": 22,
        "proteinas": 4,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Bajo en sodio y grasas saludables, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de calabacín horneados con salsa de yogurt",
        "calorias": 140,
        "carbohidratos": 15,
        "proteinas": 7,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegetariano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en antioxidantes y bajo en sodio, ideal para hipertensión."
    },
    {
        "nombre": "Batido de arándanos con proteína de soja y avena",
        "calorias": 190,
        "carbohidratos": 25,
        "proteinas": 10,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en proteínas vegetales, ideal para desarrollo muscular."
    },
    {
        "nombre": "Palitos de pepino con crema de garbanzos",
        "calorias": 130,
        "carbohidratos": 15,
        "proteinas": 6,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en sodio"],
        "observaciones": "Rico en fibra y bajo en sodio, ideal para una vida saludable."
    },
    {
        "nombre": "Chips de batata con hummus de zanahoria",
        "calorias": 160,
        "carbohidratos": 30,
        "proteinas": 5,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "bajo en carbohidratos"],
        "observaciones": "Bajo en carbohidratos y rico en fibra, ideal para bajar de peso."
    },
    {
        "nombre": "Barritas de avena con semillas de lino y chía",
        "calorias": 190,
        "carbohidratos": 30,
        "proteinas": 6,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en fibra y antioxidantes, ideal para una vida saludable."
    },
    {
        "nombre": "Yogur de coco con granola sin gluten",
        "calorias": 160,
        "carbohidratos": 20,
        "proteinas": 7,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Adecuado para personas con intolerancia a la lactosa."
    },
    {
        "nombre": "Chips de plátano con guacamole",
        "calorias": 170,
        "carbohidratos": 30,
        "proteinas": 4,
        "sodio": 10,
        "tipo": "snack",
        "categorias": ["vegetariano", "dieta amazónica", "sin gluten"],
        "observaciones": "Ideal para una dieta amazónica, rico en grasas saludables."
    },
    {
        "nombre": "Batido de espinacas con proteína de guisante y manzana",
        "calorias": 180,
        "carbohidratos": 25,
        "proteinas": 15,
        "sodio": 5,
        "tipo": "snack",
        "categorias": ["vegano", "sin gluten", "sin lactosa"],
        "observaciones": "Rico en proteínas vegetales y antioxidantes, ideal para desarrollo muscular."
    }   
]

