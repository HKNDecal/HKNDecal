from __future__ import print_function
from IPython.core.magic import register_cell_magic

import deborahscript

ys_model = deborahscript.create_model('youscript.tx')

@register_cell_magic
def ds(line, cell):
    program = deborahscript.model.model_from_str(cell)
    return deborahscript.Evaluator().visit(program)


@register_cell_magic
def ys(line, cell):
    program = ys_model.model_from_str(cell)
    return deborahscript.Evaluator().visit(program)
