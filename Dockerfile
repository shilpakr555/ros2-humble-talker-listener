# ROS 2 Humble on Ubuntu 22.04
FROM ros:humble-ros-base

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-humble-std-msgs \
    python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Source ROS automatically in interactive bash shells.
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

CMD ["bash"]
