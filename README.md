# CRUD_NEO4J_FRUTAS

Você vai encontrar neste repositório um CRUD na linguagem Python, configurado para armazenar Nome de Frutas no Banco de Dados NoSQL Neo4j.
<br>
<br>
Este é um projeto de CRUD (Create, Read, Update, Delete) desenvolvido como atividade para a disciplina de Banco de Dados Não Convencionais. O objetivo principal deste CRUD é conectar-se a um banco de dados específico.
<br>
<br>
Descrição: Inicialmente, este projeto foi concebido como um CRUD para gerenciar registros de frutas. O propósito era permitir o cadastro, visualização, atualização e exclusão de frutas através da interação com um banco de dados.
<br>
<br>
Banco de Dados: O banco de dados utilizado neste projeto é o Neo4J, uma solução de banco de dados NoSQL. Foi criado um banco chamado "Frutas", o qual possui um único atributo, que é o nome da fruta. Essa escolha foi feita para simplificar o projeto e focar no funcionamento do CRUD em si. Para armazenar o banco de dados, foi utilizada a plataforma AuraDB Free Tier, que oferece uma opção gratuita para hospedar bancos de dados Neo4J.
<br>
<br>
O CRUD implementado neste projeto permite realizar as seguintes operações:

- Criar: É possível adicionar um novo registro de fruta no banco de dados, informando apenas o nome da fruta.

- Visualizar: É possível visualizar todos os registros de frutas existentes no banco de dados.

- Atualizar: É possível atualizar o nome de uma fruta já cadastrada, fornecendo o novo nome e o identificador único da fruta a ser atualizada.

- Deletar: É possível excluir um registro de fruta do banco de dados, informando o identificador único da fruta a ser removida.
<br>
<br>
Instruções de Uso:
<br>
<br>
1. Clone este repositório em sua máquina local;
2. Certifique-se de ter o Neo4J instalado ou utilize a plataforma AuraDB Free Tier para criar um banco de dados Neo4J;
3. Configure as credenciais de conexão ao banco de dados “URI e password”, que são informados na plataforma do Neo4J;
4. Rode o comando ‘pip install neo4j’ na pasta do projeto para instalar as dependências;
5. Execute o arquivo principal do projeto para iniciar a aplicação ‘python nome_arquivo.py’;
6. Utilize os comandos disponíveis para interagir com o CRUD e gerenciar os registros de frutas.
<br>
<br>
Contribuições são bem-vindas! Caso tenha alguma ideia de melhoria, correção de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.
<br>
<br>
Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT). Sinta-se à vontade para utilizar, modificar e distribuir o código conforme os termos da licença. As os arquivos de 'senha' e 'uri' foram removidos para segurança.
<br>
<br>
<h2 >Desenvolvedores</h2>
<table>
  <tr>
    <td align="center"><a href="https://github.com/AyrtonMaia0"><img src="https://avatars.githubusercontent.com/u/98968093?v=4" width="100px;" alt="Imagem Ayrton Maia"/><br /><sub><b>Ayrton Maia</b></sub></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/sabrinam-silva/"><img src="https://encurtador.com.br/abuD9" width="100px;" alt="Imagem Sabrina Silva"/><br /><sub><b>Sabrina Silva</b></sub></a></td>
  </tr>
