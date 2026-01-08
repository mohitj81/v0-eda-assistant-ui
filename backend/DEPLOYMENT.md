# Backend Deployment Guide

## Production Deployment Options

### Option 1: Render.com (Recommended for beginners)

1. Push backend folder to GitHub
2. Create new Web Service on render.com
3. Connect your GitHub repository
4. Set environment variables:
   - ANTHROPIC_API_KEY = your-api-key
   - FRONTEND_URL = your-frontend-domain.com
5. Deploy

### Option 2: Railway.app

1. Connect GitHub repository
2. Add ANTHROPIC_API_KEY in Variables
3. Railway auto-detects Python and deploys

### Option 3: Heroku (if still available)

1. \`heroku login\`
2. \`heroku create your-app-name\`
3. \`heroku config:set ANTHROPIC_API_KEY=your-key\`
4. \`git push heroku main\`

### Option 4: AWS (EC2)

1. Launch Ubuntu EC2 instance
2. Install Python, pip, and git
3. Clone repository
4. Create virtual environment and install dependencies
5. Use systemd to run as service
6. Use Nginx as reverse proxy

### Option 5: Docker

Build and run locally:
```bash
docker build -t eda-backend .
docker run -p 8000:8000 -e ANTHROPIC_API_KEY=your-key eda-backend
```

Deploy to:
- Docker Hub
- AWS ECR
- DigitalOcean Container Registry

### Option 6: Docker Compose

```bash
docker-compose up
```

## Environment Variables

Required:
- ANTHROPIC_API_KEY

Optional:
- FRONTEND_URL (default: http://localhost:3000)
- HOST (default: 0.0.0.0)
- PORT (default: 8000)

## Health Monitoring

All services include health checks:
- Render: Auto-healing enabled
- Railway: Monitoring dashboard
- Docker: Built-in healthcheck

## CORS Configuration

For production, update CORS in main.py:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

## Performance

- Workers: 4 (adjust based on server capacity)
- Timeout: 30 seconds (for API calls)
- Session storage: In-memory (use database for persistent storage)

## Security

- Use HTTPS only in production
- Store API keys in environment variables
- Implement rate limiting for production
- Validate all file uploads
- Add authentication if needed

## Scaling

For high traffic:
- Add Redis for session caching
- Use external database instead of in-memory storage
- Implement request queuing
- Use CDN for frontend

## Troubleshooting

1. "Module not found" - Ensure all requirements installed
2. "Connection refused" - Check port 8000 is available
3. "API key error" - Verify ANTHROPIC_API_KEY is set
4. "CORS error" - Check frontend URL matches CORS config
5. "Health check failing" - Ensure application starts properly

## Logs

Access logs for debugging:
- Render: View logs in dashboard
- Railway: Real-time logs
- Docker: \`docker logs container-id\`
- Local: Check console output

## Support

For issues:
1. Check backend/README.md for API docs
2. Verify environment variables
3. Test health endpoint: GET /health
4. Check frontend can reach backend URL
"""
