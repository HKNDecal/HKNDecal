from __future__ import print_function
from IPython.core.magic import register_cell_magic

import deborahscript


@register_cell_magic
def ds(line, cell):
    program = deborahscript.model.model_from_str(cell)
    return deborahscript.Evaluator().visit(program)
