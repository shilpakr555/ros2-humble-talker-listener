# ROS 2 Humble Talker–Listener in Docker

## Project structure

- `talker.py`: publishes `std_msgs/msg/String` messages on `/chatter`.
- `listener.py`: subscribes to `/chatter`.
- `Dockerfile`: builds an Ubuntu 22.04 / ROS 2 Humble environment.

## Prerequisites

- Windows 10/11 with WSL2 and Ubuntu 22.04
- Docker Desktop with WSL integration, or Docker Engine inside WSL
- Git

## Build the image

Run from this project directory in Ubuntu/WSL:

```bash
docker build -t ros2-humble-demo:1.0 .
```

## Start a persistent container with the repository mounted

```bash
docker run -d --name ros2-demo \
  -v "$PWD:/workspace" \
  -w /workspace \
  ros2-humble-demo:1.0 sleep infinity
```

The `-v "$PWD:/workspace"` option shares the current repository directory with the container.
Edits made to the files in the host repository are immediately visible at `/workspace`.

## Terminal 1: listener

```bash
docker exec -it ros2-demo bash
source /opt/ros/humble/setup.bash
cd /workspace
python3 listener.py
```

## Terminal 2: talker

Open another Ubuntu/WSL terminal:

```bash
docker exec -it ros2-demo bash
source /opt/ros/humble/setup.bash
cd /workspace
python3 talker.py
```

## Verify ROS graph

In a third terminal:

```bash
docker exec -it ros2-demo bash
source /opt/ros/humble/setup.bash
ros2 node list
ros2 topic list
ros2 topic echo /chatter
```

Expected nodes: `/talker` and `/listener`.
Expected topic: `/chatter`.

## Prove host-to-container source sharing

On Windows, edit `talker.py` in the repository (for example, change the message prefix).
Save it, then restart the talker process inside the container. The changed message should appear.
No image rebuild is needed for Python source changes.

## Git workflow

```bash
git init
git add Dockerfile talker.py listener.py README.md .gitignore
git commit -m "Add ROS 2 Humble talker listener demo"
```

After editing:

```bash
git add talker.py listener.py
git commit -m "Update ROS 2 nodes"
```

## Cleanup

```bash
docker stop ros2-demo
docker rm ros2-demo
```

To remove the image too:

```bash
docker rmi ros2-humble-demo:1.0
```

## Important

Run both nodes in the same container for the first demonstration. This avoids cross-container DDS discovery and networking complications.
