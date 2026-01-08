# Getting Started with EDA Assistant

Welcome! This guide will help you get the complete EDA Assistant running locally and ready for deployment.

## Prerequisites

Before starting, ensure you have:
- **Node.js 18+** and npm installed
- **Python 3.9+** installed
- **Anthropic API key** (free tier available at https://console.anthropic.com/)

Verify installations:
\`\`\`bash
node --version
npm --version
python --version
\`\`\`

## Step 1: Clone and Install

\`\`\`bash
# Clone the repository
git clone <your-repo-url>
cd eda-assistant

# Install frontend dependencies
npm install
\`\`\`

## Step 2: Set Up Backend

\`\`\`bash
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Go back to root
cd ..
\`\`\`

## Step 3: Configure Environment Variables

### Frontend Configuration

Create `.env.local` in the root directory:
\`\`\`bash
echo "NEXT_PUBLIC_BACKEND_URL=http://localhost:8000" > .env.local
\`\`\`

### Backend Configuration

Create `backend/.env`:
\`\`\`bash
echo "ANTHROPIC_API_KEY=sk-ant-YOUR_KEY_HERE" > backend/.env
echo "FRONTEND_URL=http://localhost:3000" >> backend/.env
\`\`\`

Get your Anthropic API key at: https://console.anthropic.com/

## Step 4: Run Locally

Open two terminal windows:

### Terminal 1 - Frontend:
\`\`\`bash
npm run dev
\`\`\`
Frontend runs at: **http://localhost:3000**

### Terminal 2 - Backend:
\`\`\`bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python main.py
\`\`\`
Backend runs at: **http://localhost:8000**

## Step 5: Test Everything

1. Open http://localhost:3000 in your browser
2. Click "Upload Dataset"
3. Upload a CSV file
4. System will automatically:
   - Profile the data
   - Calculate risk score
   - Generate cleaning script
   - Provide AI insights

## Testing with Sample Data

Create a test CSV:
\`\`\`bash
python -c "
import pandas as pd
df = pd.DataFrame({
    'age': [25, 30, None, 45, 50],
    'salary': [50000, 60000, 65000, 70000, 75000],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'email': ['alice@test.com', 'bob@test.com', 'charlie@test.com', 'david@test.com', 'eve@test.com']
})
df.to_csv('sample.csv', index=False)
"
\`\`\`

Then upload `sample.csv` in the app.

## Troubleshooting

### Backend Connection Error
\`\`\`
"Backend connection refused"
\`\`\`
**Fix:**
1. Ensure backend is running: `python main.py` in terminal 2
2. Check `.env.local` has correct `NEXT_PUBLIC_BACKEND_URL`
3. Check backend `.env` has valid `ANTHROPIC_API_KEY`

### Invalid API Key
\`\`\`
"Invalid API key"
\`\`\`
**Fix:**
1. Get key from https://console.anthropic.com/
2. Update `ANTHROPIC_API_KEY` in `backend/.env`
3. Restart backend: `python main.py`

### Port Already in Use
\`\`\`
"Address already in use"
\`\`\`
**Fix:**
\`\`\`bash
# For port 3000 (Next.js)
npx kill-port 3000

# For port 8000 (FastAPI)
python -m pip install lsof
lsof -ti:8000 | xargs kill -9
\`\`\`

### Module Not Found Error
\`\`\`
"ModuleNotFoundError: No module named 'fastapi'"
\`\`\`
**Fix:**
\`\`\`bash
cd backend
pip install -r requirements.txt
\`\`\`

## Next Steps

1. **Customize Design:** Edit colors in `app/globals.css`
2. **Add Authentication:** See DEPLOYMENT.md for options
3. **Deploy:** Follow DEPLOYMENT.md for production setup
4. **Extend:** Add more features to match your needs

## Project Structure

\`\`\`
eda-assistant/
├── app/                    # Next.js pages
│   ├── page.tsx           # Landing page
│   ├── upload/            # Upload page
│   ├── profiling/         # Profiling page
│   ├── risk/              # Risk assessment
│   ├── explanation/       # AI insights
│   ├── comparison/        # Before/after
│   ├── script/            # Script generator
│   ├── reports/           # Reports
│   ├── documentation/     # Docs
│   └── settings/          # Settings
├── components/            # React components
│   ├── ui/               # shadcn/ui components
│   ├── layouts/          # Layout components
│   └── custom/           # Custom components
├── lib/                   # Utilities & hooks
│   ├── types.ts          # TypeScript types
│   ├── api-client.ts     # API client
│   └── context.tsx       # State management
├── public/               # Static assets
├── backend/              # FastAPI backend
│   ├── main.py          # Main application
│   └── requirements.txt  # Python dependencies
└── package.json         # npm dependencies
\`\`\`

## Key Files to Customize

- **Colors:** `app/globals.css` - Modify CSS variables
- **API URLs:** `.env.local` - Change backend URL
- **Pages:** `app/*/page.tsx` - Edit page content
- **Components:** `components/` - Modify UI

## Support

For issues:
1. Check browser console (F12) for error messages
2. Check terminal output for backend errors
3. Verify environment variables are set
4. See QUICK_START.md and DEPLOYMENT.md for more help

---

Happy data analysis! 🚀
