import streamlit as st
from PIL import Image
import boto3
import os

rekognition_client = boto3.client('rekognition')


def main():
    st.set_page_config(
        page_title="Face Recognition and Emotion Detection",
        layout="wide",
    )
    st.title('Face Recognition and Emotion Detection')

    col1, col2 = st.columns(2)

    target_image = col1.file_uploader(
        'Upload target face',
        type=['png', 'jpg', 'jpeg'],
    )
    source_image = col2.file_uploader(
        'Upload source face',
        type=['png', 'jpg', 'jpeg'],
    )

    if target_image is not None and source_image is not None:
        target_image_details = {
            'type': target_image.type,
            'name': target_image.name,
            'size': target_image.size
        }
        source_image_details = {
            'type': source_image.type,
            'name': source_image.name,
            'size': source_image.size
        }

        col1, col2 = st.columns(2)

        col1.header("Source")
        col1.image(Image.open(source_image))
        col1.write(source_image_details)

        col2.header("Target")
        col2.image(Image.open(target_image))
        col2.write(target_image_details)

        source_name = write_image(source_image)
        target_name = write_image(target_image)

        compare_faces(source_name, target_name)

        delete_file(source_name)
        delete_file(target_name)


def write_image(image):
    image_name = 'temp/' + image.name

    with open(image_name, 'wb') as f:
        f.write(image.getbuffer())

    return image_name


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


def compare_faces(source_file, target_file):
    with open(source_file, 'rb') as source_image, open(target_file, 'rb') as target_image:
        response = rekognition_client.compare_faces(
            SimilarityThreshold=80,
            SourceImage={'Bytes': source_image.read()},
            TargetImage={'Bytes': target_image.read()}
        )
    
    st.write(response)

    face_matches = response['FaceMatches']
    st.text("Face matches: " + str(len(face_matches)))

    if face_matches:
        similarity = str(face_matches[0]['Similarity'])
        st.text('The face matches with ' + similarity + '% confidence')

        analyze_emotions(target_file)


def analyze_emotions(source_file):
    with open(source_file, 'rb') as target_image:
        response = rekognition_client.detect_faces(
            Image={'Bytes': target_image.read()},
            Attributes=['EMOTIONS']
        )

    response = response['FaceDetails'][0]

    for emotion in response['Emotions']:
        st.text(emotion['Type'] + ' ')
        st.progress(int(emotion['Confidence']))


if __name__ == "__main__":
    main()
