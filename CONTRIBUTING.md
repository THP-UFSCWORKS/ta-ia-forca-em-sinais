# Contribuindo para o Projeto

Este documento contém diretrizes para garantir que a contribuição seja eficiente e alinhada com as práticas do nosso ambiente colaborativo.

## Código de Conduta

É fundamental que todos os contribuidores adotem um comportamento profissional e respeitoso. Encorajamos você a ler e seguir o [Código de Conduta](https://github.com/theHprogrammer/forca-em-sinais/blob/main/CODE_OF_CONDUCT.md) que orienta nossas interações dentro do projeto.

## Sumário

- [Como Contribuir](#como-contribuir)
  - [Issues](#issues)
  - [Pull Requests](#pull-requests)
- [Convenção de Branches](#convenção-de-branches)
- [Convenção de Commits](#convenção-de-commits)

---

## Como Contribuir

### Fork

Para começar a contribuir, primeiro faça um fork do repositório. Isso cria uma cópia do repositório em sua conta do GitHub.

1. Acesse o repositório no GitHub: [forca-em-sinais](https://github.com/theHprogrammer/forca-em-sinais)
2. Clique no botão "Fork" no canto superior direito da página.
3. Isso criará uma cópia do repositório em seu próprio GitHub.

### Issues

Contribuir através de issues é uma forma valiosa de participar do desenvolvimento do projeto. Utilize os templates específicos para cada tipo de issue para garantir que sua contribuição seja clara e eficaz.

#### Reportando Bugs

Se identificar algum problema, utilize o template `Bug Report` para criar uma issue detalhada. Isso nos ajuda a entender o problema e a implementar correções de maneira eficaz.

#### Solicitando Funcionalidades

Para novas ideias ou sugestões de melhorias, use o template `Feature Request`. Sua iniciativa é crucial para o dinamismo e inovação do projeto.

#### Documentação

Melhorias ou correções na documentação são sempre bem-vindas. Se você observar que algo pode ser melhorado ou corrigido, use o template `Documentation`.

#### Perguntas e Ajuda

Se você tem perguntas sobre o projeto, utilize o template `Question` para esclarecer suas dúvidas.

#### Problemas de Configuração

Se você enfrentar dificuldades ao configurar o ambiente necessário para o projeto, use o template `Setup Problem` para buscar assistência.

#### Solicitações de Ajuda

Para tarefas complexas ou problemas que exigem habilidades específicas, utilize o template `Help Wanted`.

### Pull Requests

Contribuir com mudanças diretas no código ou na documentação é crucial para o desenvolvimento do projeto. Para garantir que suas contribuições sejam eficazes e bem integradas, siga estas etapas:

#### 1. **Clone o Repositório do Fork**

- Clone o repositório do fork usando HTTPS ou SSH:

- **HTTPS**:
    ```bash
    git clone https://github.com/seu-usuario/forca-em-sinais.git
    ```

- **SSH**:
    ```bash
    git clone git@github.com:seu-usuario/forca-em-sinais.git
    ```

#### 2. **Crie uma Branch**

- A partir da branch principal (geralmente `main` ou `master`), crie uma branch para suas alterações:

```bash
git checkout -b nome-da-sua-branch
```

- Isso ajuda a manter o desenvolvimento organizado e facilita a criação de pull requests.

#### 3. **Commits de Qualidade**

- Siga a convenção de commits adotada para suas mensagens de commit. Exemplos:

```
git commit -m "feat: adicionar autenticação via OAuth"
git commit -m "fix: corrigir carga lenta da página de perfil"
```

- Essas convenções ajudam a manter o histórico do projeto claro e útil para todos os envolvidos.

#### 4. **Teste**

- Teste seu código completamente para garantir que todas as funcionalidades e correções estejam funcionando como esperado.
- Adicione novos testes para cobrir as mudanças feitas, o que ajuda a prevenir futuras regressões.
- Garanta que todos os testes existentes também estejam passando.

#### 5. **Documentação**

- Atualize a documentação para refletir qualquer mudança na funcionalidade ou nos procedimentos. Inclua exemplos, guias de instalação, e detalhes de API, se aplicável.

#### 6. **Submeta o Pull Request**

- Antes de submeter o pull request, sincronize sua branch com a branch principal do repositório original para incluir quaisquer atualizações recentes:

```bash
git remote add upstream https://github.com/theHprogrammer/forca-em-sinais.git
git fetch upstream
git rebase upstream/main
```

- Envie suas alterações para o repositório no GitHub:

```bash
git push origin nome-da-sua-branch
```

- Vá ao GitHub e inicie um pull request da sua branch para a branch principal do repositório original. Na descrição do pull request, inclua uma explicação clara do que foi mudado e o motivo (use o template).

## Convenção de Branches

Uma boa prática de gestão de branches facilita a organização do projeto e ajuda na colaboração entre os desenvolvedores. Abaixo estão as diretrizes para a criação e gerenciamento de branches dentro do projeto:

### Tipos de Branches

- **Main/Master**: Esta é a branch principal do repositório e deve ser a mais estável. Todas as features, hotfixes e releases são eventualmente mescladas a esta branch.

- **Develop**: Caso o projeto utilize uma branch adicional para desenvolvimento, a branch `develop` é usada como uma etapa antes da integração com a `main`. Esta branch contém avanços que ainda estão sob testes mais intensivos.

### Branches de Feature

Branches de feature são usadas para desenvolver novas funcionalidades para o projeto. Elas devem ser derivadas da branch `develop` (ou `main`, se `develop` não for usada):

```bash
git checkout -b feature/nome-da-feature
```

### Branches de Bugfix

Branches de bugfix são utilizadas para correções de bugs urgentes e devem ser criadas a partir da branch `main` ou `develop`, dependendo de onde o bug foi encontrado:

```bash
git checkout -b bugfix/descrição-do-bug
```

### Branches de Release

Branches de release são usadas para preparar uma nova versão do produto. Elas permitem que os últimos ajustes e documentações sejam feitos antes de um lançamento:

```bash
git checkout -b release/versão
```

### Branches de Hotfix

Hotfix branches são criadas para corrigir rapidamente problemas na versão em produção. Elas são baseadas na branch `main`:

```bash
git checkout -b hotfix/descrição-do-hotfix
```

### Nomenclatura de Branches

Para manter tudo organizado, use uma nomenclatura consistente para suas branches, refletindo claramente o conteúdo e o objetivo da branch:

- Para features: `feature/nome-claro-da-feature`
- Para bugs: `bugfix/descrição-clara-do-bug`
- Para releases: `release/versão`
- Para hotfixes: `hotfix/descrição-clara-do-hotfix`

### Dicas Adicionais

- Mantenha suas branches o mais curtas e focadas possível. Isso facilita a revisão por pares e a gestão do projeto.
- Antes de criar uma nova branch, certifique-se de que sua base está atualizada com a última versão da branch de origem (main ou develop).

Ao seguir estas convenções, facilitamos o processo de revisão e integração de código, mantendo nosso repositório limpo e organizado.

## Convenção de Commits

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

Utilizamos a convenção de [Conventional Commits](https://www.conventionalcommits.org/pt-br) para manter nosso histórico de commits claro e facilitar a geração automática de logs de mudanças e versões. Esta convenção estabelece um conjunto de regras para criar mensagens de commit estruturadas que são fáceis de seguir quando você olha para o histórico de desenvolvimento.

### Principais tipos e descrições

O commit semântico possui os elementos estruturais abaixo (tipos), que informam a intenção do seu commit ao utilizador(a) de seu código.

- `feat`- Commits do tipo feat indicam que seu trecho de código está incluindo um **novo recurso** (se relaciona com o MINOR do versionamento semântico).

- `fix` - Commits do tipo fix indicam que seu trecho de código commitado está **solucionando um problema** (bug fix), (se relaciona com o PATCH do versionamento semântico).

- `docs` - Commits do tipo docs indicam que houveram **mudanças na documentação**, como por exemplo no Readme do seu repositório. (Não inclui alterações em código).

- `test` - Commits do tipo test são utilizados quando são realizadas **alterações em testes**, seja criando, alterando ou excluindo testes unitários. (Não inclui alterações em código)

- `build` - Commits do tipo build são utilizados quando são realizadas modificações em **arquivos de build e dependências**.

- `perf` - Commits do tipo perf servem para identificar quaisquer alterações de código que estejam relacionadas a **performance**.

- `style` - Commits do tipo style indicam que houveram alterações referentes a **formatações de código**, semicolons, trailing spaces, lint... (Não inclui alterações em código).

- `refactor` - Commits do tipo refactor referem-se a mudanças devido a **refatorações que não alterem sua funcionalidade**, como por exemplo, uma alteração no formato como é processada determinada parte da tela, mas que manteve a mesma funcionalidade, ou melhorias de performance devido a um code review.

- `chore` - Commits do tipo chore indicam **atualizações de tarefas** de build, configurações de administrador, pacotes... como por exemplo adicionar um pacote no gitignore. (Não inclui alterações em código)

- `ci` - Commits do tipo ci indicam mudanças relacionadas a **integração contínua** (_continuous integration_).

- `raw` - Commits to tipo raw indicam mudanças relacionadas a arquivos de configurações, dados, features, parametros.

- `cleanup` - Commits do tipo cleanup são utilizados para remover código comentado, trechos desnecessários ou qualquer outra forma de limpeza do código-fonte, visando aprimorar sua legibilidade e manutenibilidade.

- `remove` - Commits do tipo remove indicam a exclusão de arquivos, diretórios ou funcionalidades obsoletas ou não utilizadas, reduzindo o tamanho e a complexidade do projeto e mantendo-o mais organizado.

### Estrutura de Commit

Ao preparar suas mensagens de commit, use a estrutura a seguir para que sejam claramente entendíveis e sigam a especificação do Conventional Commits:

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]
```

### Elementos de um Commit:

- **Tipo**: Identifica o propósito do seu commit. Pode ser um dos seguintes:
  - `fix`: Correção de um bug (corresponde ao PATCH no versionamento semântico).
  - `feat`: Novo recurso ou melhoria (corresponde ao MINOR no versionamento semântico).
  - Tipos adicionais podem incluir: `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`, e outros.

- **Escopo (Opcional)**: Fornece informações contextuais adicionais. Exemplo: `feat(parser):`.

- **Descrição**: Uma descrição concisa das mudanças realizadas.

- **Corpo (Opcional)**: Uma descrição detalhada das mudanças, se necessário.

- **Rodapé(s) (Opcional)**: Informações adicionais como `BREAKING CHANGE:` para mudanças que quebram a compatibilidade da API.

### Exemplos de Commits:

#### Commit Simples sem Corpo
```
docs: corrigir ortografia em CHANGELOG
```

#### Commit com Escopo e Indicativo de Breaking Change
```
feat(api)!: envia email para o cliente quando o produto é enviado
```

#### Commit com Breaking Change no Rodapé
```
chore!: remove suporte para Node 6

BREAKING CHANGE: refatorar para usar recursos do JavaScript não disponíveis no Node 6.
```

### Recomendações para Commits

Ao contribuir para este projeto, recomendamos as seguintes práticas para as mensagens de commit:

1. **Consistência**: Mantenha o tipo de commit consistente com o conteúdo adicionado.
2. **Concisão**: Limite a primeira linha da mensagem de commit a no máximo 50 caracteres.
3. **Descrição Detalhada**: Utilize o corpo do commit para fornecer detalhes adicionais sobre a mudança. Inicie o corpo do commit com uma linha em branco após a linha de título.
4. **Representatividade**: Inicie a mensagem de commit com um emoji representativo da ação realizada, se isso for uma prática adotada pela sua equipe.
5. **Informações Adicionais**: Inclua revisões de código, referências a issues, ou outros rodapés relevantes para fornecer mais contexto.

### Sugestões: Tipos - Emojis (Opcional) - Palavra-chave

| Tipo do commit        | Emoji              | Palavra-chave  |
|-----------------------|--------------------|----------------|
| Acessibilidade        | ♿ `:wheelchair:`  |                |
| Adicionando um teste  | ✅ `:white_check_mark:` | `test`   |
| Atualizando versão    | ⬆️ `:arrow_up:`   |                |
| Retrocedendo versão   | ⬇️ `:arrow_down:` |                |
| Adicionando dependência | ➕ `:heavy_plus_sign:` | `build` |
| Revisão de código     | 👌 `:ok_hand:`    | `style`        |
| Animações e transições | 💫 `:dizzy:`     |                |
| Bugfix                | 🐛 `:bug:`        | `fix`          |
| Comentários           | 💡 `:bulb:`       | `docs`         |
| Commit inicial        | 🎉 `:tada:`       | `init`         |
| Configuração          | 🔧 `:wrench:`    | `chore`        |
| Deploy                | 🚀 `:rocket:`     |                |
| Documentação          | 📚 `:books:`     | `docs`         |
| Em progresso          | 🚧 `:construction:` |              |
| Estilização de interface | 💄 `:lipstick:` | `feat`        |
| Infraestrutura        | 🧱 `:bricks:`    | `ci`           |
| Lista de tarefas      | 🔜 `:soon:`       |                |
| Mover/Renomear        | 🚚 `:truck:`      | `chore`        |
| Novo recurso          | ✨ `:sparkles:`   | `feat`         |
| Package.json em JS    | 📦 `:package:`    | `build`        |
| Performance           | ⚡ `:zap:`        | `perf`         |
| Refatoração           | ♻️ `:recycle:`   | `refactor`     |
| Limpeza de Código     | 🧹 `:broom:`     | `cleanup`      |
| Removendo um arquivo  | 🗑️ `:wastebasket:` | `remove`   |
| Removendo dependência | ➖ `:heavy_minus_sign:` | `build` |
| Responsividade        | 📱 `:iphone:`    |                |
| Revertendo mudanças   | 💥 `:boom:`      | `fix`          |
| Segurança             | 🔒️ `:lock:`     |                |
| SEO                   | 🔍️ `:mag:`      |                |
| Tag de versão         | 🔖 `:bookmark:`  |                |
| Teste de aprovação    | ✔️ `:heavy_check_mark:` | `test` |
| Testes                | 🧪 `:test_tube:` | `test`         |
| Texto                 | 📝 `:pencil:`    |                |
| Tipagem               | 🏷️ `:label:`    |                |
| Tratamento de erros   | 🥅 `:goal_net:`  |                |
| Dados                 | 🗃️ `:card_file_box:` | `raw`    |

#### 💻 Exemplos

Aqui estão alguns exemplos de como usar a convenção de commits com emojis:

| Comando Git                                        | Resultado no GitHub                      |
|----------------------------------------------------|------------------------------------------|
| `git commit -m ":tada: Commit inicial"`            | 🎉 Commit inicial                        |
| `git commit -m ":books: docs: Atualização do README"` | 📚 docs: Atualização do README           |
| `git commit -m ":bug: fix: Loop infinito na linha 50"` | 🐛 fix: Loop infinito na linha 50        |
| `git commit -m ":sparkles: feat: Página de login"` | ✨ feat: Página de login                  |
| `git commit -m ":bricks: ci: Modificação no Dockerfile"` | 🧱 ci: Modificação no Dockerfile         |
| `git commit -m ":recycle: refactor: Passando para arrow functions"` | ♻️ refactor: Passando para arrow functions |
| `git commit -m ":zap: perf: Melhoria no tempo de resposta"` | ⚡ perf: Melhoria no tempo de resposta    |
| `git commit -m ":boom: fix: Revertendo mudanças ineficientes"` | 💥 fix: Revertendo mudanças ineficientes  |
| `git commit -m ":lipstick: feat: Estilização CSS do formulário"` | 💄 feat: Estilização CSS do formulário    |
| `git commit -m ":test_tube: test: Criando novo teste"` | 🧪 test: Criando novo teste              |
| `git commit -m ":bulb: docs: Comentários sobre a função LoremIpsum( )"` | 💡 docs: Comentários sobre a função LoremIpsum( ) |
| `git commit -m ":card_file_box: raw: RAW Data do ano aaaa"` | 🗃️ raw: RAW Data do ano aaaa              |
| `git commit -m ":broom: cleanup: Eliminando blocos de código comentados e variáveis não utilizadas na função de validação de formulário"` | 🧹 cleanup: Eliminando blocos de código comentados e variáveis não utilizadas na função de validação de formulário |
| `git commit -m ":wastebasket: remove: Removendo arquivos não utilizados do projeto para manter a organização e atualização contínua"` | 🗑️ remove: Removendo arquivos não utilizados do projeto para manter a organização e atualização contínua |

## Perguntas ou Dúvidas?

Caso tenha dúvidas ou necessite de assistência, não hesite em abrir uma issue ou contatar diretamente os gerentes de projeto.