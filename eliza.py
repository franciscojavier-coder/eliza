

import random
import re
import time

# ---------------------------------------------------------------------
# 1) REFLEXIÓN DE PRONOMBRES
#    Cambia la persona gramatical para que la respuesta suene natural,
#    como si ELIZA le "devolviera" la frase a quien la escribió.
# ---------------------------------------------------------------------
REFLEXIONES = {
    "yo": "tú", "tú": "yo", "tu": "mi", "tus": "mis", "mi": "tu",
    "mis": "tus", "mí": "ti", "ti": "mí", "me": "te", "te": "me",
    "soy": "es", "eres": "es", "estoy": "está", "estás": "está",
    "mío": "tuyo", "mía": "tuya", "míos": "tuyos", "mías": "tuyas",
    "tuyo": "mío", "tuya": "mía", "tuyos": "míos", "tuyas": "mías",
    "conmigo": "contigo", "contigo": "conmigo",
    "nosotros": "ustedes", "nuestro": "su", "nuestra": "su",
}


def reflejar(frase: str) -> str:
    palabras = frase.strip().split()
    resultado = [REFLEXIONES.get(p.lower(), p) for p in palabras]
    return " ".join(resultado)


# ---------------------------------------------------------------------
# 2) REGLAS: (patrón de búsqueda, lista de plantillas de respuesta)
#    "{0}" se reemplaza por el fragmento capturado y reflejado.
#    Se evalúan en orden, de la más específica a la más general.
# ---------------------------------------------------------------------
REGLAS = [
    (r"\bnecesito (.*)", [
        "¿Por qué necesita {0}?",
        "¿De verdad cree que necesita {0}?",
        "¿Qué pasaría si no consigue {0}?",
    ]),
    (r"\bno puedo (.*)", [
        "¿Qué le hace pensar que no puede {0}?",
        "¿Ha intentado alguna vez {0}?",
        "¿Quizás ahora sí podría {0}?",
    ]),
    (r"\bquiero (.*)", [
        "¿Por qué quiere {0}?",
        "¿Qué significaría para usted lograr {0}?",
        "¿Desde cuándo quiere {0}?",
    ]),
    (r"\b(?:mi |mis )?(?:madre|mamá)\b(.*)", [
        "Cuénteme más sobre su familia.",
        "¿Qué relación tiene eso con lo que siente ahora?",
        "¿Cómo describiría su relación con ella?",
    ]),
    (r"\b(?:mi |mis )?(?:padre|papá)\b(.*)", [
        "Hábleme un poco más de su padre.",
        "¿Qué recuerdo tiene de él?",
        "¿Cómo se relaciona eso con su situación actual?",
    ]),
    (r"\b(?:me siento|siento)\s+(.*)", [
        "¿Por qué se siente {0}?",
        "¿Desde cuándo se siente {0}?",
        "¿Qué cree que provoca que se sienta {0}?",
    ]),
    (r"\bsoy\s+(.*)", [
        "¿Desde cuándo es {0}?",
        "¿Cree que ser {0} tiene relación con el motivo de su consulta?",
    ]),
    (r"\bporque\s+(.*)", [
        "¿Esa es la verdadera razón?",
        "¿Qué otra razón podría haber detrás de eso?",
    ]),
    (r"\b(?:sueño|soñé|sueñas|sueña)\s+(.*)", [
        "¿Qué cree que significa ese sueño?",
        "¿Sueña con eso frecuentemente?",
    ]),
    (r"\b(?:siempre|todos los días|nunca)\b(.*)", [
        "¿Puede darme un ejemplo concreto?",
        "¿Realmente 'siempre'? ¿No hay ninguna excepción?",
    ]),
    (r"\b(hola|buenas|buenas noches|buenas tardes)\b", [
        "Buenas noches. ¿Cómo se siente hoy?",
        "Hola. Cuénteme, ¿qué le trae por aquí?",
    ]),
    (r"\b(gracias)\b", [
        "No hay de qué. ¿Hay algo más que quiera comentarme?",
    ]),
]

RESPUESTAS_GENERICAS = [
    "Cuénteme más sobre eso.",
    "¿Por qué dice usted eso?",
    "Entiendo. Continúe, por favor.",
    "¿Podría explicarme un poco más?",
    "¿Cómo le hace sentir eso?",
    "Interesante. ¿Y qué más?",
    "¿Qué piensa usted al respecto?",
]

DESPEDIDAS = {"salir", "adios", "adiós", "chao", "bye", "exit", "quit"}


def responder(texto: str) -> str:
    texto_normalizado = texto.lower().strip()

    for patron, plantillas in REGLAS:
        coincidencia = re.search(patron, texto_normalizado)
        if coincidencia:
            plantilla = random.choice(plantillas)
            if coincidencia.groups() and "{0}" in plantilla:
                fragmento = reflejar(coincidencia.group(1))
                return plantilla.format(fragmento.strip(" .,!?"))
            return plantilla

    return random.choice(RESPUESTAS_GENERICAS)


# ---------------------------------------------------------------------
# 3) MODO DEMOSTRACIÓN AUTOMÁTICA
#    Reproduce, sin necesitar internet ni que nadie escriba nada,
#    una conversación de ejemplo inspirada en el artículo original
#    de Weizenbaum (1966) — útil si el proyector es lo único que
#    funciona ese día.
# ---------------------------------------------------------------------
CONVERSACION_DEMO = [
    "Todos los hombres son iguales.",
    "Siempre nos están molestando con una cosa u otra.",
    "Bueno, mi novio me hizo venir aquí.",
    "Dice que estoy triste casi todo el tiempo.",
    "Es verdad. Soy infeliz.",
    "Necesito ayuda, eso sí parece cierto.",
    "Quizás podría aprender a llevarme mejor con mi madre.",
    "Mi madre se preocupa mucho por mí.",
]


def correr_demo():
    print("=" * 60)
    print(" DEMOSTRACIÓN AUTOMÁTICA — Conversación estilo ELIZA (1966)")
    print("=" * 60)
    print("ELIZA: Buenas noches. Cuénteme qué le preocupa.\n")
    time.sleep(1)
    for linea in CONVERSACION_DEMO:
        print(f"USUARIO: {linea}")
        time.sleep(0.8)
        print(f"ELIZA:   {responder(linea)}\n")
        time.sleep(1.4)
    print("=" * 60)
    print("Fin de la demostración. Ejecute 'python eliza.py' (sin --demo)")
    print("para que el grupo escriba sus propias frases en vivo.")


# ---------------------------------------------------------------------
# 4) MODO INTERACTIVO — el que se usa en clase
# ---------------------------------------------------------------------
def correr_interactivo():
    print("=" * 60)
    print(" ELIZA — demostración en vivo (escriba 'salir' para terminar)")
    print("=" * 60)
    print("ELIZA: Buenas noches. Cuénteme, ¿qué le preocupa?\n")

    while True:
        entrada = input("USTED : ").strip()
        if not entrada:
            continue
        if entrada.lower() in DESPEDIDAS:
            print("ELIZA : Que tenga buena noche. Fue un gusto conversar.")
            break
        print(f"ELIZA : {responder(entrada)}\n")


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv:
        correr_demo()
    else:
        correr_interactivo()
