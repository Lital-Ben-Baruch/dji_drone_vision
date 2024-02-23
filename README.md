# DJI Drone Vision

## Introduction
This repository contains code for programming the DJI Tello RYZE drone for computer vision applications. It is designed to enable the drone to perform tasks such as surveillance, object detection, tracking, and other vision-related projects. The repository includes scripts, configuration files, and resources necessary for implementing computer vision algorithms on the DJI Tello RYZE drone platform.

## Features
- Control and interface with the DJI Tello RYZE drone for various computer vision applications.
- Examples and resources for common vision tasks.

## Getting Started

### Prerequisites
- DJI Tello RYZE drone
- Python version 3.12.1

### Installation
To get started with the project, you need to install the necessary libraries in your Python environment:

1. Install `djitellopy`:
   ```shell
   conda install djitellopy
   # or
   pip install djitellopy
   ```

2. Update or install OpenCV:
   ```shell
   conda update opencv
   # or
   pip install --upgrade opencv-python
   ```

### DJI App Download
To download the DJI App for the drone, visit the following link:
[Download DJI App for Android](https://service-adhoc.dji.com/download/app/android/ba88a046-6f7e-4cbb-a969-27851eb4bbf5)

## License
### Project License
The code in this repository is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for the full license text.

### Third-Party Libraries License
This project uses the `djitellopy` library, which is licensed under the MIT License. The license details for `djitellopy` can be found in the [licenses/djitellopy_LICENSE](licenses/djitellopy_LICENSE) file within this repository.

## Acknowledgments
- Special thanks to DAMIÀ FUENTES ESCOTÉ for the `djitellopy` library.

## Contributing
If you would like to contribute to this project, please feel free to make a pull request.

## Contact
For any queries or issues, please open an issue on the GitHub repository issue tracker.
