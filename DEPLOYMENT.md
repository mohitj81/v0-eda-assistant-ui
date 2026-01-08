# EDA Assistant - Full Stack Deployment Guide

This guide covers deploying both the Next.js frontend and FastAPI backend.

## Prerequisites

- Node.js 18+ (for frontend)
- Python 3.9+ (for backend)
- Anthropic API key (for AI explanations)

## Local Development Setup

### Frontend

1. Install dependencies:
   ```bash
   npm install
   ```

2. Create `.env.local`:
   ```
   NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
   NEXT_PUBLIC_LLM_API_KEY=your_anthropic_api_key
   ```

3. Run dev server:
   ```bash
   npm run dev
   ```

   Frontend runs at `http://localhost:3000`

### Backend

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env`:
   ```
   ANTHROPIC_API_KEY=your_anthropic_api_key
   FRONTEND_URL=http://localhost:3000
   ```

5. Run server:
   ```bash
   python main.py
   ```

   Backend runs at `http://localhost:8000`

## Production Deployment

### Frontend - Deploy to Vercel

1. Push your code to GitHub
2. Go to vercel.com and import your repository
3. Set environment variables in Vercel dashboard:
   - `NEXT_PUBLIC_BACKEND_URL` - Your production backend URL
   - `NEXT_PUBLIC_LLM_API_KEY` - Anthropic API key

4. Deploy automatically on push to main branch

### Backend - Deploy Options

#### Option 1: Render (Recommended for simplicity)

1. Create account at render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure settings:
   - Build command: `pip install -r backend/requirements.txt`
   - Start command: `cd backend && gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker`
   - Add environment variables in dashboard

5. Deploy

#### Option 2: Railway

1. Create account at railway.app
2. Connect GitHub repository
3. Add environment variables
4. Deploy

#### Option 3: AWS EC2

1. Launch an EC2 instance (Ubuntu 22.04)
2. SSH into instance
3. Install dependencies:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx
   ```

4. Clone your repository and set up:
   ```bash
   git clone your-repo
   cd your-repo/backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. Set up systemd service (`/etc/systemd/system/eda-backend.service`):
   ```ini
   [Unit]
   Description=EDA Assistant Backend
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/your-repo/backend
   Environment="ANTHROPIC_API_KEY=your_key"
   ExecStart=/home/ubuntu/your-repo/backend/venv/bin/gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000

   [Install]
   WantedBy=multi-user.target
   ```

6. Set up Nginx reverse proxy (`/etc/nginx/sites-available/eda`):
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

7. Enable and start service:
   ```bash
   sudo systemctl enable eda-backend
   sudo systemctl start eda-backend
   ```

#### Option 4: Docker

1. Create `backend/Dockerfile`:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY main.py .
   CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
   ```

2. Build and push:
   ```bash
   docker build -t eda-backend .
   docker tag eda-backend your-registry/eda-backend
   docker push your-registry/eda-backend
   ```

3. Deploy to any container service (Google Cloud Run, AWS ECS, etc.)

## Environment Variables

### Frontend
- `NEXT_PUBLIC_BACKEND_URL` - Backend API URL
- `NEXT_PUBLIC_LLM_API_KEY` - Anthropic API key

### Backend
- `ANTHROPIC_API_KEY` - Anthropic API key (required)
- `FRONTEND_URL` - Frontend URL for CORS

## Health Checks

Test your deployment:

```bash
# Frontend
curl https://your-frontend-url.com

# Backend
curl https://your-backend-url.com/health
```

## Scaling Considerations

### Frontend
- Vercel handles auto-scaling automatically
- Monitor usage in Vercel dashboard

### Backend
- For high traffic, increase worker count in gunicorn
- Use caching for frequently accessed results
- Consider adding Redis for session storage
- Monitor CPU and memory usage

## Monitoring

Recommended tools:
- Frontend: Vercel Analytics
- Backend: New Relic, Datadog, or Sentry
- Error tracking: Sentry.io

## Support

For issues:
1. Check backend logs: `docker logs` or `journalctl -u eda-backend`
2. Check frontend logs in Vercel dashboard
3. Verify API connectivity between frontend and backend
4. Ensure Anthropic API key is valid
