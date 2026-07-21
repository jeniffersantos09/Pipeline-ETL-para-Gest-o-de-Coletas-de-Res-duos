## 🧩 Projeto de Engenharia de Dados | Pipeline ETL para Gestão de Coletas de Resíduos

### 📘 Descrição
Este projeto foi desenvolvido com o objetivo de **simular um cenário real de operações logísticas**, aplicando conceitos de **Engenharia de Dados** para automatizar o processamento das solicitações de coleta de resíduos.  
A proposta é transformar **dados brutos** em **informações confiáveis**, permitindo que a equipe responsável pela logística tenha uma base consistente para **planejar, acompanhar e otimizar** as rotas diárias de coleta.

---

### ⚙️ Arquitetura do Pipeline
O pipeline foi projetado para realizar todo o fluxo de processamento dos dados:

- ✔ **Armazenamento** do arquivo de origem na **AWS S3**  
- ✔ **Extração automatizada** utilizando **Python**  
- ✔ **Tratamento e validação** dos registros com **Pandas**, identificando inconsistências como campos obrigatórios ausentes, pesos inválidos e outros erros de qualidade  
- ✔ **Importação** apenas dos registros válidos para o banco de dados **MySQL**  
- ✔ **Registro automático** das execuções em uma tabela de log para **monitoramento e rastreabilidade**  
- ✔ **Orquestração** do pipeline utilizando **Apache Airflow** em ambiente **Docker**

---

### 🧠 Tecnologias Utilizadas
| Tecnologia | Função |
|-------------|--------|
| **Python** | Linguagem principal para scripts de ETL |
| **Pandas** | Tratamento e validação dos dados |
| **MySQL** | Banco de dados relacional para armazenamento |
| **Apache Airflow** | Orquestração e agendamento das tarefas |
| **Docker** | Containerização do ambiente |
| **AWS S3** | Armazenamento de arquivos de origem |


---

### 📊 Interface e Visualização
Além do pipeline ETL, foi desenvolvido um **protótipo da interface do sistema** para demonstrar como as informações processadas podem ser disponibilizadas à equipe operacional, oferecendo uma visão centralizada das coletas, do status das solicitações, da operação dos caminhões e do gerenciamento dos clientes.

---

### 🚀 Objetivo Final
Este projeto aplica conceitos de **Engenharia de Dados corporativa**, integrando:
- Armazenamento em nuvem  
- Processamento automatizado  
- Validação de dados  
- Persistência em banco relacional  
- Orquestração de pipelines  
- Disponibilização das informações para apoio à **tomada de decisão operacional**

---

### 🏷️ 
**Jeniffer Santos**  
Engenheira de Dados 


---

Quer que eu adicione uma seção final com **instruções de execução** (como rodar o Docker e iniciar o Airflow) para deixar o README ainda mais completo?
