# Sistemaxi CRM

CRM/ERP multi-tenant para agências: clientes, leads e funil de vendas, projetos, tarefas, propostas com página pública, contratos, financeiro e atendimento via WhatsApp com agente de IA.

## Stack

- Backend: Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL, JWT
- Frontend: Next.js (App Router), TypeScript, Tailwind CSS, Radix UI, Recharts
- Integrações: Evolution API (WhatsApp), OpenAI/LangChain (agentes), Google Calendar, Google Places

## Rodando localmente

Pré-requisitos: Python 3.11+, Node.js 18+ e PostgreSQL.

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env           # preencha as variáveis
alembic upgrade head
python -m app.seed             # cria o primeiro admin se a tabela de usuários estiver vazia
uvicorn app.main:app --reload
```

API em http://localhost:8000 (healthcheck em `/health`).

### Frontend

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

Acesse http://localhost:3000. O Next faz proxy de `/api/*` e `/uploads/*` para `BACKEND_URL`.

## Variáveis de ambiente

Backend (`backend/.env`):

- `DATABASE_URL` ou `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_SERVER`, `POSTGRES_PORT`, `POSTGRES_DB`
- `SECRET_KEY`, `ALGORITHM`, `ACCESS_TOKEN_EXPIRE_MINUTES`
- `ADMIN_EMAIL`, `ADMIN_PASSWORD`, `ADMIN_NOME`
- `LEADS_API_KEY`
- `OPENAI_API_KEY`, `GOOGLE_PLACES_API_KEY`
- `DEBUG`, `ENVIRONMENT` (opcionais)

Frontend (`frontend/.env.local`):

- `NEXT_PUBLIC_API_URL`
- `BACKEND_URL`

## Estrutura

```
backend/
  app/api/v1/     rotas da API
  app/models/     models SQLAlchemy
  app/schemas/    schemas Pydantic
  app/services/   integrações (WhatsApp, OpenAI, agente Sofia, notificações)
  app/scripts/    tarefas de manutenção (python -m app.scripts.<nome>)
  alembic/        migrations
  scripts/        smoke test e utilitários de desenvolvimento
frontend/
  src/app/        páginas (App Router)
  src/components/ componentes por módulo
  src/lib/        cliente da API e utilitários
```

## Deploy

O backend sobe com `python -m uvicorn app.main:app` (ver `backend/Procfile` e `backend/railway.toml`).
