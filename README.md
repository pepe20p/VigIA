O VigIA é uma aplicação Web para reconhecimento de eventos em uma gravação de câmera de vigilância.

Versão: HTML 5.0

Requisitos Mínimos: Navegadores suportados

Serviço hospedado em servidor próprio devido à necessidade de complexo processamento de imagens.

Linguagens de Programação

- Python 3
- HTML
- CSS
- JavaScript

Frameworks e Bibliotecas

- Back-end: Django
- Mobile: PWA

Banco de Dados

Principal: SQLite (com adapter para qualquer BD fornecido pelo framework)

IAs

OpenCV - Redes YOLO v4 e v7 (ambas tiny) pré-treinadas

Arquitetura do Sistema

O usuário realiza upload do vídeo para o nosso servidor, onde a IA realizará a indentificação dos eventos no vídeo e após isso o usuário vai visualizar um player de video com as tags e timestamps dos eventos ocorridos na gravação.

Front-End:

Aplicação WEB para submeter o vídeo e visualização pelo usuário através do player de vídeo

Back-End:

Análise do conteúdo pela IA, formando as "tags" de maior relevância com seus respectivos momentos

Implementados pelo framework Django