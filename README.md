# 💬 ChatFlow

**A real-time multi-client chat application built with Python sockets**

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [Contact](#contact)

## 🎯 Overview

ChatFlow is a robust, real-time chat application that enables multiple clients to communicate through a central server. Built using Python's socket programming, it supports department-based user identification, message broadcasting, and comprehensive logging functionality.

## ✨ Features

### 🔥 Core Features
- **Real-time messaging** - Instant message delivery between clients
- **Multi-client support** - Unlimited concurrent users
- **Department-based identification** - Users identified by department and name
- **Message persistence** - All conversations logged to `chat_log.txt`
- **User management** - View connected users with `/list` command
- **Thread-safe operations** - Concurrent client handling with proper synchronization

### 🛡️ Reliability Features
- **Graceful disconnection handling** - Automatic cleanup when clients leave
- **Error recovery** - Robust error handling for network issues
- **Timestamped messages** - All messages include precise timestamps
- **Connection monitoring** - Real-time connection status updates

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     Client 1    │    │     Client 2    │    │     Client N    │
│  (Department-   │    │  (Department-   │    │  (Department-   │
│     Name)       │    │     Name)       │    │     Name)       │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────▼──────────────┐
                    │        ChatFlow Server     │
                    │                           │
                    │  • Message Broadcasting   │
                    │  • Client Management     │
                    │  • Logging System        │
                    │  • Thread Management     │
                    └───────────────────────────┘
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses built-in libraries)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/Mamoonalatif/chatflow.git
cd chatflow

# No additional installation required!
```

## 📖 Usage

### Step 1: Start the Server
```bash
python server.py
```
**Expected Output:**
```
[STARTING] Server listening on 127.0.0.1:65432
```

### Step 2: Connect Clients
In separate terminal windows:
```bash
python client.py
```

### Step 3: Setup Your Profile
```
Enter your department: Engineering
Enter your name: Alice
```

### Step 4: Start Chatting!
```
[SERVER] Engineering-Alice joined the chat.
Hello everyone! 👋
/list
[SERVER] Connected users:
- Engineering-Alice
- Sales-Bob
- HR-Carol
```

## 🎮 Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/list` | Display all connected users | `/list` |
| `Ctrl+C` | Exit the client | - |
| Regular text | Send message to all users | `Hello everyone!` |

## 📁 Project Structure

```
chatflow/
├── 📄 server.py          # Main server application
├── 📄 client.py          # Client application
├── 📄 README.md          # Project documentation
├── 📄 chat_log.txt       # Message logs (auto-generated)
├── 📄 .gitignore         # Git ignore rules
```

## 🔧 Technical Details

### Server Specifications
- **Protocol:** TCP/IP Socket Programming
- **Host:** 127.0.0.1 (localhost)
- **Port:** 65432
- **Architecture:** Multi-threaded server
- **Concurrency:** Thread-per-client model

### Key Technologies
- **Socket Programming** - TCP communication
- **Threading** - Concurrent client handling
- **File I/O** - Message logging system
- **Synchronization** - Thread-safe operations with locks

### Performance Features
- ⚡ **Low latency messaging** - Direct socket communication
- 🔄 **Automatic reconnection handling** - Graceful error recovery
- 📊 **Real-time user tracking** - Live connection monitoring
- 💾 **Persistent logging** - Complete chat history

## 🛠️ Development

### Running Tests
```bash
# Test server functionality
python server.py

# In separate terminals, test multiple clients
python client.py  # Terminal 1
python client.py  # Terminal 2
python client.py  # Terminal 3
```

### Configuration
Modify connection settings in both files:
```python
HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Server port
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Contributions
- 🌐 Web-based frontend
- 🔐 User authentication
- 📱 Mobile client support
- 🎨 GUI interface
- 🔒 Message encryption
- 📊 Analytics dashboard


## 🙋‍♂️ Contact

**Mamoona Latif**
- GitHub: [@Mamoonalatif](https://github.com/Mamoonalatif)
- Project Link: [https://github.com/Mamoonalatif/chatflow](https://github.com/Mamoonalatif/chatflow)

