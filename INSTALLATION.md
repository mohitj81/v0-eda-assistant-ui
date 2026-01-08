# Installation & Setup Guide

Complete step-by-step guide to set up the EDA Assistant locally.

## System Requirements

- Node.js 18.17+ (download from nodejs.org)
- Python 3.9+ (download from python.org)
- Anthropic API key (free tier at anthropic.com)
- A terminal/command prompt

## Installation Steps

### Step 1: Clone and Navigate

\`\`\`bash
# Clone the repository
git clone <your-repo-url>
cd eda-assistant
\`\`\`

### Step 2: Frontend Setup

\`\`\`bash
# Install Node dependencies
npm install

# Create frontend environment file
cp .env.example .env.local

# Edit .env.local with your settings:
# - NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
# - NEXT_PUBLIC_LLM_API_KEY=your_anthropic_key (optional)
\`\`\`

### Step 3: Backend Setup

\`\`\`bash
# Navigate to backend folder
cd backend

# Create Python virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Create backend environment file
cp .env .env.local  # or create new .env file

# Edit .env with:
# ANTHROPIC_API_KEY=your_anthropic_key
\`\`\`

### Step 4: Run the Application

**Terminal 1 - Start Backend:**

\`\`\`bash
cd backend
python main.py
\`\`\`

Backend will start at `http://localhost:8000`

**Terminal 2 - Start Frontend:**

\`\`\`bash
npm run dev
\`\`\`

Frontend will start at `http://localhost:3000`

### Step 5: Access the Application

Open your browser and go to: **http://localhost:3000**

## Configuration

### Getting Anthropic API Key

1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Create a new API key in the dashboard
4. Add to both:
   - `backend/.env` as `ANTHROPIC_API_KEY`
   - `.env.local` as `NEXT_PUBLIC_LLM_API_KEY` (optional)

### Backend Configuration

The backend accepts these environment variables:

\`\`\`
ANTHROPIC_API_KEY          # Required for AI explanations
FRONTEND_URL               # CORS allowed origin (default: http://localhost:3000)
\`\`\`

### Frontend Configuration

The frontend uses these environment variables:

\`\`\`
NEXT_PUBLIC_BACKEND_URL    # Backend API URL (default: http://localhost:8000)
NEXT_PUBLIC_LLM_API_KEY    # Anthropic API key (optional, used by frontend)
NEXT_PUBLIC_DEFAULT_THEME  # Theme: 'light' or 'dark' (default: dark)
\`\`\`

## Verify Installation

### Test Backend

\`\`\`bash
# In backend directory
curl http://localhost:8000/health

# Expected response:
# {"status":"ok","version":"1.0.0"}
\`\`\`

### Test Full Setup

\`\`\`bash
# Generate test data
cd backend
python test_data.py

# Run endpoint tests
python test_endpoints.py
\`\`\`

## Troubleshooting

### "Module not found" error

\`\`\`bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
\`\`\`

### "Port 8000 already in use"

\`\`\`bash
# Kill process using port 8000
lsof -ti:8000 | xargs kill -9    # macOS/Linux
netstat -ano | findstr :8000     # Windows (then taskkill)
\`\`\`

### "Port 3000 already in use"

\`\`\`bash
# Kill process using port 3000
lsof -ti:3000 | xargs kill -9    # macOS/Linux
\`\`\`

### "Backend connection refused"

1. Ensure backend is running: `python main.py`
2. Check `NEXT_PUBLIC_BACKEND_URL` in `.env.local`
3. Verify ports: Backend on 8000, Frontend on 3000

### "Invalid API key" error

1. Get key from https://console.anthropic.com/
2. Update `ANTHROPIC_API_KEY` in `backend/.env`
3. Restart backend server

### CSV upload fails

1. Ensure file is valid CSV format
2. Check file size (should be < 100MB)
3. Check backend logs for error details

## Next Steps

1. Upload a CSV file to test the system
2. Explore all pages and features
3. Review DEPLOYMENT.md for production setup
4. Customize colors in `app/globals.css`
5. Add authentication (optional)

## Support

- Check backend logs for errors: `python main.py`
- Check frontend console for errors: Press F12 in browser
- Review endpoint test results: `python test_endpoints.py`
