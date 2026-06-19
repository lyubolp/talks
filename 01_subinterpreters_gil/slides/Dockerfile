FROM node:latest

RUN npm i -g @slidev/cli

WORKDIR /workspace
VOLUME ["/workspace"]

EXPOSE 3030

CMD ["slidev", "slides.md", "--remote"]

