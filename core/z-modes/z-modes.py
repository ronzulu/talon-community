from typing import Dict
from talon import Module, actions

mod = Module()

global_next_pre_phrase = ""
global_next_format = ""
global_subsequent_pre_phrase = ""
global_subsequent_format = ""

@mod.action_class
class ZModeActions:
    def rz_set_next_format(pre_phrase: str, format: str):
        "Set the format used by following calls to rz_add"
        global global_next_pre_phrase, global_next_format
        global global_subsequent_pre_phrase, global_subsequent_format

        global_next_pre_phrase = pre_phrase
        global_next_format = format
        global_subsequent_pre_phrase = pre_phrase
        global_subsequent_format = format

    def rz_set_subsequent_format(pre_phrase: str, format: str):
        "Set the format used by following calls to rz_add"
        global global_subsequent_pre_phrase, global_subsequent_format

        global_subsequent_pre_phrase = pre_phrase
        global_subsequent_format = format

    def rz_add(text: str):
        "Inserts the supplied text, formatted as per last call to rz_set_format"
        global global_next_pre_phrase, global_next_format
        global global_subsequent_pre_phrase, global_subsequent_format
        
        if global_next_pre_phrase:
            actions.insert(global_next_pre_phrase)

        actions.user.insert_formatted(text, global_next_format)
        global_next_format = global_subsequent_format
        global_next_pre_phrase = global_subsequent_pre_phrase
