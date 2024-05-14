# rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def direct_batch_supplier(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'batch_size', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'batch_supplier',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def direct_batch_color(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'batch_color', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'color_batch',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def color_suppliers(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'color_batch', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'batch_supplier', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'color_supplier',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def full_param(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'batch_size', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'batch_color', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'full_supplier_params',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def direct_batch_product(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'product_batch', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'batch_product',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def product_colors(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'batch_product', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'batch_size', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'supplier_product',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def supplier_product_color_batch(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'supplier_product', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'product_batch', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'batch_color', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('facts', 'supplier_detail_product_color_batch',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),
                                rule.pattern(2).as_data(context),
                                rule.pattern(3).as_data(context),
                                rule.pattern(4).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  fc_rule.fc_rule('direct_batch_supplier', This_rule_base, direct_batch_supplier,
    (('facts', 'batch_size',
      (contexts.variable('supplier'),
       contexts.variable('units'),),
      False),),
    (contexts.variable('units'),
     contexts.variable('supplier'),
     pattern.pattern_literal(()),))
  
  fc_rule.fc_rule('direct_batch_color', This_rule_base, direct_batch_color,
    (('facts', 'batch_color',
      (contexts.variable('units'),
       contexts.variable('color'),),
      False),),
    (contexts.variable('color'),
     contexts.variable('units'),
     pattern.pattern_literal(()),))
  
  fc_rule.fc_rule('color_suppliers', This_rule_base, color_suppliers,
    (('facts', 'color_batch',
      (contexts.variable('color'),
       contexts.variable('units'),
       pattern.pattern_literal(()),),
      False),
     ('facts', 'batch_supplier',
      (contexts.variable('units'),
       contexts.variable('supplier'),
       pattern.pattern_literal(()),),
      False),),
    (contexts.variable('color'),
     contexts.variable('supplier'),
     pattern.pattern_literal(("2 level",)),))
  
  fc_rule.fc_rule('full_param', This_rule_base, full_param,
    (('facts', 'batch_size',
      (contexts.variable('supplier'),
       contexts.variable('units'),),
      False),
     ('facts', 'batch_color',
      (contexts.variable('units'),
       contexts.variable('color'),),
      False),),
    (contexts.variable('supplier'),
     contexts.variable('units'),
     contexts.variable('color'),
     pattern.pattern_literal(("2 level",)),))
  
  fc_rule.fc_rule('direct_batch_product', This_rule_base, direct_batch_product,
    (('facts', 'product_batch',
      (contexts.variable('sku'),
       contexts.variable('units'),),
      False),),
    (contexts.variable('units'),
     contexts.variable('sku'),))
  
  fc_rule.fc_rule('product_colors', This_rule_base, product_colors,
    (('facts', 'batch_product',
      (contexts.variable('units'),
       contexts.variable('sku'),),
      False),
     ('facts', 'batch_size',
      (contexts.variable('supplier'),
       contexts.variable('units'),),
      False),),
    (contexts.variable('supplier'),
     contexts.variable('sku'),
     pattern.pattern_literal(("2 level",)),))
  
  fc_rule.fc_rule('supplier_product_color_batch', This_rule_base, supplier_product_color_batch,
    (('facts', 'supplier_product',
      (contexts.variable('supplier'),
       contexts.variable('sku'),
       pattern.pattern_literal(("2 level",)),),
      False),
     ('facts', 'product_batch',
      (contexts.variable('sku'),
       contexts.variable('units'),),
      False),
     ('facts', 'batch_color',
      (contexts.variable('units'),
       contexts.variable('color'),),
      False),),
    (contexts.variable('supplier'),
     contexts.variable('sku'),
     contexts.variable('units'),
     contexts.variable('color'),
     pattern.pattern_literal(("3 levels",)),))


Krb_filename = '../rules.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 20), (5, 5)),
    ((29, 33), (9, 9)),
    ((34, 37), (11, 11)),
    ((46, 50), (15, 15)),
    ((51, 55), (16, 16)),
    ((56, 59), (18, 18)),
    ((68, 72), (22, 22)),
    ((73, 77), (23, 23)),
    ((78, 82), (25, 25)),
    ((91, 95), (29, 29)),
    ((96, 98), (31, 31)),
    ((107, 111), (35, 35)),
    ((112, 116), (36, 36)),
    ((117, 120), (38, 38)),
    ((129, 133), (42, 42)),
    ((134, 138), (43, 43)),
    ((139, 143), (44, 44)),
    ((144, 149), (46, 46)),
)
