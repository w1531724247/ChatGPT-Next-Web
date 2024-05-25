docker build -t gpt-web .
docker run -p 3500:3000 -e BASE_URL=https://api.gpt-pro.net -e OPENAI_API_KEY=sk-XIHFJpZ5WGPJooPf6fF0C8C3B64f4e298bE2B6A8C87c2e23 gpt-web
docker tag gpt-web:latest w1531724247/gpt-web:latest
docker push w1531724247/gpt-web:latest