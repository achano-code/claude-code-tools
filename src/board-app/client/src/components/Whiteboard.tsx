import React, { useEffect, useRef, useState } from 'react';
import { io, Socket } from 'socket.io-client';

interface DrawData {
  id: string;
  x: number;
  y: number;
  prevX?: number;
  prevY?: number;
  color: string;
  lineWidth: number;
  type: 'draw' | 'start';
}

const Whiteboard: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const contextRef = useRef<CanvasRenderingContext2D | null>(null);
  const socketRef = useRef<Socket | null>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [color, setColor] = useState('#000000');
  const [lineWidth, setLineWidth] = useState(2);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const context = canvas.getContext('2d');
    if (!context) return;

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight - 60;
    
    context.lineCap = 'round';
    context.strokeStyle = color;
    context.lineWidth = lineWidth;
    contextRef.current = context;

    const serverUrl = process.env.REACT_APP_SERVER_URL || 'http://localhost:5000';
    const socket = io(serverUrl);
    socketRef.current = socket;

    socket.on('draw', (data: DrawData) => {
      drawLine(data);
    });

    socket.on('loadDrawing', (drawings: DrawData[]) => {
      drawings.forEach(drawLine);
    });

    socket.on('clear', () => {
      clearCanvas();
    });

    const handleResize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight - 60;
      context.lineCap = 'round';
      context.strokeStyle = color;
      context.lineWidth = lineWidth;
    };

    window.addEventListener('resize', handleResize);

    return () => {
      socket.disconnect();
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  useEffect(() => {
    const context = contextRef.current;
    if (context) {
      context.strokeStyle = color;
      context.lineWidth = lineWidth;
    }
  }, [color, lineWidth]);

  const drawLine = (data: DrawData) => {
    const context = contextRef.current;
    if (!context) return;

    const prevStrokeStyle = context.strokeStyle;
    const prevLineWidth = context.lineWidth;

    context.strokeStyle = data.color;
    context.lineWidth = data.lineWidth;

    if (data.type === 'start') {
      context.beginPath();
      context.moveTo(data.x, data.y);
    } else if (data.prevX !== undefined && data.prevY !== undefined) {
      context.beginPath();
      context.moveTo(data.prevX, data.prevY);
      context.lineTo(data.x, data.y);
      context.stroke();
    }

    context.strokeStyle = prevStrokeStyle;
    context.lineWidth = prevLineWidth;
  };

  const startDrawing = (e: React.MouseEvent<HTMLCanvasElement>) => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    setIsDrawing(true);

    const context = contextRef.current;
    if (context) {
      context.beginPath();
      context.moveTo(x, y);
    }

    const drawData: DrawData = {
      id: Date.now().toString(),
      x,
      y,
      color,
      lineWidth,
      type: 'start'
    };

    socketRef.current?.emit('draw', drawData);
  };

  const draw = (e: React.MouseEvent<HTMLCanvasElement>) => {
    if (!isDrawing) return;

    const canvas = canvasRef.current;
    const context = contextRef.current;
    if (!canvas || !context) return;

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const prevX = e.clientX - rect.left - (e.movementX || 0);
    const prevY = e.clientY - rect.top - (e.movementY || 0);

    context.lineTo(x, y);
    context.stroke();

    const drawData: DrawData = {
      id: Date.now().toString(),
      x,
      y,
      prevX,
      prevY,
      color,
      lineWidth,
      type: 'draw'
    };

    socketRef.current?.emit('draw', drawData);
  };

  const stopDrawing = () => {
    setIsDrawing(false);
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const context = contextRef.current;
    if (!canvas || !context) return;

    context.clearRect(0, 0, canvas.width, canvas.height);
  };

  const handleClear = () => {
    clearCanvas();
    socketRef.current?.emit('clear');
  };

  return (
    <div>
      <div className="toolbar">
        <input
          type="color"
          value={color}
          onChange={(e) => setColor(e.target.value)}
        />
        <label>
          線の太さ: {lineWidth}px
          <input
            type="range"
            min="1"
            max="20"
            value={lineWidth}
            onChange={(e) => setLineWidth(Number(e.target.value))}
          />
        </label>
        <button onClick={handleClear}>クリア</button>
      </div>
      <div className="canvas-container">
        <canvas
          ref={canvasRef}
          onMouseDown={startDrawing}
          onMouseMove={draw}
          onMouseUp={stopDrawing}
          onMouseLeave={stopDrawing}
        />
      </div>
    </div>
  );
};

export default Whiteboard;