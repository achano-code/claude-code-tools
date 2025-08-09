const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: process.env.CLIENT_URL || "http://localhost:3000",
    methods: ["GET", "POST"]
  }
});

const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Whiteboard Server is running');
});

const drawings = new Map();

io.on('connection', (socket) => {
  console.log('User connected:', socket.id);

  socket.emit('loadDrawing', Array.from(drawings.values()));

  socket.on('draw', (data) => {
    drawings.set(data.id, data);
    socket.broadcast.emit('draw', data);
  });

  socket.on('clear', () => {
    drawings.clear();
    socket.broadcast.emit('clear');
  });

  socket.on('disconnect', () => {
    console.log('User disconnected:', socket.id);
  });
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});