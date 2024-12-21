# 🤖 Face Detection App with OpenCV 📷

This Python application utilizes **OpenCV** to perform **real-time face detection** using a webcam. The application uses the **Haar Cascade Classifier** (`haarcascade_frontalface_default.xml`) to detect faces in a live video feed.

## 🚀 Features
- 🔍 **Real-time face detection** using webcam.
- 📸 Draws rectangles around detected faces.
- 🖥️ Outputs whether a face was detected or not after exiting.
- ⏹️ Press **'q'** to quit the webcam feed at any time.

## ⚙️ Requirements
- Python 3.x
- **OpenCV** library (`opencv-python`)
- **NumPy** library (required for OpenCV)

## 📦 Installation
To run the application, you'll need to install the required Python libraries.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/face-detection-app.git
   cd face-detection-app
   ```

2. **Install dependencies**:
   ```bash
   pip install opencv-python numpy
   ```

3. **Download the Haar Cascade Classifier XML file**:
   Ensure that the `haarcascade_frontalface_default.xml` file is in the same directory as the script. You can download it from the [official OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## 🏃‍♂️ Usage

1. **Run the script**:
   - Open a terminal/command prompt in the project directory.
   - Run the Python script:
     ```bash
     python app.py
     ```

2. The webcam feed will open, and the application will detect faces in real-time.

3. Press **'q'** to quit the application at any time.

## 📜 Output
When the application exits, it will print a message in the terminal:
- "A face was detected during the session." if a face was detected.
- "No face was detected during the session." if no face was detected.

## 🛠️ Example

Once you run the script and the webcam is active, it will start detecting faces. Here's what the output will look like in the terminal:
```
A face was detected during the session.
```
or
```
No face was detected during the session.
```

## 🤝 Contributing

Feel free to open issues or submit pull requests if you'd like to improve this project! 🚀

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


