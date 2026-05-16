# Infrastructure Build Plan

**Goal:** Build a portfolio-worthy homelab that demonstrates production-grade DevOps skills.

---

## Phase 1: Kubernetes Foundation (Weeks 1-4)

### Week 1-2: K3s Single-Node Cluster
- [ ] Install K3s on Proxmox (single-node, existing hardware)
- [ ] Configure kubectl on host
- [ ] Deploy first workload (nginx or Jellyfin)
- [ ] Write blog post: "How I built a production-grade Kubernetes cluster in my apartment"
- [ ] Document networking (Traefik ingress, MetalLB for load balancing)

### Week 3-4: GitOps with ArgoCD
- [ ] Install ArgoCD on K3s
- [ ] Set up GitOps workflow (app-of-apps pattern)
- [ ] Migrate one existing Docker Compose stack to Kubernetes manifests
- [ ] Write blog post: "GitOps in my homelab with ArgoCD"

### Deliverables for Phase 1:
- Blog post: "From Docker Compose to Kubernetes in 2 weeks"
- GitHub repo: kubernetes-homelab
- Working K3s cluster accessible from internet

---

## Phase 2: Infrastructure as Code (Weeks 5-8)

### Week 5-6: Terraform Everything
- [ ] Write Terraform configs for Proxmox CTs (use proxmox-terraform provider)
- [ ] Terraform the monitoring stack (Prometheus + Grafana as code)
- [ ] Document: modules for reusable CT templates
- [ ] Write blog post: "I provisioned my entire homelab with Terraform"

### Week 7-8: Ansible for Configuration Management
- [ ] Install Ansible on host
- [ ] Write playbooks for: new CT creation, package installation, user management
- [ ] Integrate with Terraform (Packer + Ansible = golden images)
- [ ] Write blog post: "Homelab automation with Ansible"

### Deliverables for Phase 2:
- Blog post: "IaC for homelab"
- GitHub repo: homelab-terraform
- GitHub repo: homelab-ansible
- Terraform configs for 5+ services

---

## Phase 3: CI/CD Pipeline (Weeks 9-12)

### Week 9-10: GitHub Actions Mastery
- [ ] Build CI pipeline for homelab configs (lint + validate + deploy)
- [ ] Set up container builds (Dockerfile → GHCR)
- [ ] ArgoCD image updater for automatic deployments
- [ ] Write blog post: "My homelab CI/CD pipeline"

### Week 11-12: Observability Stack + Cloud
- [ ] Complete monitoring: Loki logs + Grafana dashboards
- [ ] Set up alerting (Grafana Alertmanager + PagerDuty/OPSGenie free tier)
- [ ] AWS free tier: deploy one workload (S3 static site or Lambda)
- [ ] Document everything

### Deliverables for Phase 3:
- Blog post: "Full observability in homelab"
- Blog post: "First AWS deployment"
- GitHub Actions pipelines for 3+ projects

---

## Tech Stack to Master

| Skill | Tools | Priority |
|-------|-------|----------|
| Container orchestration | K3s, Docker, Docker Compose | Critical |
| GitOps | ArgoCD, Flux | Critical |
| Infrastructure as Code | Terraform, Ansible | Critical |
| CI/CD | GitHub Actions, Jenkins | High |
| Monitoring | Prometheus, Grafana, Loki | High |
| Cloud | AWS (EC2, S3, Lambda, EKS) | High |
| Networking | WireGuard, Nginx, DNS | Medium |
| Security | UFW, Let's Encrypt, fail2ban | Medium |

---

## Blog Post Ideas (in order)

1. "How I built a production-grade Kubernetes cluster in my apartment for $0/month"
2. "From Docker Compose to Kubernetes in 2 weeks"
3. "GitOps in my homelab with ArgoCD"
4. "I provisioned my entire homelab with Terraform"
5. "Homelab automation with Ansible"
6. "My full CI/CD pipeline for homelab deployments"
7. "Full observability stack: Prometheus + Grafana + Loki"
8. "Deploying to AWS for free: my first cloud project"

---

## Progress

| Task | Status | Completed |
|------|--------|----------|
| K3s installed | ❌ | - |
| ArgoCD deployed | ❌ | - |
| Terraform configs | 0 | - |
| Ansible playbooks | 0 | - |
| GitHub Actions pipelines | 0 | - |
| Blog posts | 0 | - |
