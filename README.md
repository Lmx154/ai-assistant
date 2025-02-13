# Minimalist AI Chatbot

A simple chat interface built with Next.js, FastAPI, and TailwindCSS that demonstrates a basic AI assistant implementation.

## Features

- Clean, minimalist UI
- Real-time chat interface
- Conversation starters
- Responsive design
- REST API backend

## Prerequisites

- Node.js 16+ and npm
- Python 3.11+
- Conda package manager

## Setup Instructions

### Backend Setup

1. Create and activate Conda environment:
```bash
conda env create -f backend/environment.yml
conda activate chatbot-env
```

2. Start the FastAPI server:
```bash
cd backend
uvicorn main:app --reload --port 8000
```

The backend server will run on http://localhost:8000

### Frontend Setup

1. Install Node.js dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

## Usage

1. Ensure both backend and frontend servers are running
2. Open http://localhost:3000 in your browser
3. Start chatting using:
   - The text input at the bottom
   - Pre-defined conversation starters
   - "New Chat" button to reset the conversation

## Project Structure

```
minimalist-chatbot/
├── app/                 # Next.js frontend pages
├── components/          # React components
├── backend/            # FastAPI backend
│   ├── main.py         # Main API endpoints
│   └── environment.yml # Conda environment config
└── README.md
```

## Development

- Frontend modifications can be made in the `components` and `app` directories
- Backend logic is in `backend/main.py`
- Styling uses TailwindCSS

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT
