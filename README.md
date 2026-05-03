# Flask + MongoDB Website

This is a complete Flask web application with MongoDB integration, ready for hosting.

## 🚀 Quick Start

### Prerequisites
- Python 3.11.9 (already installed)
- MongoDB (local or MongoDB Atlas)

### Installation
All required packages are already installed. If you need to reinstall:
```bash
pip install -r requirements.txt
```

### Configuration
1. Edit `.env` file to configure your MongoDB connection:
   - For local MongoDB: `mongodb://localhost:27017/your_database_name`
   - For MongoDB Atlas: `mongodb+srv://username:password@cluster.mongodb.net/your_database_name`

### Running the Application

#### Development Mode
```bash
python flask_task2
```
Or:
```bash
flask run
```

#### Production Mode
```bash
gunicorn --bind 0.0.0.0:8000 flask_task2:app
```

## 📁 Project Structure
```
.
├── flask_task2          # Main Flask application
├── templates/
│   └── index.html       # Main webpage template
├── .env                 # Environment configuration
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🗄️ MongoDB Setup

### Local MongoDB
1. Install MongoDB Community Server
2. Start MongoDB service
3. Use default connection: `mongodb://localhost:27017/mywebsite`

### MongoDB Atlas (Cloud)
1. Create account at mongodb.com
2. Create a cluster
3. Get connection string from Atlas dashboard
4. Update `MONGO_URI` in `.env` file

## 🔧 Features Included
- ✅ Flask web framework
- ✅ MongoDB integration with PyMongo
- ✅ Flask-PyMongo extension
- ✅ Environment variable management
- ✅ REST API endpoints
- ✅ User creation functionality
- ✅ Production-ready with Gunicorn
- ✅ Form handling with Flask-WTF
- ✅ User authentication ready (Flask-Login)

## 🌐 API Endpoints
- `GET /` - Home page
- `GET /api/test-db` - Test MongoDB connection
- `POST /api/users` - Create new user

## 📝 Usage Examples

### Test Database Connection
Visit `http://localhost:5000` and click "Test MongoDB Connection"

### Create User
Use the web interface or make a POST request:
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

## 🚀 Deployment

### For Production Hosting
1. Set up a VPS (DigitalOcean, AWS, etc.)
2. Install MongoDB or use MongoDB Atlas
3. Clone/upload your code
4. Install dependencies: `pip install -r requirements.txt`
5. Configure environment variables
6. Run with Gunicorn: `gunicorn --bind 0.0.0.0:8000 flask_task2:app`
7. Set up Nginx as reverse proxy (recommended)

### Environment Variables
Create a `.env` file:
```
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
FLASK_ENV=production
```

## 🛠️ Development Tools
- **Flask**: Web framework
- **PyMongo**: MongoDB driver
- **Flask-PyMongo**: Flask + MongoDB integration
- **Gunicorn**: Production WSGI server
- **python-dotenv**: Environment management
- **Flask-WTF**: Form handling
- **Flask-Login**: User authentication
- **bcrypt**: Password hashing