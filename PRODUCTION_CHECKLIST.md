# Production Deployment Checklist

Use this checklist before deploying to production.

## Security

- [ ] Remove all console.log debug statements
- [ ] Update API URLs to production endpoints
- [ ] Ensure ANTHROPIC_API_KEY is not committed to git
- [ ] Enable CORS only for your domain (not *)
- [ ] Use HTTPS for all endpoints
- [ ] Add rate limiting to backend
- [ ] Implement authentication if needed
- [ ] Use environment variables for all secrets
- [ ] Enable security headers (HTTPS, CSP, etc.)

## Frontend (Next.js)

- [ ] Run `npm run build` - verify no errors
- [ ] Test all pages work correctly
- [ ] Verify API calls point to production backend
- [ ] Check theme switching works
- [ ] Test on mobile/tablet
- [ ] Verify images load correctly
- [ ] Test file upload functionality
- [ ] Check for broken links
- [ ] Optimize images and assets
- [ ] Remove unused dependencies

## Backend (FastAPI)

- [ ] Run `python -m pytest` if tests exist
- [ ] Verify all endpoints return correct status codes
- [ ] Check error handling is comprehensive
- [ ] Test with actual CSV files (various sizes)
- [ ] Verify database connections (if used)
- [ ] Set up proper logging
- [ ] Configure production ASGI server (gunicorn)
- [ ] Test rate limiting
- [ ] Verify CORS headers are correct
- [ ] Monitor response times

## Infrastructure

- [ ] Choose hosting provider (Vercel, Render, AWS, etc.)
- [ ] Set up domain name
- [ ] Configure SSL/TLS certificate
- [ ] Set up backup strategy
- [ ] Configure monitoring and alerts
- [ ] Set up logging and error tracking
- [ ] Plan capacity and scaling strategy
- [ ] Document deployment process

## Environment Variables

**Frontend (.env.local on Vercel):**
- [ ] `NEXT_PUBLIC_BACKEND_URL` - production backend URL
- [ ] `NEXT_PUBLIC_LLM_API_KEY` - Anthropic key (optional)

**Backend (.env):**
- [ ] `ANTHROPIC_API_KEY` - Valid Anthropic API key
- [ ] `FRONTEND_URL` - Production frontend URL

## Testing

- [ ] Test file upload (various CSV formats)
- [ ] Test data profiling
- [ ] Test risk assessment
- [ ] Test AI explanations
- [ ] Test script generation
- [ ] Test before/after comparison
- [ ] Test error scenarios (bad CSV, oversized file, etc.)
- [ ] Load testing (with expected user volume)
- [ ] Test on slow network
- [ ] Test on older browsers

## Performance

- [ ] Frontend build size under 500KB
- [ ] API responses under 2 seconds
- [ ] Database queries optimized
- [ ] Images compressed
- [ ] Lazy loading for heavy components
- [ ] Cache strategy implemented
- [ ] CDN configured (if applicable)

## Documentation

- [ ] README.md is complete and accurate
- [ ] API documentation up to date
- [ ] Deployment guide is clear
- [ ] Troubleshooting guide available
- [ ] Contributing guidelines (if open source)

## Monitoring & Maintenance

- [ ] Error tracking configured (Sentry)
- [ ] Performance monitoring enabled
- [ ] Uptime monitoring set up
- [ ] Log aggregation configured
- [ ] Automated backups enabled
- [ ] Dependency updates scheduled

## Launch

- [ ] Announce to users
- [ ] Monitor error logs closely
- [ ] Be ready for immediate rollback
- [ ] Have support team ready
- [ ] Plan post-launch improvements

---

After completing this checklist, your application is ready for production!
