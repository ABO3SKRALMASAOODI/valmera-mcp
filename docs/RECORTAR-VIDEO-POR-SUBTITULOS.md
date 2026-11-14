# Recorta una entrevista por subtítulos y conserva el audio

Si ya tienes un MP4 y su archivo SRT o VTT, puedes seleccionar una frase y descargar dos archivos: el fragmento de video y los subtítulos ajustados al inicio del recorte. El [editor de video online de Valmera en español](https://valmera.io/es/editor-de-video-online) procesa este corte en el navegador sin cuenta. Para pedir al agente un montaje más amplio, puedes llevar los tiempos a Studio.

## Prueba con una pregunta y una respuesta

El ejemplo usa un fragmento del tráiler de *Sintel*. El diálogo original está en inglés. Valmera preparó los subtítulos en español para este ejercicio. Puedes [descargar el MP4 original del ejercicio](https://valmera.io/examples/sintel-dialogo/original.mp4) y [abrir su archivo VTT](https://valmera.io/examples/sintel-dialogo/dialogo.vtt).

| Frase | Inicio en el fragmento | Fin |
| --- | --- | --- |
| ¿Qué te trae a la tierra de los guardianes? | 0,10 s | 2,50 s |
| Busco a alguien. | 6,55 s | 8,00 s |

Selecciona la segunda frase y pulsa **Crear MP4 del recorte**. Reproduce el resultado y escucha la entrada de la voz. Al descargar el SRT, la única frase que contiene debería ser «Busco a alguien». El inicio de esa frase coincide con el inicio del recorte.

```srt
1
00:00:00,000 --> 00:00:01,450
Busco a alguien.
```

Ahora conserva un poco de ambiente. Fija el inicio en 6,30 y el fin en 8,00. Vuelve a exportar el video y el SRT. La frase entra a los 0,25 segundos del nuevo clip. El tiempo que le restas al subtítulo de origen es el inicio del recorte, 6,30 segundos. [Descarga de referencia de la primera selección](https://valmera.io/examples/sintel-dialogo/respuesta.mp4) · [SRT de referencia](https://valmera.io/examples/sintel-dialogo/respuesta.srt).

## Lleva el corte a tu propio proyecto

Abre tu entrevista y sus subtítulos. Elige una frase que funcione sin escuchar la pregunta. Si la persona responde «sí» o alude a «eso», conserva también el contexto necesario. Reproduce el fragmento antes de aprobarlo y escucha si el corte se lleva parte de una palabra.

Para seguir con IA, pulsa **Llevar este recorte a Studio**, inicia sesión y sube el original al proyecto. Revisa el intervalo y pide la siguiente modificación en español. Por ejemplo, «Mantén esta respuesta y recupera la pausa que precede a la última frase». La edición con IA requiere un [plan de pago](https://valmera.io/subscribe). Para dirigir el mismo proyecto desde un asistente compatible, consulta la [conexión MCP](https://valmera.io/mcp/setup).

*Sintel*, © Blender Foundation, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). Valmera seleccionó, redimensionó y subtituló un fragmento del [tráiler original](https://download.blender.org/durian/trailer/sintel_trailer-1080p.mp4). [Créditos para acompañar el archivo](https://valmera.io/examples/sintel-dialogo/creditos.txt).
