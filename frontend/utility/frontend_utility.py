"""
This file contains functions for building and updating interface elements.
"""
import streamlit as st
from PIL import Image

from frontend.utility.markdown_utility import Status

RESOURCES_DIR = "./resources/"


def display_response(is_successful: bool, response_status: Status, responses: list):
    """
    Displays the given responses based on success flag.
    Args:
        is_successful: indicating whether the response is a success or error.
        responses: A list of strings containing the markdown responses to display.
        response_status: status of the response, either SUCCESS, WARNING, INFO, or ERROR.
    """
    placeholder = st.empty()
    if is_successful and response_status != Status.ERROR:
        # Join responses with line breaks
        markdown_response = "\n<br>".join(responses)
        match response_status.name:
            case Status.SUCCESS.name:
                placeholder.markdown(markdown_response, unsafe_allow_html=True)
            case Status.WARNING.name:
                placeholder.warning(markdown_response, icon="⚠️")
            case Status.INFO.name:
                placeholder.info(markdown_response, icon="ℹ️")
        st.session_state.messages.append(
            {"role": "assistant", "content": "\n".join(responses)})
    else:
        st.session_state.messages.append(
            {"role": "assistant", "content": responses})
        placeholder.error(responses)


def load_ui_from_html():
    """Loads and displays the UI from the specified HTML file."""
    try:
        with open(RESOURCES_DIR + "style.html", 'r') as file:
            html = file.read()
        st.write(html, unsafe_allow_html=True)
    except FileNotFoundError as e:
        print(f"File not found: {e}")


def load_custom_avatar(filename: str) -> Image:
    """Loads a custom avatar image from the specified file.
    Args:
        filename: The name of the avatar image file.
    """
    avatar_file_path = RESOURCES_DIR + filename
    try:
        avatar = Image.open(avatar_file_path)
    except FileNotFoundError as e:
        print(f"Avatar image not found: {avatar_file_path} \n{e}")
        return None
    return avatar
