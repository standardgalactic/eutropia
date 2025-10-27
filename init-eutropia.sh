#!/usr/bin/env bash
set -e

# --- Configuration ---
USER_NAME="standardgalactic"
REPO_NAME=$(basename "$(pwd)")

echo "🌀 Deploying or initializing: $USER_NAME/$REPO_NAME"

# --- Ensure git repo exists ---
if [ ! -d .git ]; then
  git init
  echo "✅ Initialized new git repository."
fi

# --- Switch to main branch (create if needed) ---
git checkout -B main >/dev/null 2>&1 || true

# --- Add and commit all changes ---
git add .
git commit -m "Update $(date '+%Y-%m-%d %H:%M:%S')" || echo "⚠️ No changes to commit."

# --- Check if remote repo exists ---
if gh repo view "$USER_NAME/$REPO_NAME" >/dev/null 2>&1; then
  echo "📡 Repo already exists on GitHub."
  git remote add origin "https://github.com/$USER_NAME/$REPO_NAME.git" 2>/dev/null || true
  git push -u origin main
else
  echo "🌱 Creating new GitHub repository..."
  gh repo create "$USER_NAME/$REPO_NAME" --public --source=. --remote=origin --push
fi

# --- Enable GitHub Pages (main branch, root directory) ---
echo "🌐 Enabling GitHub Pages..."
gh api \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/$USER_NAME/$REPO_NAME/pages" \
  -f source='{"branch":"main","path":"/"}' >/dev/null || \
  echo "⚠️ Could not enable GitHub Pages automatically. Enable manually in Settings > Pages."

# --- Display success info ---
echo ""
echo "✅ Deployment complete!"
echo "🔗 Repo: https://github.com/$USER_NAME/$REPO_NAME"
echo "🌍 GitHub Pages: https://$USER_NAME.github.io/$REPO_NAME/"
echo ""

