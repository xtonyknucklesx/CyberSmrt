# Use the official Node.js image as the base
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app's code
COPY . .

# Set the environment variable for the default environment (can be overridden)
ARG NODE_ENV=production
ENV NODE_ENV=$NODE_ENV

# Run different commands based on the environment
# For production, build the app; for development, run the development server
RUN if [ "$NODE_ENV" = "production" ]; then \
      npm run build; \
    fi

# Expose the port based on the environment
EXPOSE 3000

# The default command will be overridden in docker-compose.yml files for different environments
CMD ["npm", "start"]