from random import randint as ran
resp = [
    "¡Hola! Soy Athenea y tengo excelentes noticias para ti. Después de analizar tus tesis, he concluido que eres oficialmente un maestro Jedi de tu campo de estudio. También hemos preparado un PDF con los resultados de tu análisis, así que prepárate para impresionar a todos tus colegas. ¡Que la fuerza te acompañe!",
    "¡Listo! Tu tesis ha sido analizada, como dijo el gran Mario Bros: 'It's-a me, Athenea!'.",
    "Tu tesis está lista, como diría Darth Vader: 'Impresionante, la fuerza es fuerte en esta. Athenea, has cumplido con tu deber.'",
    "Athenea ha terminado de analizar tu tesis. ¡Es como si hubiéramos ganado la batalla contra los Decepticons!",
    "¡Excelente! Athenea ha terminado de analizar tu tesis. Como diría el Doc Emmett Brown: '¡Es un éxito, Marty!'",
    "La tesis ha sido analizada, y Athenea dice: 'Toto, creo que ya no estamos en Kansas'.",
    "¡Lo logramos! Athenea ha terminado de analizar tu tesis. Como diría Will Smith en 'Men in Black': '¡Aquí viene el Hombre de Negro!'",
    "Athenea ha completado el análisis de tu tesis, como diría Rocky Balboa: '¡Adriaaaaan!'",
    "Tu tesis ha sido analizada, como diría el famoso detective Sherlock Holmes: '¡Elemental, mi querido Watson!'",
    "Athenea ha terminado de analizar tu tesis. ¡Es como si el poder de la fuerza estuviera de nuestro lado, como en Star Wars!",
    "¡Excelente trabajo! Tu tesis ha sido analizada y todo parece estar en orden. Athenea dice: '¡Yo soy Iron Man!'",
    "Athenea ha concluido el análisis de tu tesis, como diría el Capitán Kirk de Star Trek: '¡Haz que suceda, Número Uno!'",
    "¡Genial! Tu tesis ha sido analizada con éxito. Athenea dice: '¡Hasta la vista, baby!', como diría Terminator.",
    "Athenea ha terminado de analizar tu tesis. Como diría Marty McFly de 'Volver al Futuro': '¡Esto es pesado!'",
    "La tesis ha sido analizada y todo parece estar en orden. Athenea dice: '¡Que la fuerza te acompañe!', como en Star Wars.",
    "Athenea ha concluido el análisis de tu tesis, como diría el personaje de 'Tron': '¡Estoy en la red!'",
    "¡Lo logramos! Athenea ha terminado de analizar tu tesis. Como diría el gran MacGyver: 'Con un poco de cinta adhesiva y un lápiz, puedes hacer cualquier cosa'.",
    "Tu tesis ha sido analizada con éxito. Athenea dice: '¡Alohomora!', como diría Harry Potter.",
    "Athenea ha completado el análisis de tu tesis, como diría el famoso Spock de Star Trek: 'Vida larga y próspera'.",
    "¡Increíble! Tu tesis ha sido analizada con éxito. Como diría el personaje de 'Matrix': '¡Despierta, Neo!'",
    "¡Athenea ha terminado de analizar tu tesis! Ahora es hora de demostrar tus habilidades como el Rey de los Mares y sumergirte en el mundo de los datos.",
    "¡Felicitaciones! Athenea ha completado su análisis de tu tesis y ha encontrado más pistas que Batman en su Batcueva.",
    "¡Alto ahí, héroe! Athenea ha completado su análisis de tu tesis y ha descubierto más secretos que la armadura de Iron Man.",
    "¡Athenea ha terminado de analizar tu tesis! Ahora tienes la fuerza de Hulk para defender tus resultados.",
    "¡Genial! Athenea ha completado su análisis de tu tesis y ha descubierto más pistas que el Detective Marciano.",
    "¡Alabado sea Rao! Athenea ha terminado de analizar tu tesis y ha encontrado más secretos que la Fortaleza de la Soledad de Superman.",
    "¡Excelente trabajo! Athenea ha completado su análisis de tu tesis y ha descubierto más pistas que la Flecha Verde en su Quiver.",
    "¡Increíble! Athenea ha terminado de analizar tu tesis y ha encontrado más secretos que el Sanctum Sanctorum del Doctor Strange.",
    "¡Athenea ha completado su análisis de tu tesis! Ahora es hora de canalizar tus poderes de Spider-Man y lanzarte a la web de resultados.",
    "¡Fantástico! Athenea ha terminado de analizar tu tesis y ha encontrado más secretos que la Zona Negativa de los Cuatro Fantásticos.",
    "¡Athenea ha completado su análisis de tu tesis! Ahora es hora de usar tus habilidades de transformación como Mystique y adaptarte a los resultados.",
    "¡Impresionante! Athenea ha terminado de analizar tu tesis y ha descubierto más pistas que la Baticueva de Batman.",
    "¡Athenea ha completado su análisis de tu tesis! Ahora es hora de controlar tus habilidades como el Profesor X y navegar por los resultados.",
    "¡Magnífico! Athenea ha terminado de analizar tu tesis y ha encontrado más secretos que la Biblioteca del Sanctum Sanctorum.",
    "¡Athenea ha completado su análisis de tu tesis! Ahora es hora de poner en práctica tus habilidades de Iron Fist y puñetear los resultados.",
    "¡Sensacional! Athenea ha terminado de analizar tu tesis y ha descubierto más pistas que la Mansión X del Profesor X.",
    "¡Athenea ha completado su análisis de tu tesis! Ahora es hora de volar con tus habilidades de Phoenix y absorber los resultados.",
    "¡Espectacular! Athenea ha terminado de analizar tu tesis y ha encontrado más secretos que el Helitransporte de Nick Fury.",
    "¡Athenea ha completado su análisis de tu tesis! Ahora es hora de usar tus habilidades de Black Widow y espiar los resultados.",
    "¡Genial! Athenea ha terminado de analizar tu tesis y ha descubierto más pistas que el Planeta Krypton de Superman",
    "¡Bazinga! Hemos terminado de analizar tus tesis, y los resultados están listos en un PDF.",
    "El poder de Athenea ha sido liberado y el análisis de tu tesis está completo. Descarga el PDF para ver los resultados.",
    "¡Excelente! Athenea ha analizado tu tesis y los resultados están disponibles en un PDF.",
    "¡Cowabunga! El análisis de tu tesis ha sido completado por Athenea y el PDF con los resultados está listo para ser descargado.",
    "Athenea ha sacado su varita mágica y ha terminado de analizar tu tesis. Descarga el PDF para ver los resultados.",
    "Hemos analizado tu tesis y los resultados están listos para ser descargados en un PDF. ¡Que la fuerza te acompañe!"
]

