# Documentação Atividade Robô 

### BackEnd

O código implementa uma aplicação web usando o framework Flask em Python que permite controlar a posição de um robô em um sistema de coordenadas tridimensional. A aplicação é capaz de armazenar as posições do robô em um banco de dados SQLite e retornar sua posição mais recente em diferentes formatos.

A aplicação possui as seguintes funcionalidades:

* Ao acessar a rota principal ("/"), o usuário é redirecionado para a rota "/robo".
* Ao acessar a rota "/robo", o usuário pode visualizar a posição atual do robô no sistema de coordenadas tridimensional em uma página web.
* Ao acessar a rota "/mover" com o método GET, o usuário é direcionado a uma página que permite inserir novos valores para a posição do robô.
* Ao acessar a rota "/mover" com o método POST, o usuário pode enviar as informações de uma nova posição para o robô, que serão armazenadas no banco de dados.
* Ao acessar a rota "/pos" com o método GET, o usuário pode obter a posição mais recente do robô em formato JSON.
* O banco de dados SQLite é criado usando a função "create_tables()" definida no código, que cria uma tabela chamada "robo" com três colunas: "id" (chave primária), "x", "y" e "z" (posições do robô nos eixos do sistema de coordenadas tridimensional).

Ao iniciar a aplicação, a função "create_tables()" é chamada para criar a tabela "robo" no banco de dados. Em seguida, a aplicação é executada na porta 3000 do localhost usando o comando "app.run()".


### FrontEnd

A primeira página do frontend permite que o usuário mova um robô para uma posição específica e utiliza o método HTTP POST para enviar dados para o servidor. O formulário de movimentação do robô contém três campos de entrada para as coordenadas X, Y e Z do robô e um botão "Mover".

A segunda página mostra a posição atual do robô em três coordenadas e um botão "Deslocamento robô", essa página utiliza o método HTTP GET para enviar dados para o servidor.

Ambas as páginas foram construídas utilizando CSS, para definição dos elementos HTML devem ser exibidos na página, incluindo a cor do fundo, a cor do texto, a largura da borda e a posição dos elementos na página.

### Simulação

A simulação do robô em Godot Script permite que este, seja controlado por um usuário para movimentar o robô nas direções desejadas. O código é dividido em duas partes principais, a primeira configura os parâmetros do robô e a outra que faz uma solicitação HTTP para obter a posição atual do objeto e, em seguida, move o corpo com base na posição recebida.

Na primeira parte do código, a funcionalidade do robô é determinada pela entrada de variáveis que contêm o segmento do braço. A função _ready() é responsável por associar cada segmento com o seu nó correspondente na cena do Godot. A função move_body() é responsável por mover o corpo do sprite com base nos números que o usuário insere na interface.

Na segunda parte do código, uma instância da classe HTTPRequest é estendida para lidar com as solicitações HTTP. A variável update_interval define o intervalo de tempo entre as solicitações HTTP. A variável url contém o endereço da API que será solicitado. A função _ready() é responsável por habilitar o processamento do nó, conectar o evento request_completed() à função _on_request_completed(), e iniciar o loop de atualização. A função _process() é responsável por chamar a função request_positions() em intervalos regulares. A função request_positions() é responsável por enviar uma solicitação HTTP para o servidor. A função _on_request_completed() é responsável por lidar com a resposta do servidor, parseando o JSON recebido e chamando a função handle_response() com os dados recebidos. A função handle_response() é responsável por obter as posições dos eixos X e Y do objeto a ser movido e chamar a função move_body() com esses dados para mover o corpo do sprite do robô.

