# Use a newer Node.js version (18 LTS)
FROM node:18

# Install pnpm globally
RUN npm install -g pnpm

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies and build the project
RUN pnpm install && pnpm build

# Start the application
CMD ["pnpm", "start"]
