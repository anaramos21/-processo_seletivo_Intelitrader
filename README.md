# -processo_seletivo_Intelitrader
Criação para o  processo seletivo na Intelitrader

Dojo Puzzles

Caso 1 - Nomes de Autores de Obras Bibliográficas

Quando se lista o nome de autores de livros, artigos e outras publicações é comum que se apresente o nome do autor ou dos autores da seguinte forma: sobrenome do autor em letras maiúsculas, seguido de uma vírgula e da primeira parte do nome apenas com as iniciais maiúsculas.

Por exemplo:

SILVA, Joao
COELHO, Paulo
ARAUJO, Celso de
Seu desafio é fazer um programa que leia um número inteiro correspondendo ao número de nomes que será fornecido, e, a seguir, leia estes nomes (que podem estar em qualquer tipo de letra) e imprima a versão formatada no estilo exemplificado acima.

As seguintes regras devem ser seguidas nesta formatação:
o sobrenome será igual a última parte do nome e deve ser apresentado em letras maiúsculas;
se houver apenas uma parte no nome, ela deve ser apresentada em letras maiúsculas (sem vírgula): se a entrada for “ Guimaraes” , a saída deve ser “ GUIMARAES”;
se a última parte do nome for igual a "FILHO", "FILHA", "NETO", "NETA", "SOBRINHO", "SOBRINHA" ou "JUNIOR" e houver duas ou mais partes antes, a penúltima parte fará parte do sobrenome. Assim: se a entrada for "Joao Silva Neto", a saída deve ser "SILVA NETO, Joao" ; se a entrada for "Joao Neto" , a saída deve ser "NETO, Joao";
as partes do nome que não fazem parte do sobrenome devem ser impressas com a inicial maiúscula e com as demais letras minúsculas;
"da", "de", "do", "das", "dos" não fazem parte do sobrenome e não iniciam por letra maiúscula.

Caso 2- Parênteses Booleanos
Dada uma expressão booleana, contendo os símbolos: 'true', 'false', 'and', 'or' e 'xor', elabore um programa que conte de quantas maneiras é possível obter uma resposta ' true', utilizando parênteses.
Por exemplo, dada a expressão 'true and false xor true' existe apenas uma maneira de a expressão retornar 'true': 'true and (false xor true)'


Caso 3- Encontre o telefone
Em alguns lugares é comum lembrar um número do telefone associando seus dígitos a letras. Dessa maneira a expressão MY LOVE significa 69 5683. Claro que existem alguns problemas, uma vez que alguns números de telefone não formam uma palavra ou uma frase e os dígitos 1 e 0 não estão associados a nenhuma letra.

Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente baseado na tabela abaixo. Uma expressão é composta por letras maiúsculas (A-Z), hifens (-) e os números 1 e 0.

Letras  ->  Número 
ABC    ->  2 
DEF    ->  3 
GHI    ->  4 
JKL    ->  5 
MNO    ->  6 
PQRS    ->  7 
TUV    ->  8 
WXYZ   ->  9 
Entrada

A entrada consiste de um conjunto de expressões. Cada expressão está sozinha em uma linha e possui C caracteres, onde 1 ≤ C ≤ 30. A entrada é terminada por fim de arquivo (EOF).

Saída
Para cada expressão você deve imprimir o número de telefone correspondente.

Exemplo de entrada:

1-HOME-SWEET-HOME 
MY-MISERABLE-JOB
Saída correspondente:

1-4663-79338-4663 
69-647372253-562
Curiosidades

A frase "The quick brown fox jumps over the lazy dog" é um pangrama (frase com sentido em que são usadas todas as letras do alfabeto de determinada língua) da língua inglesa.
