
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '2E6180939D9388C4833E31478CA02687'
    
_lr_action_items = {'(':([3,7,9,12,14,18,19,],[9,9,9,9,9,9,9,]),'$end':([1,2,5,6,10,11,13,16,20,21,23,24,25,27,],[-1,-4,-3,0,-5,-10,-9,-2,-12,-13,-11,-7,-8,-6,]),'ADD_OP':([3,7,9,10,11,12,13,14,15,17,18,19,20,21,23,24,25,],[12,12,12,18,-10,12,-9,12,18,18,12,12,-12,18,-11,-7,-8,]),'}':([1,2,5,10,11,13,16,20,21,23,24,25,26,27,],[-1,-4,-3,-5,-10,-9,-2,-12,-13,-11,-7,-8,27,-6,]),';':([1,2,5,10,11,13,20,21,23,24,25,27,],[8,-4,-3,-5,-10,-9,-12,-13,-11,-7,-8,-6,]),'MUL_OP':([10,11,13,15,17,20,21,23,24,25,],[19,-10,-9,19,19,-12,19,-11,19,-8,]),'WHILE':([0,8,22,],[7,7,7,]),'{':([11,13,15,20,23,24,25,],[-10,-9,22,-12,-11,-7,-8,]),'=':([4,],[14,]),')':([11,13,17,20,23,24,25,],[-10,-9,23,-12,-11,-7,-8,]),'IDENTIFIER':([0,3,7,8,9,12,14,18,19,22,],[4,11,11,4,11,11,11,11,11,4,]),'NUMBER':([3,7,9,12,14,18,19,],[13,13,13,13,13,13,13,]),'PRINT':([0,8,22,],[3,3,3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignation':([0,8,22,],[5,5,5,]),'statement':([0,8,22,],[1,1,1,]),'structure':([0,8,22,],[2,2,2,]),'expression':([3,7,9,12,14,18,19,],[10,15,17,20,21,24,25,]),'programme':([0,8,22,],[6,16,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parser5.py',9),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','parser5.py',13),
  ('statement -> assignation','statement',1,'p_statement','parser5.py',17),
  ('statement -> structure','statement',1,'p_statement','parser5.py',18),
  ('statement -> PRINT expression','statement',2,'p_statement_print','parser5.py',22),
  ('structure -> WHILE expression { programme }','structure',5,'p_structure','parser5.py',26),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parser5.py',30),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','parser5.py',31),
  ('expression -> NUMBER','expression',1,'p_expression_num_or_var','parser5.py',35),
  ('expression -> IDENTIFIER','expression',1,'p_expression_num_or_var','parser5.py',36),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parser5.py',40),
  ('expression -> ADD_OP expression','expression',2,'p_minus','parser5.py',44),
  ('assignation -> IDENTIFIER = expression','assignation',3,'p_assign','parser5.py',48),
]