resp1 = [
    "Buscando tesis en los repositorios de la UNAM. Espere, por favor.",
    "Estamos buscando tesis en la UNAM. Un momento, por favor.",
    "Consultando repositorios de la UNAM. Paciencia, por favor.",
    "Búsqueda de tesis en curso. Accediendo a la UNAM.",
    "Recopilando tesis de la UNAM. Aguarde, por favor.",
    "Obteniendo información sobre tesis en la UNAM. Espere un momento.",
    "Buscando tesis. Accediendo a la UNAM. Gracias por su paciencia.",
    "Consultando la UNAM en busca de tesis. Un momento, por favor.",
    "Buscando tesis en la UNAM. Paciencia mientras completamos la búsqueda.",
    "Estamos consultando la UNAM en busca de tesis. Por favor, espere.",
    "Recopilando tesis. Consultando la UNAM. Paciencia, por favor.",
    "Búsqueda de tesis en curso. Accediendo a la UNAM. Gracias por su espera.",
    "Obteniendo información sobre tesis. Espere unos momentos.",
    "Buscando tesis. Consultando la UNAM. Le pedimos paciencia.",
    "Accediendo a la UNAM para buscar tesis. Un momento, por favor.",
    "Buscando tesis en la UNAM. Le agradecemos su paciencia.",
    "Consultando la UNAM en busca de tesis. Por favor, espere unos momentos.",
    "Recopilando tesis de la UNAM. Aguarde un momento.",
    "Obteniendo información sobre tesis. Espere un instante.",
    "Buscando tesis. Consultando la UNAM. Gracias por su espera.",
    "Accediendo a la UNAM para buscar tesis. Por favor, tenga paciencia.",
    "Buscando tesis en la UNAM. Paciencia mientras completamos la búsqueda.",
    "Estamos consultando la UNAM en busca de tesis. Por favor, espere unos momentos."
]

resp_uam = [
    "Buscando tesis en los repositorios de la UAM. Espere, por favor.",
    "Estamos buscando tesis en la UAM. Un momento, por favor.",
    "Consultando repositorios de la UAM. Paciencia, por favor.",
    "Búsqueda de tesis en curso. Accediendo a la UAM.",
    "Recopilando tesis de la UAM. Aguarde, por favor.",
    "Obteniendo información sobre tesis en la UAM. Espere un momento.",
    "Buscando tesis. Accediendo a la UAM. Gracias por su paciencia.",
    "Consultando la UAM en busca de tesis. Un momento, por favor.",
    "Buscando tesis en la UAM. Paciencia mientras completamos la búsqueda.",
    "Estamos consultando la UAM en busca de tesis. Por favor, espere.",
    "Recopilando tesis. Consultando la UAM. Paciencia, por favor.",
    "Búsqueda de tesis en curso. Accediendo a la UAM. Gracias por su espera.",
    "Obteniendo información sobre tesis. Espere unos momentos.",
    "Buscando tesis. Consultando la UAM. Le pedimos paciencia.",
    "Accediendo a la UAM para buscar tesis. Un momento, por favor.",
    "Buscando tesis en la UAM. Le agradecemos su paciencia.",
    "Consultando la UAM en busca de tesis. Por favor, espere unos momentos.",
    "Recopilando tesis de la UAM. Aguarde un momento.",
    "Obteniendo información sobre tesis. Espere un instante.",
    "Buscando tesis. Consultando la UAM. Gracias por su espera.",
    "Accediendo a la UAM para buscar tesis. Por favor, tenga paciencia.",
    "Buscando tesis en la UAM. Paciencia mientras completamos la búsqueda.",
    "Estamos consultando la UAM en busca de tesis. Por favor, espere unos momentos."
]

