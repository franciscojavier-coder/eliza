# ELIZA en Python

Este proyecto implementa una versión sencilla de **ELIZA**, un programa de
conversación inspirado en el trabajo de Joseph Weizenbaum. ELIZA analiza frases
en español y responde mediante patrones, reflexiones de pronombres y respuestas
aleatorias.

## Requisitos

- Python 3
- No requiere instalar bibliotecas externas

Para comprobar que Python está instalado:

```bash
python --version
```

En algunos sistemas Linux o macOS puede ser necesario usar `python3` en lugar
de `python`.

## Descargar el proyecto

```bash
git clone https://github.com/franciscojavier-coder/eliza.git
cd eliza
```

Para usar la versión que se encuentra en desarrollo:

```bash
git switch prueba1
```

## Uso interactivo

Ejecute el programa sin argumentos:

```bash
python eliza.py
```

ELIZA mostrará un mensaje inicial y esperará que escriba una frase:

```text
ELIZA: Buenas noches. Cuénteme, ¿qué le preocupa?

USTED : Me siento triste
ELIZA : ¿Desde cuándo se siente triste?
```

Para terminar la conversación, escriba cualquiera de estas palabras:

```text
salir
adios
adiós
chao
bye
exit
quit
```

## Demostración automática

El modo de demostración reproduce una conversación de ejemplo sin solicitar
datos al usuario:

```bash
python eliza.py --demo
```

Este modo es útil para presentaciones o clases, ya que funciona sin conexión a
internet.

## Funcionamiento

El programa contiene:

- Reglas de expresiones regulares para identificar frases comunes.
- Reflexión de pronombres para adaptar las palabras del usuario.
- Varias respuestas posibles para que la conversación no sea siempre igual.
- Respuestas genéricas cuando ninguna regla coincide.
- Un modo interactivo y un modo de demostración automática.

## Archivo principal

Toda la implementación se encuentra en:

```text
eliza.py
```

## Nota

Este proyecto es una demostración educativa de procesamiento de texto. No es
una herramienta de atención psicológica ni sustituye la ayuda de un profesional.
