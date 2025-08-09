FROM node:22-alpine
WORKDIR /src

RUN npm install -g npm
RUN npm install -g @anthropic-ai/claude-code