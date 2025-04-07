[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](/fork)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

> [!TIP]
> If you are looking for the full roadmap, including this project, go back to the [getting started](https://devopsroadmap.io/getting-started) page.

This repository is the starting point for [HiveBox](https://devopsroadmap.io/projects/hivebox/), the end-to-end hands-on project.

You can fork this repository and start implementing the [HiveBox](https://devopsroadmap.io/projects/hivebox/) project. HiveBox project follows the same Dynamic MVP-style mindset used in the [roadmap](https://devopsroadmap.io/).

The project aims to cover the whole Software Development Life Cycle (SDLC). That means each phase will cover all aspects of DevOps, such as planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

Happy DevOpsing ♾️

## Before you start

Here is a pre-start checklist:

- ⭐ <a target="_blank" href="https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap">Star the **roadmap** repo</a> on GitHub for better visibility.
- ✉️ <a target="_blank" href="https://newsletter.devopsroadmap.io/subscribe">Join the community</a> for the project community activities, which include mentorship, job posting, online meetings, workshops, career tips and tricks, and more.
- 🌐 <a target="_blank" href="https://t.me/DevOpsHive/985">Join the Telegram group</a> for interactive communication.

## Preparation

- [Create GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) (if you don't have one), then [fork this repository](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork) and start from there.
- [Create GitHub project board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project) for this repository (use `Kanban` template).
- Each phase should be presented as a pull request against the `main` branch. Don’t push directly to the main branch!
- Document as you go. Always assume that someone else will read your project at any phase.
- You can get senseBox IDs by checking the [openSenseMap](https://opensensemap.org/) website. Use 3 senseBox IDs close to each other (you can use the following [5eba5fbad46fb8001b799786](https://opensensemap.org/explore/5eba5fbad46fb8001b799786), [5c21ff8f919bf8001adf2488](https://opensensemap.org/explore/5c21ff8f919bf8001adf2488), and [5ade1acf223bd80019a1011c](https://opensensemap.org/explore/5ade1acf223bd80019a1011c)). Just copy the IDs, you will need them in the next steps.

<br/>
<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox/" imageanchor="1">
    <img src="https://img.shields.io/badge/Get_Started_Now-559e11?style=for-the-badge&logo=Vercel&logoColor=white" />
  </a><br/>
</p>

---

** ADD YOUR IMPLEMENTATION DOCUMENTATION HERE **

# DevOps Journey – HiveBox Project

This repository documents my DevOps learning journey through the HiveBox project, inspired by the [DevOps Roadmap](https://devopsroadmap.io/). The goal is to put DevOps theory into practice by following real-world workflows, using automation, collaboration, and modern tools.

---

## Table of Contents

- [Overview](#overview)
- [DevOps Foundations](#devops-foundations)
- [Phase 1 - Kickoff & Preparation](#phase-1---kickoff--preparation)
  - [1.1 Kickoff](#11-kickoff)
  - [1.2 Preparation](#12-preparation)
- [Phase 2 - Core DevOps Module](#phase-2---core-devops-module)
  - [2.1 Tools](#21-tools)
  - [2.2 Code](#22-code)
  - [2.3 Containers](#23-containers)
  - [2.4 Testing](#24-testing)

---

## Overview

This project simulates a real DevOps workflow across the Software Development Life Cycle (SDLC). It follows Agile practices, and incorporates key DevOps principles: version control, CI/CD, Infrastructure as Code (IaC), testing, and automation.

---

## DevOps Foundations

### DevOps is a Methodology, Not a Tool

DevOps is about aligning development and operations to improve delivery speed, collaboration, and system reliability. It's not just about tools—it's about mindset and culture.

### Key Pillars

- **Practices**: Source Control (SCM), IaC, CI/CD pipelines, automated testing, peer reviews.
- **Tools**: Git, GitHub, Docker, Jenkins, Kubernetes (later stages), etc.
- **Culture**: Collaboration, transparency, feedback loops, shared goals.
- **Mindset**:
  - Solve the right problems, not just the visible ones.
  - Track every change (no untracked fixes).
  - Focus on solutions, not blame.
  - Avoid hero culture—prioritize maintainability.

### Core Principles

- **Automation**: Not the goal, but a means to scale and stabilize delivery.
- **Communication**: Across all teams—development, operations, testing, and business.
- **Continuous improvement**: Work iteratively, prioritize feedback, minimize waste.
- **User-centered focus**: Technical improvements should support real user needs.

### Common DevOps Roles

| Role | Focus |
|------|-------|
| **DevOps Engineer** | Improves development and deployment workflows |
| **SRE (Site Reliability Engineer)** | Ensures system reliability and performance |
| **Cloud Engineer** | Builds and maintains cloud infrastructure |
| **Platform Engineer** | Develops internal tools and platforms for developers |

---

## Phase 1 - Kickoff & Preparation

This first phase helps set expectations and define how to work effectively from the start.

### 1.1 Kickoff

This phase is about **understanding the environment and setting up the right mindset**:

- [x] I understand that DevOps is not done in isolation. Even if I’m working solo, the mindset is collaborative.
- [x] I reviewed key Agile project management principles and compared:
  - Scrum (sprint-based)
  - Scrumban (hybrid)
  - ✅ **Kanban** (my choice for this project, due to its continuous flow and adaptability)
- [x] I will follow the "Make it work → Make it right → Make it fast" principle to stay focused and avoid scope creep.
- [x] I acknowledge that I am my own project manager for this journey, and I’m responsible for organizing and delivering my work as if I were part of a larger team.

### 1.2 Preparation

Setting up the tools and structure to support the work ahead:

- [x] Created a GitHub account and forked the **HiveBox** repository.
- [x] Set up a **GitHub Project Board** using the Kanban template to track progress.
- [x] I will submit each phase as a **Pull Request** to the `main` branch.
  - No direct pushes to `main`.
- [x] I committed to documenting everything clearly and consistently.
- [x] Selected three **senseBox IDs** that are geographically close to each other from [openSenseMap](https://opensensemap.org/):
  - `5eba5fbad46fb8001b799786`
  - `5c21ff8f919bf8001adf2488`
  - `5ade1acf223bd80019a1011c`

---

## Phase 2 - Core DevOps Module

This phase will focus on putting core DevOps practices into action.

### 2.1 Tools

TBD — Will document my setup and reasoning behind choosing each DevOps tool used.

### 2.2 Code

TBD — This section will cover version control practices and coding workflows.

### 2.3 Containers

TBD — I will begin working with Docker and containerization.

### 2.4 Testing

TBD — Implement automated tests and integrate with CI pipelines.

---

## License

This project is open and educational. Feel free to fork and build your own journey.

