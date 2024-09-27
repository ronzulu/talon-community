from typing import Dict
from talon import Module, actions

mod = Module()

global_next_format = ""
global_subsequent_format = ""

@mod.action_class
class ZModeActions:
    def rz_set_format(next_format: str, subsequent_format: str = None):
        "Set the format used by following calls to rz_add"
        global global_next_format, global_subsequent_format
        global_next_format = next_format
        global_subsequent_format = subsequent_format or next_format

    def rz_add(text: str):
        "Inserts the supplied text, formatted as per last call to rz_set_format"
        global global_next_format, global_subsequent_format
        actions.user.insert_formatted(text, global_next_format)
        global_next_format = global_subsequent_format
