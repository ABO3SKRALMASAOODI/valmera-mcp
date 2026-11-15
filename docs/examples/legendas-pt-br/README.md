# Como colocar legendas em português no MP4 e manter o áudio original

[Baixe o MP4 com duas faixas de legenda](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/examples/legendas-pt-br/sintel-legendas.mp4). São 9,6 segundos de *Sintel*, com o diálogo original em inglês. Abra o arquivo em um reprodutor que permita escolher legendas, como o VLC. No menu de legendas, selecione **Português (Brasil)**, troque para **English** e desligue as legendas. O mesmo arquivo serve para as três opções.

| Tempo no vídeo | Português (Brasil) | English |
| --- | --- | --- |
| 0:01 | O que te traz à terra dos guardiões? | What brings you to the land of the gatekeepers? |
| 0:04 | Sem legenda | Sem legenda |
| 0:07 | Estou procurando alguém. | I'm searching for someone. |

Se você editar um vídeo para duas equipes, esse teste resolve uma dúvida antes da entrega. Com uma faixa selecionável, cada pessoa escolhe o idioma. Se o destino exigir texto sempre visível, inclusive em um aplicativo que descarte as faixas de legenda, exporte uma cópia com o texto gravado na imagem e confira o arquivo depois de publicá-lo.

## Confira os tempos antes de juntar os arquivos

Baixe as legendas em [português](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/examples/legendas-pt-br/dialogo.pt-BR.srt) e [inglês](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/examples/legendas-pt-br/dialogo.en.srt). Abra o [comparador gratuito do Valmera](https://valmera.io/tools/compare-srt-files?utm_source=github&utm_medium=guia&utm_campaign=legendas_pt_br), carregue o inglês em **Open original SRT**, o português em **Open revised SRT** e clique em **Compare subtitles**. As duas falas mudam de texto. Nenhuma muda de tempo. O [relatório baixado do comparador](comparacao.json) guarda os textos e os quatro limites de tempo para revisão.

A primeira fala entra em 0,100 s e sai em 2,500 s. A segunda começa em 6,550 s. Esse intervalo sem texto faz parte da cena. Se você cortar a abertura depois de traduzir, confira novamente as entradas no novo corte. O comparador verifica diferenças entre os SRTs. Para verificar a sincronização com a voz, ouça o vídeo.

## Monte seu próprio MP4 com o FFmpeg

Use uma cópia do seu vídeo e dois arquivos SRT em UTF-8. Para reproduzir o exemplo, extraia `talk.mp4` deste [pacote de referência](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/evaluation/sintel-spanish-20261107/bilingual-webvtt-player.zip) e coloque os dois SRTs na mesma pasta. O comando seleciona a primeira faixa de vídeo e a primeira de áudio. Se o seu original tiver várias faixas de som que devam ser entregues, mapeie cada uma.

```sh
ffmpeg -i talk.mp4 -i dialogo.pt-BR.srt -i dialogo.en.srt \
  -map 0:v:0 -map 0:a:0 -map 1:0 -map 2:0 \
  -c:v copy -c:a copy -c:s mov_text \
  -metadata:s:a:0 language=eng \
  -metadata:s:s:0 language=por -metadata:s:s:0 'handler_name=Português (Brasil)' \
  -metadata:s:s:1 language=eng -metadata:s:s:1 handler_name=English \
  -disposition:s:0 default -disposition:s:1 0 -movflags +faststart entrega.mp4
```

O português fica marcado como padrão, embora o reprodutor possa respeitar a preferência de idioma de quem assiste. Para entregar somente o SRT, envie o arquivo de legenda correspondente ao corte aprovado. A pessoa que recebe o vídeo poderá usá-lo num reprodutor compatível ou no campo de legendas da plataforma.

## O que verificamos na entrega

Extraímos do MP4 as duas faixas de legenda. Os textos e tempos coincidiram com os dois SRTs. Também comparamos os 230 quadros decodificados e as 460.800 amostras por canal do áudio estéreo com o trecho de origem. A imagem e o som coincidiram integralmente. Os hashes e a comparação dos pacotes e tempos estão no [registro de verificação](verificacao.json).

O Valmera comparou as legendas no navegador. O empacotamento do MP4 com faixas selecionáveis foi feito com FFmpeg. Para fazer cortes por conversa e revisar uma prévia no Studio, consulte o [exemplo de revisão com vídeo](https://valmera.io/ai-agent-that-edits-video#recorded-revision) e os [planos para edição com IA](https://valmera.io/subscribe).

**Créditos.** *Sintel*, © Blender Foundation, [trailer original](https://download.blender.org/durian/trailer/sintel_trailer-1080p.mp4), [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). O exemplo usa um trecho reduzido do trailer, de 11,9 a 21,5 segundos. O Valmera acrescentou duas faixas selecionáveis e preparou uma tradução de demonstração para o português brasileiro. Ela não é a tradução oficial do filme. Ao redistribuir o trecho, mantenha o crédito, a licença e a descrição das alterações.
