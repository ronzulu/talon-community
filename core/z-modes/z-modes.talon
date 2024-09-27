hello out there: "Shalom world90214!!"

add <user.text>$: user.rz_add(user.text)

zed one:
    user.rz_set_next_format("", "PUBLIC_CAMEL_CASE")
zed one l:
    user.rz_set_next_format("", "PRIVATE_CAMEL_CASE")
    user.rz_set_subsequent_format("", "PUBLIC_CAMEL_CASE")
zed one l s:
    user.rz_set_next_format(" ", "PRIVATE_CAMEL_CASE")
    user.rz_set_subsequent_format("", "PUBLIC_CAMEL_CASE")

zed two:
    user.rz_set_next_format("", "NOOP")
    user.rz_set_subsequent_format(" ", "NOOP")

zed three:
    user.rz_set_next_format("", "CAPITALIZE_ALL_WORDS")
    user.rz_set_subsequent_format(" ", "CAPITALIZE_ALL_WORDS")
zed three s:
    user.rz_set_next_format(" ", "CAPITALIZE_ALL_WORDS")
    user.rz_set_subsequent_format(" ", "CAPITALIZE_ALL_WORDS")

zed four:
    user.rz_set_next_format("", "ALL_CAPS")
    user.rz_set_subsequent_format(" ", "ALL_CAPS")
zed four s:
    user.rz_set_next_format(" ", "ALL_CAPS")
    user.rz_set_subsequent_format(" ", "ALL_CAPS")

zed ten: user.rz_set_format("DOUBLE_COLON_SEPARATED")
