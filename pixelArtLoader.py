import requests, bs4, json

class PixelArt:
    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        
class PixelArtEnconder(json.JSONEncoder):
    def default(self, obj):
        
        #se é um PixelArt, trata-o como um dicionario com seus atributos, que ja tem condificacao padrao
        if not isinstance(obj, PixelArt):
            return super(PixelArtEnconder, self).default(obj)
        return obj.__dict__


baseUrl = "http://www.pixelaria.org"
numOfPages = 2
pixelarts = []

for page in range(numOfPages):

    #carrega a pagina em memoria
    res = requests.get(baseUrl + "/pixelart/pagina/"+ str(page + 1))

    #coloca a pagina lida em uma estrutura consultavel
    soup = bs4.BeautifulSoup(res.text)

    pixelartLink = pixelartPage = pixelartSoup = name = desc = image = pixelart = None

    #percorre todos os componentes com class .pixelart, que sao os itens da lista de pixelarts
    for pixelart in soup.select(".pixelart"):

        #pega o link para a pagina do pixel art, usando oa atrivuto href dos componentes        
        pixelartLink = pixelart.parent.get("href")

        #faz uma nova requisicao, agora para pagina individual do pixelart
        pixelartPage = requests.get(baseUrl + pixelartLink)
        pixelartSoup = bs4.BeautifulSoup(pixelartPage.text)

        #pega informacoes sobre o pixel art usando soup
        name = pixelartSoup.select(".pixelart-title")[0].getText()
        desc = pixelartSoup.select(".pixelart-descricao")[0].getText()
        image = pixelartSoup.select(".pixelart-image img")[0].get("src")

        pixelart = PixelArt(name, desc, image)
        pixelarts.append(pixelart)

#transforma a lista em json
json_string = json.dumps(pixelarts, cls = PixelArtEnconder)
print(json_string)
