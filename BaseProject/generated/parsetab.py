
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'FF2E8155EE40A18438BE59C9A873ECE9'
    
_lr_action_items = {'<':([13,14,16,18,19,21,22,23,24,34,36,37,38,39,40,41,42,43,49,51,54,58,60,],[-17,-16,25,25,25,25,25,-19,25,25,-18,25,-10,25,25,25,-11,25,25,25,25,25,25,]),'IDENTIFIER':([0,2,4,6,10,11,12,15,17,20,25,26,27,28,29,30,31,33,35,45,47,52,53,56,59,],[1,13,13,13,13,13,13,13,1,13,13,13,13,13,13,13,13,1,1,13,13,13,1,13,13,]),',':([13,14,16,23,34,36,37,38,39,40,41,42,43,49,54,58,],[-17,-16,29,-19,45,-18,-14,-10,-13,-12,47,-11,-15,52,56,59,]),'IF':([0,17,33,35,53,],[10,10,10,10,10,]),'NUMBER':([2,4,6,10,11,12,15,20,25,26,27,28,29,30,31,45,47,52,56,59,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'{':([13,14,18,21,23,36,37,38,39,40,42,43,51,],[-17,-16,33,35,-19,-18,-14,-10,-13,-12,-11,-15,53,]),'$end':([3,5,7,8,13,14,19,22,23,32,36,37,38,39,40,42,43,48,50,57,61,],[-1,-3,-4,0,-17,-16,-5,-20,-19,-2,-18,-14,-10,-13,-12,-11,-15,-7,-8,-6,-9,]),'}':([3,5,7,13,14,19,22,23,32,36,37,38,39,40,42,43,44,46,48,50,55,57,61,],[-1,-3,-4,-17,-16,-5,-20,-19,-2,-18,-14,-10,-13,-12,-11,-15,48,50,-7,-8,57,-6,-9,]),'WHILE':([0,17,33,35,53,],[4,4,4,4,4,]),'ADD_OP':([2,4,6,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,36,37,38,39,40,41,42,43,45,47,49,51,52,54,56,58,59,60,],[12,12,12,12,12,12,-17,-16,12,26,26,26,12,26,26,-19,26,12,12,12,12,12,12,12,26,-18,26,-10,26,26,26,-11,26,12,12,26,26,12,26,12,26,12,26,]),'NOTEQUAL':([13,14,16,18,19,21,22,23,24,34,36,37,38,39,40,41,42,43,49,51,54,58,60,],[-17,-16,27,27,27,27,27,-19,27,27,-18,27,-10,27,27,27,-11,27,27,27,27,27,27,]),'=':([1,],[11,]),'EQUAL':([13,14,16,18,19,21,22,23,24,34,36,37,38,39,40,41,42,43,49,51,54,58,60,],[-17,-16,28,28,28,28,28,-19,28,28,-18,28,-10,28,28,28,-11,28,28,28,28,28,28,]),'PRINT':([0,17,33,35,53,],[6,6,6,6,6,]),')':([13,14,23,24,36,37,38,39,40,42,43,60,],[-17,-16,-19,36,-18,-14,-10,-13,-12,-11,-15,61,]),';':([3,5,7,13,14,19,22,23,36,37,38,39,40,42,43,48,50,57,61,],[17,-3,-4,-17,-16,-5,-20,-19,-18,-14,-10,-13,-12,-11,-15,-7,-8,-6,-9,]),'PRINTPIXEL':([0,17,33,35,53,],[9,9,9,9,9,]),'FOR':([0,17,33,35,53,],[2,2,2,2,2,]),'MUL_OP':([13,14,16,18,19,21,22,23,24,34,36,37,38,39,40,41,42,43,49,51,54,58,60,],[-17,-16,30,30,30,30,30,-19,30,30,-18,30,30,30,30,30,-11,30,30,30,30,30,30,]),'(':([2,4,6,9,10,11,12,15,20,25,26,27,28,29,30,31,45,47,52,56,59,],[15,15,15,20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'>':([13,14,16,18,19,21,22,23,24,34,36,37,38,39,40,41,42,43,49,51,54,58,60,],[-17,-16,31,31,31,31,31,-19,31,31,-18,31,-10,31,31,31,-11,31,31,31,31,31,31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignation':([0,17,33,35,53,],[5,5,5,5,5,]),'expression':([2,4,6,10,11,12,15,20,25,26,27,28,29,30,31,45,47,52,56,59,],[16,18,19,21,22,23,24,34,37,38,39,40,41,42,43,49,51,54,58,60,]),'structure':([0,17,33,35,53,],[7,7,7,7,7,]),'programme':([0,17,33,35,53,],[8,32,44,46,55,]),'statement':([0,17,33,35,53,],[3,3,3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parserPaint.py',9),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','parserPaint.py',14),
  ('statement -> assignation','statement',1,'p_statement','parserPaint.py',19),
  ('statement -> structure','statement',1,'p_statement','parserPaint.py',20),
  ('statement -> PRINT expression','statement',2,'p_statement_print','parserPaint.py',25),
  ('structure -> FOR expression , expression , expression { programme }','structure',9,'p_structure_for','parserPaint.py',30),
  ('structure -> WHILE expression { programme }','structure',5,'p_structure','parserPaint.py',35),
  ('structure -> IF expression { programme }','structure',5,'p_structure_if','parserPaint.py',40),
  ('statement -> PRINTPIXEL ( expression , expression , expression , expression , expression )','statement',12,'p_printPixel','parserPaint.py',45),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parserPaint.py',50),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','parserPaint.py',51),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_equal','parserPaint.py',56),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_notequal','parserPaint.py',61),
  ('expression -> expression < expression','expression',3,'p_expression_less','parserPaint.py',66),
  ('expression -> expression > expression','expression',3,'p_expression_more','parserPaint.py',71),
  ('expression -> NUMBER','expression',1,'p_expression_num_or_var','parserPaint.py',76),
  ('expression -> IDENTIFIER','expression',1,'p_expression_num_or_var','parserPaint.py',77),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parserPaint.py',82),
  ('expression -> ADD_OP expression','expression',2,'p_minus','parserPaint.py',87),
  ('assignation -> IDENTIFIER = expression','assignation',3,'p_assign','parserPaint.py',92),
]
