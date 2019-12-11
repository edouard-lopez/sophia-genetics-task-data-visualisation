FROM node:12.2.0-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY yarn.lock /app/
COPY package.json /app/
RUN yarn install --frozen-lockfile

CMD ["yarn", "start"]