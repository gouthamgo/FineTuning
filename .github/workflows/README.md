# 🤖 GitHub Actions CI/CD Workflows

This repository uses GitHub Actions for automated merging and validation.

---

## 📋 Available Workflows

### 1. **Auto-merge Claude Branches** ✨ (ACTIVE)
**File:** `auto-merge-claude-branches.yml`

**What it does:**
- Automatically merges `claude/*` branches to `main`
- Runs validation checks before merging
- Creates PR if merge fails (conflicts)
- Cleans up merged branches

**Triggers:**
- Any push to branches matching `claude/**`

**Flow:**
```
Push to claude/* → Validate → Merge to main → Delete branch
                     ↓ (if conflicts)
                   Create PR for manual review
```

**Status:** ✅ **ENABLED** - Auto-merges without manual effort

---

### 2. **Auto-PR for Claude Branches** 🔄 (ALTERNATIVE)
**File:** `auto-pr-claude-branches.yml`

**What it does:**
- Creates a Pull Request instead of direct merge
- Enables auto-merge on the PR
- Updates existing PR if it already exists
- Safer option with review capability

**Triggers:**
- Any push to branches matching `claude/**`

**Flow:**
```
Push to claude/* → Create PR → Enable auto-merge
```

**Status:** ⚠️ **DISABLED BY DEFAULT**
- To use this instead of direct merge, rename the file or disable the other workflow

---

### 3. **Validate Changes** ✅
**File:** `validate.yml`

**What it does:**
- Validates Jupyter notebooks (JSON syntax)
- Checks for large files (>10MB)
- Validates Python files (syntax)
- Validates documentation exists

**Triggers:**
- Every push to any branch
- Every pull request to main

**Flow:**
```
Push/PR → Run checks → Report status
```

**Status:** ✅ **ENABLED** - Runs on all changes

---

## 🚀 How Auto-Merge Works

When you push to a `claude/` branch:

### **Scenario 1: Clean Merge** ✅
```
1. Push to claude/my-feature-abc123
2. GitHub Actions triggers
3. Validates notebooks and files
4. Merges to main automatically
5. Pushes to main
6. Deletes claude/my-feature-abc123
7. ✅ Done! No manual action needed
```

### **Scenario 2: Merge Conflicts** ⚠️
```
1. Push to claude/my-feature-abc123
2. GitHub Actions triggers
3. Validates notebooks and files
4. Detects merge conflicts
5. Creates Pull Request instead
6. Notifies you to resolve conflicts
7. ⚠️ Manual merge required
```

---

## ⚙️ Configuration

### Enable/Disable Workflows

**To DISABLE auto-merge:**
```bash
# Rename the workflow file
mv .github/workflows/auto-merge-claude-branches.yml \
   .github/workflows/auto-merge-claude-branches.yml.disabled
```

**To ENABLE PR-based workflow instead:**
```bash
# They can coexist, but you probably want one or the other
# Just keep both enabled if you want PRs created AND auto-merged
```

### Customize Branch Pattern

Edit the workflow file and change:
```yaml
on:
  push:
    branches:
      - 'claude/**'  # Change this pattern
```

Examples:
- `'feature/**'` - Match all feature branches
- `'auto-merge/**'` - Match branches starting with auto-merge/
- `'**'` - Match ALL branches (dangerous!)

### Skip Auto-Merge for Specific Commits

Add `[skip ci]` or `[no merge]` to your commit message:
```bash
git commit -m "WIP changes [skip ci]"
```

---

## 🔒 Required Permissions

These workflows need these GitHub permissions:
- ✅ `contents: write` - To merge and push
- ✅ `pull-requests: write` - To create PRs

**Already configured in the workflows** ✅

---

## 🧪 Testing the Workflow

### Test Auto-Merge Locally

```bash
# 1. Create a test branch
git checkout -b claude/test-auto-merge-123

# 2. Make a small change
echo "Test" >> test.txt
git add test.txt
git commit -m "Test auto-merge workflow"

# 3. Push to GitHub
git push -u origin claude/test-auto-merge-123

# 4. Watch GitHub Actions tab
# The branch should auto-merge to main within 1-2 minutes
```

