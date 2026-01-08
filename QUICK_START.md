# Quick Start Guide

Get the EDA Assistant running in 5 minutes!

## Prerequisites
- Node.js 18+ and npm
- Python 3.9+
- Anthropic API key (free tier available at anthropic.com)

## One-Command Setup (Mac/Linux)

\`\`\`bash
# Clone repo
git clone your-repo-url
cd your-repo

# Install frontend
npm install

# Setup backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Create frontend .env.local
echo "NEXT_PUBLIC_BACKEND_URL=http://localhost:8000" > .env.local
echo "NEXT_PUBLIC_LLM_API_KEY=sk-ant-..." >> .env.local

# Create backend .env
echo "ANTHROPIC_API_KEY=sk-ant-..." > backend/.env

# Terminal 1: Start frontend
npm run dev

# Terminal 2: Start backend
cd backend
python main.py
\`\`\`

## Access

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## First Steps

1. Go to http://localhost:3000
2. Click "Upload Dataset"
3. Select a CSV file
4. System will automatically:
   - Profile your data
   - Calculate risk score
   - Generate cleaning script
   - Provide AI insights

## Common Issues

**"Backend connection refused"**
- Ensure backend is running: `python main.py`
- Check `NEXT_PUBLIC_BACKEND_URL` in `.env.local`

**"Invalid API key"**
- Get key from: https://console.anthropic.com/
- Update `ANTHROPIC_API_KEY` in `backend/.env`

**"Port 8000 already in use"**
- Kill process: `lsof -ti:8000 | xargs kill -9`
- Or run on different port: `uvicorn main:app --port 8001`

## Next Steps

- Customize colors in `app/globals.css`
- Add authentication using Supabase
- Deploy to production (see DEPLOYMENT.md)
- Add more data analysis features
