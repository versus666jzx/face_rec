import streamlit as st
from streamlit.elements.camera_input import CameraInputMixin, CameraInputSerde
from typing import Optional, Key



class VideoStream(CameraInputMixin):
    def _camera_input(
        self,
        label: str,
        key: Optional[Key] = None,
        help: Optional[str] = None,
        on_change: Optional[WidgetCallback] = None,
        args: Optional[WidgetArgs] = None,
        kwargs: Optional[WidgetKwargs] = None,
        *,  # keyword-only arguments:
        disabled: bool = False,
        label_visibility: LabelVisibility = "visible",
        ctx: Optional[ScriptRunContext] = None,
    ) -> SomeUploadedSnapshotFile:
        key = to_key(key)
        check_callback_rules(self.dg, on_change)
        check_session_state_rules(default_value=None, key=key, writes_allowed=False)
        maybe_raise_label_warnings(label, label_visibility)

        camera_input_proto = CameraInputProto()
        camera_input_proto.label = label
        camera_input_proto.form_id = current_form_id(self.dg)

        serde = CameraInputSerde()
        return serde


def hide_footer_and_menu():
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)