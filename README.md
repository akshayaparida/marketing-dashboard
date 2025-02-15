# Marketing Performance & Affiliate Dashboard

## Overview
The **Marketing Performance & Affiliate Dashboard** is a web-based analytics platform designed to track marketing campaigns, affiliate performance, and other key metrics. It leverages **FastAPI, PostgreSQL, Redis, Celery, SQLAlchemy, Alembic, Next.js, Less, React Query, and Ant Design** to provide a seamless data-driven experience.

## Features
- 📊 **Performance Tracking** – Monitor affiliate and campaign KPIs in real-time.
- 🔄 **Data Processing** – Background job processing with Celery and Redis.
- 📈 **Interactive Dashboard** – Built with React and Ant Design for data visualization.
- 🛠 **API-Driven Architecture** – Backend powered by FastAPI with PostgreSQL.
- 🚀 **Docker Support** – Easily deployable with Docker & Docker Compose.
- 📡 **Real-Time Updates** – Optimized data fetching using React Query.

## Tech Stack
### Backend
- **FastAPI** – High-performance Python web framework.
- **PostgreSQL** – Relational database for structured data.
- **Redis** – In-memory data store for caching and Celery task queue.
- **Celery** – Task queue for background job processing.
- **SQLAlchemy** – ORM for database interaction.
- **Alembic** – Database migrations.

### Frontend
- **Next.js** – React framework for SSR and static site generation.
- **React Query** – Efficient data fetching and caching.
- **Ant Design** – UI library for modern and responsive design.
- **Less** – CSS preprocessor for styling.

### DevOps
- **Docker** – Containerized development and deployment.
- **pnpm** – Package manager for managing dependencies.
- **Monorepo** – Organized structure for full-stack development.

## Installation
### Prerequisites
Ensure you have the following installed:
- **Docker & Docker Compose**
- **pnpm** (for managing dependencies)
- **Python 3.9+**
- **Node.js 18+**

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/marketing-dashboard.git
   cd marketing-dashboard
   ```
2. Start the backend services:
   ```sh
   cd backend
   docker-compose up --build
   ```
3. Start the frontend:
   ```sh
   cd frontend
   pnpm install
   pnpm dev
   ```
4. Access the dashboard at `http://localhost:3000`

## API Endpoints
| Method | Endpoint          | Description                      |
|--------|------------------|----------------------------------|
| **GET**    | `/api/campaigns`   | Fetch marketing campaign data   |
| **GET**    | `/api/affiliates`  | Get affiliate performance stats |
| **POST**   | `/api/bookmarks`   | Bookmark an important campaign  |
| **DELETE** | `/api/bookmarks/:id` | Remove a bookmarked campaign  |

## Environment Variables
Create a `.env` file in the backend directory with the following:
```ini
DATABASE_URL=postgresql://user:password@localhost:5432/marketing_db
REDIS_URL=redis://localhost:6379
SECRET_KEY=your_secret_key
```

