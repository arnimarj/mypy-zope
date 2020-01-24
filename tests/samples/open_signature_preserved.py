"""Bug where the revealed type of open('file') is changed
"""
reveal_type(open('str'))


"""
<output>
open_signature_preserved.py:3: note: Revealed type is 'typing.TextIO'
</output>
"""
