# BlogPilot - AI-Powered Blogging Platform

## 🎥 Demo

Watch the project demo: [BlogPilot Demo Video](https://www.loom.com/share/76e07205c28c4520a1b63e007fe44c96?sid=7a3d9d88-d8ba-4c46-9a10-9278cfd42b2a)

## 🌐 Live Demo

Try the live application: [BlogPilot Live Demo](https://blogpilot-backend-production.up.railway.app/docs)

## 📝 Description

BlogPilot is a modern, AI-powered blogging platform built with FastAPI and PostgreSQL. It provides a robust backend API for creating, managing, and summarizing blog posts, with integrated AI capabilities using the Gemini API.

## ✨ Features

### Core Features

- **User Authentication**

  - JWT-based authentication system
  - Secure user registration and login
  - Protected routes for authenticated users

- **Blog Management**

  - Create, read, update, and delete blog posts
  - Public access to view all blogs
  - Filter and search blogs by keywords, tags, or author
  - User-specific blog post management

- **AI Integration**
  - Automatic blog post summarization using Gemini API
  - Intelligent content analysis
  - Concise summary generation

### Technical Features

- Asynchronous request handling with AsyncIO
- Strong data validation using Pydantic
- PostgreSQL database integration
- RESTful API design
- Secure password hashing
- JWT token-based authentication

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **Authentication**: JWT
- **AI Integration**: Gemini API
- **Data Validation**: Pydantic
- **Async Support**: AsyncIO
- **Password Hashing**: bcrypt

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## 🚀 Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/BlogPilot.git
   cd BlogPilot
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r app/requirements.txt
   ```

4. **Environment Setup**
   Create a `.env` file in the `app` directory with the following variables:

   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/blogpilot
   SECRET_KEY=your_secret_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. **Database Setup**

   - Create a PostgreSQL database named 'blogpilot'
   - Run the database initialization script:

   ```bash
   python app/create_tables.py
   ```

6. **Start the Server**
   ```bash
   python app/main.py
   ```

## 📁 Project Structure

```
app/
├── main.py              # Application entry point
├── requirements.txt     # Project dependencies
├── dependencies.py      # FastAPI dependencies
├── create_tables.py     # Database initialization
├── jwtTokens.py         # JWT authentication
├── hashing.py          # Password hashing
├── gemini.py           # AI integration
├── .env                # Environment variables
├── schemas/            # Pydantic models
├── models/             # Database models
├── db/                 # Database configuration
└── routers/            # API endpoints
    ├── blog.py         # Blog-related routes
    ├── authentication.py # Auth routes
    └── user.py         # User management routes
```

## 🔑 API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout

### Blog Posts

- `GET /blogs` - Get all blog posts
- `GET /blogs/{id}` - Get specific blog post
- `POST /blogs` - Create new blog post
- `PUT /blogs/{id}` - Update blog post
- `DELETE /blogs/{id}` - Delete blog post
- `GET /blogs/search` - Search blogs
- `POST /blogs/summarize` - Generate AI summary

### Users

- `GET /users/me` - Get current user profile
- `PUT /users/me` - Update user profile

## 🔒 Security Features

- JWT-based authentication
- Password hashing using bcrypt
- Protected routes for authenticated users
- Secure environment variable management

## 🤖 AI Integration

The platform uses Google's Gemini API for generating concise summaries of blog posts. The AI integration is implemented in `gemini.py` and can be accessed through the `/blogs/summarize` endpoint.

## 📝 Notes

- All API endpoints follow REST principles
- Asynchronous operations are used for better performance
- Strong data validation ensures data integrity
- Comprehensive error handling is implemented