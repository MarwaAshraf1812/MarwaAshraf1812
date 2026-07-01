<div align="center">

<!-- Waving Gradient Header matching the Lavender/Purple theme -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=7C3AED,8B5CF6,A78BFA,C4B5FD&height=130&section=header" width="100%" />

<br/>

<!-- Custom Typing SVG -->
<img src="https://readme-typing-svg.demolab.com?font=Outfit&size=30&duration=2000&pause=1000&color=A78BFA&center=true&vCenter=true&width=650&lines=Hi+there%2C+I'm+Marwa+Ashraf+%F0%9F%8C%B8;Full+Stack+Software+Engineer;Node.js+%7C+React+%7C+Next.js;Clean+code%2C+clean+architecture+%E2%9C%A8" alt="Typing SVG" />

<br/>

<!-- Social badging -->
[![Portfolio](https://img.shields.io/badge/Portfolio-%237C3AED.svg?style=for-the-badge&logo=vercel&logoColor=white)](https://marwaashraf1812.github.io/My_Portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%238B5CF6.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marwa-ashraf1/)
[![Gmail](https://img.shields.io/badge/Gmail-%23A78BFA.svg?style=for-the-badge&logo=gmail&logoColor=white)](mailto:marwaashrafabdullah@gmail.com)

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=marwaashraf1812&color=A78BFA&style=flat-square&label=Profile+Views)

</div>

---

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="360" align="right" />

### 💜 About Me

I am a **Full Stack Software Engineer** specializing in constructing scalable backend architectures and designing interactive frontends. My engineering philosophy revolves around Clean Code, SOLID Principles, and architectural design patterns.

- 🔭 Currently building **[Fusion Store](https://github.com/MarwaAshraf1812/fusion-store)** — a high-performance Next.js 16 e-commerce engine.
- 🌱 Deepening expertise in **System Architectures**, **NestJS**, and **Next.js Server Actions**.
- 🏛️ Engineering Fellow at **ITI (Information Technology Institute)**.
- 🏆 ALX Software Engineering Graduate — specialized in Backend Systems.
- 📍 Based in **Egypt**

<br clear="right"/>

---

### 🏛️ Engineering Blueprint & System Flow
Below is a technical architecture diagram representing the asynchronous workflow I implement in multi-agent processing systems (such as my recruitment platform **Naqla AI**):

```mermaid
graph TD
    classDef client fill:#7C3AED,stroke:#A78BFA,stroke-width:2px,color:#fff;
    classDef server fill:#1E1B2E,stroke:#7C3AED,stroke-width:2px,color:#C4B5FD;
    classDef agent fill:#8B5CF6,stroke:#A78BFA,stroke-width:2px,color:#fff;
    classDef db fill:#5B21B6,stroke:#7C3AED,stroke-width:2px,color:#fff;

    Client["React / Next.js Client App"]:::client
    Gateway["Node.js / Express API Gateway"]:::server
    Queue["BullMQ / Redis Background Worker"]:::server
    
    subgraph "Multi-Agent Engine (LangGraph.js)"
        AgentEngine["Workflow Orchestrator"]:::agent
        AgentA["Resume Parser Agent"]:::agent
        AgentB["Technical Evaluation Agent"]:::agent
        AgentC["Behavioral Assessment Agent"]:::agent
    end

    DB[("PostgreSQL / MongoDB / Prisma")]:::db

    Client -->|HTTP POST / GraphQL| Gateway
    Gateway -->|Publish Event| Queue
    Queue -->|Process Event| AgentEngine
    AgentEngine --> AgentA
    AgentEngine --> AgentB
    AgentEngine --> AgentC
    AgentA -->|Store Results and State| DB
    AgentB -->|Store Results and State| DB
    AgentC -->|Store Results and State| DB
```

---

### 🛠️ Tech Stack & Tooling

<table>
  <tr>
    <td valign="top" width="50%">
      <h4>⚡ Backend & APIs</h4>
      <img src="https://img.shields.io/badge/Node.js-%235B21B6.svg?style=flat-square&logo=node.js&logoColor=white" />
      <img src="https://img.shields.io/badge/Express.js-%237C3AED.svg?style=flat-square&logo=express&logoColor=white" />
      <img src="https://img.shields.io/badge/Python-%238B5CF6.svg?style=flat-square&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/Django-%235B21B6.svg?style=flat-square&logo=django&logoColor=white" />
      <img src="https://img.shields.io/badge/Flask-%237C3AED.svg?style=flat-square&logo=flask&logoColor=white" />
      <img src="https://img.shields.io/badge/Convex-%238B5CF6.svg?style=flat-square&logo=convex&logoColor=white" />
      <img src="https://img.shields.io/badge/Supabase-%23A78BFA.svg?style=flat-square&logo=supabase&logoColor=white" />
    </td>
    <td valign="top" width="50%">
      <h4>🎨 Frontend & Styling</h4>
      <img src="https://img.shields.io/badge/React-%235B21B6.svg?style=flat-square&logo=react&logoColor=white" />
      <img src="https://img.shields.io/badge/Next.js-%237C3AED.svg?style=flat-square&logo=next.js&logoColor=white" />
      <img src="https://img.shields.io/badge/Angular-%238B5CF6.svg?style=flat-square&logo=angular&logoColor=white" />
      <img src="https://img.shields.io/badge/TypeScript-%23A78BFA.svg?style=flat-square&logo=typescript&logoColor=white" />
      <img src="https://img.shields.io/badge/JavaScript-%235B21B6.svg?style=flat-square&logo=javascript&logoColor=white" />
      <img src="https://img.shields.io/badge/Tailwind-%237C3AED.svg?style=flat-square&logo=tailwind-css&logoColor=white" />
      <img src="https://img.shields.io/badge/ShadCN-%238B5CF6.svg?style=flat-square&logo=shadcnui&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <h4>💾 Databases & ORMs</h4>
      <img src="https://img.shields.io/badge/MongoDB-%235B21B6.svg?style=flat-square&logo=mongodb&logoColor=white" />
      <img src="https://img.shields.io/badge/PostgreSQL-%237C3AED.svg?style=flat-square&logo=postgresql&logoColor=white" />
      <img src="https://img.shields.io/badge/MySQL-%238B5CF6.svg?style=flat-square&logo=mysql&logoColor=white" />
      <img src="https://img.shields.io/badge/Prisma-%23A78BFA.svg?style=flat-square&logo=prisma&logoColor=white" />
      <img src="https://img.shields.io/badge/Mongoose-%235B21B6.svg?style=flat-square&logo=mongoose&logoColor=white" />
    </td>
    <td valign="top" width="50%">
      <h4>🐳 DevOps & Architecture</h4>
      <img src="https://img.shields.io/badge/Docker-%235B21B6.svg?style=flat-square&logo=docker&logoColor=white" />
      <img src="https://img.shields.io/badge/Git-%237C3AED.svg?style=flat-square&logo=git&logoColor=white" />
      <img src="https://img.shields.io/badge/Linux-%238B5CF6.svg?style=flat-square&logo=linux&logoColor=white" />
      <img src="https://img.shields.io/badge/Nginx-%23A78BFA.svg?style=flat-square&logo=nginx&logoColor=white" />
      <img src="https://img.shields.io/badge/Clean_Architecture-%237C3AED.svg?style=flat-square" />
      <img src="https://img.shields.io/badge/SOLID-%238B5CF6.svg?style=flat-square" />
    </td>
  </tr>
</table>

---

### 💜 Featured Projects

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3>🛍️ Fusion Store</h3>
      <p>A premium e-commerce platform built with Next.js 16 App Router. Features include a dynamic product customizer studio, real-time drop countdowns, stripe checkout, and role-based stock protection rules.</p>
      <p>
        <img src="https://img.shields.io/badge/Next.js-16-%237C3AED?style=flat-square" />
        <img src="https://img.shields.io/badge/MongoDB-Atlas-%235B21B6?style=flat-square" />
        <img src="https://img.shields.io/badge/Zustand-State-%238B5CF6?style=flat-square" />
      </p>
      <a href="https://github.com/MarwaAshraf1812/fusion-store">View Code →</a>
    </td>
    <td width="50%" valign="top">
      <h3>🤖 Naqla AI</h3>
      <p>A multi-agent recruitment platform leveraging LLM workflows. It parses applications, evaluates technical answers, profiles candidates, and scores applicants asynchronously through a 5-stage pipeline.</p>
      <p>
        <img src="https://img.shields.io/badge/LangGraph.js-Agentic-%237C3AED?style=flat-square" />
        <img src="https://img.shields.io/badge/BullMQ-Redis-%235B21B6?style=flat-square" />
        <img src="https://img.shields.io/badge/Node.js-Backend-%238B5CF6?style=flat-square" />
      </p>
      <a href="https://github.com/MarwaAshraf1812">View Code →</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🕌 Noor</h3>
      <p>A gamified Quran memorization tracker for kids, including custom goal dashboards, rewards/gem systems, interactive quizzes, and visual progress maps.</p>
      <p>
        <img src="https://img.shields.io/badge/Express.js-API-%237C3AED?style=flat-square" />
        <img src="https://img.shields.io/badge/PostgreSQL-DB-%235B21B6?style=flat-square" />
        <img src="https://img.shields.io/badge/React-UI-%238B5CF6?style=flat-square" />
      </p>
      <a href="https://github.com/MarwaAshraf1812">View Code →</a>
    </td>
    <td width="50%" valign="top">
      <h3>💼 Workshop Management System</h3>
      <p>A secure server administration API to organize software workshops, assign homework tasks, host automated quizzes, and calculate real-time student leaderboards.</p>
      <p>
        <img src="https://img.shields.io/badge/Express-REST-%237C3AED?style=flat-square" />
        <img src="https://img.shields.io/badge/Prisma-ORM-%235B21B6?style=flat-square" />
        <img src="https://img.shields.io/badge/Socket.io-Realtime-%238B5CF6?style=flat-square" />
      </p>
      <a href="https://github.com/MarwaAshraf1812">View Code →</a>
    </td>
  </tr>
</table>

---

### 📊 GitHub Dashboard

<div align="center">
  <table border="0" cellpadding="0" cellspacing="0">
    <tr>
      <td>
        <img height="180em" src="https://github-stats-extended.vercel.app/api?username=marwaashraf1812&show_icons=true&hide_border=true&bg_color=1E1B2E&title_color=A78BFA&text_color=C4B5FD&icon_color=8B5CF6" />
      </td>
      <td>
        <img height="180em" src="https://github-stats-extended.vercel.app/api/top-langs/?username=marwaashraf1812&layout=compact&hide_border=true&bg_color=1E1B2E&title_color=A78BFA&text_color=C4B5FD" />
      </td>
    </tr>
    <tr>
      <td colspan="2" align="center">
        <img height="180em" src="https://github-readme-streak-stats.herokuapp.com/?user=marwaashraf1812&hide_border=true&background=1E1B2E&ring=A78BFA&fire=7C3AED&currStreakLabel=C4B5FD&sideLabels=A78BFA&dates=8B5CF6" />
      </td>
    </tr>
  </table>
</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=7C3AED,8B5CF6,A78BFA,C4B5FD&height=80&section=footer" width="100%" />

*"Code with intention, build with love."* 💜

</div>
