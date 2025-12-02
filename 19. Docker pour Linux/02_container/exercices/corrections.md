## Exercice 01

```bash
docker run alpine echo "Hello from container"
```

## Exercice 02

## 2.1

```bash
docker run -d --name test-nginx nginx 
docker ps
```

## 2.2

```bash
docker exec test-nginx ls -l
```

## 2.3

```bash
docker logs test-nginx
```

## Exercice 03

```bash
docker run -d --cap-drop=ALL --read-only alpine
```
