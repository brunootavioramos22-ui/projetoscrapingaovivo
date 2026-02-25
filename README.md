# 📚 Web Scraping - Books to Scrape

Projeto de Web Scraping desenvolvido com **Python** e **Scrapy** para extração automatizada de dados do site de testes:

🔗 https://books.toscrape.com/catalogue/page-1.html

---

## 🚀 Objetivo

Coletar automaticamente informações detalhadas de todos os livros disponíveis no site, incluindo:

- 📌 Título
- 💰 Preço
- 📝 Descrição
- 📂 Categoria
- 📦 Disponibilidade (Estoque)
- 🖼 URL da imagem
- ⬇ Download automático das imagens

---

## 🛠 Tecnologias Utilizadas

- Python 3.14
- Scrapy 2.13.4
- Conda (Ambiente Virtual)
- PowerShell / Anaconda Prompt

---

## 📂 Estrutura do Projeto
primeiraspider/
│
├── primeiraspider/
│
└── scrapy.cfg
├── spiders/
│ └── books.py
├── settings.py
├── items.py

---

## ⚙️ Como Funciona

### 1️⃣ Navegação

A spider:

- Acessa a página inicial do catálogo
- Percorre automaticamente todas as páginas (paginação)
- Coleta os links individuais de cada livro

### 2️⃣ Extração

Para cada livro, o sistema acessa sua página individual e extrai:

```python
{
    'titulo': ...,
    'preco': ...,
    'descricao': ...,
    'categoria': ...,
    'estoque': ...,
    'image_urls': [...]
}
``` 

 ### 🗺️ Download Automático de Imagens

O projeto utiliza o ImagesPipeline do Scrapy para baixar automaticamente as imagens dos livros.

Configuração no settings.py:

ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
}

IMAGES_STORE = 'imagens'

As imagens são armazenadas na pasta:

imagens/full/

### ▶️ Como Executar:

  1️⃣ Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

2️⃣ Acesse a pasta do projeto:

``` bash
 cd primeiraspider
```
3️⃣ Ative o ambiente virtual (se estiver usando Conda):

``` bash
 conda activate primeiraspider
```
4️⃣ Execute a spider:

```bash
 scrapy crawl books -O livros.json
```
### 📊 Resultado

O arquivo livros.json será gerado contendo todos os livros extraídos do site em formato estruturado.

Exemplo:
  ``` json
{
  "titulo": "A Light in the Attic",
  "preco": "£51.77",
  "descricao": "...",
  "categoria": "Poetry",
  "estoque": "In stock (22 available)"
}
  ```
### 🧠 Aprendizados

Durante o desenvolvimento foram aplicados conceitos como:

Web Scraping estruturado

Seletores CSS e XPath

Tratamento de dados com normalize-space()

Conversão de URLs relativas para absolutas

Automação de paginação

Download automático de mídia
