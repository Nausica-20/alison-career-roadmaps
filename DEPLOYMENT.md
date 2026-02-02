# Deploying Alison Career Roadmaps to GitHub

## Prerequisites

- GitHub account ([create one here](https://github.com/join))
- Git installed on your computer ([download here](https://git-scm.com/downloads))
- Basic command line knowledge

## Step-by-Step Deployment

### Step 1: Create a GitHub Repository

1. **Log in to GitHub**
   - Go to [github.com](https://github.com)
   - Sign in with your account

2. **Create New Repository**
   - Click the "+" icon in the top right
   - Select "New repository"
   - Name it: `alison-career-roadmaps`
   - Description: "Free learning paths for 30 in-demand careers"
   - Choose "Public" for GitHub Pages
   - Don't initialize with README (we have one)
   - Click "Create repository"

### Step 2: Initialize Local Git Repository

Open your terminal/command prompt and navigate to the project folder:

```bash
cd path/to/alison-career-roadmaps-blog

# Initialize git repository
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: 30 career roadmaps with Alison courses"

# Add remote repository (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/alison-career-roadmaps.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. **Go to Repository Settings**
   - Navigate to your repository on GitHub
   - Click "Settings" tab
   - Scroll down to "Pages" in the left sidebar

2. **Configure GitHub Pages**
   - Source: Deploy from a branch
   - Branch: `main`
   - Folder: `/ (root)`
   - Click "Save"

3. **Wait for Deployment**
   - GitHub will build your site (takes 1-2 minutes)
   - Refresh the page to see the URL
   - Your site will be at: `https://YOUR-USERNAME.github.io/alison-career-roadmaps/`

### Step 4: Verify Deployment

1. **Check the URL**
   - Click the "Visit site" button in Settings > Pages
   - Or go directly to your GitHub Pages URL

2. **Test Navigation**
   - Verify homepage loads correctly
   - Click on roadmap links
   - Check that all pages work

3. **Fix Issues if Needed**
   - If links don't work, check file paths
   - Ensure all markdown files are in correct folders
   - Commit and push any fixes

## Updating Your Site

### Making Changes

```bash
# Edit files locally
# Then:

git add .
git commit -m "Describe your changes"
git push origin main
```

GitHub Pages will automatically rebuild (1-2 minutes).

### Adding New Roadmaps

1. Create new markdown file in `roadmaps/` folder
2. Follow existing format
3. Update main README.md with link
4. Commit and push changes

## Custom Domain (Optional)

### Using Your Own Domain

1. **Purchase a Domain** (e.g., from Namecheap, GoDaddy)

2. **Configure DNS**
   - Add A records pointing to GitHub:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - Or add CNAME record: `YOUR-USERNAME.github.io`

3. **Update GitHub Settings**
   - Settings > Pages > Custom domain
   - Enter your domain
   - Check "Enforce HTTPS"

4. **Create CNAME File**
   ```bash
   echo "yourdomain.com" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push origin main
   ```

## Troubleshooting

### Site Not Showing Up
- Wait 5-10 minutes for initial deployment
- Check Settings > Pages for errors
- Ensure repository is public
- Verify files are in main branch

### Links Not Working
- Use relative paths (e.g., `roadmaps/file.md`)
- Check file names match exactly (case-sensitive)
- Ensure all `.md` extensions are included

### Images Not Loading
- Images should be in repository
- Use relative paths
- Check file names and extensions

### Changes Not Appearing
- Clear browser cache (Ctrl+Shift+R)
- Wait a few minutes for rebuild
- Check GitHub Actions for build status

## Best Practices

### Commit Messages
- Be descriptive: "Add cybersecurity roadmap"
- Use present tense: "Update salary information"
- Keep under 50 characters for summary

### File Organization
- Keep structure consistent
- Use lowercase filenames with hyphens
- Organize by categories

### Regular Maintenance
- Update course links quarterly
- Check for broken links monthly
- Update salary information annually
- Add new courses as available

## GitHub Actions (Optional)

### Automated Link Checking

Create `.github/workflows/check-links.yml`:

```yaml
name: Check Links

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly
  workflow_dispatch:

jobs:
  check-links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check links
        uses: gaurav-nelson/github-action-markdown-link-check@v1
```

This will automatically check for broken links weekly.

## Security

### Protecting Your Repository
- Never commit sensitive information
- Review changes before pushing
- Use `.gitignore` for local files
- Be cautious with pull requests

## Analytics (Optional)

### Adding Google Analytics

1. Get GA tracking ID from [analytics.google.com](https://analytics.google.com)
2. Add to `_config.yml`:
   ```yaml
   google_analytics: UA-XXXXXXXXX-X
   ```
3. Commit and push

### GitHub Insights
- Check Settings > Insights for:
  - Traffic data
  - Popular content
  - Referral sources
  - Clone statistics

## Promoting Your Site

### Share on Social Media
- LinkedIn - Professional audience
- Twitter - Tech community
- Reddit - r/learnprogramming, r/careeradvice
- Facebook - Educational groups

### SEO Optimization
- Use descriptive titles
- Add meta descriptions
- Include relevant keywords
- Create quality content
- Build backlinks

## Support

### Getting Help
- GitHub Docs: [docs.github.com/pages](https://docs.github.com/pages)
- GitHub Community: [github.community](https://github.community)
- Stack Overflow: [stackoverflow.com](https://stackoverflow.com)

### Contributing
- Read [CONTRIBUTING.md](CONTRIBUTING.md)
- Open issues for bugs
- Submit pull requests for improvements

---

## Quick Reference

### Essential Commands
```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/alison-career-roadmaps.git

# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Your message"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main
```

### Useful Links
- Your repo: `https://github.com/YOUR-USERNAME/alison-career-roadmaps`
- Your site: `https://YOUR-USERNAME.github.io/alison-career-roadmaps/`
- GitHub Pages docs: `https://docs.github.com/pages`

---

**Need help?** Open an issue or contact the community!

---

*Last Updated: February 2026*
