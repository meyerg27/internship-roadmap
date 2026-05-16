# Grayson Meyer's Internship Roadmap — Summer 2027

**Goal:** Land a DevOps/SRE/Platform Engineering internship for Summer 2027  
**Current status:** Week 02 — Infrastructure build phase  
**Started:** May 16, 2026  
**Timeline:** ~14 months until internship

---

## 🎯 The Goal

**Target:** $130-160K DevOps/SRE internship (NYC area)
**Companies:** Google, Meta, Amazon, JPMorgan, Datadog, Cloudflare, and 40+
**Skills needed:** K8s, Terraform, CI/CD, monitoring, networking

---

## 📊 Current Status — May 16, 2026

### ✅ Done Today
- K3s v1.35.4 deployed on Proxmox host
- MetalLB (192.168.50.200-250 pool)
- Traefik ingress controller
- Test nginx: **192.168.50.201**
- PostgreSQL: running
- Umami analytics: **192.168.50.202**
- ArgoCD: installing
- **LeetCode: Two Sum #1 solved** ✅
- GitHub push attempted (token expired — noted)

### 🏗️ Infrastructure Built (Today)
- Complete `homelab-infra/` repo (20+ files)
- Terraform Proxmox configs
- K8s manifests (Umami, PostgreSQL, MetalLB, Traefik)
- Ansible playbooks
- GitHub Actions CI pipeline
- 3 blog post drafts written

---

## 📅 Roadmap

### Phase 1: Foundation (May-June 2026) ← **YOU ARE HERE**
- [x] K3s cluster running ✅ (May 16)
- [ ] ArgoCD GitOps setup
- [ ] First 3 real apps deployed
- [ ] GitHub repo initialized + first commit
- [ ] Hashnode account created
- [ ] Blog post #1 published
- [ ] 50 LeetCode problems

### Phase 2: Portfolio (June-August 2026)
- [ ] 150 LeetCode problems (target)
- [ ] 6 blog posts published
- [ ] Resume finalized
- [ ] LinkedIn updated
- [ ] GitHub profile polished
- [ ] 3 infrastructure projects documented

### Phase 3: Applications (August-September 2026)
- [ ] Apply to 50+ companies
- [ ] Practice OAs
- [ ] Get referrals
- [ ] Phone screens

### Phase 4: Interviews (October-November 2026)
- [ ] Technical interviews
- [ ] Systems design prep
- [ ] Offer negotiation

---

## 🏗️ homelab-infra Repo

**Location:** `/root/.openclaw/workspace/projects/homelab-infra/`

```
homelab-infra/
├── README.md
├── .github/workflows/ci.yaml       # GitHub Actions CI
├── terraform/                       # Proxmox IaC
│   ├── provider.tf
│   ├── proxmox.auto.tfvars.example
│   └── ct/sample.tf
├── k8s/                            # Kubernetes manifests
│   ├── install-k3s.sh
│   ├── ubuntu-kickstart.cfg
│   ├── core/                      # MetalLB, Traefik, ArgoCD, cert-manager
│   └── apps/                      # Umami, namespace
├── ansible/                        # Configuration management
│   ├── site.yml
│   ├── docker.yml
│   └── inventory.yml
├── scripts/
│   └── deploy-k3s.sh
├── docs/
│   └── github-secrets.md
└── blog/                           # Draft blog posts
    ├── 01-monitoring-stack.md
    ├── 02-self-hosted-cloud.md
    └── 03-42-services-homelab.md
```

---

## 📝 Files Created Today

| File | Purpose |
|------|---------|
| `tracking/applications-tracker.md` | 33+ companies to apply to |
| `tracking/leetcode-tracker.md` | Full NeetCode 150 problem list |
| `blog/ideas.md` | 12 blog post ideas + schedule |
| `applications/companies.md` | Detailed company research |
| `weekly/W02.md` | Week 2 execution plan |

---

## 📚 Blog Post Ideas

1. ✅ "How I Monitor 42 Services with Prometheus + Grafana"
2. ✅ "I Replaced Google Workspace With My Homelab"
3. ✅ "42 Services on One Server: How My Homelab Works"
4. 🔲 "From Docker Compose to Kubernetes in 2 Weeks"
5. 🔲 "GitOps in My Homelab: ArgoCD Changed Everything"
6. 🔲 "I Provisioned My Entire Homelab with Terraform"

---

## 📈 Progress

| Metric | Target | Current | % |
|--------|--------|---------|---|
| LeetCode | 150 | 2 | 0.7% |
| Blog Posts | 6 | 0 published | 0% |
| K8s Apps | 10 | 3 | 30% |
| GitHub Stars | 10 | 0 | 0% |
| Companies Researched | 33+ | 0 | 0% |
| Applications Sent | 50+ | 0 | 0% |

---

## 🚀 Next Steps

1. **Today:** Wait for ArgoCD to finish installing
2. **Today:** Solve 2 LeetCode problems (Two Sum + Valid Anagram)
3. **This week:** Get ArgoCD working, push repo to GitHub
4. **This week:** Publish first blog post
5. **Next week:** Deploy more apps, start LeetCode grind

---

## 💡 Key Lessons

- **Start before you're ready.** K3s on Proxmox = harder than expected (kernel modules in LXC). Fixed by installing on host.
- **K3s on bare metal (Proxmox host) works.** Single-node K3s is production-viable for homelab.
- **MetalLB makes K8s services accessible from the LAN.** No cloud provider needed.
- **Document everything.** First blog post draft took 30 min, generates lasting value.

---

*Last updated: May 16, 2026*
