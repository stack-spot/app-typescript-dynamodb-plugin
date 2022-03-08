## Uso
Nessa seção mostra como é feita a utilização do plugin por meio do CLI, criando uma aplicação baseada no template [**app-typescript-template**](https://github.com/stack-spot/app-typescript-template)  
Após a criação da aplicação é possível aplicar o plugin **skynet-typescript-dynamodb-plugin**

### Pre-requisitos
Necessário a configuração de alguns pré-requisitos para utilização do plugin.
- [**Instalação StakSpot CLI**](https://docs.stackspot.com/v3.0.0/os-cli/installation/)
- [**NodeJS**](https://nodejs.org/en/)
- [**Git**](https://git-scm.com/)
- [**AWS CLI**](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
- [**CDK**](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

### Recomendado
Recomendamos a utilização de algumas ferramentas para desenvolvimento
- [**LocalStack**](https://github.com/localstack/localstack)
- [**dynamodb-admin**](https://www.npmjs.com/package/dynamodb-admin)

### Configuração Stack CLI
Executar comando abaixo para atualização de local com a stack que contém OpenAPI plugin:
```bash
stk add stack https://github.com/stack-spot/skynet-typescript-api-stack
```

#### Verificacao template e plugin
Executando os comandos abaixo é possível verificar que o catálogo foi carregado localmente  
**Listagem plugin disponíveis localmente:**
```bash
stk list plugin
```

**Exemplo output:**
```bash
Stack: skynet-typescript-api-stack
+-----------------------------------+-------------------------------------------------------------------------------------------+---------+-----------------+
| name                              | description                                                                               | types   | version(latest) |
+-----------------------------------+-------------------------------------------------------------------------------------------+---------+-----------------+
| skynet-typescript-dynamodb-plugin | Plugin that applies dynamoDB integration to a typescript lambda app                       | ['app'] | no release      |
|                                   |                                                                                           |         |                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+---------+-----------------+
```

**Listagem template disponíveis localmente:**
```bash
stk list template
```

**Exemplo output:**
```bash
Stack: skynet-typescript-api-stack
+----------------------+---------------------------------------------+------------------+-----------------+
| name                 | description                                 | types            | version(latest) |
+----------------------+---------------------------------------------+------------------+-----------------+
| base-app-ts-template | Base template to work with typescript stack | ['app-template'] | no release      |
|                      |                                             |                  |                 |
+----------------------+---------------------------------------------+------------------+-----------------+
```

### Instalacao
Os passos dessa seção mostram como criar e configurar o plugin na aplicação

**Passo 1.** Copie e cole a URL abaixo no seu terminal:
```bash
stk create app meu-teste-app -t skynet-typescript-api-stack/base-app-ts-template
```

**Passo 2.** Acessar projeto criado:
```bash
cd meu-teste-app
```

**Passo 3.** Aplicação de plugin baseado em catálogo:
```bash
stk apply plugin skynet-typescript-api-stack/skynet-typescript-dynamodb-plugin
```

### Inputs
Abaixo estão listados os inputs do plugin.

Os inputs necessários para utilizar o plugin são:
<table>
  <thead>
    <th>Campo</th>
    <th>Tipo</th>
    <th>Descrição</th>
    <th>Valor Padrão</th>
  </thead>
  <tbody>
    <tr>
      <td>table_name</td>
      <td>text</td>
      <td>Defines the DynamoDB Table name.</td>
      <td>Entity</td>
    </tr>
  </tbody>
</table>

## Useful commands

- `npm run build` compile typescript to jsii
- `npm run watch` watch for changes and compile
- `npm run test` perform the jest unit tests
- `npm run package` package library using jsii
- `npm run coverage` run tests with coverage reports
- `npm run local synth` synthesize CDK project with _cdk local_ and generate/update service stubs
- `npm run local deploy` deploy build _lamba_ to localstack