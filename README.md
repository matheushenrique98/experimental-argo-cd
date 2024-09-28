## Local Dockers Workers

### -- 1 --
### podman build -f deploy/Dockerfile -t experimental-argo-cd-backend .
### podman run -p 8000:8000 experimental-argo-cd-backend