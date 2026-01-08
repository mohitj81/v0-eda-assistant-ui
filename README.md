# EDA Assistant - Data Analysis Platform

A modern, production-grade web application for automated exploratory data analysis, data quality assessment, risk evaluation, and guided data cleaning.

## Features

- **Data Upload & Preview** - Drag-and-drop CSV file upload with preview
- **Data Profiling** - Comprehensive analysis of dataset structure, types, and distributions
- **Risk Assessment** - Intelligent data quality scoring and issue detection
- **AI Insights** - AI-generated explanations and recommendations
- **Before/After Comparison** - Visualize improvements from data cleaning
- **Script Generation** - Auto-generated Python cleaning scripts
- **Reports & Export** - Download comprehensive analysis reports
- **Dark/Light Mode** - Full theme support with next-themes
- **Responsive Design** - Works on desktop and mobile devices

## Tech Stack

- **Framework**: Next.js 16 (App Router)
- **UI Components**: shadcn/ui
- **Styling**: Tailwind CSS v4
- **Theme Management**: next-themes
- **Icons**: Lucide React
- **State Management**: React Context API
- **Forms**: React Hook Form + Zod

## Project Structure

```
app/
├── layout.tsx              # Root layout with providers
├── globals.css             # Global styles and theme tokens
├── page.tsx                # Landing page
├── upload/                 # Dataset upload page
├── profiling/              # Data profiling summary
├── risk/                   # Risk assessment page
├── explanation/            # AI insights page
├── comparison/             # Before/after comparison
├── script/                 # Script generator page
├── reports/                # Reports & export page
├── documentation/          # Documentation & FAQ
└── settings/               # Settings & configuration

components/
├── ui/                     # shadcn/ui components
├── layouts/                # Layout components (sidebar, topbar)
│   ├── root-layout.tsx
│   ├── sidebar.tsx
│   └── topbar.tsx
├── custom/                 # Custom reusable components
│   ├── data-table.tsx
│   ├── code-block.tsx
│   ├── risk-meter.tsx
│   ├── metric-card.tsx
│   ├── loading-skeleton.tsx
│   ├── issue-alert.tsx
│   └── index.ts
└── theme-provider.tsx      # Theme provider setup

lib/
├── types.ts                # TypeScript type definitions
├── api-client.ts           # API client for backend communication
├── context.tsx             # EDA context provider and hooks
└── utils.ts                # Utility functions

public/                      # Static assets
```

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. Clone the repository or download the project:
```bash
git clone <repository-url>
cd eda-assistant
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables by creating a `.env.local` file:
```bash
cp .env.example .env.local
```

4. Configure the backend URL in `.env.local`:
```env
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
```

### Running the Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser to see the application.

## API Integration

The application is designed to work with a FastAPI backend. The backend should implement the following endpoints:

### Upload Dataset
```
POST /upload
Content-Type: multipart/form-data
Body: { file: CSV file }
Response: { dataset_id: string, preview: string[] }
```

### Get Profiling Results
```
GET /profile/{dataset_id}
Response: { summary: {...}, columns: [...] }
```

### Get Risk Assessment
```
GET /risk/{dataset_id}
Response: { score: "Low|Medium|High", numeric_score: number, critical_issues: [...], warnings: [...] }
```

### Get AI Explanation
```
GET /explain/{dataset_id}
Response: { explanation: string }
```

### Get Cleaning Script
```
GET /script/{dataset_id}
Response: { script: string }
```

## Customization

### Theme Configuration

Edit `app/globals.css` to customize the color scheme:
- Primary color: oklch(0.456 0.194 262.1) - Purple/Blue
- Background: oklch(0.098 0 0) - Dark
- Accent: oklch(0.456 0.194 262.1) - Purple/Blue

### Adding New Pages

1. Create a new directory under `app/`
2. Add a `page.tsx` file
3. The page will automatically be available at the corresponding route
4. Update the sidebar navigation in `components/layouts/sidebar.tsx`

### Extending the API Client

Add new API calls to `lib/api-client.ts`:

```typescript
async newEndpoint(params: any): Promise<any> {
  const response = await fetch(`${API_BASE_URL}/endpoint`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
  })
  if (!response.ok) throw new Error("Failed to fetch")
  return response.json()
}
```

## State Management

The application uses React Context for state management. Access global state with the `useEDA()` hook:

```typescript
import { useEDA } from "@/lib/context"

export function MyComponent() {
  const { currentDataset, profiling, loading, uploadDataset } = useEDA()
  
  return (
    // component code
  )
}
```

## Building for Production

```bash
npm run build
npm start
```

The application will be optimized and ready for production deployment.

## Deployment

### Deploy to Vercel

The easiest way to deploy is with [Vercel](https://vercel.com):

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Set environment variables in Vercel dashboard
4. Deploy with one click

### Deploy to Other Platforms

This is a standard Next.js application and can be deployed to:
- AWS (Amplify, EC2)
- Google Cloud (Cloud Run, App Engine)
- Azure (App Service)
- Heroku
- DigitalOcean
- Docker containers

## Development Tips

### Component Development

- Use the Storybook-like approach: test components in isolation
- shadcn/ui components are pre-installed in `components/ui/`
- Create custom components in `components/custom/`

### Debugging

Use `console.log()` statements with descriptive prefixes:
```typescript
console.log("[v0] Dataset uploaded:", dataset)
```

### Styling

- Use Tailwind CSS classes for styling
- Leverage design tokens in `globals.css`
- Keep components responsive with `md:` and `lg:` prefixes

## Troubleshooting

### Backend Connection Issues

If the API calls are failing:
1. Ensure backend is running on the configured URL
2. Check CORS configuration on the backend
3. Verify the endpoint paths match the backend implementation
4. Check browser console for error messages

### Theme Not Applying

1. Clear browser cache
2. Verify `suppressHydrationWarning` is set on `<html>` element
3. Check that `ThemeProvider` wraps the entire application

### File Upload Errors

1. Verify file is a valid CSV
2. Check file size is under 50MB
3. Ensure no special characters in filename

## Contributing

To contribute to this project:
1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
1. Check the Documentation page in the app
2. Review the FAQ section
3. Check error messages in browser console
4. File an issue on GitHub

---

Built with ❤️ using Next.js and shadcn/ui
