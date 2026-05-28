# 🕒 Overtime Board Management System

A full-stack overtime management platform modeled after real-world public safety staffing workflows. The system is designed to separate supervisor administrative controls from employee overtime bidding and shift management functionality.

> ⚠️ **Project Status:** Active Development — Core API Live / Auth Phase  
> The base backend architecture (Models, Migrations, Serializers, Views, and URLs) is fully operational. The current sprint is implementing secure Token-based authentication and Role-Based Access Control (RBAC).

---

## 🏗️ Completed Backend Features

### 📡 Live Core REST API
Built out and mapped scalable REST API endpoints using Django REST Framework, establishing functional data serialization pipelines for user profiles, shift tracking, and assignment workflows.

### 🗄️ Relational Schema Design
Designed and migrated a comprehensive SQL database schema optimized to manage employee data, overtime shifts, and real-time assignment states without data race conditions.

---

## 🛠️ Tech Stack

* **Backend Engine:** Python, Django, Django REST Framework
* **Database Layer:** SQLite (Local development) / PostgreSQL-ready architecture
* **Client Frontend:** React, Tailwind CSS *(Upcoming Integration Phase)*

---

## 🗺️ Development Roadmap

- [x] Design relational database schema and shift-state models
- [x] Deploy live base REST API endpoints (Views, Serializers, URLs)
- [ ] Implement Badge Number + PIN Authentication (*Current Sprint*)
- [ ] Restrict endpoints with Role-Based Access Control (Supervisor permissions vs. Employee bidding)
- [ ] Initialize React frontend workspace and connect authentication/API contexts
