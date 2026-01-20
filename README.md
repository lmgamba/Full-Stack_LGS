# 🎓 Full-Stack Development Bootcamp Portfolio

A comprehensive collection of projects developed during my Full-Stack Developer Bootcamp, showcasing progressive learning from frontend fundamentals to backend API development.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)


## 🎯 Projects Overview


## 📊 Project Overview

| Project | Technologies | Key Highlights |
|---------|--------------|----------------|
| **🛒 E-commerce with Testing** | [![My Skills](https://skillicons.dev/icons?i=js,jest,html,css)](https://skillicons.dev) | Unit testing, Filter logic, Clean architecture |
| **⚡ REST API with FastAPI** | [![My Skills](https://skillicons.dev/icons?i=python,fastapi,mysql)](https://skillicons.dev)  | Full CRUD, Authentication, Database design |
| **📱 Responsive Landing Page** | [![My Skills](https://skillicons.dev/icons?i=vscode,html,css)](https://skillicons.dev) | Mobile-first, Responsive design |
| **🅰️ Angular Application** | [![My Skills](https://skillicons.dev/icons?i=nodejs,angular,typescript)](https://skillicons.dev) | Component architecture, RxJS, Full-stack planning |

---

## 📁 Repository Structure
### 🧭 Learning Path Progression
📦 full-stack_LGS/

├── 📂 1_static_front_hamburgueseria/ # Module 1: HTML/CSS Foundations

├── 📂 2_e-commerce_front_with_JS/ # Module 2: JavaScript & DOM Manipulation

├── 📂 3_CRUD_api_mysql_python/ # Module 3: Backend Development

└── 📂 4_angular/ # Module 4: Modern Framework (In Progress)

---
### 1. Static Restaurant Website - "Rovers Hamburgers"
**Folder:** `1_static_front_hamburgueseria/`  
**Technologies:** HTML5, CSS3, Flexbox, Responsive Design

**Key Features:**
**📱 Mobile-First Design** Fully responsive design (mobile, tablet, desktop)
**🎨 CSS Architecture**  | CSS Flexbox-based system
**🍔 Interactive Navigation** | Iimplementing a hamburger menu for mobile


## 2. 🛒 Interactive E-commerce with JavaScript Testing

**📁 Folder:** `2_e-commerce_front_with_JS/`  
**🏷️ Status:** ✅ Production Ready  
**🔧 Technologies:** JavaScript (ES6+), Jest, DOM API, CSS3, HTML5

### 🎯 Key Features

**🔍 Real-time Product Filtering** | Dynamic filtering by price, name, and category  
**🧪 Unit Testing with Jest** | Comprehensive test suite for business logic  
**🖼️ Dynamic DOM Rendering** | JavaScript-generated product cards from JSON data   
**🏗️ Clean Architecture** | Separation of logic (logic.js) and presentation (script.js)  
**📱 Responsive UI** | CSS Flexbox/Grid for all device sizes  

### 📈 Technical Highlights

```javascript
// Example of tested business logic
✅ filtrar_producto() - Filter function with 100% test coverage
✅ destacar() - Product starring system with edge case handling
✅ 15+ unit tests covering normal/edge cases
```
---

### 3. Complete REST API with FastAPI & MySQL
**Folder:** `3_CRUD_api_mysql_python/`  
**Technologies:** Python, FastAPI, MySQL, SQLAlchemy, Pydantic

**Key Features:**
- Complete CRUD operations for products with RESTful API  
**✅ Input Validation** |  Pydantic and ModelBase Classes
- Advanced filtering (price ranges, text search)  
**📊 Advanced Query System** | Relational database design (User ↔ Product)  
**🔐 Full Authentication** | Dependencies and Authentication with password hashing
**:warning:Proper error handling** and HTTP status codes  

---

### 4. Angular Practice (In Development)
**Folder:** `4_angular/`  
**Status:** Actively learning and building

**Current Focus:**
- TypeScript
- Angular component architecture
- Services and dependency injection
- Planning to integrate previous projects into a full-stack application


## 🛠️ Technical Skills Demonstrated

### Frontend Development
- **HTML/CSS:** Semantic markup, responsive design, CSS Flexbox
- **JavaScript:** ES6+ syntax, DOM manipulation, event handling, array methods
- **Version Control:** Git and GitHub for project management

### Backend Development
- **Python:** Core language features, data structures, classes, packages gestion
- **FastAPI:** Modern web framework, model base, authentication, automatic documentation
- **MySQL:** Database design, relational modeling, query writing
- **API Design:** REST principles, endpoint structure, dependency, error handling

### Development Practices
- Project organization and architecture
- Code readability and maintainability
- Progressive enhancement approach
- Documentation and comments

---
## 🚀 How to Run These Projects

Each project folder contains its own setup instructions. Generally:

### For Frontend Projects (1 & 2):
```bash
# Just open the HTML file in a browser
open index.html
```
### For Backend Project (3):
```bash
#cd 3_CRUD_api_mysql_python/
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
# Configure .env file with database credentials
uvicorn app.main:app --reload
```
---

### 🔮 :soon: **Next Steps**
1. Complete Angular module and integrate with existing backend
2. Add testing to all projects (Jest done for frontend :white_check_mark: , pytest for backend tbd)
3. Containerize applications with Docker
4. Deploy projects to demonstrate live applications

### :telephone_receiver: **Contact & Links**
- GitHub: [![Static Badge](https://img.shields.io/badge/my-github-white)](https://github.com/lmgamba)
- LinkedIn: [![text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/laura-gamba-sanchez/)
- Other project you might like: [Data-driven Dashboard](https://repositorio.uniandes.edu.co/entities/publication/bdc17c51-a11d-45a4-8acf-1c88cd7b4c37)


---
*This repository represents my hands-on learning journey through a Full-Stack Development Bootcamp in UpgradeHub. Each project reflects the skills and concepts I've mastered at different stages of my training.*

*Note: These are educational projects developed as part of a structured bootcamp curriculum. The design specifications and and learning objectives were provided; implementation demonstrates practical application of concepts and technical problem-solving skills as part of the learning process.*
