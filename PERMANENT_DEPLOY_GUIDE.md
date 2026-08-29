
# HydroSentinel AI - PERMANENT DEPLOY GUIDE

## Permanent Deploy (Free Forever - No Sleep)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Permanent deploy"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hydrosentinel-advanced.git
git push -u origin main
```

### Step 2: Deploy Backend to KOYEB (Permanent, No Sleep)
1. Go to https://app.koyeb.com -> Create Service -> GitHub -> Select your repo
2. Builder: Dockerfile
3. Port: 8000
4. Deploy -> You get https://your-app.koyeb.app -> THIS IS PERMANENT (does not sleep like Render)

### Step 3: Deploy Frontend to VERCEL (Permanent)
1. Go to https://vercel.com/new -> Import same GitHub repo
2. Framework: Other, Root Directory: ./
3. Deploy -> You get https://hydrosentinel-advanced.vercel.app -> PERMANENT

### Step 4: Connect Both (Optional)
In frontend/index.html, change API_URL to your Koyeb backend URL:
const API_URL = "https://your-app.koyeb.app"

### Alternative Permanent: Hugging Face Spaces (Easiest)
1. Go to https://huggingface.co/spaces -> Create New Space -> Docker
2. Upload all files
3. It gives permanent link forever.

### Custom Domain (Make it like hydrosentinel.in)
1. Buy domain from GoDaddy/Hostinger (~₹400/year)
2. In Vercel -> Settings -> Domains -> Add your domain
3. Done, permanent professional link.

### Keep Alive (If you use Render)
If you still want Render, use https://uptimerobot.com to ping your site every 5 min so it never sleeps.