### Test Conflict Handling

```bash
# 1. Create conflicting changes on main
git checkout main
echo "Change on main" >> README.md
git add README.md
git commit -m "Change on main"
git push

# 2. Create conflicting branch
git checkout -b claude/test-conflict-123
echo "Different change" >> README.md
git add README.md
git commit -m "Conflicting change"
git push -u origin claude/test-conflict-123

# 3. Watch GitHub Actions
# Should create a PR instead of merging
```

---

## 📊 Monitoring

### View Workflow Runs

1. Go to your GitHub repo
2. Click "Actions" tab
3. See all workflow runs

### Check Merge Status

```bash
# See if your branch was merged
git fetch origin
git log origin/main --oneline -10

# Should see your auto-merge commit
```

### Notifications

GitHub will notify you:
- ✅ When auto-merge succeeds
- ❌ When auto-merge fails
- 📝 When PR is created (if conflicts)

---

## 🛡️ Safety Features

### Built-in Protections

1. **Validation checks** - Notebooks must be valid JSON
2. **Conflict detection** - Creates PR if conflicts exist
3. **Fallback to PR** - Never fails silently
4. **Branch cleanup** - Removes merged branches automatically

### Override Safety (Advanced)

If you want **maximum automation** (merge even with conflicts):

Create `.github/workflows/force-merge.yml`:
```yaml
name: Force Merge (Use with Caution)

on:
  push:
    branches:
      - 'force/**'  # Only for force/ branches

jobs:
  force-merge:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - uses: actions/checkout@v4
      - name: Force merge to main
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git fetch origin main
          git checkout main
          git merge --no-ff ${{ github.ref_name }} --strategy-option theirs
          git push origin main
```

⚠️ **Warning:** This will **override conflicts** using "theirs" strategy!

---

## 🔧 Troubleshooting

### Workflow Not Running

**Check:**
1. Workflow file is in `.github/workflows/`
2. File has `.yml` extension
3. Branch name matches pattern (`claude/`)
4. GitHub Actions is enabled in repo settings

### Merge Failed

**Possible reasons:**
1. Merge conflicts (check PR created)
2. Protected branch rules (disable for auto-merge)
3. Permission issues (check workflow permissions)

**Fix:**
```bash
# Check GitHub Actions logs
# Go to Actions tab → Click failed workflow → View logs
```

### Branch Not Deleted

**Reason:** Delete step failed (safe to ignore)

**Manual cleanup:**
```bash
git push origin --delete claude/old-branch-name
```

---

## 📚 Best Practices

### ✅ DO:
- Use descriptive branch names: `claude/feature-xyz-123`
- Keep commits small and focused
- Let CI validate before merging
- Review PR if conflicts occur

### ❌ DON'T:
- Push large files (>10MB) without Git LFS
- Force push to `claude/` branches after workflow starts
- Disable validation checks without good reason
- Merge manually if auto-merge is enabled (causes confusion)

---

## 🆘 Emergency Stop

### Disable All Auto-Merge

```bash
# Quick disable - rename workflows
cd .github/workflows
mv auto-merge-claude-branches.yml auto-merge-claude-branches.yml.disabled
mv auto-pr-claude-branches.yml auto-pr-claude-branches.yml.disabled
git add -A
git commit -m "Disable auto-merge workflows"
git push
```

### Re-enable

```bash
# Rename back
mv auto-merge-claude-branches.yml.disabled auto-merge-claude-branches.yml
git add -A
git commit -m "Re-enable auto-merge"
git push
```

---

## 📈 Workflow Statistics

View in GitHub:
- **Actions** tab → **Auto-merge Claude Code Branches**
- See success rate, average merge time, etc.

---

## 🤝 Contributing

Want to improve these workflows?

1. Test changes in a fork first
2. Create PR with workflow improvements
3. Document changes in this README

---

**Questions?** Check [GitHub Actions docs](https://docs.github.com/en/actions) or open an issue.

---

**Last Updated:** 2025-11-16
**Maintained by:** AI-powered development workflows ✨
