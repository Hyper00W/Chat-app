# Python Real-Time Chat Application

A simple **terminal-based real-time chat application** built with **Python**, demonstrating **client-server architecture**, **socket programming**, and **multithreading**. Multiple clients can connect to a server and exchange messages in real-time.

---

## Features

- Multi-client support
- Real-time message broadcasting
- Graceful handling of client disconnections
- Built entirely with Python’s standard library (`socket` and `threading`)
- Easy to run and extend

---

## Technologies Used

- Python 3.x
- `socket` — for TCP network communication
- `threading` — to handle multiple clients concurrently

---

## How It Works

1. **Server**:  
   - Listens for incoming client connections.
   - Accepts clients and starts a dedicated thread for each.
   - Broadcasts messages received from one client to all others.

2. **Client**:  
   - Connects to the server.
   - Spawns a thread to receive messages so the user can simultaneously send messages.
   - Sends user-typed messages to the server.


git clone https://github.com/Hyper00W/Chat-app.git
)
cd chat-app
