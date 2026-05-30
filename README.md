# Docker Capstone Project: Employee Management System

A containerised, production-style web application built as the capstone of a 10-day Docker learning sprint.

## What It Does

A full-stack Employee Management System that allows users to:
- View all employees in a sortable list
- View individual employee profiles
- Add new employees (name, department, role, email)
- Delete employees

## Architecture

Three services run on an isolated internal Docker network. Flask is not exposed to the host — all traffic routes through Nginx as a reverse proxy.

## Stack

| Layer | Technology |
|---|---|
| Web server | Nginx (Alpine) |
| Application | Python 3.12, Flask |
| Database | PostgreSQL 16 (Alpine) |
| Containerisation | Docker, Docker Compose |
| Security scanning | Trivy |
| Image registry | AWS ECR |

## How to Run

**Prerequisites:** Docker and Docker Compose installed.

```bash
git clone https://github.com/Jason2303/Docker-capstone.git
cd Docker-capstone
docker compose up --build
```

Visit `http://localhost` in your browser.

To stop:
```bash
docker compose down
```

To stop and remove the database volume:
```bash
docker compose down -v
```

## Security: Trivy Vulnerability Scan

The Flask app image was scanned with Trivy before and after hardening.

**Hardening applied:** Removed `perl-base`, `ncurses-bin`, and `ncurses-base` from the base image — unnecessary packages that carried HIGH and CRITICAL CVEs.

### Before

![Trivy Before](docs/screenshots/trivy_before_pic.png)

| Severity | Count |
|---|---|
| CRITICAL | 2 |
| HIGH | 8 |
| MEDIUM | 42 |
| LOW | 65 |
| **Total** | **121** |

### After

![Trivy After](docs/screenshots/trivy_after_pic.png)

| Severity | Count |
|---|---|
| CRITICAL | 0 |
| HIGH | 2 |
| MEDIUM | 29 |
| LOW | 60 |
| **Total** | **92** |

CRITICAL vulnerabilities eliminated. Remaining 2 HIGH findings are OS-level packages with no upstream fix available at time of writing.

## Project Structure

```

capstone/
├── docker-compose.yml
├── flask-app/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── nginx/
│   └── nginx.conf
├── postgres/
│   └── init.sql
└── docs/
├── trivy-before.txt
├── trivy-after.txt
└── screenshots/
├── trivy_before_pic.png
└── trivy_after_pic.png

```

## AWS ECR

Image pushed to AWS Elastic Container Registry as part of the CI/CD workflow.