resp_tec = [
    "Buscando tesis en los repositorios del Tecnológico de Monterrey. Espere, por favor.",
    "Estamos buscando tesis en el Tecnológico de Monterrey. Un momento, por favor.",
    "Consultando repositorios del Tecnológico de Monterrey. Paciencia, por favor.",
    "Búsqueda de tesis en curso. Accediendo al Tecnológico de Monterrey.",
    "Recopilando tesis del Tecnológico de Monterrey. Aguarde, por favor.",
    "Obteniendo información sobre tesis en el Tecnológico de Monterrey. Espere un momento.",
    "Buscando tesis. Accediendo al Tecnológico de Monterrey. Gracias por su paciencia.",
    "Consultando el Tecnológico de Monterrey en busca de tesis. Un momento, por favor.",
    "Buscando tesis en el Tecnológico de Monterrey. Paciencia mientras completamos la búsqueda.",
    "Estamos consultando el Tecnológico de Monterrey en busca de tesis. Por favor, espere.",
    "Recopilando tesis. Consultando el Tecnológico de Monterrey. Paciencia, por favor.",
    "Búsqueda de tesis en curso. Accediendo al Tecnológico de Monterrey. Gracias por su espera.",
    "Obteniendo información sobre tesis. Espere unos momentos.",
    "Buscando tesis. Consultando el Tecnológico de Monterrey. Le pedimos paciencia.",
    "Accediendo al Tecnológico de Monterrey para buscar tesis. Un momento, por favor.",
    "Buscando tesis en el Tecnológico de Monterrey. Le agradecemos su paciencia.",
    "Consultando el Tecnológico de Monterrey en busca de tesis. Por favor, espere unos momentos.",
    "Recopilando tesis del Tecnológico de Monterrey. Aguarde un momento.",
    "Obteniendo información sobre tesis. Espere un instante.",
    "Buscando tesis. Consultando el Tecnológico de Monterrey. Gracias por su espera.",
    "Accediendo al Tecnológico de Monterrey para buscar tesis. Por favor, tenga paciencia.",
    "Buscando tesis en el Tecnológico de Monterrey. Paciencia mientras completamos la búsqueda.",
    "Estamos consultando el Tecnológico de Monterrey en busca de tesis. Por favor, espere unos momentos."
]

resp2 = [
    "Buscando en repositorios del Poli. Espera, por favor.",
    "Recopilando info del Poli. Paciencia, pronto mostraré resultados.",
    "Consultando repositorios del Poli. Un momento, por favor.",
    "Búsqueda en archivos del Poli en curso. Necesito más tiempo.",
    "Trabajando para obtener datos del Poli. Gracias por esperar.",
    "En proceso de búsqueda en el Poli. Pronto mostraré resultados.",
    "Revisando repositorios del Poli. Espera un momento.",
    "Recopilando info académica del Poli. Pronto mostraré resultados.",
    "Repositorios del Poli están siendo revisados. Gracias por tu paciencia.",
    "Búsqueda en archivos del Poli en progreso. Un poco más de tiempo.",
    "Consultando recursos académicos del Poli. Espera, por favor.",
    "Revisando repositorios del Poli. Te mostraré resultados pronto.",
    "Recopilando datos del Poli. Gracias por tu paciencia.",
    "Trabajando en búsqueda en repositorios del Poli. Resultados en breve.",
    "Consultando registros académicos del Poli. Espera un momento.",
    "Búsqueda en repositorios del Poli en curso. Resultados próximamente.",
    "Recabando información del Poli. Un momento, por favor.",
    "Investigando en archivos del Poli. Ten paciencia, por favor.",
    "Trabajando para encontrar info en el Poli. Pronto te la mostraré.",
    "Revisando recursos académicos del Poli. Espera, por favor."
]



def messageAPICutRespUNAM():
    return resp1[ran(0, len(resp1))]

def messageAPICutRespUAM():
    return resp_uam[ran(0, len(resp_uam))]

def messageAPICutRespTec():
    return resp_tec[ran(0, len(resp_tec))]

def messageAPICutPoli():
    return resp2[ran(0, len(resp2))]

def messageResp():
    return resp[ran(0, len(resp))]