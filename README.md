# Qual a ideia do prjeto?

- Sistema de inventario para os intens a serem emprestados da CTI
- Usando dearPyGui
- Banco de Dados: SQLite


## Tabelas:
### Name: Itens
| COD | NOME | QUANTIDADE | CATEGORIA |

Ex:
_______________________________________________________
| COD | NOME             | QUANTIDADE | CATEGORIA     |
| 001 | Adaptador HDMI   |     010    | Áudio e Vídeo |
| 002 | Cabo HDMI        |     060    | Áudio e Vídeo |
| 003 | Monitor Dell 21' |     012    | Periféricos   |
-------------------------------------------------------

### Name: Imprestimos
| PROTOCOLO | CPF | COD(Nome do Item) | QUANTIDADE | SAIDA | DEVOLUCAO |

Ex:
===========================================================================================
| PROTOCOLO | CPF         | COD(Nome do Item) | QUANTIDADE | SAIDA            | DEVOLUCAO |
|    0001   | 03885826003 |        002        |     001    | 10:06 18/01/2024 |    NÃO    |
===========================================================================================
