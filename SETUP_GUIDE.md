# EDA Assistant - Setup Guide

## Quick Start (5 minutes)

### 1. Install Dependencies
\`\`\`bash
npm install
\`\`\`

### 2. Configure Backend
Create `.env.local`:
\`\`\`env
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
\`\`\`

### 3. Start Development Server
\`\`\`bash
npm run dev
\`\`\`

### 4. Open in Browser
Navigate to `http://localhost:3000`

## Complete Setup

### Step 1: Environment Setup

Copy the example environment file:
\`\`\`bash
cp .env.example .env.local
\`\`\`

Edit `.env.local` with your configuration:
\`\`\`env
# Required: Backend API URL
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000

# Optional: For AI explanations
NEXT_PUBLIC_LLM_API_KEY=your-api-key-here

# Optional: Default theme
NEXT_PUBLIC_DEFAULT_THEME=dark
\`\`\`

### Step 2: Install Dependencies

\`\`\`bash
npm install
\`\`\`

This installs:
- Next.js 16 with App Router
- React 19.2
- shadcn/ui components
- Tailwind CSS v4
- next-themes for dark mode
- All other required dependencies

### Step 3: Verify Installation

Run the development server:
\`\`\`bash
npm run dev
\`\`\`

Expected output:
\`\`\`
▲ Next.js 16.0.10
- Local:        http://localhost:3000
- Environments: .env.local
\`\`\`

### Step 4: Check Application

Open your browser to `http://localhost:3000` and verify:
- Home page loads with feature cards
- Sidebar navigation appears
- Theme switcher works in topbar
- No console errors

## Backend Integration

### API Endpoints Required

Your FastAPI backend should implement:

#### 1. Dataset Upload
\`\`\`python
@app.post("/upload")
async def upload_dataset(file: UploadFile):
    # Process CSV and return preview
    return {
        "dataset_id": "unique-id",
        "preview": ["header", "row1", "row2"]
    }
\`\`\`

#### 2. Data Profiling
\`\`\`python
@app.get("/profile/{dataset_id}")
async def get_profiling(dataset_id: str):
    return {
        "summary": {
            "rows": 1000,
            "columns": 12,
            "missing_percentage": 8.2,
            "duplicate_rows": 15
        },
        "columns": [
            {
                "name": "Age",
                "dtype": "int",
                "missing": 12,
                "unique": 42
            }
        ]
    }
\`\`\`

#### 3. Risk Assessment
\`\`\`python
@app.get("/risk/{dataset_id}")
async def get_risk(dataset_id: str):
    return {
        "score": "Medium",
        "numeric_score": 53,
        "critical_issues": ["Issue 1", "Issue 2"],
        "warnings": ["Warning 1"]
    }
\`\`\`

#### 4. AI Explanation
\`\`\`python
@app.get("/explain/{dataset_id}")
async def get_explanation(dataset_id: str):
    return {
        "explanation": "Your dataset has..."
    }
\`\`\`

#### 5. Cleaning Script
\`\`\`python
@app.get("/script/{dataset_id}")
async def get_script(dataset_id: str):
    return {
        "script": "import pandas as pd\n..."
    }
\`\`\`

### Testing API Integration

Use the Upload page to test:
1. Upload a sample CSV
2. Check browser console for API calls
3. Verify responses in Network tab
4. Navigate to Profiling page to confirm data flow

## Customization Guide

### Changing Colors

Edit `app/globals.css` - search for `--primary`:

\`\`\`css
:root {
  --primary: oklch(0.456 0.194 262.1); /* Change this */
  /* Other tokens... */
}
\`\`\`

Color format: `oklch(lightness saturation hue)`

### Adding Navigation Items

Edit `components/layouts/sidebar.tsx`:

\`\`\`typescript
const navItems = [
  // ... existing items
  { href: "/your-page", label: "Your Page", icon: YourIcon },
]
\`\`\`

### Changing Default Theme

Edit `.env.local`:
\`\`\`env
NEXT_PUBLIC_DEFAULT_THEME=light
\`\`\`

Or edit `app/layout.tsx`:
\`\`\`tsx
<ThemeProvider defaultTheme="light" ...>
\`\`\`

## Deployment Checklist

Before deploying to production:

- [ ] Backend API is running and accessible
- [ ] Environment variables are set correctly
- [ ] All API endpoints are implemented
- [ ] CORS is configured on backend
- [ ] SSL/HTTPS is enabled
- [ ] Error handling is tested
- [ ] Performance is optimized
- [ ] Analytics are configured

### Build for Production

\`\`\`bash
npm run build
npm start
\`\`\`

### Deploy to Vercel (Recommended)

\`\`\`bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
\`\`\`

Follow the prompts to:
1. Link to your GitHub repository
2. Set environment variables
3. Configure deployment settings

## Troubleshooting

### Issue: "Cannot GET /"
**Solution**: Ensure dev server is running on port 3000

### Issue: API calls returning 404
**Solution**: Check `NEXT_PUBLIC_BACKEND_URL` is correct and backend is running

### Issue: Theme not switching
**Solution**: Clear browser cache and restart dev server

### Issue: Components not styled
**Solution**: Verify Tailwind CSS is imported in `app/globals.css`

### Issue: File upload not working
**Solution**: 
1. Check file is CSV format
2. Verify file size < 50MB
3. Check backend `/upload` endpoint

## Next Steps

1. **Customize the Design**: Update colors and fonts in `app/globals.css`
2. **Implement Backend**: Create FastAPI endpoints matching the API contracts
3. **Test Upload Flow**: Upload a sample CSV and verify data flows through all pages
4. **Deploy**: Push to GitHub and deploy to Vercel
5. **Monitor**: Set up error tracking and analytics

## Getting Help

- Check the Documentation page in the app
- Review the README.md for technical details
- Inspect browser console for error messages
- Check API responses in Network tab
- Review backend logs for server-side issues

---

Happy analyzing! 📊
