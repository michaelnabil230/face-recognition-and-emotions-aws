# Face Recognition and Emotion Detection with AWS

This project demonstrates how to perform face recognition and emotion detection using Amazon Web Services (AWS) and Python. The application leverages the power of AWS Rekognition service to analyze facial features and emotions in images.

## Prerequisites

Before running the project, make sure you have the following:

1. Python 3.x installed on your machine.
2. AWS account credentials with access to the Rekognition service. If you don't have one, create a new account on the AWS website and generate access keys.

## Setup

1. Clone the repository or download the project files to your local machine.
2. Install the required Python dependencies by running the following command in your terminal:

```bash
   pip install -r requirements.txt
```

3. Configure your AWS credentials by either setting environment variables or using the AWS CLI. Make sure the credentials provide access to the Rekognition service.

## Usage

1. Place the images you want to analyze in the `images` directory of the project.
2. Run the following command in your terminal to start the application:

```bash
   streamlit run main.py
```

3. The application will analyze the images using the AWS Rekognition service and display the recognized faces and detected emotions in the terminal.

## Customization

The project can be customized according to your needs. Here are a few suggestions:

- **Image Sources**: You can modify the `images` directory or integrate the project with other data sources such as webcams or live video streams.
- **Output Format**: Currently, the application displays the results in the terminal. You can modify the code to store the results in a database or generate visual reports.
- **Additional Features**: AWS Rekognition provides various other capabilities like age estimation, gender detection, and celebrity recognition. You can explore these features and extend the project accordingly.

## Limitations

- The project requires a stable internet connection to access the AWS Rekognition service.
- The accuracy of face recognition and emotion detection may vary depending on the quality of the images and the complexity of the emotions displayed.

## Contributing

Contributions are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project was inspired by the capabilities of AWS Rekognition and various open-source face recognition libraries.

## Resources

- [AWS Rekognition Documentation](https://docs.aws.amazon.com/rekognition/index.html)
- [Python SDK for AWS (Boto3) Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)