def montar_html(cidades):
    letra = ''
    cidades.sort()
    nome_arquivo = 'cidades.html'
    arquivo_html = open(nome_arquivo, 'w', encoding='utf-8')
    html = '<!DOCTYPE html>\n'
    html += '<html lang="pt-br">\n'
    html += '    <head>\n'
    html += '        <meta charset="utf-8">\n'
    html += '        <title>Cidades do Estado de São Paulo</title>\n'
    html += '    </head>\n'
    html += '    <body>\n'
    for cidade in cidades:
        if letra != cidade[0]:
            letra = cidade[0]
            html += '        <h1>' + letra.upper() + '</h1>\n'
        html += '        <p>' + cidade + '</p>\n'
    html += '    </body>\n'
    html += '</html>\n'
    arquivo_html.write(html)
    arquivo_html.close()
    return nome_arquivo
