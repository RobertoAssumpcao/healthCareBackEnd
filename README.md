<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]

<br />
<div align="center">
  <h1 align="center">Health care</h1>
  <h2>Back End</h2>

  <p align="center">
    <a href="https://github.com/RobertoAssumpcao/healthCareBackEnd/issues">Report Bug</a>
    ·
    <a href="https://github.com/RobertoAssumpcao/healthCareBackEnd/issues">Request Feature</a>
  </p>
</div>

## About

Este projeto tem como objetivo registrar [glicose](https://www.healthline.com/health/glucose) para análises futuras ou para facilitar o manejo, especialmente para pessoas que têm dificuldade em gerenciar seus níveis, seja registrando ou verificando a quantidade de glicose que precisam ingerir.

**Este projeto foi inspirado na minha avó =) =)**

## Como usar

> Python 3.12.6

1. **Clone o repository:**

   ```bash
   git clone https://github.com/RobertoAssumpcao/healthCareBackEnd.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd healthCareBackEnd
   ```

> ⚠️ O desenvolvimento foi feito usando o sistema operacional Fedora Linux 40. Dependendo do seu sistema operacional, a maneira de instalar e ativar o ambiente virtual pode mudar. Em caso de dúvida, consulte os [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

3. **Criar o ambiente virtual**

   ```bash
   python3 -m venv .venv
   ```

4. **Ativar o ambiente virtual**

   ```bash
   source .venv/bin/activate
   ```

5. **Instalar as dependências**

   ```bash
   pip install -r requirements.txt
   ```

6. **run a API:**

   ```bash
   flask run --host 0.0.0.0 --port 5000
   ```

   OR

   ```bash
   flask run --host 0.0.0.0 --port 5000 --reload
   ```

> Este segundo comando reiniciará automaticamente o servidor após uma alteração no código-fonte.

Para atualizar o requirements.txt

   ```bash
   pip freeze > requirements.txt
   ```

## Contribuição

Contribuições são o que fazem a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

Se você tiver uma sugestão que possa melhorar este projeto, por favor, faça um fork do repositório e crie um pull request. Você também pode simplesmente abrir uma issue. Não se esqueça de dar uma estrela ao projeto! Muito obrigado!

1. Faça um fork do projeto
2. Crie sua Branch de Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Faça o push da sua Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

<p align="right">(<a href="#top">voltar ao topo</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/RobertoAssumpcao/healthCareBackEnd.svg?style=for-the-badge

[contributors-url]: https://github.com/RobertoAssumpcao/healthCareBackEnd/graphs/contributors

[issues-shield]: https://img.shields.io/github/issues/RobertoAssumpcao/healthCareBackEnd.svg?style=for-the-badge

[issues-url]: https://github.com/RobertoAssumpcao/healthCareBackEnd/issues
