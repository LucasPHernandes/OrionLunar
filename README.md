
# OrionLunar
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/LucasPHernandes/OrionLunar)
![GitHub License](https://img.shields.io/github/license/LucasPHernandes/OrionLunar)
![GitHub Release](https://img.shields.io/github/v/release/LucasPHernandes/OrionLunar)

Sistema de inventário de itens, pensado para grandes fluxos, com necessidade de agilidade.
Inteiramente focado para itens de alta rotabilidade, utilizando-se do DearPyGui como proposta de
desenvolvimento de interface rápida e simples.

O uso de SQLite possibilita uma maior agilidade na manipulação de dados, assim como de manutenção
quando **em menor escala**.



## Organização dos dados:
Espaço com a proposta de organizar a estrutura de dados presente no OrionLunar.
### Name: Itens
Tabela respoonsável pelo armazenamento dos itens disponíveis par empréstimo.
| COD | NOME      | QUANTIDADE | CATEGORIA |
| --- | --------- | ---------- | --------- |

Ex:

| COD | NOME             | QUANTIDADE | CATEGORIA     |
| --- | ---------------  | ---------- | ------------- |
| 001 | Adaptador HDMI   | 010        | Áudio e Vídeo |
| 002 | Cabo HDMI        | 060        | Áudio e Vídeo |
| 003 | Monitor Dell 21' | 012        | Periféricos   |


### Name: Emprestimos
Tabela responsável pelo controle dos empréstimos já realizados, assim como as datas de saída e chegada do item.
| PROTOCOLO | CPF | COD(Nome do Item) | QUANTIDADE | SAIDA | DEVOLUCAO |
| --------- | --- | ----------------- | ---------- | ----- | --------- |

Ex:

| PROTOCOLO | CPF         | COD(Nome do Item) | QUANTIDADE | SAIDA            | DEVOLUCAO |
| --------- | ----------- | ------------------ | ---------- | ---------------- | --------- |
|   0001    | 12345678909 |        002         |    001     | 10:06 18/01/2024 |    NÃO    |

### Name: Pessoas
Usar informações do LDAP, para pegar o nome e fazer a conferência da quantidade de itens que retirou,
além de ver se está faltando devolver algo, assim como decidir se pode ter acesso a determinados itens.

## Licença
Este software está sobre a licença GNU